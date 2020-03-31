# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
The following operations are supported:

* Creation: POST network/ip/bgp/peer-groups
* Collection Get: GET network/ip/bgp/peer-groups
* Instance Get: GET network/ip/bgp/peer-groups/{uuid}
* Instance Patch: PATCH network/ip/bgp/peer-groups/{uuid}
* Instance Delete: DELETE network/ip/bgp/peer-groups/{uuid}
## Retrieving network BGP sessions information
The IP BGP peer-groups GET API retrieves and displays relevant information pertaining to the BGP peer-groups configured in the cluster. The response can contain a list of multiple BGP peer-groups or a specific peer-group. Each BGP peer-group represents a BGP session configured between a local interface and a peer router.
## Examples
### Retrieving all BGP peer-groups in the cluster
The following example shows the list of all BGP peer-groups configured in a cluster.
<br/>
---
```
# The API:
/api/network/ip/bgp/peer-groups
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/bgp/peer-groups" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "5f22ae9d-87b2-11e9-a3a6-005056bb81a4",
      "name": "pg1",
      "_links": {
        "self": {
          "href": "/api/network/ip/bgp/peer-groups/5f22ae9d-87b2-11e9-a3a6-005056bb81a4"
        }
      }
    },
    {
      "uuid": "5fd08be3-87b2-11e9-952f-005056bb2170",
      "name": "pg2",
      "_links": {
        "self": {
          "href": "/api/network/ip/bgp/peer-groups/5fd08be3-87b2-11e9-952f-005056bb2170"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/network/ip/bgp/peer-groups"
    }
  }
}
```
---
### Retrieving a specific BGP peer-group
The following example shows the response when a specific BGP peer-group is requested. The system returns an error when there is no peer-group with the requested UUID.
<br/>
---
```
# The API:
/api/network/ip/bgp/peer-groups/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/bgp/peer-groups/5fd08be3-87b2-11e9-952f-005056bb2170" -H "accept: application/hal+json"
# The response:
{
  "uuid": "5fd08be3-87b2-11e9-952f-005056bb2170",
  "name": "pg2",
  "ipspace": {
    "uuid": "84fd3375-879a-11e9-a3a6-005056bb81a4",
    "name": "Default",
    "_links": {
      "self": {
        "href": "/api/network/ipspaces/84fd3375-879a-11e9-a3a6-005056bb81a4"
      }
    }
  },
  "local": {
    "interface": {
      "uuid": "5e76a305-87b2-11e9-952f-005056bb2170",
      "name": "bgp2",
      "ip": {
        "address": "10.10.10.2"
      }
    },
    "port": {
      "uuid": "f8ff73de-879a-11e9-952f-005056bb2170",
      "name": "e0h",
      "node": {
        "name": "node1"
      }
    }
  },
  "peer": {
    "address": "10.10.10.1",
    "asn": 65501
  },
  "state": "up",
  "_links": {
    "self": {
      "href": "/api/network/ip/bgp/peer-groups/5fd08be3-87b2-11e9-952f-005056bb2170"
    }
  }
}
```
---
### Retrieving specific fields and limiting the output using filters
The following example shows the response when a filter is applied (location.port.node.name=node1) and only certain fields are requested. Filtered fields are in the output in addition to the default fields and requested fields.
<br/>
---
```
# The API:
/api/network/ip/bgp/peer-groups
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/bgp/peer-groups?local.port.node.name=node1&fields=local.interface.ip,peer" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "5f22ae9d-87b2-11e9-a3a6-005056bb81a4",
      "name": "pg1",
      "local": {
        "interface": {
          "ip": {
            "address": "10.10.10.1"
          }
        },
        "port": {
          "node": {
            "name": "node1"
          }
        }
      },
      "peer": {
        "address": "10.10.10.2",
        "asn": 65501
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/bgp/peer-groups/5f22ae9d-87b2-11e9-a3a6-005056bb81a4"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/network/ip/bgp/peer-groups?local.port.node.name=node1&fields=local.interface.ip,peer"
    }
  }
}
```
---
## Creating a BGP peer-group
The BGP peer-group POST API is used to create a peer-group as shown in the following examples.
<br/>
---
## Examples
### Creating a BGP peer-group with an existing interface
The following example shows how to create a BGP peer-group between an existing interface "bgp1" and peer router with the address "10.10.10.10". The local interface "bgp1" needs to support the management-bgp service, otherwise the system returns an error.
<br/>
---
```
# The API:
/api/network/ip/bgp/peer-groups
# The call:
curl -X POST "https://<mgmt-ip>/api/network/bgp/peer-groups?return_records=true" -d'{"name": "newPg", "ipspace.name":"Default", "local.interface.name": "bgp1", "peer.address":"10.10.10.10"}'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "e3faacc6-87cb-11e9-a3a6-005056bb81a4",
      "name": "newPg",
      "ipspace": {
        "name": "Default"
      },
      "local": {
        "interface": {
          "name": "bgp1"
        }
      },
      "peer": {
        "address": "10.10.10.10"
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/bgp/peer-groups/e3faacc6-87cb-11e9-a3a6-005056bb81a4"
        }
      }
    }
  ]
}
```
---
### Creating a BGP peer-group and provisioning a new local interface
The following example shows how to create a BGP peer-group with any local interface. If the local interface doesn't exist, the system will create it first before creating the peer-group.
<br/>
---
```
# The API:
/api/network/ip/bgp/peer-groups
# The call:
curl -X POST "https://<mgmt-ip>/api/network/bgp/peer-groups?return_records=true" -d'{"name": "newPg1", "ippace.name":"Default", "local": {"interface": {"name": "newlif"}, "ip": {"address": "9.9.9.9", "netmask": "24"}, "port": {"name": "e0f", "node": {"name": "node1"}}}, "peer.address":"10.10.10.10"}'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "c292f069-8872-11e9-a3a6-005056bb81a4",
      "name": "newPg1",
      "ipspace": {
        "name": "Default"
      },
      "local": {
        "interface": {
          "name": "newlif"
        },
        "port": {
          "name": "e0f",
          "node": {
            "name": "node1"
          }
        }
      },
      "peer": {
        "address": "10.10.10.10"
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/bgp/peer-groups/c292f069-8872-11e9-a3a6-005056bb81a4"
        }
      }
    }
  ]
}
```
---
## Updating BGP peer-groups
The BGP peer-groups PATCH API is used to update attributes of a peer-group.
<br/>
---
## Examples
### Updating the peer router address
The following example shows how the PATCH request changes the peer router IP address.
<br/>
---
```
# The API:
/api/network/ip/bgp/peer-groups/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/bgp/peer-groups/80d271c9-1f43-11e9-803e-005056a7646a" -H "accept: application/hal+json" -d '{"peer.address": "10.10.10.20" }'
{
}
```
---
### Updating the peer-group to a new name
The following example shows how the PATCH request renames the peer-group.
<br/>
---
```
# The API:
/api/network/ip/bgp/peer-groups/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/bgp/peer-groups/80d271c9-1f43-11e9-803e-005056a7646a" -H "accept: application/hal+json" -d '{"name": "NewName"}'
{
}
```
---
## Deleting BGP peer-groups
The BGP peer-groups DELETE API is used to delete an BGP peer-group.
<br/>
---
## Example
### Deleting a BGP peer-group
The following DELETE request deletes a BGP peer-group.
<br/>
---
```
# The API:
/api/network/ip/bgp/peer-group/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/network/ip/bgp/peer-groups/80d271c9-1f43-11e9-803e-005056a7646a"
{
}
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


__all__ = ["BgpPeerGroup", "BgpPeerGroupSchema"]
__pdoc__ = {
    "BgpPeerGroupSchema.resource": False,
    "BgpPeerGroupSchema.patchable_fields": False,
    "BgpPeerGroupSchema.postable_fields": False,
}


class BgpPeerGroupSchema(ResourceSchema):
    """The fields of the BgpPeerGroup object"""

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the bgp_peer_group. """

    local = fields.Nested("netapp_ontap.models.bgp_peer_group_local.BgpPeerGroupLocalSchema", data_key="local", unknown=EXCLUDE)
    r""" The local field of the bgp_peer_group. """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the peer group

Example: bgpv4peer """

    peer = fields.Nested("netapp_ontap.models.bgp_peer_group_peer.BgpPeerGroupPeerSchema", data_key="peer", unknown=EXCLUDE)
    r""" The peer field of the bgp_peer_group. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['up', 'down']),
    )
    r""" State of the peer group

Valid choices:

* up
* down """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" UUID of the peer group

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return BgpPeerGroup

    @property
    def patchable_fields(self):
        return [
            "local",
            "name",
            "peer",
        ]

    @property
    def postable_fields(self):
        return [
            "ipspace.name",
            "ipspace.uuid",
            "local",
            "name",
            "peer",
        ]

class BgpPeerGroup(Resource):
    r""" A BGP peer group between a local network interface and a router, for the purpose of announcing VIP interface locations for SVMs in this IPspace. """

    _schema = BgpPeerGroupSchema
    _path = "/api/network/ip/bgp/peer-groups"
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
        r"""Retrieves the details of all BGP peer groups for VIP.
### Related ONTAP Commands
* `network bgp peer-group show`

### Learn more
* [`DOC /network/ip/bgp/peer-groups`](#docs-networking-network_ip_bgp_peer-groups)"""
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
        r"""Updates a BGP peer group for VIP.
### Related ONTAP commands
* `network bgp peer-group modify`
* `network bgp peer-group rename`

### Learn more
* [`DOC /network/ip/bgp/peer-groups`](#docs-networking-network_ip_bgp_peer-groups)"""
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
        r"""Deletes a BGP peer group for VIP.
### Related ONTAP commands
* `network bgp peer-group delete`

### Learn more
* [`DOC /network/ip/bgp/peer-groups`](#docs-networking-network_ip_bgp_peer-groups)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the details of all BGP peer groups for VIP.
### Related ONTAP Commands
* `network bgp peer-group show`

### Learn more
* [`DOC /network/ip/bgp/peer-groups`](#docs-networking-network_ip_bgp_peer-groups)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves details of a BGP peer group for VIP.
### Related ONTAP commands
* `network bgp peer-group show`

### Learn more
* [`DOC /network/ip/bgp/peer-groups`](#docs-networking-network_ip_bgp_peer-groups)"""
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
        r"""Creates a new BGP peer group for VIP. Multipath-routing is turned on cluster-wide automatically if the peer group being created results in multiple paths being available for an existing or future VIP interface.<br/>
### Required properties
* `name` - Name of the peer-group to create.
* `ipspace.name` or `ipspace.uuid`
  * Required with local.interface.name to identify a local interface
  * Optional when local.interface.uuid is specified
* `local.interface.uuid` or `local.interface.name`
  * Required when specifying an existing local interface.
* `local.interface.name`, `local.ip` and `local.port`
  * Required to create a new local interface.
* `peer.address` - IP address of the peer router
### Related ONTAP commands
* `network bgp peer-group create`

### Learn more
* [`DOC /network/ip/bgp/peer-groups`](#docs-networking-network_ip_bgp_peer-groups)"""
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
        r"""Updates a BGP peer group for VIP.
### Related ONTAP commands
* `network bgp peer-group modify`
* `network bgp peer-group rename`

### Learn more
* [`DOC /network/ip/bgp/peer-groups`](#docs-networking-network_ip_bgp_peer-groups)"""
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
        r"""Deletes a BGP peer group for VIP.
### Related ONTAP commands
* `network bgp peer-group delete`

### Learn more
* [`DOC /network/ip/bgp/peer-groups`](#docs-networking-network_ip_bgp_peer-groups)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


