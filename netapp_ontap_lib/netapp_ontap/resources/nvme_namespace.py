# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An NVMe namespace is a collection of addressable logical blocks presented to hosts connected to the storage virtual machine using the NVMe over Fabrics protocol.<br/>
The NVMe namespace REST API allows you to create, update, delete and discover NVMe namespaces.<br/>
In ONTAP, an NVMe namespace is located within a volume. Optionally, it can be located within a qtree in a volume.<br/>
An NVMe namespace is created to a specified size using thin or thick provisioning as determined by the volume on which it is created. NVMe namespaces support being cloned. An NVMe namespace cannot be renamed, resized, or moved to a different volume. NVMe namespaces do not support the assignment of a QoS policy for performance management, but a QoS policy can be assigned to the volume containing the namespace. See the NVMe namespace object model to learn more about each of the properties supported by the NVMe namespace REST API.<br/>
An NVMe namespace must be mapped to an NVMe subsystem to grant access to the subsystem's hosts. Hosts can then access the NVMe namespace and perform I/O using the NVMe over Fabrics protocol.
## Examples
### Creating an NVMe namespace
This example creates a 300 gigabyte NVMe namespace, with 4096-byte blocks, in SVM _svm1_, volume _vol1_, configured for use by _linux_ hosts. The `return_records` query parameter is used to retrieve properties of the newly created NVMe namespace in the POST response.
<br/>
```
# The API:
POST /api/storage/namespaces
# The call:
curl -X POST 'https://<mgmt-ip>/api/storage/namespaces?return_records=true' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "os_type": "linux", "space": { "block_size": "4096", "size": "300G" }, "name" : "/vol/vol1/namespace1" }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "dccdc3e6-cf4e-498f-bec6-f7897f945669",
      "svm": {
        "uuid": "6bf967fd-2a1c-11e9-b682-005056bbc17d",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/6bf967fd-2a1c-11e9-b682-005056bbc17d"
          }
        }
      },
      "name": "/vol/vol1/namespace1",
      "location": {
        "namespace": "namespace1",
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
      "enabled": true,
      "os_type": "linux",
      "space": {
        "block_size": 4096,
        "size": 322122547200,
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
          "href": "/api/storage/namespaces/dccdc3e6-cf4e-498f-bec6-f7897f945669"
        }
      }
    }
  ]
}
```
---
### Updating an NVMe namespace
This example sets the `comment` property of an NVMe namespace.
<br/>
```
# The API:
PATCH /api/storage/namespaces/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/storage/namespaces/dccdc3e6-cf4e-498f-bec6-f7897f945669' -H 'accept: application/hal+json' -d '{ "comment": "Data for the research department." }'
```
---
### Retrieving NVMe namespaces
This example retrieves summary information for all online NVMe namespaces in SVM _svm1_. The `svm.name` and `status.state` query parameters are to find the desired NVMe namespaces.
<br/>
```
# The API:
GET /api/storage/namespaces
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/namespaces?svm.name=svm1&status.state=online' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "uuid": "5c254d22-96a6-42ac-aad8-0cd9ebd126b6",
      "svm": {
        "name": "svm1"
      },
      "name": "/vol/vol1/namespace2",
      "status": {
        "state": "online"
      },
      "_links": {
        "self": {
          "href": "/api/storage/namespaces/5c254d22-96a6-42ac-aad8-0cd9ebd126b6"
        }
      }
    },
    {
      "uuid": "dccdc3e6-cf4e-498f-bec6-f7897f945669",
      "svm": {
        "name": "svm1"
      },
      "name": "/vol/vol1/namespace1",
      "status": {
        "state": "online"
      },
      "_links": {
        "self": {
          "href": "/api/storage/namespaces/dccdc3e6-cf4e-498f-bec6-f7897f945669"
        }
      }
    },
    {
      "uuid": "be732687-20cf-47d2-a0e2-2a989d15661d",
      "svm": {
        "name": "svm1"
      },
      "name": "/vol/vol2/namespace3",
      "status": {
        "state": "online"
      },
      "_links": {
        "self": {
          "href": "/api/storage/namespaces/be732687-20cf-47d2-a0e2-2a989d15661d"
        }
      }
    }
  ],
  "num_records": 3,
  "_links": {
    "self": {
      "href": "/api/storage/namespaces?svm.name=svm1&status.state=online"
    }
  }
}
```
---
### Retrieving details for a specific NVMe namespace
In this example, the `fields` query parameter is used to request all fields, including advanced fields, that would not otherwise be returned by default for the NVMe namespace.
<br/>
```
# The API:
GET /api/storage/namespaces/{uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/namespaces/dccdc3e6-cf4e-498f-bec6-f7897f945669?fields=**' -H 'accept: application/hal+json'
# The response:
{
  "uuid": "dccdc3e6-cf4e-498f-bec6-f7897f945669",
  "svm": {
    "uuid": "6bf967fd-2a1c-11e9-b682-005056bbc17d",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/6bf967fd-2a1c-11e9-b682-005056bbc17d"
      }
    }
  },
  "name": "/vol/vol1/namespace1",
  "location": {
    "namespace": "namespace1",
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
  "enabled": true,
  "comment": "Data for the research department.",
  "os_type": "linux",
  "space": {
    "block_size": 4096,
    "size": 322122547200,
    "used": 0,
    "guarantee": {
      "requested": false,
      "reserved": false
    }
  },
  "status": {
    "container_state": "online",
    "mapped": true,
    "read_only": false,
    "state": "online"
  },
  "subsystem_map": {
    "nsid": "00000001h",
    "anagrpid": "00000001h",
    "subsystem": {
      "uuid": "01f17d05-2be9-11e9-bed2-005056bbc17d",
      "name": "subsystem1",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/subsystems/01f17d05-2be9-11e9-bed2-005056bbc17d"
        }
      }
    },
    "_links": {
      "self": {
        "href": "/api/protocols/nvme/subsystem-maps/dccdc3e6-cf4e-498f-bec6-f7897f945669/01f17d05-2be9-11e9-bed2-005056bbc17d"
      }
    }
  },
  "_links": {
    "self": {
      "href": "/api/storage/namespaces/dccdc3e6-cf4e-498f-bec6-f7897f945669?fields=**"
    }
  }
}
```
---
## Cloning NVMe namespaces
A clone of an NVMe namespace is an independent "copy" of the namespace that shares unchanged data blocks with the original. As blocks of the source and clone are modified, unique blocks are written for each. NVMe namespace clones can be created quickly and consume very little space initially. They can be created for the purpose of back-up, or to replicate data for multiple consumers.<br/>
An NVMe namespace clone can also be set to auto-delete by setting the `auto_delete` property. If the namespace's volume is configured for automatic deletion, NVMe namespaces that have auto-delete enabled are deleted when a volume is nearly full to reclaim a target amount of free space in the volume.
### Creating a new NVMe namespace clone
You create an NVMe namespace clone as you create any NVMe namespace -- a POST to [`/storage/namespaces`](#/NVMe/nvme_namespace_create). Set `clone.source.uuid` or `clone.source.name` to identify the source NVMe namespace from which the clone is created. The NVMe namespace clone and its source must reside in the same volume.
<br/>
The source NVMe namespace can reside in a Snapshot copy, in which case, the `clone.source.name` field must be used to identify it. Add `/.snapshot/<snapshot_name>` to the path after the volume name to identify the Snapshot copy. For example `/vol/vol1/.snapshot/snap1/namespace1`.
<br/>
```
# The API:
POST /api/storage/namespaces
# The call:
curl -X POST 'https://<mgmt-ip>/api/storage/namespaces' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "name": "/vol/vol1/namespace2clone1", "clone": { "source": { "name": "/vol/vol1/namespace2" } } }'
```
---
### Over-writing an existing NVMe namespace's data as a clone of another
You can over-write an existing NVMe namespace as a clone of another. You do this as a PATCH on the NVMe namespace to overwrite -- a PATCH to [`/storage/namespaces/{uuid}`](#/NVMe/nvme_namespace_modify). Set the `clone.source.uuid` or `clone.source.name` property to identify the source NVMe namespace from which the clone data is taken. The NVMe namespace clone and its source must reside in the same volume.<br/>
When used in a PATCH, the patched NVMe namespace's data is over-written as a clone of the source and the following properties are preserved from the patched namespace unless otherwise specified as part of the PATCH: `auto_delete`, `subsystem_map`, `status.state`, and `uuid`.
<br/>
```
# The API:
PATCH /api/storage/namespaces/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/storage/namespaces/dccdc3e6-cf4e-498f-bec6-f7897f945669' -H 'accept: application/hal+json' -d '{ "clone": { "source": { "name": "/vol/vol1/namespace2" } } }'
```
---
## Deleting an NVMe namespace
```
# The API:
DELETE /api/storage/namespaces/{uuid}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/storage/namespaces/5c254d22-96a6-42ac-aad8-0cd9ebd126b6' -H 'accept: application/hal+json'
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


__all__ = ["NvmeNamespace", "NvmeNamespaceSchema"]
__pdoc__ = {
    "NvmeNamespaceSchema.resource": False,
    "NvmeNamespaceSchema.patchable_fields": False,
    "NvmeNamespaceSchema.postable_fields": False,
}


class NvmeNamespaceSchema(ResourceSchema):
    """The fields of the NvmeNamespace object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the nvme_namespace. """

    auto_delete = fields.Boolean(
        data_key="auto_delete",
    )
    r""" This property marks the NVMe namespace for auto deletion when the volume containing the namespace runs out of space. This is most commonly set on namespace clones.<br/>
When set to _true_, the NVMe namespace becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the namespace is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/>
This property is optional in POST and PATCH. The default value for a new NVMe namespace is _false_.<br/>
There is an added cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more. """

    clone = fields.Nested("netapp_ontap.models.nvme_namespace_clone.NvmeNamespaceCloneSchema", data_key="clone", unknown=EXCLUDE)
    r""" The clone field of the nvme_namespace. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=254),
    )
    r""" A configurable comment available for use by the administrator. Valid in POST and PATCH. """

    create_time = fields.DateTime(
        data_key="create_time",
    )
    r""" The time the NVMe namespace was created.

Example: 2018-06-04T19:00:00.000+0000 """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The enabled state of the NVMe namespace. Certain error conditions cause the namespace to become disabled. If the namespace is disabled, you can check the `state` property to determine what error disabled the namespace. An NVMe namespace is enabled automatically when it is created. """

    location = fields.Nested("netapp_ontap.models.nvme_namespace_location.NvmeNamespaceLocationSchema", data_key="location", unknown=EXCLUDE)
    r""" The location field of the nvme_namespace. """

    name = fields.Str(
        data_key="name",
    )
    r""" The fully qualified path name of the NVMe namespace composed of a "/vol" prefix, the volume name, the (optional) qtree name and base name of the namespace. Valid in POST.<br/>
NVMe namespaces do not support rename, or movement between volumes.


Example: /vol/volume1/qtree1/namespace1 """

    os_type = fields.Str(
        data_key="os_type",
        validate=enum_validation(['linux', 'vmware', 'windows']),
    )
    r""" The operating system type of the NVMe namespace.<br/>
Required in POST when creating an NVMe namespace that is not a clone of another. Disallowed in POST when creating a namespace clone.


Valid choices:

* linux
* vmware
* windows """

    space = fields.Nested("netapp_ontap.models.nvme_namespace_space.NvmeNamespaceSpaceSchema", data_key="space", unknown=EXCLUDE)
    r""" The space field of the nvme_namespace. """

    status = fields.Nested("netapp_ontap.models.nvme_namespace_status.NvmeNamespaceStatusSchema", data_key="status", unknown=EXCLUDE)
    r""" The status field of the nvme_namespace. """

    subsystem_map = fields.Nested("netapp_ontap.models.nvme_namespace_subsystem_map.NvmeNamespaceSubsystemMapSchema", data_key="subsystem_map", unknown=EXCLUDE)
    r""" The subsystem_map field of the nvme_namespace. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the nvme_namespace. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the NVMe namespace.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return NvmeNamespace

    @property
    def patchable_fields(self):
        return [
            "auto_delete",
            "clone",
            "comment",
            "status",
            "subsystem_map",
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
            "name",
            "os_type",
            "space",
            "status",
            "subsystem_map",
            "svm.name",
            "svm.uuid",
        ]

class NvmeNamespace(Resource):
    r""" An NVMe namespace is a collection of addressable logical blocks presented to hosts connected to the storage virtual machine using the NVMe over Fabrics protocol.<br/>
In ONTAP, an NVMe namespace is located within a volume. Optionally, it can be located within a qtree in a volume.<br/>
An NVMe namespace is created to a specified size using thin or thick provisioning as determined by the volume on which it is created. NVMe namespaces support being cloned. An NVMe namespace cannot be renamed, resized, or moved to a different volume. NVMe namespaces do not support the assignment of a QoS policy for performance management, but a QoS policy can be assigned to the volume containing the namespace. See the NVMe namespace object model to learn more about each of the properties supported by the NVMe namespace REST API.<br/>
An NVMe namespace must be mapped to an NVMe subsystem to grant access to the subsystem's hosts. Hosts can then access the NVMe namespace and perform I/O using the NVMe over Fabrics protocol. """

    _schema = NvmeNamespaceSchema
    _path = "/api/storage/namespaces"
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
        r"""Retrieves NVMe namespaces.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `auto_delete`
* `subsystem_map.*`
* `status.mapped`
### Related ONTAP commands
* `vserver nvme namespace show`
* `vserver nvme subsystem map show`
### Learn more
* [`DOC /storage/namespaces`](#docs-NVMe-storage_namespaces) to learn more and examples.
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
        r"""Updates an NVMe namespace.
### Related ONTAP commands
* `volume file clone autodelete`
* `vserver nvme namespace modify`
### Learn more
* [`DOC /storage/namespaces`](#docs-NVMe-storage_namespaces)
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
        r"""Deletes an NVMe namespace.
### Related ONTAP commands
* `vserver nvme namespace delete`
### Learn more
* [`DOC /storage/namespaces`](#docs-NVMe-storage_namespaces)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves NVMe namespaces.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `auto_delete`
* `subsystem_map.*`
* `status.mapped`
### Related ONTAP commands
* `vserver nvme namespace show`
* `vserver nvme subsystem map show`
### Learn more
* [`DOC /storage/namespaces`](#docs-NVMe-storage_namespaces) to learn more and examples.
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an NVMe namespace.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `auto_delete`
* `subsystem_map.*`
* `status.mapped`
### Related ONTAP commands
* `vserver nvme namespace show`
* `vserver nvme subsystem map show`
### Learn more
* [`DOC /storage/namespaces`](#docs-NVMe-storage_namespaces)
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
        r"""Creates an NVMe namespace.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the NVMe namespace.
* `name`, `location.volume.name` or `location.volume.uuid` - Existing volume in which to create the NVMe namespace.
* `name` or `location.namespace` - Base name for the NVMe namespace.
* `os_type` - Operating system from which the NVMe namespace will be accessed. (Not used for clones, which are created based on the `os_type` of the source NVMe namespace.)
* `space.size` - Size for the NVMe namespace. (Not used for clones, which are created based on the size of the source NVMe namespace.)
### Default property values
If not specified in POST, the following default property values are assigned:
* `auto_delete` - _false_
* `space.block_size` - _4096_
### Related ONTAP commands
* `volume file clone autodelete`
* `volume file clone create`
* `vserver nvme namespace create`
### Learn more
* [`DOC /storage/namespaces`](#docs-NVMe-storage_namespaces)
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
        r"""Updates an NVMe namespace.
### Related ONTAP commands
* `volume file clone autodelete`
* `vserver nvme namespace modify`
### Learn more
* [`DOC /storage/namespaces`](#docs-NVMe-storage_namespaces)
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
        r"""Deletes an NVMe namespace.
### Related ONTAP commands
* `vserver nvme namespace delete`
### Learn more
* [`DOC /storage/namespaces`](#docs-NVMe-storage_namespaces)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


