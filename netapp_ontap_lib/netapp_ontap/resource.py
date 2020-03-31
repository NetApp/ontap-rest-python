# pylint: disable=line-too-long
"""
Copyright &copy; 2019 NetApp Inc.
All rights reserved.

This module defines the base Resource class. This class is implemented by each
resource object for the system. The methods here allow the client application to
perform actions against the host (GET, POST, PATCH, DELETE) via its REST interface.
"""

# pylint: disable=too-many-lines

import collections.abc
import datetime
import json
import logging
import operator
import time
from typing import (  # pylint: disable=unused-import
    Any,
    Iterable,
    List,
    Optional,
    Type,
    Union,
    cast,
)
import urllib.parse

import marshmallow  # type: ignore
import requests

import netapp_ontap
from netapp_ontap import config, utils
from netapp_ontap.error import NetAppRestError
from netapp_ontap.host_connection import HostConnection
from netapp_ontap.response import NetAppResponse


# we don't really need to document the ResourceSchema class externally since no
# client application should use it directly
__all__ = ["Resource"]

# prevent "No handlers" message if consumer application doesn't configure logging at all
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class ResourceSchema(marshmallow.Schema):
    """An abstract class which is the base of all resource schemas.

    A resource schema defines the fields of a resource with which the client can
    interact. When transforming to and from a REST request or response, the schema
    is responsible for validating and transforming the data.
    """

    @property
    def resource(self) -> "Type[Resource]":
        """The resource class associated with this schema.

        Any time this schema is used to load/deserialize a dict, it will create
        an instance of the `netapp_ontap.resource.Resource` class provided.
        Typically, if the resource class name is "Foo", then the associated schema
        would be called "FooSchema".

        Returns:
            An instance of a `type` object which descends from `netapp_ontap.resource.Resource`
        """

    @marshmallow.post_load
    def make_resource(self, data: dict, **_kwargs) -> "Resource":
        """Automatically called by the library after we load data from a dict.

        A new instance of the associated `netapp_ontap.resource.Resource` is
        instantiated with all of the values which were verified and loaded.

        Args:
            data: A `dict` representing the state of a resource object
            _kwargs: Other arguments passed in by marshmallow (many and partial)

        Returns:
            A `netapp_ontap.resource.Resource` instance holding all of the state
            of the input dictionary.
        """

        return self.resource(**data)

    @property
    def patchable_fields(self):
        """Only fields in this list will be considered when patching a resource"""

        return []

    @property
    def postable_fields(self):
        """Only fields in this list will be considered when posting a resource"""

        return []

class ResourceJSONEncoder(json.JSONEncoder):
    """A custom JSON encoder for the Resource class"""

    def default(self, obj):  # pylint: disable=method-hidden,arguments-differ
        if isinstance(obj, Resource):
            return obj.to_dict()
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


