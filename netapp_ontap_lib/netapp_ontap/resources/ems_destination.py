# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Manages a specific instance of a destination. There are limits to the information that you can modify after a destination is created. For example, you cannot change a destination's type, but you can modify the underlying details of the type.
See the documentation for [/support/ems/destinations](#/docs/support/support_ems_destinations) for details on the various properties in a destination.
## Examples
### Retrieving a specific destination instance
```JSON
# API
GET /api/support/ems/destinations/snmp-traphost
# Response
200 OK
# JSON Body
{
  "name": "snmp-traphost",
  "type": "snmp",
  "destination": "",
  "filters": [
    {
      "name": "default-trap-events",
      "_links": {
        "self": {
          "href": "/api/support/ems/filters/default-trap-events"
        }
      }
    }
  ],
  "_links": {
    "self": {
      "href": "/api/support/ems/destinations/snmp-traphost"
    }
  }
}
```
### Updating an existing destination (change of email address)
```JSON
# API
PATCH /api/support/ems/destinations/test-destination
# JSON Body
{
  "destination": "support@mycompany.com"
}
# Response
200 OK
```
### Deleting an existing destination
```JSON
# API
DELETE /api/support/ems/destinations/test-destination
# Response
200 OK
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["EmsDestination", "EmsDestinationSchema"]
__pdoc__ = {
    "EmsDestinationSchema.resource": False,
    "EmsDestinationSchema.patchable_fields": False,
    "EmsDestinationSchema.postable_fields": False,
}


class EmsDestinationSchema(ResourceSchema):
    """The fields of the EmsDestination object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ems_destination. """

    certificate = fields.Nested("netapp_ontap.models.ems_destination_certificate.EmsDestinationCertificateSchema", data_key="certificate", unknown=EXCLUDE)
    r""" The certificate field of the ems_destination. """

    destination = fields.Str(
        data_key="destination",
    )
    r""" Event destination

Example: administrator@mycompany.com """

    filters = fields.List(fields.Nested("netapp_ontap.resources.ems_filter.EmsFilterSchema", unknown=EXCLUDE), data_key="filters")
    r""" The filters field of the ems_destination. """

    name = fields.Str(
        data_key="name",
    )
    r""" Destination name.  Valid in POST.

Example: Admin_Email """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['snmp', 'email', 'syslog', 'rest_api']),
    )
    r""" Type of destination. Valid in POST.

Valid choices:

* snmp
* email
* syslog
* rest_api """

    @property
    def resource(self):
        return EmsDestination

    @property
    def patchable_fields(self):
        return [
            "certificate",
            "destination",
            "filters.name",
        ]

    @property
    def postable_fields(self):
        return [
            "certificate",
            "destination",
            "filters.name",
            "name",
            "type",
        ]

class EmsDestination(Resource):
    """Allows interaction with EmsDestination objects on the host"""

    _schema = EmsDestinationSchema
    _path = "/api/support/ems/destinations"
    @property
    def _keys(self):
        return ["name"]

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a collection of event destinations.
### Related ONTAP commands
* `event notification destination show`
* `event notification show`

### Learn more
* [`DOC /support/ems/destinations`](#docs-support-support_ems_destinations)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates an event destination.
### Recommended optional properties
* `filters.name` - New list of filters that should direct to this destination. The existing list is discarded.
* `certificate` - New certificate parameters when the destination type is `rest api`.
### Related ONTAP commands
* `event notification destination modify`
* `event notification modify`

### Learn more
* [`DOC /support/ems/destinations/{name}`](#docs-support-support_ems_destinations_{name})"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def delete_collection(
        cls,
        *args,
        body: Union[Resource, dict] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an event destination.
### Related ONTAP commands
* `event notification destination delete`
* `event notification delete`

### Learn more
* [`DOC /support/ems/destinations/{name}`](#docs-support-support_ems_destinations_{name})"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of event destinations.
### Related ONTAP commands
* `event notification destination show`
* `event notification show`

### Learn more
* [`DOC /support/ems/destinations`](#docs-support-support_ems_destinations)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves event destinations.
### Related ONTAP commands
* `event notification destination show`
* `event notification show`

### Learn more
* [`DOC /support/ems/destinations/{name}`](#docs-support-support_ems_destinations_{name})"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates an event destination.
### Required properties
* `name` - String that uniquely identifies the destination.
* `type` - Type of destination that is to be created.
* `destination` - String that identifies the destination. The contents of this property changes depending on type.
### Recommended optional properties
* `filters.name` - List of filter names that should direct to this destination.
* `certificate` - When specifying a rest api destination, a client certificate can be provided.
### Related ONTAP commands
* `event notification destination create`
* `event notification create`

### Learn more
* [`DOC /support/ems/destinations`](#docs-support-support_ems_destinations)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates an event destination.
### Recommended optional properties
* `filters.name` - New list of filters that should direct to this destination. The existing list is discarded.
* `certificate` - New certificate parameters when the destination type is `rest api`.
### Related ONTAP commands
* `event notification destination modify`
* `event notification modify`

### Learn more
* [`DOC /support/ems/destinations/{name}`](#docs-support-support_ems_destinations_{name})"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an event destination.
### Related ONTAP commands
* `event notification destination delete`
* `event notification delete`

### Learn more
* [`DOC /support/ems/destinations/{name}`](#docs-support-support_ems_destinations_{name})"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


