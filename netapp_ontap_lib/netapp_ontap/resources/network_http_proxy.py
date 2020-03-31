# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Configuration of an HTTP proxy for an SVM or a Cluster IPspace.
## Retrieve HTTP proxy information
The HTTP proxy GET operation retrieves all configurations for an SVM or a Cluster IPspace via '/api/cluster'.
## Examples
### Retrieving all fields for all HTTP proxy configurations
```
# The API:
/api/network/http-proxy
# The call:
curl -X GET "https://<mgmt-ip>/api/network/http-proxy?fields=*&return_records=true&return_timeout=15" -H  "accept: application/json"
# The response:
{
  "records": [
    {
      "uuid": "4133a1fc-7228-11e9-b40c-005056bb4f0c",
      "svm": {
          "name": "vs1",
          "uuid": "4133a1fc-7228-11e9-b40c-005056bb4f0c"
      },
      "server": "server1.example.com",
      "port": 3128
    },
    {
      "uuid": "96219ce3-7214-11e9-828c-005056bb4f0c",
      "svm": {
          "name": "cluster-1",
          "uuid": "96219ce3-7214-11e9-828c-005056bb4f0c"
      },
      "ipspace": {
          "uuid": "7433520f-7214-11e9-828c-005056bb4f0c",
          "name": "Default"
      },
      "server": "1.1.1.",
      "port": 3128
     }
  ],
  "num_records": 2
}
```
### Retrieving the HTTP proxy configuration for a specific SVM
```
# The API:
/api/network/http-proxy/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/http-proxy/96219ce3-7214-11e9-828c-005056bb4f0c" -H  "accept: application/json"
# The response
{
  "uuid": "96219ce3-7214-11e9-828c-005056bb4f0c",
  "svm": {
      "name": "cluster-1",
      "uuid": "96219ce3-7214-11e9-828c-005056bb4f0c"
  },
  "ipspace": {
      "uuid": "7433520f-7214-11e9-828c-005056bb4f0c",
      "name": "Default"
  },
  "server": "1.1.1.1",
  "port": 3128
}
```
## Creating an HTTP proxy configuration
You can use the HTTP proxy POST operation to create an HTTP proxy configuration for the specified SVM.
## Examples
### Creating an HTTP proxy configuration for a particular SVM
```
# The API:
/api/network/http-proxy
# The call:
curl -X POST "https://<mgmt-ip>/api/network/http-proxy" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{    \"port\": 3128,  \"server\": \"1.1.1.1\",  \"svm\": {      \"name\": \"cluster-1\"  }}"
```
### Creating an HTTP proxy configuration for a particular IPspace
```
# The API:
/api/network/http-proxy
# The call:
curl -X POST "https://<mgmt-ip>/api/network/http-proxy" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"ipspace\": {    \"name\": \"Default\"  },  \"port\": 3128,  \"server\": \"1.1.1.1\"}"
```
## Update an HTTP proxy configuration for a specified SVM
You can use the HTTP proxy PATCH operation to update the HTTP proxy configuration for the specified SVM.
## Example
The following example shows how a PATCH operation is used to update an HTTP proxy configuration for a specific SVM:
```
# The API:
/api/network/http-proxy/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/http-proxy/96219ce3-7214-11e9-828c-005056bb4f0c" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{    \"port\": 3128,  \"server\": \"server2.example.com\"}"
```
## Delete an HTTP proxy configuration for a specified SVM
You can use the HTTP proxy DELETE operation to delete the HTTP proxy configuration for the specified SVM.
## Example
The following example shows how a DELETE operation is used to delete an HTTP proxy configuration for a specific SVM:
```
# The API:
/api/network/http-proxy/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/network/http-proxy/96219ce3-7214-11e9-828c-005056bb4f0c" -H  "accept: application/json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["NetworkHttpProxy", "NetworkHttpProxySchema"]
__pdoc__ = {
    "NetworkHttpProxySchema.resource": False,
    "NetworkHttpProxySchema.patchable_fields": False,
    "NetworkHttpProxySchema.postable_fields": False,
}


class NetworkHttpProxySchema(ResourceSchema):
    """The fields of the NetworkHttpProxy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the network_http_proxy. """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the network_http_proxy. """

    port = fields.Integer(
        data_key="port",
        validate=integer_validation(minimum=1, maximum=65535),
    )
    r""" The port number on which the HTTP proxy service is configured on the
proxy server.


Example: 3128 """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to “svm” for proxy owned by an SVM. Otherwise, set to "cluster".


Valid choices:

* svm
* cluster """

    server = fields.Str(
        data_key="server",
    )
    r""" The fully qualified domain name (FQDN) or IP address of the proxy server. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the network_http_proxy. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The UUID that uniquely identifies the HTTP proxy. """

    @property
    def resource(self):
        return NetworkHttpProxy

    @property
    def patchable_fields(self):
        return [
            "port",
            "server",
        ]

    @property
    def postable_fields(self):
        return [
            "ipspace.name",
            "ipspace.uuid",
            "port",
            "server",
            "svm.name",
            "svm.uuid",
        ]

class NetworkHttpProxy(Resource):
    """Allows interaction with NetworkHttpProxy objects on the host"""

    _schema = NetworkHttpProxySchema
    _path = "/api/network/http-proxy"
    @property
    def _keys(self):
        return ["uuid"]

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
        r"""Retrieves the HTTP proxy configurations of all the SVMs and Cluster IPspaces.
### Related ONTAP commands
* `vserver http-proxy show`

### Learn more
* [`DOC /network/http-proxy`](#docs-networking-network_http-proxy)"""
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
        r"""Updates the proxy server, port, username, and password parameters.
Important notes:
* IPv6 must be enabled if IPv6 family addresses are specified in the "server" field.
* The server and the port combination specified using the "server" and "port" fields is validated during this operation. The validation will fail in the following scenarios:
  * The HTTP proxy service is not configured on the server.
  * The HTTP proxy service is not running on the specified port.
  * The server is unreachable.
### Related ONTAP commands
* `vserver http-proxy modify`

### Learn more
* [`DOC /network/http-proxy`](#docs-networking-network_http-proxy)"""
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
        r"""Deletes the HTTP proxy configuration of the specified SVM or Cluster IPspace.
### Related ONTAP commands
* `vserver http-proxy delete`

### Learn more
* [`DOC /network/http-proxy`](#docs-networking-network_http-proxy)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the HTTP proxy configurations of all the SVMs and Cluster IPspaces.
### Related ONTAP commands
* `vserver http-proxy show`

### Learn more
* [`DOC /network/http-proxy`](#docs-networking-network_http-proxy)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Displays the HTTP proxy server, port, and IPspace of the specified SVM or Cluster IPspace.
### Related ONTAP commands
* `vserver http-proxy show`

### Learn more
* [`DOC /network/http-proxy`](#docs-networking-network_http-proxy)"""
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
        r"""Creates an HTTP proxy configuration for an SVM or a Cluster IPspace.
Important notes:
* IPv6 must be enabled if IPv6 family addresses are specified in the "server" field.
* The server and the port combination specified using the "server" and "port" fields is validated during this operation. The validation will fail in the following scenarios:
  * The HTTP proxy service is not configured on the server.
  * The HTTP proxy service is not running on the specified port.
  * The server is unreachable.
### Required properties
* SVM-scoped HTTP proxy
  * `svm.uuid` or `svm.name` - Existing SVM in which to create the HTTP proxy.
* Cluster-scoped HTTP proxy
  * `ipspace.uuid` or `ipspace.name` - Exisitng Cluster IPspace in which to create the HTTP proxy.
* `server` - HTTP proxy server FQDN or IP address.
* `port` - HTTP proxy server port.
### Related ONTAP commands
* `vserver http-proxy create`

### Learn more
* [`DOC /network/http-proxy`](#docs-networking-network_http-proxy)"""
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
        r"""Updates the proxy server, port, username, and password parameters.
Important notes:
* IPv6 must be enabled if IPv6 family addresses are specified in the "server" field.
* The server and the port combination specified using the "server" and "port" fields is validated during this operation. The validation will fail in the following scenarios:
  * The HTTP proxy service is not configured on the server.
  * The HTTP proxy service is not running on the specified port.
  * The server is unreachable.
### Related ONTAP commands
* `vserver http-proxy modify`

### Learn more
* [`DOC /network/http-proxy`](#docs-networking-network_http-proxy)"""
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
        r"""Deletes the HTTP proxy configuration of the specified SVM or Cluster IPspace.
### Related ONTAP commands
* `vserver http-proxy delete`

### Learn more
* [`DOC /network/http-proxy`](#docs-networking-network_http-proxy)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


