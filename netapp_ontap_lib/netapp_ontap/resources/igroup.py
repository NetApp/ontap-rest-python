# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An initiator group (igroup) is a collection of Fibre Channel (FC) world wide port names (WWPNs), and/or iSCSI Qualified Names (IQNs), and/or iSCSI EUIs (Extended Unique Identifiers) that identify host initiators.<br/>
Initiator groups are used to control which hosts can access specific LUNs. To grant access to a LUN from one or more hosts, create an initiator group containing the host initiator names, then create a LUN map that associates the initiator group with the LUN.<br/>
The initator group REST API allows you to create, update, delete, and discover initiator groups, and add and remove initiators that can access the target and associated LUNs.
An initiator can appear in multiple initiator groups. An initiator group can be mapped to multiple LUNs. A specific initiator can be mapped to a specific LUN only once.<br/>
All initiators in an initiator group must be from the same operating system. The initiator group's operating system is specified when the initiator group is created.<br/>
When an initiator group is created, the `protocol` property is used to restrict member initiators to Fibre Channel (_fcp_), iSCSI (_iscsi_), or both (_mixed_).<br/>
Zero or more initiators can be supplied when the initiator group is created. After creation, initiators can be added or removed from the initiator group using the `/protocols/san/igroups/{igroup.uuid}/initiators` endpoint. See [`POST /protocols/san/igroups/{igroup.uuid}/initiators`](#/SAN/igroup_initiator_create) and [`DELETE /protocols/san/igroups/{igroup.uuid}/initiators/{name}`](#/SAN/igroup_initiator_delete) for more details.<br/>
An FC WWPN consist of 16 hexadecimal digits grouped as 8 pairs separated by colons. The format for an iSCSI IQN is _iqn.yyyy-mm.reverse_domain_name:any_. The iSCSI EUI format consists of the _eui._ prefix followed by 16 hexadecimal characters.
## Examples
### Creating an initiator group with no initiators
The example initiator group is for Linux iSCSI initiators only. Note that the `return_records` query parameter is used to obtain the newly created initiator group in the response.
<br/>
```
# The API:
POST /api/protocols/san/igroups
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/san/igroups?return_records=true' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "name": "igroup1", "os_type": "linux", "protocol": "iscsi" }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
          }
        }
      },
      "uuid": "8f249e7d-ab9f-11e8-b8a3-005056bb7072",
      "name": "igroup1",
      "protocol": "iscsi",
      "os_type": "linux",
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072"
        }
      }
    }
  ]
}
```
---
### Creating an initiator group with initiators
The example initiator group is for Windows. FC Protocol and iSCSI initiators are allowed. Note that the `return_records` query parameter is used to obtain the newly created initiator group in the response.
<br/>
```
# The API:
POST /api/protocols/san/igroups
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/san/igroups?return_records=true' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "name": "igroup2", "os_type": "windows", "protocol": "mixed", "initiators": [ { "name": "20:01:00:50:56:bb:70:72" }, { "name": "iqn.1991-05.com.ms:host1" } ] }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
          }
        }
      },
      "uuid": "abf9c39d-ab9f-11e8-b8a3-005056bb7072",
      "name": "igroup2",
      "protocol": "mixed",
      "os_type": "windows",
      "initiators": [
        {
          "name": "20:01:00:50:56:bb:70:72",
          "_links": {
            "self": {
              "href": "/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072/initiators/20:01:00:50:56:bb:70:72"
            }
          }
        },
        {
          "name": "iqn.1991-05.com.ms:host1",
          "_links": {
            "self": {
              "href": "/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072/initiators/iqn.1991-05.com.ms:host1"
            }
          }
        }
      ],
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072"
        }
      }
    }
  ]
}
```
---
### Retrieving all initiator groups
```
# The API:
GET /api/protocols/san/igroups
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/igroups' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
          }
        }
      },
      "uuid": "8f249e7d-ab9f-11e8-b8a3-005056bb7072",
      "name": "igroup1",
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072"
        }
      }
    },
    {
      "svm": {
        "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
          }
        }
      },
      "uuid": "abf9c39d-ab9f-11e8-b8a3-005056bb7072",
      "name": "igroup2",
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/san/igroups"
    }
  }
}
```
---
### Retrieving all properties of all initiator groups
The `fields` query parameter is used to request all initiator group properties.
<br/>
```
# The API:
GET /api/protocols/san/igroups
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/igroups?fields=*' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
          }
        }
      },
      "uuid": "8f249e7d-ab9f-11e8-b8a3-005056bb7072",
      "name": "igroup1",
      "protocol": "iscsi",
      "os_type": "linux",
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072"
        }
      }
    },
    {
      "svm": {
        "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
          }
        }
      },
      "uuid": "abf9c39d-ab9f-11e8-b8a3-005056bb7072",
      "name": "igroup2",
      "protocol": "mixed",
      "os_type": "windows",
      "initiators": [
        {
          "name": "20:01:00:50:56:bb:70:72",
          "_links": {
            "self": {
              "href": "/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072/initiators/20:01:00:50:56:bb:70:72"
            }
          }
        },
        {
          "name": "iqn.1991-05.com.ms:host1",
          "_links": {
            "self": {
              "href": "/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072/initiators/iqn.1991-05.com.ms:host1"
            }
          }
        }
      ],
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/san/igroups?fields=*"
    }
  }
}
```
---
### Retrieving all initiator groups for Linux
The `os_type` query parameter is used to perform the query.
<br/>
```
# The API:
GET /api/protocols/san/igroups
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/igroups?os_type=linux' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
          }
        }
      },
      "uuid": "8f249e7d-ab9f-11e8-b8a3-005056bb7072",
      "name": "igroup1",
      "os_type": "linux",
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/protocols/san/igroups?os_type=linux"
    }
  }
}
```
---
### Retrieving a specific initiator group
```
# The API:
GET /api/protocols/san/igroups/{uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
      }
    }
  },
  "uuid": "8f249e7d-ab9f-11e8-b8a3-005056bb7072",
  "name": "igroup1",
  "protocol": "iscsi",
  "os_type": "linux",
  "_links": {
    "self": {
      "href": "/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072"
    }
  }
}
```
---
### Retrieving LUNs mapped to a specific initiator group
The `fields` parameter is used to specify the desired properties.
<br/>
```
# The API:
GET /api/protocols/san/igroups
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072?fields=lun_maps' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "02b0dfff-aa28-11e8-a653-005056bb7072",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/02b0dfff-aa28-11e8-a653-005056bb7072"
      }
    }
  },
  "uuid": "8f249e7d-ab9f-11e8-b8a3-005056bb7072",
  "name": "igroup1",
  "lun_maps": [
    {
      "logical_unit_number": 0,
      "lun": {
        "name": "/vol/vol1/lun1",
        "uuid": "4b33ba57-c4e0-4dbb-bc47-214800d18a71",
        "node": {
          "name": "node1",
          "uuid": "f17182af-223f-4d51-8197-2cb2146d5c4c",
          "_links": {
            "self": {
              "href": "/api/cluster/nodes/f17182af-223f-4d51-8197-2cb2146d5c4c"
            }
          }
        },
        "_links": {
          "self": {
            "href": "/api/storage/luns/4b33ba57-c4e0-4dbb-bc47-214800d18a71"
          }
        }
      }
    }
  ]
  "_links": {
    "self": {
      "href": "/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072"
    }
  }
}
```
---
### Renaming an initiator group
Note that renaming an initiator group must be done in a PATCH request separate from any other modifications.
<br/>
```
# The API:
PATCH /api/protocols/san/igroups/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072' -H 'accept: application/hal+json' -d '{ "name": "igroup1_newName" }'
```
---
### Changing the operating system type of an initiator group
```
# The API:
PATCH /api/protocols/san/igroups/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072' -H 'accept: application/hal+json' -d '{ "os_type": "aix" }'
```
---
### Adding an initiator to an initiator group
```
# The API:
POST /api/protocols/san/igroups/{igroup.uuid}/initiators
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072/initiators' -H 'accept: application/hal+json' -d '{ "name": "iqn.1991-05.com.ms:host2" }'
```
---
### Adding multiple initiators to an initiator group
Note the use of the `records` property to add multiple initiators to the initiator group in a single API call.
<br/>
```
# The API:
POST /api/protocols/san/igroups/{igroup.uuid}/initiators
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072/initiators' -H 'accept: application/hal+json' -d '{ "records": [ { "name": "iqn.1991-05.com.ms:host3" }, { "name": "iqn.1991-05.com.ms:host4" } ] }'
```
---
### Removing an initiator from an initiator group
```
# The API:
DELETE /api/protocols/san/igroups/{igroup.uuid}/initiators/iqn.1991-05.com.ms:host3
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072/initiators/iqn.1991-05.com.ms:host3' -H 'accept: application/hal+json'
```
---
### Removing an initiator from a mapped initiator group
Normally, removing an initiator from an initiator group that is mapped to a LUN is not allowed. The removal can be forced using the `allow_delete_while_mapped` query parameter.
<br/>
```
# The API:
DELETE /api/protocols/san/igroups/{igroup.uuid}/initiators/iqn.1991-05.com.ms:host4
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/protocols/san/igroups/8f249e7d-ab9f-11e8-b8a3-005056bb7072/initiators/iqn.1991-05.com.ms:host4?allow_delete_while_mapped=true' -H 'accept: application/hal+json'
```
---
### Deleting an initiator group
```
# The API:
DELETE /api/protocols/san/igroups/{uuid}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072' -H 'accept: application/hal+json'
```
---
### Deleting a mapped initiator group
Normally, deleting an initiator group that is mapped to a LUN is not allowed. The deletion can be forced using the `allow_delete_while_mapped` query parameter.
<br/>
```
# The API:
DELETE /api/protocols/san/igroups/{uuid}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/protocols/san/igroups/abf9c39d-ab9f-11e8-b8a3-005056bb7072?allow_delete_while_mapped=true' -H 'accept: application/hal+json'
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Igroup", "IgroupSchema"]
__pdoc__ = {
    "IgroupSchema.resource": False,
    "IgroupSchema.patchable_fields": False,
    "IgroupSchema.postable_fields": False,
}


class IgroupSchema(ResourceSchema):
    """The fields of the Igroup object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the igroup. """

    delete_on_unmap = fields.Boolean(
        data_key="delete_on_unmap",
    )
    r""" An option that causes the initiator group to be deleted when the last LUN map associated with it is deleted. Optional in PATCH only; not available in POST. This property defaults to _false_ when the initiator group is created. """

    initiators = fields.List(fields.Nested("netapp_ontap.models.igroup_initiator_no_records.IgroupInitiatorNoRecordsSchema", unknown=EXCLUDE), data_key="initiators")
    r""" The initiators that are members of the group. Optional in POST.<br/>
Zero or more initiators can be supplied when the initiator group is created. After creation, initiators can be added or removed from the initiator group using the `/protocols/san/igroups/{igroup.uuid}/initiators` endpoint. See [`POST /protocols/san/igroups/{igroup.uuid}/initiators`](#/SAN/igroup_initiator_create) and [`DELETE /protocols/san/igroups/{igroup.uuid}/initiators/{name}`](#/SAN/igroup_initiator_delete) for more details. """

    lun_maps = fields.List(fields.Nested("netapp_ontap.models.igroup_lun_maps.IgroupLunMapsSchema", unknown=EXCLUDE), data_key="lun_maps")
    r""" All LUN maps with which the initiator is associated.<br/>
There is an added cost to retrieving property values for `lun_maps`. They not populated for either a collection GET or an instance GET unless explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=96),
    )
    r""" The name of the initiator group. Required in POST; optional in PATCH.<br/>
Note that renaming an initiator group must be done in a PATCH request separate from any other modifications.


Example: igroup1 """

    os_type = fields.Str(
        data_key="os_type",
        validate=enum_validation(['aix', 'hpux', 'hyper_v', 'linux', 'netware', 'openvms', 'solaris', 'vmware', 'windows', 'xen']),
    )
    r""" The host operating system of the initiator group. All initiators in the group should be hosts of the same operating system. Required in POST; optional in PATCH.


Valid choices:

* aix
* hpux
* hyper_v
* linux
* netware
* openvms
* solaris
* vmware
* windows
* xen """

    protocol = fields.Str(
        data_key="protocol",
        validate=enum_validation(['fcp', 'iscsi', 'mixed']),
    )
    r""" The protocols supported by the initiator group. This restricts the type of initiators that can be added to the initiator group. Optional in POST; if not supplied, this defaults to _mixed_.<br/>
The protocol of an initiator group cannot be changed after creation of the group.


Valid choices:

* fcp
* iscsi
* mixed """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the igroup. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the initiator group.


Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return Igroup

    @property
    def patchable_fields(self):
        return [
            "delete_on_unmap",
            "name",
            "os_type",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "initiators",
            "name",
            "os_type",
            "protocol",
            "svm.name",
            "svm.uuid",
        ]

class Igroup(Resource):
    r""" An initiator group (igroup) is a collection of Fibre Channel (FC) world wide port names (WWPN), and/or iSCSI Qualified Names (IQNs), and/or iSCSI EUIs (Extended Unique Identifiers) that identify host initiators.<br/>
Initiator groups are used to control which hosts can access specific LUNs. To grant access to a LUN from one or more hosts, create an initiator group containing the hosts' initiator names, then create a LUN map that associates the initiator group with the LUN.<br/>
An initiator can appear in multiple initiator groups. An initiator group can be mapped to multiple LUNs. A specific initiator can be mapped to a specific LUN only once.<br/>
All initiators in an initiator group must be from the same operating system. The initiator group's operating system is specified when the initiator group is created.<br/>
When an initiator group is created, the `protocol` property is used to restrict member initiators to Fibre Channel (_fcp_), iSCSI (_iscsi_), or both (_mixed_).<br/>
Zero or more initiators can be supplied when the initiator group is created. After creation, initiators can be added or removed from the initiator group using the `/protocols/san/igroups/{igroup.uuid}/initiators` endpoint. See [`POST /protocols/san/igroups/{igroup.uuid}/initiators`](#/SAN/igroup_initiator_create) and [`DELETE /protocols/san/igroups/{igroup.uuid}/initiators/{name}`](#/SAN/igroup_initiator_delete) for more details.<br/> """

    _schema = IgroupSchema
    _path = "/api/protocols/san/igroups"
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
        r"""Retrieves initiator groups.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `lun_maps.*`
### Related ONTAP commands
* `lun igroup show`
* `lun mapping show`
### Learn more
* [`DOC /protocols/san/igroups`](#docs-SAN-protocols_san_igroups)
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
        r"""Updates an initiator group.
### Related ONTAP commands
* `lun igroup modify`
* `lun igroup rename`
### Learn more
* [`DOC /protocols/san/igroups`](#docs-SAN-protocols_san_igroups)
"""
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
        r"""Deletes an initiator group.
### Related ONTAP commands
* `lun igroup delete`
### Learn more
* [`DOC /protocols/san/igroups`](#docs-SAN-protocols_san_igroups)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves initiator groups.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `lun_maps.*`
### Related ONTAP commands
* `lun igroup show`
* `lun mapping show`
### Learn more
* [`DOC /protocols/san/igroups`](#docs-SAN-protocols_san_igroups)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an initiator group.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `lun_maps.*`
### Related ONTAP commands
* `lun igroup show`
* `lun mapping show`
### Learn more
* [`DOC /protocols/san/igroups`](#docs-SAN-protocols_san_igroups)
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
        r"""Creates an initiator group.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the initiator group.
* `name` - Name of the initiator group.
* `os_type` - Operating system of the initiator group's initiators.
### Recommended optional properties
* `initiators.name` - Name(s) of initiator group's initiators. This property can be used to create the initiator group and populate it with initiators in a single request.
### Default property values
If not specified in POST, the following default property values are assigned.
* `protocol` - _mixed_ - Data protocol of the initiator group's initiators.
### Learn more
* [`DOC /protocols/san/igroups`](#docs-SAN-protocols_san_igroups)
"""
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
        r"""Updates an initiator group.
### Related ONTAP commands
* `lun igroup modify`
* `lun igroup rename`
### Learn more
* [`DOC /protocols/san/igroups`](#docs-SAN-protocols_san_igroups)
"""
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
        r"""Deletes an initiator group.
### Related ONTAP commands
* `lun igroup delete`
### Learn more
* [`DOC /protocols/san/igroups`](#docs-SAN-protocols_san_igroups)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


