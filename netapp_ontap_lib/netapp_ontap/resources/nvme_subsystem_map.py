# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An NVMe subsystem map is an association of an NVMe namespace with an NVMe subsystem. When an NVMe namespace is mapped to an NVMe subsystem, the NVMe subsystem's hosts are granted access to the NVMe namespace. The relationship between an NVMe subsystem and an NVMe namespace is one subsystem to many namespaces.<br/>
The NVMe subsystem map REST API allows you to create, delete and discover NVMe subsystem maps.
## Examples
### Creating an NVMe subsystem map
```
# The API:
POST /api/protocols/nvme/subsystem-maps
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/nvme/subsystem-maps' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "subsystem": { "name": "subsystem1" }, "namespace": { "name": "/vol/vol1/namespace1" } }'
```
---
### Retrieving all of the NVMe subsystem maps
```
# The API:
GET /api/protocols/nvme/subsystem-maps
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/nvme/subsystem-maps' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "0e91b214-fe40-11e8-91a0-005056a79967",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/0e91b214-fe40-11e8-91a0-005056a79967"
          }
        }
      },
      "subsystem": {
        "uuid": "580a6b1e-fe43-11e8-91a0-005056a79967",
        "name": "subsystem1",
        "_links": {
          "self": {
            "href": "/api/protocols/nvme/subsystems/580a6b1e-fe43-11e8-91a0-005056a79967"
          }
        }
      },
      "namespace": {
        "uuid": "3ccdedc6-2519-4206-bc1f-b0f4adab6f89",
        "name": "/vol/vol1/namespace1",
        "_links": {
          "self": {
            "href": "/api/storage/namespaces/3ccdedc6-2519-4206-bc1f-b0f4adab6f89"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/subsystem-maps/580a6b1e-fe43-11e8-91a0-005056a79967/3ccdedc6-2519-4206-bc1f-b0f4adab6f89"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/protocols/nvme/subsystem-maps"
    }
  }
}
```
---
### Retrieving a specific NVMe subsystem map
The NVMe subsystem map is identified by the UUID of the NVMe subsystem followed by the UUID of the NVMe namespace.
<br/>
```
# The API:
GET /api/protocols/nvme/subsystem-maps/{subsystem.uuid}/{namespace.uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/nvme/subsystem-maps/580a6b1e-fe43-11e8-91a0-005056a79967/3ccdedc6-2519-4206-bc1f-b0f4adab6f89' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "0e91b214-fe40-11e8-91a0-005056a79967",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/0e91b214-fe40-11e8-91a0-005056a79967"
      }
    }
  },
  "subsystem": {
    "uuid": "580a6b1e-fe43-11e8-91a0-005056a79967",
    "name": "subsystem1",
    "_links": {
      "self": {
        "href": "/api/protocols/nvme/subsystems/580a6b1e-fe43-11e8-91a0-005056a79967"
      }
    }
  },
  "namespace": {
    "uuid": "3ccdedc6-2519-4206-bc1f-b0f4adab6f89",
    "name": "/vol/vol1/namespace1",
    "node": {
      "name": "node1",
      "uuid": "012b4508-67d6-4788-8c2d-801f254ce976",
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/012b4508-67d6-4788-8c2d-801f254ce976"
        }
      }
    }
    "_links": {
      "self": {
        "href": "/api/storage/namespaces/3ccdedc6-2519-4206-bc1f-b0f4adab6f89"
      }
    }
  },
  "nsid": "00000001h",
  "_links": {
    "self": {
      "href": "/api/protocols/nvme/subsystem-maps/580a6b1e-fe43-11e8-91a0-005056a79967/3ccdedc6-2519-4206-bc1f-b0f4adab6f89"
    }
  }
}
```
---
### Deleting an NVMe subsystem map
```
# The API:
DELETE /api/protocols/nvme/subsystem-maps/{subsystem.uuid}/{namespace.uuid}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/protocols/nvme/subsystem-maps/580a6b1e-fe43-11e8-91a0-005056a79967/3ccdedc6-2519-4206-bc1f-b0f4adab6f89' -H 'accept: application/hal+json'
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["NvmeSubsystemMap", "NvmeSubsystemMapSchema"]
__pdoc__ = {
    "NvmeSubsystemMapSchema.resource": False,
    "NvmeSubsystemMapSchema.patchable_fields": False,
    "NvmeSubsystemMapSchema.postable_fields": False,
}


class NvmeSubsystemMapSchema(ResourceSchema):
    """The fields of the NvmeSubsystemMap object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the nvme_subsystem_map. """

    anagrpid = fields.Str(
        data_key="anagrpid",
    )
    r""" The Asymmetric Namespace Access Group ID (ANAGRPID) of the NVMe namespace.<br/>
The format for an ANAGRPID is 8 hexadecimal digits (zero-filled) followed by a lower case "h".<br/>
There is an added cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.


Example: 00103050h """

    namespace = fields.Nested("netapp_ontap.models.nvme_subsystem_map_namespace.NvmeSubsystemMapNamespaceSchema", data_key="namespace", unknown=EXCLUDE)
    r""" The namespace field of the nvme_subsystem_map. """

    nsid = fields.Str(
        data_key="nsid",
    )
    r""" The NVMe namespace identifier. This is an identifier used by an NVMe controller to provide access to the NVMe namespace.<br/>
The format for an NVMe namespace identifier is 8 hexadecimal digits (zero-filled) followed by a lower case "h".


Example: 00000001h """

    subsystem = fields.Nested("netapp_ontap.resources.nvme_subsystem.NvmeSubsystemSchema", data_key="subsystem", unknown=EXCLUDE)
    r""" The subsystem field of the nvme_subsystem_map. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the nvme_subsystem_map. """

    @property
    def resource(self):
        return NvmeSubsystemMap

    @property
    def patchable_fields(self):
        return [
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "namespace",
            "subsystem.name",
            "subsystem.uuid",
            "svm.name",
            "svm.uuid",
        ]

class NvmeSubsystemMap(Resource):
    r""" An NVMe subsystem map is an association of an NVMe namespace with an NVMe subsystem. When an NVMe namespace is mapped to an NVMe subsystem, the NVMe subsystem's hosts are granted access to the NVMe namespace. The relationship between an NVMe subsystem and an NVMe namespace is one subsystem to many namespaces. """

    _schema = NvmeSubsystemMapSchema
    _path = "/api/protocols/nvme/subsystem-maps"
    @property
    def _keys(self):
        return ["subsystem.uuid", "namespace.uuid"]

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
        r"""Retrieves NVMe subsystem maps.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `anagrpid`
### Related ONTAP commands
* `vserver nvme subsystem map show`
### Learn more
* [`DOC /protocols/nvme/subsystem-maps`](#docs-NVMe-protocols_nvme_subsystem-maps)
"""
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
        r"""Deletes an NVMe subsystem map.
### Related ONTAP commands
* `vserver nvme subsystem map delete`
### Learn more
* [`DOC /protocols/nvme/subsystem-maps`](#docs-NVMe-protocols_nvme_subsystem-maps)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves NVMe subsystem maps.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `anagrpid`
### Related ONTAP commands
* `vserver nvme subsystem map show`
### Learn more
* [`DOC /protocols/nvme/subsystem-maps`](#docs-NVMe-protocols_nvme_subsystem-maps)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an NVMe subsystem map.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `anagrpid`
### Related ONTAP commands
* `vserver nvme subsystem map show`
### Learn more
* [`DOC /protocols/nvme/subsystem-maps`](#docs-NVMe-protocols_nvme_subsystem-maps)
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
        r"""Creates an NVMe subsystem map.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the NVMe subsystem map.
* `namespace.uuid` or `namespace.name` - Existing NVMe namespace to map to the specified NVme subsystem.
* `subsystem.uuid` or `subsystem.name` - Existing NVMe subsystem to map to the specified NVMe namespace.
### Related ONTAP commands
* `vserver nvme subsystem map create`
### Learn more
* [`DOC /protocols/nvme/subsystem-maps`](#docs-NVMe-protocols_nvme_subsystem-maps)
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
        r"""Deletes an NVMe subsystem map.
### Related ONTAP commands
* `vserver nvme subsystem map delete`
### Learn more
* [`DOC /protocols/nvme/subsystem-maps`](#docs-NVMe-protocols_nvme_subsystem-maps)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


