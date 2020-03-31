# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Fibre Channel (FC) ports are the physical ports of FC adapters on ONTAP cluster nodes that can be connected to FC networks to provide FC network connectivity. An FC port defines the location of an FC interface within the ONTAP cluster.<br/>
The Fibre Channel port REST API allows you to discover FC ports, obtain status information for FC ports, and configure FC port properties. POST and DELETE requests are not supported. You must physically add and remove FC adapters to ONTAP nodes to create and remove ports from the ONTAP cluster.
## Examples
### Retrieving all FC ports
```
# The API:
GET /api/network/fc/ports
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/ports" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      },
      "uuid": "931b20f8-b047-11e8-9af3-005056bb838e",
      "name": "0a",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b20f8-b047-11e8-9af3-005056bb838e"
        }
      }
    },
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      },
      "uuid": "931b23f7-b047-11e8-9af3-005056bb838e",
      "name": "0b",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b23f7-b047-11e8-9af3-005056bb838e"
        }
      }
    },
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      },
      "uuid": "931b25ba-b047-11e8-9af3-005056bb838e",
      "name": "0c",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b25ba-b047-11e8-9af3-005056bb838e"
        }
      }
    },
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      },
      "uuid": "931b2748-b047-11e8-9af3-005056bb838e",
      "name": "0d",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b2748-b047-11e8-9af3-005056bb838e"
        }
      }
    },
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      },
      "uuid": "931b28c2-b047-11e8-9af3-005056bb838e",
      "name": "0e",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b28c2-b047-11e8-9af3-005056bb838e"
        }
      }
    },
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      },
      "uuid": "931b2a7b-b047-11e8-9af3-005056bb838e",
      "name": "0f",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b2a7b-b047-11e8-9af3-005056bb838e"
        }
      }
    },
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      },
      "uuid": "931b2e2b-b047-11e8-9af3-005056bb838e",
      "name": "1b",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b2e2b-b047-11e8-9af3-005056bb838e"
        }
      }
    }
  [,
  "num_records": 8,
  "_links": {
    "self": {
      "href": "/api/network/fc/ports"
    }
  }
}
```
---
### Retrieving all FC ports with state _online_
The `state` query parameter is used to perform the query.
<br/>
```
# The API:
GET /api/network/fc/ports
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/ports?state=online" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      }
      "uuid": "931b20f8-b047-11e8-9af3-005056bb838e",
      "name": "0a",
      "state": "online",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b20f8-b047-11e8-9af3-005056bb838e"
        }
      }
    },
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      }
      "uuid": "931b23f7-b047-11e8-9af3-005056bb838e",
      "name": "0b",
      "state": "online",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b23f7-b047-11e8-9af3-005056bb838e"
        }
      }
    },
    {
      "node": {
        "name": "node1",
        "uuid": "3c768e01-1abc-4b3b-b7c0-629ceb62a497",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/3c768e01-1abc-4b3b-b7c0-629ceb62a497"
          }
        }
      }
      "uuid": "931b25ba-b047-11e8-9af3-005056bb838e",
      "name": "0c",
      "state": "online",
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/931b25ba-b047-11e8-9af3-005056bb838e"
        }
      }
    }
  [,
  "num_records": 3,
  "_links": {
    "self": {
      "href": "/api/network/fc/ports?state=online"
    }
  }
}
```
---
### Retrieving an FC port
```
# The API:
GET /api/network/fc/ports/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/ports/931b20f8-b047-11e8-9af3-005056bb838e" -H "accept: application/hal+json"
# The response:
{
  "node": {
    "name": "node1",
    "uuid": "5a534a72-b047-11e8-9af3-005056bb838e",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/5a534a72-b047-11e8-9af3-005056bb838e"
      }
    }
  },
  "uuid": "931b20f8-b047-11e8-9af3-005056bb838e",
  "name": "0a",
  "description": "Fibre Channel Target Adapter 0a (ACME Fibre Channel Adapter, rev. 1.0.0, 8G)",
  "enabled": true,
  "fabric": {
    "connected": true,
    "connected_speed": 8,
    "name": "55:0e:b1:a0:20:40:80:00",
    "port_address": "52100",
    "switch_port": "ssan-g620-03:1"
  },
  "physical_protocol": "fibre_channel",
  "speed": {
    "maximum": "8",
    "configured": "auto"
  },
  "state": "online",
  "supported_protocols": [
    "fcp"
  ],
  "transceiver": {
    "form_factor": "SFP",
    "manufacturer": "ACME",
    "capabilities": [
      4,
      8
    ],
    "part_number": "1000"
  },
  "wwnn": "50:0a:09:80:bb:83:8e:00",
  "wwpn": "50:0a:09:82:bb:83:8e:00",
  "_links": {
    "self": {
      "href": "/api/network/fc/ports/931b20f8-b047-11e8-9af3-005056bb838e"
    }
  }
}
```
---
### Disabling an FC port
If an active FC interface exists on an FC port, the port cannot be disabled.
<br/>
```
# The API:
PATCH /api/network/fc/ports/{uuid}
# The call:
curl -X PATCH "http://<mgmt-ip>/api/network/fc/ports/931b20f8-b047-11e8-9af3-005056bb838e" -H "accept: application/hal+json" -d '{ "enabled": false }'
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["FcPort", "FcPortSchema"]
__pdoc__ = {
    "FcPortSchema.resource": False,
    "FcPortSchema.patchable_fields": False,
    "FcPortSchema.postable_fields": False,
}


class FcPortSchema(ResourceSchema):
    """The fields of the FcPort object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the fc_port. """

    description = fields.Str(
        data_key="description",
    )
    r""" A description of the FC port.


Example: Fibre Channel Target Adapter 0a (ACME Fibre Channel Adapter, rev. 1.0.0, 8G) """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The administrative state of the FC port. If this property is set to _false_, all FC connectivity to FC interfaces are blocked. Optional in PATCH. """

    fabric = fields.Nested("netapp_ontap.models.fc_port_fabric.FcPortFabricSchema", data_key="fabric", unknown=EXCLUDE)
    r""" The fabric field of the fc_port. """

    name = fields.Str(
        data_key="name",
    )
    r""" The FC port name.


Example: 0a """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the fc_port. """

    physical_protocol = fields.Str(
        data_key="physical_protocol",
        validate=enum_validation(['fibre_channel', 'ethernet']),
    )
    r""" The physical network protocol of the FC port.


Valid choices:

* fibre_channel
* ethernet """

    speed = fields.Nested("netapp_ontap.models.fc_port_speed.FcPortSpeedSchema", data_key="speed", unknown=EXCLUDE)
    r""" The speed field of the fc_port. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['startup', 'link_not_connected', 'online', 'link_disconnected', 'offlined_by_user', 'offlined_by_system', 'node_offline', 'unknown']),
    )
    r""" The operational state of the FC port.
- startup - The port is booting up.
- link_not_connected - The port has finished initialization, but a link with the fabric is not established.
- online - The port is initialized and a link with the fabric has been established.
- link_disconnected - The link was present at one point on this port but is currently not established.
- offlined_by_user - The port is administratively disabled.
- offlined_by_system - The port is set to offline by the system. This happens when the port encounters too many errors.
- node_offline - The state information for the port cannot be retrieved. The node is offline or inaccessible.


Valid choices:

* startup
* link_not_connected
* online
* link_disconnected
* offlined_by_user
* offlined_by_system
* node_offline
* unknown """

    supported_protocols = fields.List(fields.Str, data_key="supported_protocols")
    r""" The network protocols supported by the FC port. """

    transceiver = fields.Nested("netapp_ontap.models.fc_port_transceiver.FcPortTransceiverSchema", data_key="transceiver", unknown=EXCLUDE)
    r""" The transceiver field of the fc_port. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the FC port.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    wwnn = fields.Str(
        data_key="wwnn",
    )
    r""" The base world wide node name (WWNN) for the FC port.


Example: 20:00:00:50:56:b4:13:a8 """

    wwpn = fields.Str(
        data_key="wwpn",
    )
    r""" The base world wide port name (WWPN) for the FC port.


Example: 20:00:00:50:56:b4:13:a8 """

    @property
    def resource(self):
        return FcPort

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "fabric",
            "node.name",
            "node.uuid",
            "speed",
            "transceiver",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "fabric",
            "node.name",
            "node.uuid",
            "speed",
            "transceiver",
        ]

class FcPort(Resource):
    r""" A Fibre Channel (FC) port is the physical port of an FC adapter on an ONTAP cluster node that can be connected to an FC network to provide FC network connectivity. An FC port defines the location of an FC interface within the ONTAP cluster. """

    _schema = FcPortSchema
    _path = "/api/network/fc/ports"
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
        r"""Retrieves FC ports.<br/>
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `fabric.name`
### Related ONTAP commands
* `network fcp adapter show`
### Learn more
* [`DOC /network/fc/ports`](#docs-networking-network_fc_ports)
"""
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
        r"""Updates an FC port.
### Related ONTAP commands
* `network fcp adapter modify`
### Learn more
* [`DOC /network/fc/ports`](#docs-networking-network_fc_ports)
"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves FC ports.<br/>
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `fabric.name`
### Related ONTAP commands
* `network fcp adapter show`
### Learn more
* [`DOC /network/fc/ports`](#docs-networking-network_fc_ports)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an FC port.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `fabric.name`
### Related ONTAP commands
* `network fcp adapter show`
### Learn more
* [`DOC /network/fc/ports`](#docs-networking-network_fc_ports)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member


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
        r"""Updates an FC port.
### Related ONTAP commands
* `network fcp adapter modify`
### Learn more
* [`DOC /network/fc/ports`](#docs-networking-network_fc_ports)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



