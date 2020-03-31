# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
A LUN is the logical representation of storage in a storage area network (SAN).<br/>
The LUN REST API allows you to create, update, delete, and discover LUNs.<br/>
In ONTAP, a LUN is located within a volume. Optionally, it can be located within a qtree in a volume.<br/>
A LUN can be created to a specified size using thin or thick provisioning. A LUN can then be renamed, resized, cloned, and moved to a different volume. LUNs support the assignment of a quality of service (QoS) policy for performance management or a QoS policy can be assigned to the volume containing the LUN. See the LUN object model to learn more about each of the properties supported by the LUN REST API.<br/>
A LUN must be mapped to an initiator group to grant access to the initiator group's initiators (client hosts). Initiators can then access the LUN and perform I/O over a Fibre Channel (FC) fabric using the FC Protocol or a TCP/IP network using iSCSI.
## Performance monitoring
Performance of a LUN can be monitored by observing the `metric.*` and `statistics.*` properties. These properties show the performance of a LUN in terms of IOPS, latency and throughput. The `metric.*` properties denote an average whereas `statistics.*` properies denote a real-time monotonically increasing value aggregated across all nodes.
## Examples
### Creating a LUN
This example creates a 300 gigabyte, thin-provisioned LUN in SVM _svm1_, volume _vol1_, configured for use by _linux_ initiators. The `return_records` query parameter is used to retrieve properties of the newly created LUN in the POST response.
<br/>
```
# The API:
POST /api/storage/luns
# The call:
curl -X POST 'https://<mgmt-ip>/api/storage/luns?return_records=true' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "os_type": "linux", "space": { "size": "300G" }, "name" : "/vol/vol1/lun1" }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "5a24ae5b-28af-47fb-b129-5adf6cfba0a6",
      "svm": {
        "uuid": "6bf967fd-2a1c-11e9-b682-005056bbc17d",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/6bf967fd-2a1c-11e9-b682-005056bbc17d"
          }
        }
      },
      "name": "/vol/vol1/lun1",
      "location": {
        "logical_unit": "lun1",
        "volume": {
          "uuid": "71cd0dba-2a1c-11e9-b682-005056bbc17d",
          "name": "vol1",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/71cd0dba-2a1c-11e9-b682-005056bbc17d"
            }
          }
        }
      },
      "class": "regular",
      "enabled": true,
      "os_type": "linux",
      "serial_number": "wf0Iq+N4uck3",
      "space": {
        "size": 322163441664,
        "used": 0,
        "guarantee": {
          "requested": false,
          "reserved": false
        }
      },
      "status": {
        "container_state": "online",
        "read_only": false,
        "state": "online"
      },
      "_links": {
        "self": {
          "href": "/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6"
        }
      }
    }
  ]
}
```
---
### Updating a LUN
This example sets the `comment` property of a LUN.
<br/>
```
# The API:
PATCH /api/storage/luns/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6' -H 'accept: application/hal+json' -d '{ "comment": "Data for the finance department." }'
```
---
### Retrieving LUNs
This example retrieves summary information for all online LUNs in SVM _svm1_. The `svm.name` and `status.state` query parameters are used to find the desired LUNs.
<br/>
```
# The API:
GET /api/storage/luns
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/luns?svm.name=svm1&status.state=online' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "uuid": "5a24ae5b-28af-47fb-b129-5adf6cfba0a6",
      "svm": {
        "name": "svm1"
      },
      "name": "/vol/vol1/lun1",
      "status": {
        "state": "online"
      },
      "_links": {
        "self": {
          "href": "/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6"
        }
      }
    },
    {
      "uuid": "c903a978-9bac-4ce9-8237-4a3ba8b13f08",
      "svm": {
        "name": "svm1"
      },
      "name": "/vol/vol1/lun2",
      "status": {
        "state": "online"
      },
      "_links": {
        "self": {
          "href": "/api/storage/luns/c903a978-9bac-4ce9-8237-4a3ba8b13f08"
        }
      }
    },
    {
      "uuid": "7faf0a9e-0a47-4876-8318-3638d5da16bf",
      "svm": {
        "name": "svm1"
      },
      "name": "/vol/vol2/lun3",
      "status": {
        "state": "online"
      },
      "_links": {
        "self": {
          "href": "/api/storage/luns/7faf0a9e-0a47-4876-8318-3638d5da16bf"
        }
      }
    }
  ],
  "num_records": 3,
  "_links": {
    "self": {
      "href": "/api/storage/luns?svm.name=svm1&status.state=online"
    }
  }
}
```
---
### Retrieving details for a specific LUN
In this example, the `fields` query parameter is used to request all fields, including advanced fields, that would not otherwise be returned by default for the LUN.
<br/>
```
# The API:
GET /api/storage/luns/{uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6?fields=**' -H 'accept: application/hal+json'
# The response:
{
  "uuid": "5a24ae5b-28af-47fb-b129-5adf6cfba0a6",
  "svm": {
    "uuid": "6bf967fd-2a1c-11e9-b682-005056bbc17d",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/6bf967fd-2a1c-11e9-b682-005056bbc17d"
      }
    }
  },
  "name": "/vol/vol1/lun1",
  "location": {
    "logical_unit": "lun1",
    "volume": {
      "uuid": "71cd0dba-2a1c-11e9-b682-005056bbc17d",
      "name": "vol1",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/71cd0dba-2a1c-11e9-b682-005056bbc17d"
        }
      }
    }
  },
  "auto_delete": false,
  "class": "regular",
  "comment": "Data for the finance department.",
  "enabled": true,
  "lun_maps": [
    {
      "logical_unit_number": 0,
      "igroup": {
        "uuid": "2b9d57e1-2a66-11e9-b682-005056bbc17d",
        "name": "ig1",
        "_links": {
          "self": {
            "href": "/api/protocols/san/igroups/2b9d57e1-2a66-11e9-b682-005056bbc17d"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/protocols/san/lun-maps/5a24ae5b-28af-47fb-b129-5adf6cfba0a6/2b9d57e1-2a66-11e9-b682-005056bbc17d"
        }
      }
    }
  ],
  "os_type": "linux",
  "serial_number": "wf0Iq+N4uck3",
  "space": {
    "size": 322163441664,
    "used": 0,
    "guarantee": {
      "requested": false,
      "reserved": false
    }
  },
 "metric": {
    "timestamp": "2019-04-09T05:50:15Z",
    "duration": "PT15S",
    "status": "ok",
    "latency": {
      "other": 0,
      "total": 0,
      "read": 0,
      "write": 0
    },
    "iops": {
      "read": 0,
      "write": 0,
      "other": 0,
      "total": 0
    },
    "throughput": {
      "read": 0,
      "write": 0,
      "other": 0,
      "total": 0
    }
  },
  "statistics": {
    "timestamp": "2019-04-09T05:50:42Z",
    "status": "ok",
    "latency_raw": {
      "other": 38298,
      "total": 38298,
      "read": 0,
      "write": 0
    },
    "iops_raw": {
      "read": 0,
      "write": 0,
      "other": 3,
      "total": 3
    },
    "throughput_raw": {
      "read": 0,
      "write": 0,
      "other": 0,
      "total": 0
    }
  },
  "status": {
    "container_state": "online",
    "mapped": true,
    "read_only": false,
    "state": "online"
  },
  "_links": {
    "self": {
      "href": "/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6?fields=**"
    }
  }
}
```
---
## Cloning LUNs
A clone of a LUN is an independent "copy" of the LUN that shares unchanged data blocks with the original. As blocks of the source and clone are modified, unique blocks are written for each. LUN clones can be created quickly and consume very little space initially. They can be created for the purpose of back-up, or to replicate data for multiple consumers.<br/>
Space reservations can be set for the LUN clone independent of the source LUN by setting the `space.guarantee.requested` property in a POST or PATCH request.<br/>
A LUN clone can also be set to auto-delete by setting the `auto_delete` property. If the LUN's volume is configured for automatic deletion, LUNs that have auto-delete enabled are deleted when a volume is nearly full to reclaim a target amount of free space in the volume.
## Examples
### Creating a new LUN clone
You create a new LUN clone as you create any LUN - a POST request to [`/storage/luns`](#/SAN/lun_create). Set `clone.source.uuid` or `clone.source.name` to identify the source LUN from which the clone is created. The LUN clone and its source must reside in the same volume.
<br/>
The source LUN can reside in a Snapshot copy, in which case the `clone.source.name` field must be used to identify it. Add `/.snapshot/<snapshot_name>` to the path after the volume name to identify the Snapshot copy. For example `/vol/vol1/.snapshot/snap1/lun1`.
<br/>
By default, new LUN clones do not inherit the QoS policy of the source LUN; a QoS policy should be set for the clone by setting the `qos_policy` property.
<br/>
```
# The API:
POST /api/storage/luns
# The call:
curl -X POST 'https://<mgmt-ip>/api/storage/luns' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "name": "/vol/vol1/lun2clone1", "clone": { "source": { "name": "/vol/vol1/lun2" } }, "qos_policy": { "name": "qos1" } }'
```
### Over-writing an existing LUN's data as a clone of another
You can overwrite an existing LUN as a clone of another, using a PATCH request to [`/storage/luns/{uuid}`](#/SAN/lun_modify). Set the `clone.source.uuid` or `clone.source.name` property to identify the source LUN from which the clone data is taken. The LUN clone and its source must reside in the same volume.<br/>
When used in a PATCH request, the patched LUN's data is overwritten as a clone of the source. The following properties are preserved from the patched LUN unless otherwise specified as part of the PATCH: `class`, `auto_delete`, `lun_maps`, `serial_number`, `status.state`, and `uuid`.<br/>
Persistent reservations for the updated LUN are also preserved.
<br/>
```
# The API:
PATCH /api/storage/luns/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6' -H 'accept: application/hal+json' -d '{ "clone": { "source": { "name": "/vol/vol1/lun2" } } }'
```
---
## Moving LUNs between volumes
You move a LUN between volumes by using a PATCH request to [`/storage/luns/{uuid}`](#/SAN/lun_modify). Set the volume portion of the fully qualified LUN path `name` property, `path.volume.uuid`, or `path.volume.name` property to a different volume than the LUN's current volume. Moving a LUN between volumes is an asynchronous activity. A successful request returns a response of 200 synchronously, which indicates that the movement has been successfully queued. The LUN object can then be further polled with a GET request to [`/storage/luns/{uuid}`](#lun_get) to monitor the status of the movement.<br/>
The `movement` sub-object of the LUN object is populated while a LUN movement is in progress and for two minutes following completion of a movement.
## Examples
### Starting a LUN movement
```
# The API:
PATCH /api/storage/luns/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/storage/luns/7faf0a9e-0a47-4876-8318-3638d5da16bf' -H 'accept: application/hal+json' -d '{ "name": "/vol/vol1/lun3" }'
```
### Checking on the status of the LUN movement
```
# The API:
GET /api/storage/luns/{uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/luns/7faf0a9e-0a47-4876-8318-3638d5da16bf?fields=movement' -H 'accept: application/hal+json'
# The response:
{
  "uuid": "7faf0a9e-0a47-4876-8318-3638d5da16bf",
  "name": "/vol/vol1/lun3",
  "movement": {
    "paths": {
      "destination": "/vol/vol1/lun3",
      "source": "/vol/vol2/lun3"
    },
    "progress": {
      "elapsed": 1,
      "percent_complete": 0,
      "state": "preparing",
      "volume_snapshot_blocked": false
    }
  },
  "_links": {
    "self": {
      "href": "/api/storage/luns/7faf0a9e-0a47-4876-8318-3638d5da16bf"
    }
  }
}
```
---
### Deleting a LUN
```
# The API:
DELETE /api/storage/luns/{uuid}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/storage/luns/c903a978-9bac-4ce9-8237-4a3ba8b13f08' -H 'accept: application/hal+json'
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


__all__ = ["Lun", "LunSchema"]
__pdoc__ = {
    "LunSchema.resource": False,
    "LunSchema.patchable_fields": False,
    "LunSchema.postable_fields": False,
}


class LunSchema(ResourceSchema):
    """The fields of the Lun object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the lun. """

    auto_delete = fields.Boolean(
        data_key="auto_delete",
    )
    r""" This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/>
When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/>
This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/>
There is an added cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more. """

    class_ = fields.Str(
        data_key="class",
        validate=enum_validation(['regular', 'protocol_endpoint', 'vvol']),
    )
    r""" The class of LUN. Only _regular_ LUNs can be created using the REST API.


Valid choices:

* regular
* protocol_endpoint
* vvol """

    clone = fields.Nested("netapp_ontap.models.lun_clone.LunCloneSchema", data_key="clone", unknown=EXCLUDE)
    r""" The clone field of the lun. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=254),
    )
    r""" A configurable comment available for use by the administrator. Valid in POST and PATCH. """

    create_time = fields.DateTime(
        data_key="create_time",
    )
    r""" The time the LUN was created.

Example: 2018-06-04T19:00:00.000+0000 """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. """

    location = fields.Nested("netapp_ontap.models.lun_location.LunLocationSchema", data_key="location", unknown=EXCLUDE)
    r""" The location field of the lun. """

    lun_maps = fields.List(fields.Nested("netapp_ontap.models.lun_lun_maps.LunLunMapsSchema", unknown=EXCLUDE), data_key="lun_maps")
    r""" The LUN maps with which the LUN is associated.<br/>
There is an added cost to retrieving property values for `lun_maps`. They are not populated for either a collection GET or an instance GET unless explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more. """

    metric = fields.Nested("netapp_ontap.resources.performance_metric.PerformanceMetricSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the lun. """

    movement = fields.Nested("netapp_ontap.models.lun_movement.LunMovementSchema", data_key="movement", unknown=EXCLUDE)
    r""" The movement field of the lun. """

    name = fields.Str(
        data_key="name",
    )
    r""" The fully qualified path name of the LUN composed of a "/vol" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/>
A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/>
A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation.


Example: /vol/volume1/qtree1/lun1 """

    os_type = fields.Str(
        data_key="os_type",
        validate=enum_validation(['aix', 'hpux', 'hyper_v', 'linux', 'netware', 'openvms', 'solaris', 'solaris_efi', 'vmware', 'windows', 'windows_2008', 'windows_gpt', 'xen']),
    )
    r""" The operating system type of the LUN.<br/>
Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone.


Valid choices:

* aix
* hpux
* hyper_v
* linux
* netware
* openvms
* solaris
* solaris_efi
* vmware
* windows
* windows_2008
* windows_gpt
* xen """

    qos_policy = fields.Nested("netapp_ontap.models.lun_qos_policy.LunQosPolicySchema", data_key="qos_policy", unknown=EXCLUDE)
    r""" The qos_policy field of the lun. """

    serial_number = fields.Str(
        data_key="serial_number",
        validate=len_validation(minimum=12, maximum=12),
    )
    r""" The LUN serial number. The serial number is generated by ONTAP when the LUN is created. """

    space = fields.Nested("netapp_ontap.models.lun_space.LunSpaceSchema", data_key="space", unknown=EXCLUDE)
    r""" The space field of the lun. """

    statistics = fields.Nested("netapp_ontap.models.performance_metric_raw.PerformanceMetricRawSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the lun. """

    status = fields.Nested("netapp_ontap.models.lun_status.LunStatusSchema", data_key="status", unknown=EXCLUDE)
    r""" The status field of the lun. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the lun. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return Lun

    @property
    def patchable_fields(self):
        return [
            "auto_delete",
            "clone",
            "comment",
            "enabled",
            "location",
            "movement",
            "name",
            "qos_policy",
            "space",
            "statistics.iops_raw",
            "statistics.latency_raw",
            "statistics.throughput_raw",
            "status",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "auto_delete",
            "clone",
            "comment",
            "location",
            "movement",
            "name",
            "os_type",
            "qos_policy",
            "space",
            "statistics.iops_raw",
            "statistics.latency_raw",
            "statistics.throughput_raw",
            "status",
            "svm.name",
            "svm.uuid",
        ]

class Lun(Resource):
    r""" A LUN is the logical representation of storage in a storage area network (SAN).<br/>
In ONTAP, a LUN is located within a volume. Optionally, it can be located within a qtree in a volume.<br/>
A LUN can be created to a specified size using thin or thick provisioning. A LUN can then be renamed, resized, cloned, and moved to a different volume. LUNs support the assignment of a quality of service (QoS) policy for performance management or a QoS policy can be assigned to the volume containing the LUN. See the LUN object model to learn more about each of the properties supported by the LUN REST API.<br/>
A LUN must be mapped to an initiator group to grant access to the initiator group's initiators (client hosts). Initiators can then access the LUN and perform I/O over a Fibre Channel (FC) fabric using the Fibre Channel Protocol or a TCP/IP network using iSCSI. """

    _schema = LunSchema
    _path = "/api/storage/luns"
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
        r"""Retrieves LUNs.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `auto_delete`
* `lun_maps.*`
* `movement.*`
* `status.mapped`
* `statistics.*`
* `metrics.*`
### Related ONTAP commands
* `lun mapping show`
* `lun move show`
* `lun show`
* `volume file clone show-autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
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
        r"""Updates the properties of a LUN. A PATCH request can also be be used to overwrite the contents of a LUN as a clone of another, to begin movement of a LUN between volumes, and to pause and resume the movement of a LUN between volumes.
### Related ONTAP commands
* `lun modify`
* `lun move modify`
* `lun move pause`
* `lun move resume`
* `lun move start`
* `lun resize`
* `volume file clone autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
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
        r"""Deletes a LUN.
### Related ONTAP commands
* `lun delete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves LUNs.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `auto_delete`
* `lun_maps.*`
* `movement.*`
* `status.mapped`
* `statistics.*`
* `metrics.*`
### Related ONTAP commands
* `lun mapping show`
* `lun move show`
* `lun show`
* `volume file clone show-autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a LUN.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `auto_delete`
* `lun_maps.*`
* `movement.*`
* `status.mapped`
* `statistics.*`
* `metrics.*`
### Related ONTAP commands
* `lun mapping show`
* `lun move show`
* `lun show`
* `volume file clone show-autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
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
        r"""Creates a LUN.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the LUN.
* `name`, `location.volume.name` or `location.volume.uuid` - Existing volume in which to create the LUN.
* `name` or `location.logical_unit` - Base name of the LUN.
* `os_type` - Operating system from which the LUN will be accessed. Required when creating a non-clone LUN and disallowed when creating a clone of an existing LUN. A clone's `os_type` is taken from the source LUN.
* `space.size` - Size of the LUN. Required when creating a non-clone LUN and disallowed when creating a clone of an existing LUN. A clone's size is taken from the source LUN.
### Recommended optional properties
* `qos_policy.name` or `qos_policy.uuid` - Existing traditional or adaptive QoS policy to be applied to the LUN. All LUNs should be managed by a QoS policy at the volume or LUN level.
### Default property values
If not specified in POST, the follow default property values are assigned.
* `auto_delete` - _false_
### Related ONTAP commands
* `lun create`
* `volume file clone autodelete`
* `volume file clone create`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
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
        r"""Updates the properties of a LUN. A PATCH request can also be be used to overwrite the contents of a LUN as a clone of another, to begin movement of a LUN between volumes, and to pause and resume the movement of a LUN between volumes.
### Related ONTAP commands
* `lun modify`
* `lun move modify`
* `lun move pause`
* `lun move resume`
* `lun move start`
* `lun resize`
* `volume file clone autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
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
        r"""Deletes a LUN.
### Related ONTAP commands
* `lun delete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


