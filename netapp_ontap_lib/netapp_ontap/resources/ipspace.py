# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An IPspace is an addressing domain within which each IP address is unique. The same address may appear in a different IPspace, but the matching addresses are considered to be distinct. SVMs and broadcast domains, and therefore IP interfaces and Ethernet ports, are associated with a single IPspace. This endpoint supports the following operations: GET (collection and instance), POST, PATCH, and DELETE.
## Retrieving IPspace information
You can use the IPspaces GET API to retrieve all IPspaces configured in the cluster, including built-in and custom IPspaces, and specifically requested IPspaces.
## Examples
### Retrieving a list of the IPspaces in the cluster
The following example returns the requested list of IPspaces configured in the cluster.
```
# The API:
/api/network/ipspaces
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ipspaces?fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "dcc7e79c-5acc-11e8-b9de-005056b42b32",
      "name": "Default",
      "_links": {
        "self": {
          "href": "/api/network/ipspaces/dcc7e79c-5acc-11e8-b9de-005056b42b32"
        }
      }
    },
    {
      "uuid": "dfd3c1b2-5acc-11e8-b9de-005056b42b32",
      "name": "Cluster",
      "_links": {
        "self": {
          "href": "/api/network/ipspaces/dfd3c1b2-5acc-11e8-b9de-005056b42b32"
        }
      }
    },
    {
      "uuid": "dedec1be-5aec-1eee-beee-0eee56be2b3e",
      "name": "Ipspace1",
      "_links": {
        "self": {
          "href": "/api/network/ipspaces/dedec1be-5aec-1eee-beee-0eee56be2b3e"
        }
      }
    }
  ],
  "num_records": 3,
  "_links": {
    "self": {
      "href": "/api/network/ipspaces?fields=*"
    }
  }
}
```
---
### Retrieving a specific IPspace in the cluster
The following example returns the specific IPspace requested. The system returns an error if there is no IPspace with the requested UUID.
<br/>
---
```
# The API:
/api/network/ipspaces/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ipspaces/dfd3c1b2-5acc-11e8-b9de-005056b42b32?fields=*" -H "accept: application/hal+json"
# The response:
  {
    "uuid": "dcc7e79c-5acc-11e8-b9de-005056b42b32",
    "name": "Default",
    "_links": {
      "self": {
        "href": "/api/network/ipspaces/dcc7e79c-5acc-11e8-b9de-005056b42b32"
      }
    }
  }
```
---
## Creating IPspaces
You can use the network IPspaces POST API to create IPspaces.
<br/>
---
## Example
### Creating an IPspace
The following output displays the record returned after the creation of an IPspace with the name "ipspace1".
<br/>
---
```
# The API:
/api/network/ipspaces
# The call:
curl -X POST "https://<mgmt-ip>/api/network/ipspaces?return_records=true" -H  "accept: application/hal+json" -d "{  \"name\": \"ipspace2\"}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "4165655e-0528-11e9-bd68-005056bb046a",
      "name": "ipspace2",
      "_links": {
        "self": {
          "href": "/api/network/ipspaces/4165655e-0528-11e9-bd68-005056bb046a"
        }
      }
    }
  ]
}
```
---
## Updating IPspaces
You can use the IPspaces PATCH API to update the attributes of the IPspace.
<br/>
---
## Example
### Updating the name of an IPspace
The following PATCH request is used to update the name of the IPspace from "ipspace2" to "ipspace20".
<br/>
---
```
# The API:
/api/network/ipspaces/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/ipspaces/4165655e-0528-11e9-bd68-005056bb046a" -H  "accept: application/hal+json" -d "{  \"name\": \"ipspace20\"}"
```
---
## Deleting IPspaces
You can use the IPspaces DELETE API to delete an IPspace.
<br/>
---
## Example
### Deleting an IPspace
The following DELETE request is used to delete an IPspace.
<br/>
---
```
# The API:
/api/network/ipspaces/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/network/ipspaces/4165655e-0528-11e9-bd68-005056bb046a" -H  "accept: application/hal+json" -H  "Content-Type: application/json"
```
---
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Ipspace", "IpspaceSchema"]
__pdoc__ = {
    "IpspaceSchema.resource": False,
    "IpspaceSchema.patchable_fields": False,
    "IpspaceSchema.postable_fields": False,
}


class IpspaceSchema(ResourceSchema):
    """The fields of the Ipspace object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ipspace. """

    name = fields.Str(
        data_key="name",
    )
    r""" IPspace name

Example: ipspace1 """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The UUID that uniquely identifies the IPspace.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return Ipspace

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]

class Ipspace(Resource):
    """Allows interaction with Ipspace objects on the host"""

    _schema = IpspaceSchema
    _path = "/api/network/ipspaces"
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
        r"""Retrieves a collection of IPspaces for the entire cluster.
### Related ONTAP commands
* `network ipspace show`

### Learn more
* [`DOC /network/ipspaces`](#docs-networking-network_ipspaces)"""
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
        r"""Updates an IPspace object.
### Related ONTAP commands
* `network ipspace rename`

### Learn more
* [`DOC /network/ipspaces`](#docs-networking-network_ipspaces)"""
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
        r"""Deletes an IPspace object.
### Related ONTAP commands
* `network ipspace delete`

### Learn more
* [`DOC /network/ipspaces`](#docs-networking-network_ipspaces)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of IPspaces for the entire cluster.
### Related ONTAP commands
* `network ipspace show`

### Learn more
* [`DOC /network/ipspaces`](#docs-networking-network_ipspaces)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves information about a specific IPspace.
### Related ONTAP commands
* `network ipspace show`

### Learn more
* [`DOC /network/ipspaces`](#docs-networking-network_ipspaces)"""
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
        r"""Creates a new domain within which IP addresses are unique. SVMs, ports, and networks are scoped to a single IPspace.
### Required properties
* `name` - Name of the IPspace to create.
### Related ONTAP commands
* `network ipspace create`

### Learn more
* [`DOC /network/ipspaces`](#docs-networking-network_ipspaces)"""
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
        r"""Updates an IPspace object.
### Related ONTAP commands
* `network ipspace rename`

### Learn more
* [`DOC /network/ipspaces`](#docs-networking-network_ipspaces)"""
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
        r"""Deletes an IPspace object.
### Related ONTAP commands
* `network ipspace delete`

### Learn more
* [`DOC /network/ipspaces`](#docs-networking-network_ipspaces)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


