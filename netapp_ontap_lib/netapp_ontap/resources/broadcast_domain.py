# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
A broadcast domain is a collection of Ethernet ports that have layer 2 connectivity. They are used to determine which Ethernet ports can host interfaces of various types. The broadcast domain REST API allows you to retrieve, create, modify, and delete broadcast domains. The broadcast domain APIs do not manage port membership. To add a port to a broadcast domain or to move a port to a different broadcast domain, use PATCH /network/ethernet/ports/<uuid>.
## Retrieving network Ethernet broadcast domain information
The broadcast domains GET API retrieves and displays relevant information pertaining to the broadcast domains configured in the cluster. The API retrieves the list of all broadcast domains configured in the cluster, or a specific broadcast domain.
<br/>
---
## Examples
### Retrieving all broadcast domains in the cluster
The following output shows the list of all broadcast domains configured in a cluster.
<br/>
---
```
# The API:
/api/network/ethernet/broadcast-domains
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ethernet/broadcast-domains" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "6970c2a9-f34f-11e8-8373-005056bb6b85",
      "name": "Cluster",
      "ipspace": {
        "uuid": "6267eff8-f34f-11e8-8373-005056bb6b85",
        "name": "Cluster",
        "_links": {
          "self": {
            "href": "/api/network/ipspaces/6267eff8-f34f-11e8-8373-005056bb6b85"
          }
        }
      },
      "ports": [
        {
          "uuid": "626b4d19-f34f-11e8-8373-005056bb6b85",
          "name": "e0a",
          "node": {
            "name": "examplecluster-node01"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/626b4d19-f34f-11e8-8373-005056bb6b85"
            }
          }
        },
        {
          "uuid": "626b77b9-f34f-11e8-8373-005056bb6b85",
          "name": "e0b",
          "node": {
            "name": "examplecluster-node01"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/626b77b9-f34f-11e8-8373-005056bb6b85"
            }
          }
        }
      ],
      "mtu": 9000,
      "_links": {
        "self": {
          "href": "/api/network/ethernet/broadcast-domains/6970c2a9-f34f-11e8-8373-005056bb6b85"
        }
      }
    },
    {
      "uuid": "6972416c-f34f-11e8-8373-005056bb6b85",
      "name": "Default",
      "ipspace": {
        "uuid": "5f650349-f34f-11e8-8373-005056bb6b85",
        "name": "Default",
        "_links": {
          "self": {
            "href": "/api/network/ipspaces/5f650349-f34f-11e8-8373-005056bb6b85"
          }
        }
      },
      "ports": [
        {
          "uuid": "626bae19-f34f-11e8-8373-005056bb6b85",
          "name": "e0c",
          "node": {
            "name": "examplecluster-node01"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/626bae19-f34f-11e8-8373-005056bb6b85"
            }
          }
        },
        {
          "uuid": "626bd677-f34f-11e8-8373-005056bb6b85",
          "name": "e0d",
          "node": {
            "name": "examplecluster-node01"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/626bd677-f34f-11e8-8373-005056bb6b85"
            }
          }
        }
      ],
      "mtu": 1500,
      "_links": {
        "self": {
          "href": "/api/network/ethernet/broadcast-domains/6972416c-f34f-11e8-8373-005056bb6b85"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/network/ethernet/broadcast-domains?fields=*"
    }
  }
}
```
---
### Retrieving a specific broadcast domain
The following output shows the response returned when a specific broadcast domain is requested. The system returns an error if there is no broadcast domain with the requested UUID.
<br/>
---
```
# The API:
/api/network/ethernet/broadcast-domains/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ethernet/broadcast-domains/4475a2c8-f8a0-11e8-8d33-005056bb986f/?fields=*" -H "accept: application/hal+json"
# The response:
{
  "uuid": "4475a2c8-f8a0-11e8-8d33-005056bb986f",
  "name": "Cluster",
  "ipspace": {
    "uuid": "3e518ed5-f8a0-11e8-8d33-005056bb986f",
    "name": "Cluster",
    "_links": {
      "self": {
        "href": "/api/network/ipspaces/3e518ed5-f8a0-11e8-8d33-005056bb986f"
      }
    }
  },
  "ports": [
    {
      "uuid": "3e539a62-f8a0-11e8-8d33-005056bb986f",
      "name": "e0a",
      "node": {
        "name": "examplecluster-node01"
      },
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/3e539a62-f8a0-11e8-8d33-005056bb986f"
        }
      }
    },
    {
      "uuid": "3e53c94a-f8a0-11e8-8d33-005056bb986f",
      "name": "e0b",
      "node": {
        "name": "examplecluster-node01"
      },
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/3e53c94a-f8a0-11e8-8d33-005056bb986f"
        }
      }
    }
  ],
  "mtu": 9000,
  "_links": {
    "self": {
      "href": "/api/network/ethernet/broadcast-domains/4475a2c8-f8a0-11e8-8d33-005056bb986f/"
    }
  }
}
```
---
### Retrieving all broadcast domains with a specific name
The following output shows the response returned when broadcast domains with a specific name in any IPspace are requested.
<br/>
---
```
# The API:
/api/network/ethernet/broadcast-domains
# The call:
curl -X GET "https://10.224.87.121/api/network/ethernet/broadcast-domains/?name=bd1" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "66b607e5-4bee-11e9-af6a-005056bb13c0",
      "name": "bd1",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/broadcast-domains/66b607e5-4bee-11e9-af6a-005056bb13c0"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/network/ethernet/broadcast-domains/?name=bd1"
    }
  }
}
```
---
### Retrieving the broadcast domains for an IPspace
The following output shows the response returned when the broadcast domains for a specified IPspace are requested.
<br/>
---
```
# The API:
/api/network/ethernet/broadcast-domains
# The call:
curl -X GET "https://10.224.87.121/api/network/ethernet/broadcast-domains/?ipspace.name=Cluster&fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "ae69070c-4bed-11e9-af6a-005056bb13c0",
      "name": "Cluster",
      "ipspace": {
        "uuid": "ac466a88-4bed-11e9-af6a-005056bb13c0",
        "name": "Cluster",
        "_links": {
          "self": {
            "href": "/api/network/ipspaces/ac466a88-4bed-11e9-af6a-005056bb13c0"
          }
        }
      },
      "ports": [
        {
          "uuid": "acd67884-4bed-11e9-af6a-005056bb13c0",
          "name": "e0a",
          "node": {
            "name": "examplecluster-node-1"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/acd67884-4bed-11e9-af6a-005056bb13c0"
            }
          }
        },
        {
          "uuid": "ace1a36f-4bed-11e9-af6a-005056bb13c0",
          "name": "e0b",
          "node": {
            "name": "examplecluster-node-1"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/ace1a36f-4bed-11e9-af6a-005056bb13c0"
            }
          }
        }
      ],
      "mtu": 1500,
      "_links": {
        "self": {
          "href": "/api/network/ethernet/broadcast-domains/ae69070c-4bed-11e9-af6a-005056bb13c0"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/network/ethernet/broadcast-domains/?ipspace.name=Cluster&fields=*"
    }
  }
}
```
---
## Creating network Ethernet broadcast domains
You can use the POST API to create broadcast domains.
<br/>
---
## Example
### Creating a new broadcast domain
The following example shows how to create a broadcast domain with a name of 'bd1' and an MTU of 1500.
<br/>
---
```
# The API:
/api/network/ethernet/broadcast-domains
# The call:
curl -X POST "https://<mgmt-ip>/api/network/ethernet/broadcast-domains?return_records=true" -H "accept: application/hal+json" -d '{ "name": "bd1", "mtu": 1500 }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "name": "bd1",
      "mtu": 1500,
      "_links": {
        "self": {
          "href": "/api/network/ethernet/broadcast-domains/"
        }
      }
    }
  ]
}
```
---
## Updating network Ethernet broadcast domains
You can use the PATCH API to update the attributes of broadcast domains.
<br/>
---
## Examples
### Updating the name and MTU of a specific broadcast domain
The following example shows how the PATCH request changes the broadcast domain name to 'bd2' and the broadcast domain MTU to 9000.
<br/>
---
```
# The API:
/api/network/ethernet/broadcast-domains/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/ethernet/broadcast-domains/6cde03b2-f8a2-11e8-8d33-005056bb986f/" -d '{ "name": "bd2", "mtu": 9000 }'
{
}
```
---
### Updating the IPspace of a specific broadcast domain
The following example shows how the PATCH request changes the IPspace of a broadcast domain to 'ipspace2'.
<br/>
---
```
# The API:
/api/network/ethernet/broadcast-domains/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/ethernet/broadcast_domains/c6fe2541-61f4-11e9-a66e-005056bbe83e" -d '{ "ipspace" : { "name" : "ipspace2" } }'
{
}
```
---
## Deleting network Ethernet broadcast domains
You can use the DELETE API to delete a broadcast domain from the cluster configuration.
## Example
### Deleting a specific broadcast domain
The following DELETE request deletes a broadcast domain.
<br/>
---
```
# The API:
/api/network/ethernet/broadcast-domains/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/network/ethernet/broadcast-domains/6cde03b2-f8a2-11e8-8d33-005056bb986f/"
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


__all__ = ["BroadcastDomain", "BroadcastDomainSchema"]
__pdoc__ = {
    "BroadcastDomainSchema.resource": False,
    "BroadcastDomainSchema.patchable_fields": False,
    "BroadcastDomainSchema.postable_fields": False,
}


class BroadcastDomainSchema(ResourceSchema):
    """The fields of the BroadcastDomain object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the broadcast_domain. """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the broadcast_domain. """

    mtu = fields.Integer(
        data_key="mtu",
        validate=integer_validation(minimum=68),
    )
    r""" Maximum transmission unit, largest packet size on this network

Example: 1500 """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the broadcast domain, scoped to its IPspace

Example: bd1 """

    ports = fields.List(fields.Nested("netapp_ontap.resources.port.PortSchema", unknown=EXCLUDE), data_key="ports")
    r""" Ports that belong to the broadcast domain """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Broadcast domain UUID

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return BroadcastDomain

    @property
    def patchable_fields(self):
        return [
            "ipspace.name",
            "ipspace.uuid",
            "mtu",
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "ipspace.name",
            "ipspace.uuid",
            "mtu",
            "name",
        ]

class BroadcastDomain(Resource):
    r""" Set of ports that will receive a broadcast Ethernet packet from any of them """

    _schema = BroadcastDomainSchema
    _path = "/api/network/ethernet/broadcast-domains"
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
        r"""Retrieves a collection of broadcast domains for the entire cluster.
### Related ONTAP commands
* `network port broadcast-domain show`

### Learn more
* [`DOC /network/ethernet/broadcast-domains`](#docs-networking-network_ethernet_broadcast-domains)"""
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
        r"""Updates the properties of a broadcast domain.
### Related ONTAP commands
* `network port broadcast-domain modify`
* `network port broadcast-domain rename`

### Learn more
* [`DOC /network/ethernet/broadcast-domains`](#docs-networking-network_ethernet_broadcast-domains)"""
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
        r"""Deletes a broadcast domain.
### Related ONTAP commands
* `network port broadcast-domain delete`

### Learn more
* [`DOC /network/ethernet/broadcast-domains`](#docs-networking-network_ethernet_broadcast-domains)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of broadcast domains for the entire cluster.
### Related ONTAP commands
* `network port broadcast-domain show`

### Learn more
* [`DOC /network/ethernet/broadcast-domains`](#docs-networking-network_ethernet_broadcast-domains)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves details of a broadcast domain.
### Related ONTAP commands
* `network port broadcast-domain show`

### Learn more
* [`DOC /network/ethernet/broadcast-domains`](#docs-networking-network_ethernet_broadcast-domains)"""
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
        r"""Creates a new broadcast domain.<br/>
### Required properties
* `name` - Name of the broadcast-domain to create.
* `mtu` - Maximum transmission unit (MTU) of the broadcast domain.
### Recommended optional properties
* `ipspace.name` or `ipspace.uuid` - IPspace the broadcast domain belongs to.
### Default property values
If not specified in POST, the following default property values are assigned:
* `ipspace` - _Default_
### Related ONTAP commands
* `network port broadcast-domain create`

### Learn more
* [`DOC /network/ethernet/broadcast-domains`](#docs-networking-network_ethernet_broadcast-domains)"""
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
        r"""Updates the properties of a broadcast domain.
### Related ONTAP commands
* `network port broadcast-domain modify`
* `network port broadcast-domain rename`

### Learn more
* [`DOC /network/ethernet/broadcast-domains`](#docs-networking-network_ethernet_broadcast-domains)"""
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
        r"""Deletes a broadcast domain.
### Related ONTAP commands
* `network port broadcast-domain delete`

### Learn more
* [`DOC /network/ethernet/broadcast-domains`](#docs-networking-network_ethernet_broadcast-domains)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


