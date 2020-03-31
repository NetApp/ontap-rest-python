# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Retrieving storage port information
The storage port GET API retrieves all of the storage ports in the cluster.
<br/>
---
## Examples
### 1) Retrieve a list of storage ports from the cluster
#### The following example shows the response with a list of storage ports in the cluster:
---
```
# The API:
/api/storage/ports
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/ports" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "name": "0a",
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0a"
        }
      }
    },
    {
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "name": "0b",
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0b"
        }
      }
    },
    {
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "name": "0c",
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0c"
        }
      }
    },
    {
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "name": "0d",
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0d"
        }
      }
    },
    {
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "name": "0e",
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0e"
        }
      }
    },
    {
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "name": "0f",
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0f"
        }
      }
    },
    {
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "name": "0g",
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0g"
        }
      }
    },
  ],
  "num_records": 7,
  "_links": {
    "self": {
      "href": "/api/storage/ports"
    }
  }
}
```
---
### 2) Retrieve a specific storage port from the cluster
#### The following example shows the response of the requested storage port. If there is no storage port with the requested node uuid and name, an error is returned.
---
```
# The API:
/api/storage/ports/{node.uuid}/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0a" -H "accept: application/hal+json"
# The response:
{
  "node": {
    "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
    "name": "node-1",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
      }
    }
  },
  "name": "0a",
  "description": "SAS Host Adapter 0a (PMC-Sierra PM8001 rev. C)",
  "wwn": "500a098003633df0",
  "speed": 6,
  "cable": {
    "part_number": "112-00429+A0",
    "serial_number": "629230774",
    "identifier": "500a0980066e2c01-500a098003633df0",
    "length": "0.5m"
  },
  "state": "online",
  "_links": {
    "self": {
      "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0a"
    }
  }
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


__all__ = ["StoragePort", "StoragePortSchema"]
__pdoc__ = {
    "StoragePortSchema.resource": False,
    "StoragePortSchema.patchable_fields": False,
    "StoragePortSchema.postable_fields": False,
}


class StoragePortSchema(ResourceSchema):
    """The fields of the StoragePort object"""

    board_name = fields.Str(
        data_key="board_name",
    )
    r""" The board_name field of the storage_port. """

    cable = fields.Nested("netapp_ontap.models.shelf_cable.ShelfCableSchema", data_key="cable", unknown=EXCLUDE)
    r""" The cable field of the storage_port. """

    description = fields.Str(
        data_key="description",
    )
    r""" The description field of the storage_port.

Example: SAS Host Adapter 2a (PMC-Sierra PM8072 rev. C) """

    error = fields.Nested("netapp_ontap.models.storage_port_error.StoragePortErrorSchema", data_key="error", unknown=EXCLUDE)
    r""" The error field of the storage_port. """

    mac_address = fields.Str(
        data_key="mac_address",
    )
    r""" The mac_address field of the storage_port. """

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the storage_port.

Example: 2a """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the storage_port. """

    part_number = fields.Str(
        data_key="part_number",
    )
    r""" The part_number field of the storage_port.

Example: 111-03801 """

    serial_number = fields.Str(
        data_key="serial_number",
    )
    r""" The serial_number field of the storage_port.

Example: 7A2463CC45B """

    speed = fields.Number(
        data_key="speed",
    )
    r""" Operational port speed in Gbps

Example: 6.0 """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['online', 'offline', 'error']),
    )
    r""" The state field of the storage_port.

Valid choices:

* online
* offline
* error """

    wwn = fields.Str(
        data_key="wwn",
    )
    r""" World Wide Name

Example: 50000d1703544b80 """

    @property
    def resource(self):
        return StoragePort

    @property
    def patchable_fields(self):
        return [
            "board_name",
            "cable",
            "description",
            "error",
            "mac_address",
            "name",
            "node.name",
            "node.uuid",
            "part_number",
            "serial_number",
            "speed",
            "state",
            "wwn",
        ]

    @property
    def postable_fields(self):
        return [
            "board_name",
            "cable",
            "description",
            "error",
            "mac_address",
            "name",
            "node.name",
            "node.uuid",
            "part_number",
            "serial_number",
            "speed",
            "state",
            "wwn",
        ]

class StoragePort(Resource):
    """Allows interaction with StoragePort objects on the host"""

    _schema = StoragePortSchema
    _path = "/api/storage/ports"
    @property
    def _keys(self):
        return ["node.uuid", "name"]

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
        r"""Retrieves a collection of storage ports.
### Related ONTAP commands
* `storage port show`
### Learn more
* [`DOC /storage/ports`](#docs-storage-storage_ports)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of storage ports.
### Related ONTAP commands
* `storage port show`
### Learn more
* [`DOC /storage/ports`](#docs-storage-storage_ports)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific storage port.
### Related ONTAP commands
* `storage port show`
### Learn more
* [`DOC /storage/ports`](#docs-storage-storage_ports)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





