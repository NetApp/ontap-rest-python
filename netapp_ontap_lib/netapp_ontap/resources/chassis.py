# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
You can use the chassis GET API to retrieve all of the chassis information in the cluster.
<br/>
## Examples
### Retrieving a list of chassis from the cluster
The following example shows the response with a list of chassis in the cluster:
```
# The API:
/api/cluster/chassis
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/chassis" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "id": "021352005981",
      "_links": {
        "self": {
          "href": "/api/cluster/chassis/021352005981"
        }
      }
    },
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/cluster/chassis"
    }
  }
}
```
---
### Retrieving a specific chassis from the cluster
The following example shows the response of the requested chassis. If there is no chassis with the requested ID, an error is returned.
```
# The API:
/api/cluster/chassis/{id}
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/chassis/021352005981" -H "accept: application/hal+json"
# The response:
{
  "id": "021352005981",
  "state": "ok",
  "nodes": [
    {
      "name": "node-1",
      "uuid": "6ede364b-c3d0-11e8-a86a-00a098567f31",
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/6ede364b-c3d0-11e8-a86a-00a098567f31"
        }
      }
    }
  ],
  "frus": [
    {
      "id": "PSU2",
      "type": "psu",
      "state": "ok"
    },
    {
      "id": "PSU1",
      "type": "psu",
      "state": "ok"
    },
    {
      "id": "Fan2",
      "type": "fan",
      "state": "ok"
    },
    {
      "id": "Fan3",
      "type": "fan",
      "state": "ok"
    },
    {
      "id": "Fan1",
      "type": "fan",
      "state": "ok"
    }
  ],
  "_links": {
    "self": {
      "href": "/api/cluster/chassis/021352005981"
    }
  }
}
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Chassis", "ChassisSchema"]
__pdoc__ = {
    "ChassisSchema.resource": False,
    "ChassisSchema.patchable_fields": False,
    "ChassisSchema.postable_fields": False,
}


class ChassisSchema(ResourceSchema):
    """The fields of the Chassis object"""

    frus = fields.List(fields.Nested("netapp_ontap.models.chassis_frus.ChassisFrusSchema", unknown=EXCLUDE), data_key="frus")
    r""" List of FRUs in chassis. """

    id = fields.Str(
        data_key="id",
    )
    r""" The id field of the chassis.

Example: 2.1352005981E10 """

    nodes = fields.List(fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE), data_key="nodes")
    r""" List of nodes in chassis. """

    shelves = fields.List(fields.Nested("netapp_ontap.resources.shelf.ShelfSchema", unknown=EXCLUDE), data_key="shelves")
    r""" List of shelves in chassis. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['ok', 'error']),
    )
    r""" The state field of the chassis.

Valid choices:

* ok
* error """

    @property
    def resource(self):
        return Chassis

    @property
    def patchable_fields(self):
        return [
            "frus",
            "id",
            "nodes.name",
            "nodes.uuid",
            "shelves",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "frus",
            "id",
            "nodes.name",
            "nodes.uuid",
            "shelves",
            "state",
        ]

class Chassis(Resource):
    """Allows interaction with Chassis objects on the host"""

    _schema = ChassisSchema
    _path = "/api/cluster/chassis"
    @property
    def _keys(self):
        return ["id"]

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
        r"""Retrieves a collection of chassis.
### Related ONTAP commands
* `system chassis show`
* `system chassis fru show`
### Learn more
* [`DOC /cluster/chassis`](#docs-cluster-cluster_chassis)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of chassis.
### Related ONTAP commands
* `system chassis show`
* `system chassis fru show`
### Learn more
* [`DOC /cluster/chassis`](#docs-cluster-cluster_chassis)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific chassis.
### Related ONTAP commands
* `system chassis show`
* `system chassis fru show`
### Learn more
* [`DOC /cluster/chassis`](#docs-cluster-cluster_chassis)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