class Resource:  # pylint: disable=too-many-instance-attributes
    """An abstract class which is the base of all resources.

    A resource represents a moment in time snapshot of an object which exists on
    the connected host. This object can be fetched, updated, and returned to the
    host in order to perform meaningful work.
    """

    _schema = ResourceSchema
    _schema_instance = None  # type: ResourceSchema
    _schema_fields = None  # type: List[str]
    _path = ""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the instance of the resource.

        Any keyword arguments are set on the instance as properties. For example,
        if the class was named 'MyResource', then this statement would be true:

            MyResource(name='foo').name == 'foo'

        Args:
            *args: Each positional argument represents a parent key as used in
                the URL of the object. That is, each value will be used to fill
                in a segment of the URL which refers to some parent object. The
                order of these arguments must match the order they are specified
                in the URL, from left to right.
            **kwargs: each entry will have its key set as an attribute name on
                the instance and its value will be the value of that attribute.
        """

        self._prevent_recurse = False
        self._connection = HostConnection.get_host_context()
        self._last_response = None  # type: Optional[NetAppResponse]
        self._request_session = None  # type: Optional[requests.Session]
        self.parent_keys = args
        if getattr(self.__class__, "_schema_instance", None) is None:
            self.__class__._schema_instance = self._schema()  # pylint: disable=protected-access
            self.__class__._schema_fields = list(  # pylint: disable=protected-access
                self._schema_instance.fields.keys()
            )
        self._last_state = self.to_dict()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, name):
        """Emulate dictionary addressing"""

        return getattr(self, name)

    def __repr__(self) -> str:
        """Return the a representation of this resource as a dictionary"""

        return "%s(%s)" % (self.__class__.__name__, self.to_dict())

    def __dir__(self) -> List[str]:
        """Return a list of attributes that belong to the resource. This is useful
        for autocompletion of the otherwise dynamic fields since the list of
        attributes belongs to the associated schema object instead of the resource
        itself.

        https://docs.python.org/3/library/functions.html#dir
        """

        return list(super().__dir__()) + self._schema_fields

    def __getattribute__(self, name):
        """Here we will examine the name being retrieved. If it is a child resource
        then we will bind ourselves to it so that it has our context.
        """

        try:
            value = super().__getattribute__(name)
        except AttributeError:
            schema = super().__getattribute__("_schema_instance")
            if name in schema.fields:
                raise AttributeError(
                    "The '%s' field has not been set on the %s. Try refreshing"
                    " the object by calling get()." %
                    (name, super().__getattribute__("__class__").__name__)
                ) from None
            raise

        # Make sure we don't recurse into ourselves. That is, if we're already
        # trying to bind our keys into a sub object on property access, we don't
        # need to do it again.
        if super().__getattribute__("_prevent_recurse"):
            return value
        self._prevent_recurse = True

        # Get a list of the values of our keys and set them on our child object
        # so that they have access
        key_values = super().__getattribute__("_key_values")
        if isinstance(value, Resource):
            value.parent_keys = key_values
        if isinstance(value, collections.abc.Iterable) and not isinstance(value, str):
            for item in value:
                if isinstance(item, Resource):
                    item.parent_keys = key_values

        self._prevent_recurse = False
        return value

    @property
    def _keys(self) -> List[str]:
        """A list of keys that uniquely identify the object on the host.

        This list is what you would see if you built the path/location of the
        object. For example, if the path to the object was
        /api/storage/volumes/55be2443/snapshots/005056bb3fd7, then the keys
        would be ['volume.uuid', 'uuid']

        Returns:
            A list of strings. Entries in the list which are dotted are foreign
            keys (i.e. keys belonging to a parent object). Entries which do not
            have a dot belong natively to this object.
        """

        return []

    @property
    def _key_values(self) -> List:
        """Return a list of values of the keys of the object.

        Returns:
            A list of values or Nones if the value is not currently set.
        """

        values = []
        for key in self._keys:
            try:
                values.append(operator.attrgetter(key)(self))
            except AttributeError:
                values.append(None)
        return values

    @property
    def path_keys(self) -> List[str]:
        """All keys that are not native to the object (foreign keys).

        In terms of URL, this would typically be all of the keys except for the
        last key. For example, if the path to the object was
        /api/storage/volumes/55be2443/snapshots/005056bb3fd7, then this value
        would be ['volume.uuid']

        Returns:
            A list of strings. Entries in the list are dotted which represent the object they belong to and the attribute on that object.
        """

        path_keys = []  # type: List[str]
        for key in self._keys:
            if "." in key:
                parent, prop = key.split(".")
                if "%s[%s]" % (parent, prop) in self._path:
                    path_keys.append(key)
        return path_keys

    @property
    def _location(self) -> str:
        """The location of a resource is the API path to its collection.

        This can be seen in the Location header which is returned with any POST
        request. It is also the path for any GET/PATCH/DELETE on this object. It
        consists of fixed values and key values in the form /api/foos/{foo_key}/bars.

        Returns:
            A string representing the path to this resource's containing collection.
            When calling `netapp_ontap.resource.Resource.post`, this will be used
            as the target URL.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If not all required parent keys
                are present in the object.
        """

        try:
            format_keys = {}

            # if we were given parent_keys when the object was constructed, then
            # use those
            if len(self.parent_keys) == len(self.path_keys):
                for index, key in enumerate(self.path_keys):
                    pieces = key.split(".")
                    format_keys[pieces[0]] = {pieces[1]: self.parent_keys[index]}
            else:
                representative = self
                if self._last_state:
                    representative = self.__class__.from_dict(self._last_state)
                for key in self.path_keys:
                    key = key.split(".")[0]
                    format_keys[key] = operator.attrgetter(key)(representative)

            return self._path.format(**format_keys)
        except Exception as exc:
            msg = (
                "Could not compute the location of the %s collection. Values for"
                " %s are required." % (self.__class__.__name__, self.path_keys)
            )
            raise NetAppRestError(message=msg, cause=exc) from None

    @property
    def instance_location(self) -> str:
        """Calculate this instance's location based on its key.

        For example:

            snapshot = Snapshot(volume=Volume(uuid='1234'), uuid='5678')
            assert snapshot._keys == ['volume.uuid', 'uuid']
            assert snapshot.volume.uuid == '1234'
            assert snapshot.uuid == '5678'
            assert snapshot.instance_location == '/api/storage/volumes/1234/snapshots/5678'

        Returns:
            A string representing the full path to this resource. When interacting with the host, this location is used as the URL.
        """

        # a keyless resource looks more like a collection location
        if not self._keys:
            return self._location

        representative = self
        if self._last_state:
            representative = self.__class__.from_dict(self._last_state)

        key_diff = set(self._keys) - set(self.path_keys)
        # get values for our keys if they are instance keys, preserving order
        key_vals = []
        for key in [key for key in self._keys if key in key_diff]:
            try:
                key_vals.append(urllib.parse.quote_plus(str(operator.attrgetter(key)(representative))))
            except AttributeError:
                pass

        if key_vals:
            return "%s/%s" % (self._location, "/".join(key_vals))
        return self._location

    @property
    def _session(self) -> requests.Session:
        """A `requests.Session` object which is used for all API calls.

        This session is reused for each API call made with this resource. Multiple
        requests may therefore be sent through the same TCP connection assuming
        the host supports keep-alive.

        Note: If a new `netapp_ontap.host_connection.HostConnection` object is set
        on `netapp_ontap.config.CONNECTION`, this does not update the connection
        or session objects on already existing resources. To update a connection
        on a long lived resource object, call `netapp_ontap.resource.Resource.set_connection`
        and the associated `requests.Session` object will also be refreshed.

        Returns:
            A `requests.Session` object which is used for all API calls.
        """

        current_session = getattr(self, "_request_session", None)
        if current_session:
            conn = self.get_connection()
            if conn.request_headers and current_session.headers != conn.request_headers:
                current_session.headers.update(conn.request_headers)
            return current_session

        conn = self.get_connection()

        self._request_session = requests.Session()
        self._request_session.mount(
            '%s://%s' % (conn.scheme, conn.host),
            requests.adapters.HTTPAdapter(max_retries=5),
        )
        if conn.basic_auth:
            self._request_session.auth = conn.basic_auth
        else:
            self._request_session.cert = conn.cert_auth
        if conn.request_headers:
            self._request_session.headers.update(conn.request_headers)
        self._request_session.verify = conn.verify
        self._request_session.headers.update(
            {"X-Dot-Client-App": "netapp-ontap-python-%s" % netapp_ontap.__version__}
        )

        return self._request_session

    @classmethod
    def from_dict(cls, input_dict: dict, *args, strict: bool = False) -> "Resource":
        """Construct a resource from a dictionary.

        This is essentially a named constructor that returns a `netapp_ontap.resource.Resource`
        object from the values provided. It will verify that all required parent
        keys are present in the input.

        Args:
            input_dict: A set of key/value pairs which are set on the returned
                instance as attributes.
            *args: Each positional argument represents a parent key as used in
                the URL of the object. That is, each value will be used to fill
                in a segment of the URL which refers to some parent object. The
                order of these arguments must match the order they are specified
                in the URL, from left to right.
            strict: If set to True, any value in the input dictionary that is
                not part of the defined schema will cause an exception to be
                raised. If set to False, any value in the input schema will be
                accepted and set as a member of the object.

        Returns:
            A resource object that can be used to interact with the host and contains the data from the input dictionary.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If not all required parent keys
                are present in the input or extra input is provided and strict
                is set to True.
        """
        for field in input_dict.keys():
            if isinstance(input_dict[field], datetime.datetime):
                input_dict[field] = input_dict[field].isoformat()

        if getattr(cls, "_schema_instance", None) is None:
            cls._schema_instance = cls._schema()
        unknown_policy = marshmallow.RAISE if strict else marshmallow.INCLUDE
        try:
            if cls.__name__ == "Software":
                input_dict = _cluster_software_fix(cls, input_dict)
            resource = cls._schema_instance.load(input_dict, unknown=unknown_policy)
        except Exception as exc:
            raise NetAppRestError(cause=exc) from None

        resource.__init__(*args)
        return resource

    def to_dict(self, only: tuple = None) -> dict:
        """Return a dictionary representing the object (and its sub-objects).

        Args:
            only: If a subset of fields are desired instead of all fields belonging
                to this object, `only` may be passed as a tuple of strings.

        Returns:
            A dictionary representing the state of this object and any child objects it may contain.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the current values stored in
                the resource don't match the schema defined for the resource, then
                an error will be raised. For example, if a field is supposed to
                be an integer and a non-integer value is set on it.
        """

        try:
            data = self._schema_instance.dump(self)
            if only:
                return {k: v for k, v in data.items() if k in only}
            return data
        except Exception as exc:
            raise NetAppRestError(cause=exc) from None

    def get_connection(self) -> HostConnection:
        """Returns the `netapp_ontap.host_connection.HostConnection` for this object.

        If there is a `netapp_ontap.host_connection.HostConnection` active as the
        current context (i.e. using a with statement), then that connection will
        be returned. Second, if a connection has been associated with this resource
        (by calling `netapp_ontap.resource.Resource.set_connection`), then that
        connection will be returned. Finally, it will return the connection that
        is associated with `netapp_ontap.config.CONNECTION`.

        Returns:
            A connection to be used for API calls.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If there is no connection
                available to use either set on the object or on the library.
        """

        host_context = HostConnection.get_host_context()

        if host_context is not None:
            return host_context
        if self._connection:
            return self._connection
        if config.CONNECTION:
            return config.CONNECTION

        values = [getattr(self, key, "") for key in self._keys]
        raise NetAppRestError(
            "No connection is setup for %s %s. Either call set_connection() on"
            " the resource or set a global connection object for the library."
            % (self.__class__.__name__, ",".join(values))
        )

    def set_connection(self, connection: HostConnection) -> None:
        """Sets a HostConnection object on the resource.

        This connection will be used for all host operation (GET, PATCH, etc.)
        and overrides any connection that might be set at the library level.

        Args:
            connection: The `netapp_ontap.host_connection.HostConnection` object
                to use for all future API calls on this object.
        """

        self._request_session = None
        self._connection = connection

    def get_collection_url(self, connection: HostConnection = None) -> str:
        """Return the URL for collection-based actions (GET, PATCH, DELETE).

        Args:
            connection: The `netapp_ontap.host_connection.HostConnection` object
                to use for this API call. If unset, tries to use the connection
                which is set globally for the library or from the current context.

        Returns:
            A URL to perform the action on in the form of a string.
        """

        host_context = HostConnection.get_host_context()
        if connection:
            self.set_connection(connection)
        elif host_context is not None:
            self.set_connection(host_context)

        return "%s%s" % (self.get_connection().origin, self._location)

    # pylint: disable=bad-continuation
    @classmethod
    @utils.api
    def _get_collection(
        cls, *args, connection: HostConnection = None, max_records: int = None, **kwargs
    ) -> Iterable["Resource"]:
        """Fetch a list of all objects of this type from the host.

           This is a lazy fetch, making API calls only as necessary when the result
           of this call is iterated over. For instance, if max_records is set to 5,
           then iterating over the collection causes an API call to be sent to the
           server once for every 5 records. If the client stops iterating before
           getting to the 6th record, then no additional API calls are made.

        Args:
            *args: Each entry represents a parent key which is used to build the
                path to the child object. If the URL definition were
                /api/foos/{foo.name}/bars, then to get the collection of bars
                for a particular foo, the foo.name value should be passed.
            connection: The `netapp_ontap.host_connection.HostConnection` object
                to use for this API call. If unset, tries to use the connection
                which is set globally for the library or from the current context.
            max_records: The maximum number of records to return per call
            **kwargs: Any key/value pairs passed will be sent as query parameters
                to the host.

        Returns:
            A list of `netapp_ontap.resource.Resource` objects

        Raises:
            `netapp_ontap.error.NetAppRestError`: If there is no connection
                available to use either passed in or on the library. This would
                be not be raised when get_collection() is called, but rather
                when the result is iterated.
        """

        params = dict(kwargs)
        params["max_records"] = max_records
        sample = cls.from_dict({}, *args)
        url = sample.get_collection_url(connection=connection)
        try:
            while url:
                response = sample._session.get(  # pylint: disable=protected-access
                    url, params=params
                )
                response.raise_for_status()
                if utils.LOG_ALL_API_CALLS:
                    utils.pretty_print_request_response(response)
                body = response.json()
                next_link = body.get("_links", {}).get("next", {}).get("href", None)
                if next_link:
                    url = "%s%s" % (sample.get_connection().origin, next_link)
                    # the next link will give us all our params back, so don't
                    # add them to the URL a second time
                    params = {}
                else:
                    url = ""

                for record in body.get("records", []):
                    yield cls.from_dict(record, *args)
        except requests.exceptions.HTTPError as error:
            # our @utils.api wrapper cannot help us generically catch this error
            # since this is a generator function and not a normal function
            utils.on_api_fail(error)

    @classmethod
    @utils.api
    def _patch_collection(
        cls, body: dict, *args, connection: HostConnection = None, **kwargs
    ) -> NetAppResponse:
        """Patch all objects in a collection which match the given query.

        All records on the host which match the query will be patched with the
        provided body.

        Args:
            body: A dictionary of name/value pairs to set on all matching members
                of the collection.
            *args: Each entry represents a parent key which is used to build the
                path to the child object. If the URL definition were
                /api/foos/{foo.name}/bars, then to patch the collection of bars
                for a particular foo, the foo.name value should be passed.
            connection: The `netapp_ontap.host_connection.HostConnection` object
                to use for this API call. If unset, tries to use the connection
                which is set globally for the library or from the current context.
            **kwargs: Any key/value pairs passed will be sent as query parameters
                to the host. Only resources matching this query will be patched.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        sample = cls.from_dict({}, *args)
        params = dict(kwargs)
        url = sample.get_collection_url(connection=connection)
        while url:
            response = sample._session.patch(  # pylint: disable=protected-access
                url,
                data=json.dumps(body, cls=ResourceJSONEncoder).encode("utf-8"),
                params=params,
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
            response_body = response.json()
            next_link = (
                response_body.get("_links", {}).get("next", {}).get("href", None)
            )
            if next_link:
                url = "%s%s" % (sample.get_connection().origin, next_link)
                # the next link will give us all our params back, so don't
                # add them to the URL a second time
                params = {}
            else:
                url = ""
        return NetAppResponse(response)

    # pylint: disable=bad-continuation
    @classmethod
    @utils.api
    def _delete_collection(
        cls,
        *args,
        body: Union["Resource", dict] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        """Delete all objects in a collection which match the given query.

        All records on the host which match the query will be deleted.

        Args:
            *args: Each entry represents a parent key which is used to build the
                path to the child object. If the URL definition were
                /api/foos/{foo.name}/bars, then to delete the collection of bars
                for a particular foo, the foo.name value should be passed.
            body: The body of the delete request. This could be a Resource instance
                or a dictionary object.
            connection: The `netapp_ontap.host_connection.HostConnection` object
                to use for this API call. If unset, tries to use the connection
                which is set globally for the library or from the current context.
            **kwargs: Any key/value pairs passed will be sent as query parameters
                to the host. Only resources matching this query will be patched.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        sample = cls.from_dict({}, *args)
        params = dict(kwargs)
        url = sample.get_collection_url(connection=connection)
        while url:
            body_data = sample._get_body_data(body)  #pylint: disable=protected-access
            response = sample._session.delete(  # pylint: disable=protected-access
                url, json=body_data, params=params,
            )
            response.raise_for_status()
            response_body = response.json()
            next_link = response_body.get("_links", {}).get("next", {}).get("href", None)
            if next_link:
                url = "%s%s" % (sample.get_connection().origin, next_link)
                # the next link will give us all our params back, so don't
                # add them to the URL a second time
                params = {}
            else:
                url = ""
        return NetAppResponse(response)

    @classmethod
    @utils.api
    def _find(cls, *args, connection: HostConnection = None, **kwargs) -> Optional["Resource"]:
        """Find an instance of an object on the host given a query.

        The host will be queried with the provided key/value pairs to find a
        matching resource. If 0 are found, None will be returned.
        If more than 1 is found, an error will be raised or returned.
        If there is exactly 1 matching record, then it will be returned.

        Args:
            *args: Each entry represents a parent key which is used to build the
                path to the child object. If the URL definition were
                /api/foos/{foo.name}/bars, then to find a bar for a particular
                foo, the foo.name value should be passed.
            connection: The `netapp_ontap.host_connection.HostConnection` object
                to use for this API call. If unset, tries to use the connection
                which is set globally for the library or from the current context.
            **kwargs: Any key/value pairs passed will be sent as query parameters
                to the host.

        Returns:
            A `netapp_ontap.resource.Resource` object containing the
            details of the object or None if no matches were found.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned more
                than 1 matching resource.
        """
        results = list(
            cls._get_collection(*args, connection=connection, **_flatten_dict(kwargs))
        )
        if not results:
            return None
        if len(results) != 1:
            msg = "Only 1 resource was expected. Found %s with query %s" % (
                len(results),
                ",".join("%s=%s" % (key, value) for key, value in kwargs.items()),
            )
            raise NetAppRestError(message=msg)

        resource = results[0]
        resource.set_connection(connection)
        resource._get(fields=kwargs.get("fields"))  # pylint: disable=protected-access
        return resource

    @utils.api
    def _get(self, **kwargs) -> NetAppResponse:
        """Fetch the details of the object from the host.

        Requires the keys to be set (if any). After returning, new or changed
        properties from the host will be set on the instance.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        url = "%s%s" % (self.get_connection().origin, self.instance_location)
        response = self._session.get(url, params=kwargs)
        response.raise_for_status()
        self._clone_from_dict(response.json())
        self._set_last_state()
        self._last_response = NetAppResponse(response)
        return self._last_response

    # pylint: disable=bad-continuation
    @utils.api
    def _post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        """Send this object to the host as a creation request.

        Args:
            hydrate: If set to True, after the response is received from
                the call, a a GET call will be made to refresh all fields of the object.
            poll: If set to True, the call will not return until the
                asynchronous job on the host has completed. Has no effect if the
                host did not return a job response.
            hydrate: If set to True, after the response is received from
                the call, a GET call will be made to refresh all fields of the object.
            poll_interval: If the operation returns a job, this specifies how
                often to query the job for updates.
            poll_timeout: If the operation returns a job, this specifies how
                long to continue monitoring the job's status for completion.
            **kwargs: Any key/value pairs passed will be sent as query parameters
                to the host.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        url = "%s%s" % (self.get_connection().origin, self._location)
        body_data = self._get_postable_data()
        # trim out any keys from the body which are present as part of the path
        for key in self.path_keys:
            body_data.pop(key.split(".")[0], None)
        response = self._session.post(
            url,
            data=json.dumps(body_data, cls=ResourceJSONEncoder).encode("utf-8"),
            params=kwargs,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()

        if not 'Location' in response.headers:
            # if a resource wasn't created, this must be some sort of action
            if poll:
                return utils.poll(response, connection=self.get_connection())
            return NetAppResponse(response)
        self._set_keys(response)
        self._clone_from_dict(self.to_dict())
        self._set_last_state()
        self._last_response = NetAppResponse(response)

        if poll:
            return self._poll(
                hydrate=hydrate, interval=poll_interval, timeout=poll_timeout,
            )
        return self._last_response

    # pylint: disable=bad-continuation
    @utils.api
    def _patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        """Send the difference in the object's state to the host as a modification request.

        Calculates the difference in the object's state since the last time we
        interacted with the host and sends this in the request body.

        Args:
            hydrate: If set to True, after the response is received from
                the call, a a GET call will be made to refresh all fields of the object.
            poll: If set to True, the call will not return until the
                asynchronous job on the host has completed. Has no effect if the
                host did not return a job response.
            hydrate: If set to True, after the response is received from
                the call, a a GET call will be made to refresh all fields of the object.
            poll_interval: If the operation returns a job, this specifies how
                often to query the job for updates.
            poll_timeout: If the operation returns a job, this specifies how
                long to continue monitoring the job's status for completion.
            **kwargs: Any key/value pairs passed will be sent as query parameters
                to the host.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        url = "%s%s" % (self.get_connection().origin, self.instance_location)
        response = self._session.patch(
            url,
            data=json.dumps(self._get_changed_data(), cls=ResourceJSONEncoder).encode(
                "utf-8"
            ),
            params=kwargs,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
        self._set_last_state()
        self._last_response = NetAppResponse(response)

        if poll:
            return self._poll(
                hydrate=hydrate, interval=poll_interval, timeout=poll_timeout,
            )
        return self._last_response

    # pylint: disable=bad-continuation
    @utils.api
    def _delete(
        self,
        body: Union["Resource", dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        """Send a deletion request to the host for this object.

        Args:
            body: The body of the delete request. This could be a Resource instance
                or a dictionary object.
            poll: If set to True, the call will not return until the
                asynchronous job on the host has completed. Has no effect if the
                host did not return a job response.
            poll_interval: If the operation returns a job, this specifies how
                often to query the job for updates.
            poll_timeout: If the operation returns a job, this specifies how
                long to continue monitoring the job's status for completion.
            **kwargs: Any key/value pairs passed will be sent as query parameters
                to the host.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        url = "%s%s" % (self.get_connection().origin, self.instance_location)
        response = self._session.delete(url, json=self._get_body_data(body), params=kwargs)
        response.raise_for_status()
        self._last_response = NetAppResponse(response)

        if poll:
            return self._poll(interval=poll_interval, timeout=poll_timeout)
        return self._last_response

    # pylint: disable=bad-continuation
    # pylint: disable=too-many-arguments
    @utils.api
    def _action(
        self,
        path: str,
        body: Union["Resource", dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        """Perform a custom action on this resource which is not a simple CRUD action

        Args:
            path: The action verb for this request. This will be added as a postfix
                to the instance location of the resource.
            body: The body of the action request. This should be a Resource instance.
                The connection and URL will be determined based on the values from
                this object.
            poll: If set to True, the call will not return until the
                asynchronous job on the host has completed. Has no effect if the
                host did not return a job response.
            poll_interval: If the operation returns a job, this specifies how
                often to query the job for updates.
            poll_timeout: If the operation returns a job, this specifies how
                long to continue monitoring the job's status for completion.
            **kwargs: Any key/value pairs passed will be sent as query parameters
                to the host.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        url = "%s%s/%s" % (self.get_connection().origin, self.instance_location, path)
        response = self._session.post(url, json=self._get_body_data(body), params=kwargs)
        response.raise_for_status()

        if poll:
            return utils.poll(
                response, connection=self.get_connection(),
                interval=poll_interval, timeout=poll_timeout,
            )
        return NetAppResponse(response)

    @utils.api
    def poll(
        self, hydrate: bool = False, timeout: int = None, interval: int = None
    ) -> NetAppResponse:
        """Wait for a job which is running for this resource is complete.

        This function may be called when the client knows there was a job
        started after a previous API call was made for this object. It will go
        get the state of that job and then block until it is complete. If hydrate
        is set to True, this function will continue to block until a subsequent
        GET call on the resource completes and refreshes the attributes of the
        resource.

        Args:
            hydrate: If set to True, after the response is received from
                the call, a GET call will be made to refresh all fields of the object.
            timeout: Seconds to wait before timing out of poll request. If set,
                the value overrides the timeout set in the active HostConnection.
                Otherwise, the timeout set in the active HostConnection is used.
            interval: How long to wait between making REST API calls to check the
                job status. If set, the value overrides the interval set in the
                active HostConnection. Otherwise, the interval set in the active
                HostConnection is used.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        return self._poll(hydrate=hydrate, timeout=timeout, interval=interval)

    def _poll(
        self, hydrate: bool = False, timeout: int = None, interval: int = None
    ) -> NetAppResponse:
        """Non-decorated internal implementation of the poll function. Used for
        calling from other actions (post, patch).

        Args:
            hydrate: If set to True, after the response is received from
                the call, a GET call will be made to refresh all fields of the object.
            timeout: Seconds to wait before timing out of poll request. If set,
                the value overrides the timeout set in the active HostConnection.
                Otherwise, the timeout set in the active HostConnection is used.
            interval: How long to wait between making REST API calls to check the
                job status. If set, the value overrides the interval set in the
                active HostConnection. Otherwise, the interval set in the active
                HostConnection is used.

        Returns:
            A `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400 or if there has not been any requests made for this
                resource (and therefore no jobs to track).
        """

        if not self._last_response:
            values = [getattr(self, key, "") for key in self._keys]
            raise NetAppRestError(
                message="No requests have been made for %s %s."
                % (self.__class__.__name__, ",".join(values))
            )
        response = self._last_response.poll(
            connection=self.get_connection(), timeout=timeout, interval=interval
        )
        if hydrate:
            response = self._get(fields='*')
        self._set_last_state()
        self._last_response = response
        return self._last_response

    def _get_body_data(self, body: Optional[Union["Resource", dict]]) -> dict:
        """Returns a dictionary meant to be used as the body of the request. If
        None is provided, then an empty dict is returned. Any keys for the resource
        are trimmed out of the body dict in case they are provided.
        """

        if body is not None:
            if isinstance(body, Resource):
                body_data = body.to_dict()
            else:
                body_data = dict(body)
            # trim out any keys from the body which are present as part of the path
            for key in self.path_keys:
                body_data.pop(key.split(".")[0], None)
        else:
            body_data = {}

        return body_data

    def _clone_from_dict(self, input_dict: dict) -> None:
        """Refresh almost all fields of the object by replacing with just fetched
        version. We should keep the connection around though.

        Args:
            input_dict: We read the object from the response, inflate it and then
                steal all of its fields.
        """

        connection = self._connection
        session = self._request_session
        parent_keys = self.parent_keys
        self.__dict__ = self.from_dict(  # pylint: disable=attribute-defined-outside-init
            input_dict
        ).__dict__
        self.parent_keys = parent_keys
        self._connection = connection
        self._request_session = session

    def _set_keys(self, post_response: requests.Response) -> None:
        """Parse the Location header from a response and set keys on the object.

        Based on the response to a POST call, we should set the keys on our
        instance so that the user can use this for GET/PATCH/DELETE.

        If the Location header contains a query string, this method will loop for
        10 seconds (waiting 1 second inbetween) and follow that query to try and
        determine the full location of the resource.

        Args:
            post_response: The response returned from a POST API call to the host

        Raises:
            `netapp_ontap.error.NetAppRestError`: Will be raised if the object's
                final location could not be determined within the timeout.
        """

        location = post_response.headers["Location"]

        # if the location is a query, we need to turn around and do a GET to find
        # the "real" location. This is a burt sort of situation. Workaround is
        # implemented below.
        if "?" in location:
            if utils.DEBUG:
                LOGGER.debug(
                    "!!!BURT THIS!!! Location returned for %s contains a query. Location"
                    " was: %s",
                    post_response.request.url,
                    location,
                )
            url = "%s%s" % (self.get_connection().origin, location)
            num_tries = 10
            tries = 0
            while tries < num_tries:
                response = self._session.get(url)
                if response.json().get("records"):
                    location = response.json()["records"][0]["_links"]["self"]["href"]
                    break
                time.sleep(1)
                tries += 1
            if tries >= num_tries:
                msg = (
                    "Not able to find the location of the posted resource after"
                    " %s seconds." % num_tries
                )
                raise NetAppRestError(message=msg)

        # now pick apart the URL and fill in our keys
        location = location.replace(self._location, "").replace("/", "", 1)
        for key_index in range(len(self._keys) - len(self.path_keys)):
            key_attr = self._keys[-key_index - 1]
            self._attrsetter(key_attr, location.split("/")[-key_index - 1])

    def _attrsetter(self, attribute: str, value) -> None:
        """Set a complex property on the object

        Allows for setting something like this:

            self.owner.uuid = '12345'

        when the owner.uuid part is a string. Similar to the builtin setattr()
        function of Python.

        Args:
            attribute: The complex attribute to set on the object. This can be
                in a dotted notation. All parts of the attribute up to the final
                part must already exist in the object.
            value: The value to be set

        Raises:
            `AttributeError`: If the object tree cannot be navigated all the way
                to the final attribute.
        """

        obj = self
        attrs = attribute.split(".")
        for name in attrs[:-1]:
            if not hasattr(obj, name):
                setattr(obj, name, _EmptyObject())
            obj = getattr(obj, name)
        setattr(obj, attrs[-1], value)

    def _set_last_state(self) -> None:
        """Set the last known host state on the object as its dictionary representation.

        This is performed recursively for all of its sub-objects too. The last
        known state is used as part of future PATCH calls to determine the delta
        to send to the host.
        """

        for field in self._schema_instance.fields:
            value = getattr(self, field, None)
            if isinstance(value, Resource):
                value._set_last_state()  # pylint: disable=protected-access

        self._last_state = self.to_dict()

    def _get_changed_data(
        self,
        starting_value: dict = None,
        ref_fields: List[str] = None,
    ) -> dict:
        """Return a diff of the current state of the object vs. the last known state.

        Args:
            starting_value: Instead of comparing the object's last retrieved state
                vs. its current state, this value can be provided to compare
                against its current state. Useful for sub-objects.
            ref_fields: if provided, these fields will be considered patchable
                even if they are not normally. This would be used when posting
                an object that contains a ref to part of another object

        Returns:
            A diff in the form of a dictionary. This is meant to be sent to the
            PATCH API of the resource.
        """

        last_state = getattr(self, "_last_state", {})
        if starting_value is not None:
            last_state = starting_value
        changed_data = {}
        self._clone_from_dict(self.to_dict())
        schema = self._schema_instance
        for field in schema.fields:
            if self._should_skip_field(schema, field, "patch", ref_fields=ref_fields):
                continue

            current_value = getattr(self, field, None)
            previous_value = last_state.get(field, None)

            if current_value is not None and current_value != marshmallow.missing:
                current_value = _get_current_value(
                    schema, field, current_value, previous_value,
                )
                if current_value is not None and current_value != previous_value:
                    if isinstance(current_value, datetime.datetime):
                        current_value = schema.fields[field].serialize(field, self)
                    changed_data[field] = current_value

        # round trip through marshmallow's encoder/decoder so that we get the
        # benefit of any field name mapping
        return self.from_dict(changed_data).to_dict()

    def _get_postable_data(
        self,
        ref_fields: List[str] = None,
    ) -> dict:
        """Return a dict of only the postable fields for this resource.

        Args:
            ref_fields: if provided, these fields will be considered postable
                even if they are not normally. This would be used when posting
                an object that contains a ref to part of another object

        Returns:
            A fields in the form of a dictionary. This is meant to be sent to the
            POST API of the resource.
        """

        changed_data = {}
        self._clone_from_dict(self.to_dict())
        schema = self._schema_instance
        for field in schema.fields:
            if self._should_skip_field(schema, field, "post", ref_fields=ref_fields):
                continue

            current_value = getattr(self, field, None)

            if current_value is not None and current_value != marshmallow.missing:
                current_value = _get_postable_value(
                    schema, field, current_value
                )
                if current_value is not None:
                    if isinstance(current_value, datetime.datetime):
                        current_value = schema.fields[field].serialize(field, self)
                    changed_data[field] = current_value

        # round trip through marshmallow's encoder/decoder so that we get the
        # benefit of any field name mapping
        return self.from_dict(changed_data).to_dict()

    def _should_skip_field(
        self, schema: ResourceSchema, field: str, action: str, ref_fields: List[str] = None,
    ) -> bool:
        """Determine if we should skip sending this field in a POST or PATCH
        request and warn the user that we are doing so
        """

        action_fields = getattr(schema, "%sable_fields" % action)
        warning = "%s.%s is not a %sable field so it is not being sent."

        # if the field is not in the action list, then warn
        if not ref_fields:
            if not [f for f in action_fields if f.startswith(field)]:
                LOGGER.debug(warning, self.__class__.__name__, field, action)
                return True
        elif not field in ref_fields:
            LOGGER.debug(warning, self.__class__.__name__, field, action)
            return True

        current_value = schema.fields[field].serialize(field, self)
        return current_value is None or current_value == marshmallow.missing


# pylint: disable=bad-continuation
def _get_postable_value(
    schema: ResourceSchema, field: str, current_value: Any
) -> Any:
    """Return the current value of the field. If the value is a Resource, recursively
    looks at its fields to determine the changed data. If it is a list, looks at
    each element to determine the changed data.
    """

    if not isinstance(current_value, (Resource, list)):
        return current_value

    if isinstance(current_value, Resource):
        ref_fields = [f.split(".")[1] for f in schema.postable_fields if f.startswith(field + ".")]
        current_value = current_value._get_postable_data(  # pylint: disable=protected-access
            ref_fields=ref_fields,
        )
    elif isinstance(current_value, list):
        changed_items = []
        for value in current_value:
            if isinstance(value, Resource):
                ref_fields = [f.split(".")[1] for f in schema.postable_fields if f.startswith(field + ".")]
                changed = value._get_postable_data(  # pylint: disable=protected-access
                    ref_fields=ref_fields,
                )
                if changed:
                    changed_items.append(changed)
            else:
                changed_items.append(value)
        current_value = changed_items

    if not current_value:
        current_value = None

    return current_value

# pylint: disable=bad-continuation
def _get_current_value(
    schema: ResourceSchema, field: str, current_value: Any, previous_value: Any
) -> Any:
    """Return the current value of the field. If the value is a Resource, recursively
    looks at its fields to determine the changed data.
    """

    if not isinstance(current_value, (list, Resource)):
        return current_value

    if isinstance(current_value, Resource):
        ref_fields = [f.split(".")[1] for f in schema.patchable_fields if f.startswith(field + ".")]
        current_value = current_value._get_changed_data(  # pylint: disable=protected-access
            starting_value=previous_value,
            ref_fields=ref_fields,
        )
    else:
        new_list = []
        for thing in current_value:
            if isinstance(thing, Resource):
                new_list.append(thing.to_dict())
            else:
                new_list.append(thing)
        current_value = new_list

    if not current_value:
        current_value = None

    return current_value


def _flatten_dict(initial: dict, parent_key: str = "") -> dict:
    """Flatten a nested dictionary structure so that nested elements are turned
    into compound keys.

    For example:

    {'foo': {'bar': 'baz'}, 'fizz': 'buzz'} => {'foo.bar': 'baz', 'fizz': 'buzz'}

    Args:
        initial: The dictionary to be flattened
        parent_key: Used for recursive calls

    Returns:
        A flattened dictionary where each key maps to a value non-dict value.
    """

    result = {}
    for key, value in initial.items():
        key = parent_key + key
        if isinstance(value, dict):
            result.update(_flatten_dict(value, key + "."))
        else:
            result[key] = value
    return result


def _cluster_software_fix(cls: Type[Resource], input_dict: dict) -> dict:
    """This returns the correct schema for the /cluster/software endpoint
    to fix the backwards compatibility issue due to the model changing after 9.6
    Once we no longer support ONTAP 9.6, this hardcoded fix can be removed.
    """
    # pylint: disable=protected-access,invalid-name

    # adjust the schema definition due to bad YAML (burt 1291133)
    try:
        validation_field = cls._schema_instance.declared_fields["validation_results"]
        # help mypy understand that this is a List and not just a Field
        validation_field = cast(marshmallow.fields.List, validation_field)
        schema_class_path = validation_field.inner.nested
        SoftwareValidationSchema = marshmallow.class_registry._registry[schema_class_path][0]
        action_field = SoftwareValidationSchema._declared_fields["action"]
        issue_field = SoftwareValidationSchema._declared_fields["issue"]

        # if we've already adjusted the schema once, this would fail so check if
        # it is what we expect before doing it
        if isinstance(action_field, marshmallow.fields.List):
            SoftwareValidationSchema._declared_fields["action"] = action_field.inner
        if isinstance(issue_field, marshmallow.fields.List):
            SoftwareValidationSchema._declared_fields["issue"] = issue_field.inner
    except Exception as exc:  # pylint: disable=broad-except
        LOGGER.error("Failed to adjust schema for SoftwareValidationSchema: %s", exc)

    # adjust the response from ONTAP due to breaking implementation changes
    for obj in ["validation_results", "status_details"]:
        if not obj in input_dict:
            continue
        items = input_dict[obj]
        for item in items:
            #in 9.6, message and action are returned as top level fields
            if isinstance(item.get("message", None), str):
                item["issue"] = {"message": item["message"]}
            if isinstance(item.get("action", None), str):
                item["action"] = {"message": item["action"]}

    return input_dict


class _EmptyObject:  # pylint: disable=too-few-public-methods
    """This class is to be used to add dynamic, nested attributes to resources."""
