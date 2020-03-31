# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
A port is a physical or virtual Ethernet network device. Physical ports may be combined into Link Aggregation Groups (LAGs or ifgrps), or divided into Virtual LANs (VLANs).<br/>
GET (collection), GET (instance), and PATCH APIs are available for all port types. POST and DELETE APIs are available for "lag" (ifgrp) and "vlan" port types.<br/>
## Retrieving network port information
The network ports GET API retrieves and displays relevant information pertaining to the ports configured in the cluster. The API retrieves the list of all ports configured in the cluster, or specifically requested ports. The fields returned in the response vary for different ports and configurations.
## Examples
### Retrieving all ports in the cluster
The following output displays the UUID, name, and port type for all ports configured in a 2-node cluster. The port types are physical, vlan, and lag (ifgrp).
<br/>
---
```
# The API:
/api/network/ethernet/ports
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ethernet/ports?fields=uuid,name,type" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "2d2c90c0-f70d-11e8-b145-005056bb5b8e",
      "name": "e0a",
      "type": "physical",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/2d2c90c0-f70d-11e8-b145-005056bb5b8e"
        }
      }
    },
    {
      "uuid": "2d3004da-f70d-11e8-b145-005056bb5b8e",
      "name": "e0b",
      "type": "physical",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/2d3004da-f70d-11e8-b145-005056bb5b8e"
        }
      }
    },
    {
      "uuid": "2d34a2cb-f70d-11e8-b145-005056bb5b8e",
      "name": "e0c",
      "type": "physical",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/2d34a2cb-f70d-11e8-b145-005056bb5b8e"
        }
      }
    },
    {
      "uuid": "2d37189f-f70d-11e8-b145-005056bb5b8e",
      "name": "e0d",
      "type": "physical",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/2d37189f-f70d-11e8-b145-005056bb5b8e"
        }
      }
    },
    {
      "uuid": "35de5d8b-f70d-11e8-abdf-005056bb7fc8",
      "name": "e0a",
      "type": "physical",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/35de5d8b-f70d-11e8-abdf-005056bb7fc8"
        }
      }
    },
    {
      "uuid": "35de78cc-f70d-11e8-abdf-005056bb7fc8",
      "name": "e0b",
      "type": "physical",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/35de78cc-f70d-11e8-abdf-005056bb7fc8"
        }
      }
    },
    {
      "uuid": "35dead3c-f70d-11e8-abdf-005056bb7fc8",
      "name": "e0c",
      "type": "physical",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/35dead3c-f70d-11e8-abdf-005056bb7fc8"
        }
      }
    },
    {
      "uuid": "35deda90-f70d-11e8-abdf-005056bb7fc8",
      "name": "e0d",
      "type": "physical",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/35deda90-f70d-11e8-abdf-005056bb7fc8"
        }
      }
    },
    {
      "uuid": "42e25145-f97d-11e8-ade9-005056bb7fc8",
      "name": "e0c-100",
      "type": "vlan",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/42e25145-f97d-11e8-ade9-005056bb7fc8"
        }
      }
    },
    {
      "uuid": "569e0abd-f97d-11e8-ade9-005056bb7fc8",
      "name": "a0a",
      "type": "lag",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/569e0abd-f97d-11e8-ade9-005056bb7fc8"
        }
      }
    }
  ],
  "num_records": 10,
  "_links": {
    "self": {
      "href": "/api/network/ethernet/ports?fields=uuid,name,type"
    }
  }
}
```
---
### Retrieving a specific physical port
The following output displays the response when a specific physical port is requested. The system returns an error when there is no port with the requested UUID. Also, the speed field is set only if the state of the port is up.
<br/>
---
```
# The API:
/api/network/ethernet/ports/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ethernet/ports/2d37189f-f70d-11e8-b145-005056bb5b8e?fields=*" -H "accept: application/hal+json"
# The response:
{
  "uuid": "2d37189f-f70d-11e8-b145-005056bb5b8e",
  "name": "e0d",
  "mac_address": "00:50:56:bb:62:2d",
  "type": "physical",
  "node": {
    "uuid": "faa56898-f70c-11e8-b145-005056bb5b8e",
    "name": "user-cluster-01",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/faa56898-f70c-11e8-b145-005056bb5b8e"
      }
    }
  },
  "broadcast_domain": {
    "uuid": "36434bec-f70d-11e8-b145-005056bb5b8e",
    "name": "Default",
    "ipspace": {
      "name": "Default"
    },
    "_links": {
      "self": {
        "href": "/api/network/ethernet/broadcast-domains/36434bec-f70d-11e8-b145-005056bb5b8e"
      }
    }
  },
  "enabled": true,
  "state": "up",
  "mtu": 1500,
  "speed": "1000",
  "_links": {
    "self": {
      "href": "/api/network/ethernet/ports/2d37189f-f70d-11e8-b145-005056bb5b8e"
    }
  }
}
```
---
### Retrieving a specific VLAN port
The following output displays the response when a specific VLAN port is requested. The system returns an error when there is no port with the requested UUID. Also, the speed field is set only if the state of the port is up.
<br/>
---
```
# The API:
/api/network/ethernet/ports/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ethernet/ports/42e25145-f97d-11e8-ade9-005056bb7fc8?fields=*" -H "accept: application/hal+json"
# The response:
{
  "uuid": "42e25145-f97d-11e8-ade9-005056bb7fc8",
  "name": "e0e-100",
  "mac_address": "00:50:56:bb:52:2f",
  "type": "vlan",
  "node": {
    "uuid": "6042cf47-f70c-11e8-abdf-005056bb7fc8",
    "name": "user-cluster-02",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/6042cf47-f70c-11e8-abdf-005056bb7fc8"
      }
    }
  },
  "enabled": true,
  "state": "up",
  "mtu": 1500,
  "speed": "1000",
  "vlan": {
    "tag": 100,
    "base_port": {
      "uuid": "35deff03-f70d-11e8-abdf-005056bb7fc8",
      "name": "e0e",
      "node": {
        "name": "user-cluster-02"
      },
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/35deff03-f70d-11e8-abdf-005056bb7fc8"
        }
      }
    }
  },
  "_links": {
    "self": {
      "href": "/api/network/ethernet/ports/42e25145-f97d-11e8-ade9-005056bb7fc8"
    }
  }
}
```
---
### Retrieving a specific LAG port
The following output displays the response when a specific LAG port is requested. The system returns an error when there is no port with the requested UUID. Also, the speed and lag.active_ports fields are set only if the state of the port is up.
<br/>
---
```
# The API:
/api/network/ethernet/ports/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ethernet/ports/569e0abd-f97d-11e8-ade9-005056bb7fc8?fields=*" -H "accept: application/hal+json"
# The response:
{
  "uuid": "569e0abd-f97d-11e8-ade9-005056bb7fc8",
  "name": "a0a",
  "mac_address": "02:50:56:bb:7f:c8",
  "type": "lag",
  "node": {
    "uuid": "6042cf47-f70c-11e8-abdf-005056bb7fc8",
    "name": "user-cluster-02",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/6042cf47-f70c-11e8-abdf-005056bb7fc8"
      }
    }
  },
  "enabled": true,
  "state": "up",
  "mtu": 1500,
  "speed": "1000",
  "lag": {
    "mode": "singlemode",
    "distribution_policy": "mac",
    "member_ports": [
      {
        "uuid": "35df318d-f70d-11e8-abdf-005056bb7fc8",
        "name": "e0f",
        "node": {
          "name": "user-cluster-02"
        },
        "_links": {
          "self": {
            "href": "/api/network/ethernet/ports/35df318d-f70d-11e8-abdf-005056bb7fc8"
          }
        }
      },
      {
        "uuid": "35df5bad-f70d-11e8-abdf-005056bb7fc8",
        "name": "e0g",
        "node": {
          "name": "user-cluster-02"
        },
        "_links": {
          "self": {
            "href": "/api/network/ethernet/ports/35df5bad-f70d-11e8-abdf-005056bb7fc8"
          }
        }
      },
      {
        "uuid": "35df9926-f70d-11e8-abdf-005056bb7fc8",
        "name": "e0h",
        "node": {
          "name": "user-cluster-02"
        },
        "_links": {
          "self": {
            "href": "/api/network/ethernet/ports/35df9926-f70d-11e8-abdf-005056bb7fc8"
          }
        }
      }
    ],
    "active_ports": [
      {
        "uuid": "35df318d-f70d-11e8-abdf-005056bb7fc8",
        "name": "e0f",
        "_links": {
          "self": {
            "href": "/api/network/ethernet/ports/35df318d-f70d-11e8-abdf-005056bb7fc8"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "/api/network/ethernet/ports/569e0abd-f97d-11e8-ade9-005056bb7fc8"
    }
  }
}
```
---
### Retrieving all LAG (ifgrp) ports in the cluster
This command retrieves all LAG ports in the cluster (that is, all ports with type=LAG). The example shows how to filter a GET collection based on type.
<br/>
---
```
# The API:
/api/network/ethernet/ports
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ethernet/ports?type=lag&node.name=user-cluster-01&fields=name,enabled,speed,mtu" -H  "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "0c226db0-4b63-11e9-8113-005056bbe040",
      "name": "a0b",
      "type": "lag",
      "node": {
        "name": "user-cluster-01"
      },
      "enabled": true,
      "mtu": 1500,
      "speed": "1000",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/0c226db0-4b63-11e9-8113-005056bbe040"
        }
      }
    },
    {
      "uuid": "d3a84153-4b3f-11e9-a00d-005056bbe040",
      "name": "a0a",
      "type": "lag",
      "node": {
        "name": "user-cluster-01"
      },
      "enabled": true,
      "mtu": 1500,
      "speed": "1000",
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/d3a84153-4b3f-11e9-a00d-005056bbe040"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/network/ethernet/ports?fields=name,enabled,speed,mtu&type=lag&node.name=user-cluster-01"
    }
  }
}
```
---
## Creating VLAN and LAG ports
You can use the network ports POST API to create VLAN and LAG ports.
<br/>
---
## Examples
### Creating a VLAN port
The following output displays the record returned after the creation of a VLAN port on "e0e" and VLAN tag "100". Also, the VLAN port is added to the "Default" broadcast domain in the "Default" IPspace.
<br/>
---
```
# The API:
/api/network/ethernet/ports
# The call:
curl -X POST "https://<mgmt-ip>/api/network/ethernet/ports?return_records=true" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{     \"type\": \"vlan\", \"node\": { \"name\": \"user-cluster-01\" }, \"broadcast_domain\": { \"name\": \"Default\", \"ipspace\": { \"name\": \"Default    \" } }, \"enabled\": true, \"vlan\": { \"tag\": 100, \"base_port\": { \"name\": \"e0e\", \"node\": { \"name\": \"user-cluster-01\" } } }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "88b2f682-fa42-11e8-a6d7-005056bb5b8e",
      "type": "vlan",
      "node": {
        "uuid": "faa56898-f70c-11e8-b145-005056bb5b8e",
        "name": "user-cluster-01",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/faa56898-f70c-11e8-b145-005056bb5b8e"
          }
        }
      },
      "broadcast_domain": {
        "uuid": "36434bec-f70d-11e8-b145-005056bb5b8e",
        "name": "Default",
        "ipspace": {
          "name": "Default"
        },
        "_links": {
          "self": {
            "href": "/api/network/ethernet/broadcast-domains/36434bec-f70d-11e8-b145-005056bb5b8e"
          }
        }
      },
      "enabled": true,
      "vlan": {
        "tag": 100,
        "base_port": {
          "uuid": "2d39df72-f70d-11e8-b145-005056bb5b8e",
          "name": "e0e",
          "node": {
            "name": "user-cluster-01"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/2d39df72-f70d-11e8-b145-005056bb5b8e"
            }
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/88b2f682-fa42-11e8-a6d7-005056bb5b8e"
        }
      }
    }
  ]
}
```
---
### Creating a LAG (ifgrp) port
The following output displays the record returned after the creation of a LAG port with "e0f", "e0g" and "e0h" as member ports.
<br/>
---
```
# The API:
/api/network/ethernet/ports
# The call:
curl -X POST "https://<mgmt-ip>/api/network/ethernet/ports?return_records=true" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"type\": \"lag\",  \"node\": { \"name\": \"user-cluster-01\"  }, \"broadcast_domain\": { \"name\": \"Default\", \"ipspace\": { \"name\": \"Default\" } }, \"enabled\": true, \"lag\": { \"mode\": \"singlemode\", \"distribution_policy\": \"mac\", \"member_ports\": [ { \"name\": \"e0f\", \"node\": { \"name\": \"user-cluster-01\" } }, { \"name\": \"e0g\", \"node\": { \"name\": \"user-cluster-01\" }}, { \"name\": \"e0h\", \"node\": { \"name\": \"user-cluster-01\" } } ]  } }" -u admin:netapp1! -k
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "1807772a-fa4d-11e8-a6d7-005056bb5b8e",
      "type": "lag",
      "node": {
        "uuid": "faa56898-f70c-11e8-b145-005056bb5b8e",
        "name": "user-cluster-01"
      },
      "broadcast_domain": {
        "uuid": "36434bec-f70d-11e8-b145-005056bb5b8e",
        "name": "Default",
        "ipspace": {
          "name": "Default"
        }
      },
      "enabled": true,
      "lag": {
        "mode": "singlemode",
        "distribution_policy": "mac",
        "member_ports": [
          {
            "uuid": "2d3c9adc-f70d-11e8-b145-005056bb5b8e",
            "name": "e0f",
            "node": {
              "name": "user-cluster-01"
            }
          },
          {
            "uuid": "2d40b097-f70d-11e8-b145-005056bb5b8e",
            "name": "e0g",
            "node": {
              "name": "user-cluster-01"
            }
          },
          {
            "uuid": "2d46d01e-f70d-11e8-b145-005056bb5b8e",
            "name": "e0h",
            "node": {
              "name": "user-cluster-01"
            }
          }
        ]
      }
    }
  ]
}
```
---
## Updating ports
You can use the network ports PATCH API to update the attributes of ports.
<br/>
---
## Examples
### Updating the broadcast domain of a port
The following PATCH request removes the port from the current broadcast domain and adds it to the specified broadcast domain.
<br/>
---
```
# The API:
/api/network/ethernet/ports/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/ethernet/ports/6867efaf-d702-11e8-994f-005056bbc994" -H  "accept: application/hal+json" -H  "Content-Type: application/json" -d "{ \"broadcast_domain\": { \"name\": \"Default\", \"ipspace\": { \"name\": \"Default\" }}}"
```
---
### Updating the admin status of a port
The following PATCH request brings the specified port down.
<br/>
---
```
# The API:
/api/network/ethernet/ports/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/ethernet/ports/51d3ab39-d86d-11e8-aca6-005056bbc994" -H  "accept: application/hal+json" -H  "Content-Type: application/json" -d "{ \"enabled\": \"false\" }"
```
---
## Deleting ports
You can use the network ports DELETE API to delete VLAN and LAG ports in the cluster. Note that physical ports cannot be deleted.
Deleting a port also removes the port from the broadcast domain.
---
## Example
### Deleting a VLAN port
The network ports DELETE API is used to delete a VLAN port.
<br/>
---
```
# The API:
/api/network/ethernet/ports/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/network/ethernet/ports/6867efaf-d702-11e8-994f-005056bbc994" -H  "accept: application/hal+json" -H  "Content-Type: application/json"
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


__all__ = ["Port", "PortSchema"]
__pdoc__ = {
    "PortSchema.resource": False,
    "PortSchema.patchable_fields": False,
    "PortSchema.postable_fields": False,
}


class PortSchema(ResourceSchema):
    """The fields of the Port object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the port. """

    broadcast_domain = fields.Nested("netapp_ontap.resources.broadcast_domain.BroadcastDomainSchema", data_key="broadcast_domain", unknown=EXCLUDE)
    r""" The broadcast_domain field of the port. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The enabled field of the port. """

    lag = fields.Nested("netapp_ontap.models.port_lag.PortLagSchema", data_key="lag", unknown=EXCLUDE)
    r""" The lag field of the port. """

    mac_address = fields.Str(
        data_key="mac_address",
    )
    r""" The mac_address field of the port.

Example: 01:02:03:04:05:06 """

    mtu = fields.Integer(
        data_key="mtu",
        validate=integer_validation(minimum=68),
    )
    r""" MTU of the port in bytes. Set by broadcast domain.

Example: 1500 """

    name = fields.Str(
        data_key="name",
    )
    r""" Portname, such as e0a, e1b-100 (VLAN on ethernet), a0c (LAG/ifgrp), a0d-200 (vlan on LAG/ifgrp)

Example: e1b """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the port. """

    speed = fields.Integer(
        data_key="speed",
    )
    r""" Link speed in Mbps

Example: 1000 """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['up', 'down']),
    )
    r""" Operational state of the port.

Valid choices:

* up
* down """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['vlan', 'physical', 'lag']),
    )
    r""" Type of physical or virtual port

Valid choices:

* vlan
* physical
* lag """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Port UUID

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    vlan = fields.Nested("netapp_ontap.models.port_vlan.PortVlanSchema", data_key="vlan", unknown=EXCLUDE)
    r""" The vlan field of the port. """

    @property
    def resource(self):
        return Port

    @property
    def patchable_fields(self):
        return [
            "broadcast_domain.ipspace",
            "broadcast_domain.name",
            "broadcast_domain.uuid",
            "enabled",
            "lag",
        ]

    @property
    def postable_fields(self):
        return [
            "broadcast_domain.ipspace",
            "broadcast_domain.name",
            "broadcast_domain.uuid",
            "enabled",
            "lag",
            "node.name",
            "node.uuid",
            "type",
            "vlan",
        ]

class Port(Resource):
    """Allows interaction with Port objects on the host"""

    _schema = PortSchema
    _path = "/api/network/ethernet/ports"
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
        r"""Retrieves a collection of ports (physical, VLAN and LAG) for an entire cluster.
### Related ONTAP commands
* `network port show`
* `network port ifgrp show`
* `network port vlan show`

### Learn more
* [`DOC /network/ethernet/ports`](#docs-networking-network_ethernet_ports)"""
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
        r"""Updates a port.
### Related ONTAP commands
* `network port broadcast-domain add-ports`
* `network port broadcast-domain remove-ports`
* `network port ifgrp modify`
* `network port modify`
* `network port vlan modify`

### Learn more
* [`DOC /network/ethernet/ports`](#docs-networking-network_ethernet_ports)"""
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
        r"""Deletes a VLAN or LAG.
### Related ONTAP commands
* `network port ifgrp delete`
* `network port vlan delete`

### Learn more
* [`DOC /network/ethernet/ports`](#docs-networking-network_ethernet_ports)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of ports (physical, VLAN and LAG) for an entire cluster.
### Related ONTAP commands
* `network port show`
* `network port ifgrp show`
* `network port vlan show`

### Learn more
* [`DOC /network/ethernet/ports`](#docs-networking-network_ethernet_ports)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the details of a physical port, VLAN, or LAG.
### Related ONTAP commands
* `network port show`
* `network port ifgrp show`
* `network port vlan show`

### Learn more
* [`DOC /network/ethernet/ports`](#docs-networking-network_ethernet_ports)"""
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
        r"""Creates a new VLAN (such as node1:e0a-100) or LAG (ifgrp, such as node2:a0a).
### Required properties
* `node` - Node the port will be created on.
* `broadcast_domain` - Broadcast domain the port is associated with.
* `type` - Defines if a VLAN or LAG will be created:
  * VLAN
    * `vlan.base_port` - Physical port or LAG the VLAN will be created on.
    * `vlan.tag` - Tag used to identify VLAN on the base port.
  * LAG
    * `lag.mode` - Policy for the LAG that will be created.
    * `lag.distribution_policy` - Indicates how the packets are distributed between ports.
    * `lag.member_ports` - Set of ports the LAG consists of.
### Related ONTAP commands
* `network port ifgrp create`
* `network port vlan create`

### Learn more
* [`DOC /network/ethernet/ports`](#docs-networking-network_ethernet_ports)"""
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
        r"""Updates a port.
### Related ONTAP commands
* `network port broadcast-domain add-ports`
* `network port broadcast-domain remove-ports`
* `network port ifgrp modify`
* `network port modify`
* `network port vlan modify`

### Learn more
* [`DOC /network/ethernet/ports`](#docs-networking-network_ethernet_ports)"""
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
        r"""Deletes a VLAN or LAG.
### Related ONTAP commands
* `network port ifgrp delete`
* `network port vlan delete`

### Learn more
* [`DOC /network/ethernet/ports`](#docs-networking-network_ethernet_ports)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


