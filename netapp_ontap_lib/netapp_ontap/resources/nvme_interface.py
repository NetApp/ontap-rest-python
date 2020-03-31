# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
NVMe interfaces are network interfaces configured to support an NVMe over Fabrics (NVMe-oF) protocol. The NVMe interfaces are Fibre Channel (FC) interfaces supporting an NVMe-oF data protocol. Regardless of the underlying physical and data protocol, NVMe interfaces are treated equally for host-side application configuration. This endpoint provides a consolidated view of all NVMe interfaces for the purpose of configuring host-side applications.<br/>
The NVMe interfaces REST API provides NVMe-specific information about network interfaces configured to support an NVMe-oF protocol.<br/>
NVMe interfaces must be created using the protocol-specific endpoints for FC interfaces. See [`POST /network/fc/interfaces`](#/networking/fc_interface_create). After creation, the interfaces are available via this interface.
## Examples
### Retrieving summary information for all NVMe interfaces
```
# The API:
GET /api/protocols/nvme/interfaces
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/nvme/interfaces' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "013e2c44-0d30-11e9-a684-005056bbdb14",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/013e2c44-0d30-11e9-a684-005056bbdb14"
          }
        }
      },
      "uuid": "74d69872-0d30-11e9-a684-005056bbdb14",
      "name": "nvme1",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/interfaces/74d69872-0d30-11e9-a684-005056bbdb14"
        }
      }
    },
    {
      "svm": {
        "uuid": "013e2c44-0d30-11e9-a684-005056bbdb14",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/013e2c44-0d30-11e9-a684-005056bbdb14"
          }
        }
      },
      "uuid": "77ded991-0d30-11e9-a684-005056bbdb14",
      "name": "nvme2",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/interfaces/77ded991-0d30-11e9-a684-005056bbdb14"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/nvme/interfaces"
    }
  }
}
```
---
### Retrieving detailed information for a specific NVMe interface
```
# The API:
GET /api/protocols/nvme/interfaces/{uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/nvme/interfaces/77ded991-0d30-11e9-a684-005056bbdb14' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "013e2c44-0d30-11e9-a684-005056bbdb14",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/013e2c44-0d30-11e9-a684-005056bbdb14"
      }
    }
  },
  "uuid": "77ded991-0d30-11e9-a684-005056bbdb14",
  "name": "nvme2",
  "enabled": true,
  "node": {
    "name": "node1",
    "uuid": "cd4d47fd-0d2e-11e9-a684-005056bbdb14",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/cd4d47fd-0d2e-11e9-a684-005056bbdb14"
      }
    }
  },
  "transport_address": "nn-0x2003005056bbdb14:pn-0x2005005056bbdb14",
  "fc_interface": {
    "wwnn": "20:03:00:50:56:bb:db:14",
    "wwpn": "20:05:00:50:56:bb:db:14",
    "port": {
      "name": "1a",
      "uuid": "081ec491-0d2f-11e9-a684-005056bbdb14",
      "node": {
        "name": "node1"
      },
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/081ec491-0d2f-11e9-a684-005056bbdb14"
        }
      }
    },
    "_links": {
      "self": {
        "href": "/api/network/fc/interfaces/77ded991-0d30-11e9-a684-005056bbdb14"
      }
    }
  },
  "_links": {
    "self": {
      "href": "/api/protocols/nvme/interfaces/77ded991-0d30-11e9-a684-005056bbdb14"
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


__all__ = ["NvmeInterface", "NvmeInterfaceSchema"]
__pdoc__ = {
    "NvmeInterfaceSchema.resource": False,
    "NvmeInterfaceSchema.patchable_fields": False,
    "NvmeInterfaceSchema.postable_fields": False,
}


class NvmeInterfaceSchema(ResourceSchema):
    """The fields of the NvmeInterface object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the nvme_interface. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The administrative state of the NVMe interface. """

    fc_interface = fields.Nested("netapp_ontap.models.nvme_interface_fc_interface.NvmeInterfaceFcInterfaceSchema", data_key="fc_interface", unknown=EXCLUDE)
    r""" The fc_interface field of the nvme_interface. """

    name = fields.Str(
        data_key="name",
    )
    r""" The name of the NVMe interface.


Example: lif1 """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the nvme_interface. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the nvme_interface. """

    transport_address = fields.Str(
        data_key="transport_address",
    )
    r""" The transport address of the NVMe interface.


Example: nn-0x200a00a0989062da:pn-0x200100a0989062da """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the NVMe interface.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return NvmeInterface

    @property
    def patchable_fields(self):
        return [
            "fc_interface",
            "node.name",
            "node.uuid",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "fc_interface",
            "node.name",
            "node.uuid",
            "svm.name",
            "svm.uuid",
        ]

class NvmeInterface(Resource):
    r""" NVMe interfaces are network interfaces configured to support an NVMe over Fabrics (NVMe-oF) protocol. The NVMe interfaces are Fibre Channel interfaces supporting an NVMe-oF data protocol. Regardless of the underlying physical and data protocol, NVMe interfaces are treated equally for host-side application configuration. This endpoint provides a consolidated view of all NVMe interfaces for the purpose of configuring host-side applications.<br/>
NVMe interfaces must be created using the protocol-specific endpoints for Fibre Channel interfaces. See [`POST /network/fc/interfaces`](#/networking/fc_interface_create). After creation, the interfaces are available via this interface. """

    _schema = NvmeInterfaceSchema
    _path = "/api/protocols/nvme/interfaces"
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
        r"""Retrieves NVMe interfaces.
### Related ONTAP commands
* `vserver nvme show-interface`
### Learn more
* [`DOC /protocols/nvme/interfaces`](#docs-NVMe-protocols_nvme_interfaces)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves NVMe interfaces.
### Related ONTAP commands
* `vserver nvme show-interface`
### Learn more
* [`DOC /protocols/nvme/interfaces`](#docs-NVMe-protocols_nvme_interfaces)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an NVMe interface.
### Related ONTAP commands
* `vserver nvme show-interface`
### Learn more
* [`DOC /protocols/nvme/interfaces`](#docs-NVMe-protocols_nvme_interfaces)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





