# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Retrieving storage shelf information
The storage shelf GET API retrieves all of the shelves in the cluster.
<br/>
---
## Examples
### 1) Retrieve a list of shelves from the cluster
#### The following example shows the response with a list of shelves in the cluster:
---
```
# The API:
/api/storage/shelves
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/shelves" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uid": "3109174803597886800",
      "_links": {
        "self": {
          "href": "/api/storage/shelves/3109174803597886800"
        }
      }
    },
    {
      "uid": "9237728366621690448",
      "_links": {
        "self": {
          "href": "/api/storage/shelves/9237728366621690448"
        }
      }
    },
    {
      "uid": "9946762738829886800",
      "_links": {
        "self": {
          "href": "/api/storage/shelves/9946762738829886800"
        }
      }
    },
    {
      "uid": "10318311901725526608",
      "_links": {
        "self": {
          "href": "/api/storage/shelves/10318311901725526608"
        }
      }
    },
    {
      "uid": "13477584846688355664",
      "_links": {
        "self": {
          "href": "/api/storage/shelves/13477584846688355664"
        }
      }
    }
  ],
  "num_records": 5,
  "_links": {
    "self": {
      "href": "/api/storage/shelves/"
    }
  }
}
```
---
### 2) Retrieve a specific shelf from the cluster
#### The following example shows the response of the requested shelf. If there is no shelf with the requested uid, an error is returned.
---
```
# The API:
/api/storage/shelves/{uid}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/shelves/3109174803597886800" -H "accept: application/hal+json"
# The response:
{
  "uid": "3109174803597886800",
  "name": "6.10",
  "id": "10",
  "serial_number": "SHU0954292N0HAH",
  "model": "DS4246",
  "module_type": "iom6",
  "internal": false,
  "state": "ok",
  "connection_type": "sas",
  "disk_count": 24,
  "paths": [
    {
      "name": "0e",
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0e"
        }
      }
    },
    {
      "name": "0g",
      "node": {
        "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
        "name": "node-1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/storage/ports/0530d6c1-8c6d-11e8-907f-00a0985a72ee/0g"
        }
      }
    }
  ],
  "bays": [
    {
      "id": 0,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 1,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 2,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 3,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 4,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 5,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 6,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 7,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 8,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 9,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 10,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 11,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 12,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 13,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 14,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 15,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 16,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 17,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 18,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 19,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 20,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 21,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 22,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    },
    {
      "id": 23,
      "has_disk": true,
      "type": "single_disk",
      "state": "ok"
    }
  ],
  "frus": [
    {
      "type": "module",
      "id": 0,
      "state": "ok",
      "part_number": "111-00690+B2",
      "serial_number": "8001900099",
      "firmware_version": "0191"
    },
    {
      "type": "module",
      "id": 1,
      "state": "ok",
      "part_number": "111-00190+B0",
      "serial_number": "7903785183",
      "firmware_version": "0191"
    },
    {
      "type": "psu",
      "id": 1,
      "state": "ok",
      "part_number": "0082562-12",
      "serial_number": "PMW82562007513E",
      "firmware_version": "0311"
    },
    {
      "type": "psu",
      "id": 2,
      "state": "ok",
      "part_number": "0082562-12",
      "serial_number": "PMW825620075138",
      "firmware_version": "0311"
    },
    {
      "type": "psu",
      "id": 3,
      "state": "ok",
      "part_number": "0082562-12",
      "serial_number": "PMW8256200750BA",
      "firmware_version": "0311"
    },
    {
      "type": "psu",
      "id": 4,
      "state": "ok",
      "part_number": "0082562-12",
      "serial_number": "PMW8256200750A2",
      "firmware_version": "0311"
    }
  ],
  "ports": [
    {
      "id": 0,
      "module_id": "a",
      "designator": "square",
      "state": "connected",
      "internal": false,
      "wwn": "500A098000C9EDBF",
      "cable": {
        "identifier": "5001086000702488-500a098000c9edbf",
        "part_number": "112-00430+A0",
        "length": "2m",
        "serial_number": "APF16510229807"
      },
      "remote": {
        "wwn": "5001086000702488",
        "phy": "08"
      }
    },
    {
      "id": 1,
      "module_id": "a",
      "designator": "circle",
      "state": "connected",
      "internal": false,
      "wwn": "500A098000C9EDBF",
      "cable": {
        "identifier": "500a098000d5c4bf-500a098000c9edbf",
        "part_number": "112-00176+A0",
        "length": "0.5-1.0m",
        "serial_number": "APF133917610YT"
      },
      "remote": {
        "wwn": "500A098000D5C4BF",
        "phy": "00"
      }
    },
    {
      "id": 2,
      "module_id": "b",
      "designator": "square",
      "state": "connected",
      "internal": false,
      "wwn": "500A098004F208BF",
      "cable": {
        "identifier": "5001086000702648-500a098004f208bf",
        "part_number": "112-00430+A0",
        "length": "2m",
        "serial_number": "APF16510229540"
      },
      "remote": {
        "wwn": "5001086000702648",
        "phy": "08"
      }
    },
    {
      "id": 3,
      "module_id": "b",
      "designator": "circle",
      "state": "connected",
      "internal": false,
      "wwn": "500A098004F208BF",
      "cable": {
        "identifier": "500a0980062ba33f-500a098004f208bf",
        "part_number": "112-00176+20",
        "length": "0.5-1.0m",
        "serial_number": "832210017"
      },
      "remote": {
        "wwn": "500A0980062BA33F",
        "phy": "00"
      }
    }
  ],
  "_links": {
    "self": {
      "href": "/api/storage/shelves/3109174803597886800"
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


__all__ = ["Shelf", "ShelfSchema"]
__pdoc__ = {
    "ShelfSchema.resource": False,
    "ShelfSchema.patchable_fields": False,
    "ShelfSchema.postable_fields": False,
}


class ShelfSchema(ResourceSchema):
    """The fields of the Shelf object"""

    bays = fields.List(fields.Nested("netapp_ontap.models.shelf_bays.ShelfBaysSchema", unknown=EXCLUDE), data_key="bays")
    r""" The bays field of the shelf. """

    connection_type = fields.Str(
        data_key="connection_type",
        validate=enum_validation(['unknown', 'fc', 'sas', 'nvme']),
    )
    r""" The connection_type field of the shelf.

Valid choices:

* unknown
* fc
* sas
* nvme """

    disk_count = fields.Integer(
        data_key="disk_count",
    )
    r""" The disk_count field of the shelf.

Example: 12 """

    drawers = fields.List(fields.Nested("netapp_ontap.models.shelf_drawers.ShelfDrawersSchema", unknown=EXCLUDE), data_key="drawers")
    r""" The drawers field of the shelf. """

    frus = fields.List(fields.Nested("netapp_ontap.models.shelf_frus.ShelfFrusSchema", unknown=EXCLUDE), data_key="frus")
    r""" The frus field of the shelf. """

    id = fields.Str(
        data_key="id",
    )
    r""" The id field of the shelf.

Example: 1 """

    internal = fields.Boolean(
        data_key="internal",
    )
    r""" The internal field of the shelf. """

    model = fields.Str(
        data_key="model",
    )
    r""" The model field of the shelf.

Example: DS2246 """

    module_type = fields.Str(
        data_key="module_type",
        validate=enum_validation(['unknown', 'iom6', 'iom6e', 'iom12', 'iom12e', 'iom12f', 'nsm100', 'psm3e']),
    )
    r""" The module_type field of the shelf.

Valid choices:

* unknown
* iom6
* iom6e
* iom12
* iom12e
* iom12f
* nsm100
* psm3e """

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the shelf.

Example: 1.1 """

    paths = fields.List(fields.Nested("netapp_ontap.resources.storage_port.StoragePortSchema", unknown=EXCLUDE), data_key="paths")
    r""" The paths field of the shelf. """

    ports = fields.List(fields.Nested("netapp_ontap.models.shelf_ports.ShelfPortsSchema", unknown=EXCLUDE), data_key="ports")
    r""" The ports field of the shelf. """

    serial_number = fields.Str(
        data_key="serial_number",
    )
    r""" The serial_number field of the shelf.

Example: SHFMS1514000895 """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['unknown', 'ok', 'error']),
    )
    r""" The state field of the shelf.

Valid choices:

* unknown
* ok
* error """

    uid = fields.Str(
        data_key="uid",
    )
    r""" The uid field of the shelf.

Example: 7777841915827391056 """

    @property
    def resource(self):
        return Shelf

    @property
    def patchable_fields(self):
        return [
            "bays",
            "connection_type",
            "disk_count",
            "drawers",
            "frus",
            "id",
            "internal",
            "model",
            "module_type",
            "name",
            "paths.name",
            "paths.node",
            "ports",
            "serial_number",
            "state",
            "uid",
        ]

    @property
    def postable_fields(self):
        return [
            "bays",
            "connection_type",
            "disk_count",
            "drawers",
            "frus",
            "id",
            "internal",
            "model",
            "module_type",
            "name",
            "paths.name",
            "paths.node",
            "ports",
            "serial_number",
            "state",
            "uid",
        ]

class Shelf(Resource):
    """Allows interaction with Shelf objects on the host"""

    _schema = ShelfSchema
    _path = "/api/storage/shelves"
    @property
    def _keys(self):
        return ["uid"]

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
        r"""Retrieves a collection of shelves.
### Related ONTAP commands
* `storage shelf show`
* `storage shelf port show`
* `storage shelf drawer show`
### Learn more
* [`DOC /storage/shelves`](#docs-storage-storage_shelves)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of shelves.
### Related ONTAP commands
* `storage shelf show`
* `storage shelf port show`
* `storage shelf drawer show`
### Learn more
* [`DOC /storage/shelves`](#docs-storage-storage_shelves)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific shelf.
### Related ONTAP commands
* `storage shelf show`
* `storage shelf port show`
* `storage shelf drawer show`
### Learn more
* [`DOC /storage/shelves`](#docs-storage-storage_shelves)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





