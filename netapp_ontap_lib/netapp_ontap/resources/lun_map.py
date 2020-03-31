# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
A LUN map is an association between a LUN and an initiator group. When a LUN is mapped to an initiator group, the initiator group's initiators are granted access to the LUN. The relationship between an initiator group and a LUN is many initiator groups to many LUNs.<br/>
The LUN map REST API allows you to create, delete, and discover LUN maps.
## Examples
### Creating a LUN map
```
# The API:
POST /api/protocols/san/lun-maps
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/san/lun-maps' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "igroup": { "name": "igroup1" }, "lun": { "name": "/vol/vol1/lun1" } }'
```
---
### Retrieving all of the LUN maps
```
# The API:
GET /api/protocols/san/lun-maps
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/lun-maps' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "03157e81-24c5-11e9-9ec1-005056bba643",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/03157e81-24c5-11e9-9ec1-005056bba643"
          }
        }
      },
      "lun": {
        "uuid": "a60d9862-9bee-49a6-8162-20d2421bb1a6",
        "name": "/vol/vol1/lun1",
        "_links": {
          "self": {
            "href": "/api/storage/luns/a60d9862-9bee-49a6-8162-20d2421bb1a6"
          }
        }
      },
      "igroup": {
        "uuid": "40d98b2c-24c5-11e9-9ec1-005056bba643",
        "name": "ig1",
        "_links": {
          "self": {
            "href": "/api/protocols/san/igroups/40d98b2c-24c5-11e9-9ec1-005056bba643"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/protocols/san/lun-maps/a60d9862-9bee-49a6-8162-20d2421bb1a6/40d98b2c-24c5-11e9-9ec1-005056bba643"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/protocols/san/lun-maps"
    }
  }
}
```
---
### Retrieving a specific LUN map
```
# The API:
GET /api/protocols/san/lun-maps/{lun.uuid}/{igroup.uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/lun-maps/a60d9862-9bee-49a6-8162-20d2421bb1a6/40d98b2c-24c5-11e9-9ec1-005056bba643' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "03157e81-24c5-11e9-9ec1-005056bba643",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/03157e81-24c5-11e9-9ec1-005056bba643"
      }
    }
  },
  "lun": {
    "uuid": "a60d9862-9bee-49a6-8162-20d2421bb1a6",
    "name": "/vol/vol1/lun1",
    "node": {
      "uuid": "7d8607ea-24c1-11e9-9ec1-005056bba643",
      "name": "node1",
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/7d8607ea-24c1-11e9-9ec1-005056bba643"
        }
      }
    },
    "_links": {
      "self": {
        "href": "/api/storage/luns/a60d9862-9bee-49a6-8162-20d2421bb1a6"
      }
    }
  },
  "igroup": {
    "uuid": "40d98b2c-24c5-11e9-9ec1-005056bba643",
    "name": "ig1",
    "os_type": "linux",
    "protocol": "mixed",
    "_links": {
      "self": {
        "href": "/api/protocols/san/igroups/40d98b2c-24c5-11e9-9ec1-005056bba643"
      }
    }
  },
  "logical_unit_number": 0,
  "_links": {
    "self": {
      "href": "/api/protocols/san/lun-maps/a60d9862-9bee-49a6-8162-20d2421bb1a6/40d98b2c-24c5-11e9-9ec1-005056bba643"
    }
  }
}
```
---
### Deleting a LUN map
```
# The API:
DELETE /api/protocols/san/lun-maps/{lun.uuid}/{igroup.uuid}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/protocols/san/lun-maps/a60d9862-9bee-49a6-8162-20d2421bb1a6/40d98b2c-24c5-11e9-9ec1-005056bba643' -H 'accept: application/hal+json'
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["LunMap", "LunMapSchema"]
__pdoc__ = {
    "LunMapSchema.resource": False,
    "LunMapSchema.patchable_fields": False,
    "LunMapSchema.postable_fields": False,
}


class LunMapSchema(ResourceSchema):
    """The fields of the LunMap object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the lun_map. """

    igroup = fields.Nested("netapp_ontap.models.lun_map_igroup.LunMapIgroupSchema", data_key="igroup", unknown=EXCLUDE)
    r""" The igroup field of the lun_map. """

    logical_unit_number = fields.Integer(
        data_key="logical_unit_number",
    )
    r""" The logical unit number assigned to the LUN when mapped to the specified initiator group. The number is used to identify the LUN to initiators in the initiator group when communicating through Fibre Channel Protocol or iSCSI. Optional in POST; if no value is provided, ONTAP assigns the lowest available value.


Example: 1 """

    lun = fields.Nested("netapp_ontap.models.lun_map_lun.LunMapLunSchema", data_key="lun", unknown=EXCLUDE)
    r""" The lun field of the lun_map. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the lun_map. """

    @property
    def resource(self):
        return LunMap

    @property
    def patchable_fields(self):
        return [
            "igroup",
            "lun",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "igroup",
            "logical_unit_number",
            "lun",
            "svm.name",
            "svm.uuid",
        ]

class LunMap(Resource):
    r""" A LUN map is an association between a LUN and an initiator group. When a LUN is mapped to an initiator group, the initiator group's initiators are granted access to the LUN. The relationship between a LUN and an initiator group is many LUNs to many initiator groups. """

    _schema = LunMapSchema
    _path = "/api/protocols/san/lun-maps"
    @property
    def _keys(self):
        return ["lun.uuid", "igroup.uuid"]

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
        r"""Retrieves LUN maps.
### Related ONTAP commands
* `lun mapping show`
* [`DOC /protocols/san/lun-maps`](#docs-SAN-protocols_san_lun-maps)

### Learn more
* [`DOC /protocols/san/lun-maps`](#docs-SAN-protocols_san_lun-maps)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member


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
        r"""Deletes a LUN map.
### Related ONTAP commands
* `lun mapping delete`
### Learn more
* [`DOC /protocols/san/lun-maps`](#docs-SAN-protocols_san_lun-maps)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves LUN maps.
### Related ONTAP commands
* `lun mapping show`
* [`DOC /protocols/san/lun-maps`](#docs-SAN-protocols_san_lun-maps)

### Learn more
* [`DOC /protocols/san/lun-maps`](#docs-SAN-protocols_san_lun-maps)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a LUN map.
### Related ONTAP commands
* `lun mapping show`
### Learn more
* [`DOC /protocols/san/lun-maps`](#docs-SAN-protocols_san_lun-maps)
"""
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
        r"""Creates a LUN map.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the LUN map.
* `igroup.uuid` or `igroup.name` - Existing initiator group to map to the specified LUN.
* `lun.uuid` or `lun.name` - Existing LUN to map to the specified initiator group.
### Default property values
If not specified in POST, the following default property values are assigned.
* `logical_unit_number` - If no value is provided, ONTAP assigns the lowest available value.
### Related ONTAP commands
* `lun mapping create`
### Learn more
* [`DOC /protocols/san/lun-maps`](#docs-SAN-protocols_san_lun-maps)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member


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
        r"""Deletes a LUN map.
### Related ONTAP commands
* `lun mapping delete`
### Learn more
* [`DOC /protocols/san/lun-maps`](#docs-SAN-protocols_san_lun-maps)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


