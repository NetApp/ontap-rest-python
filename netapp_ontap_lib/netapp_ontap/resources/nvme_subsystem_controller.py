# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Non-Volatile Memory Express (NVMe) subsystem controllers represent dynamic connections between hosts and a storage solution.<br/>
The NVMe subsystem controllers REST API provides information about connected hosts.
## Examples
### Retrieving the NVMe subsystem controllers for the entire system
```
# The API:
GET /api/protocols/nvme/subsystem-controllers
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/nvme/subsystem-controllers' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "f0f5b928-2593-11e9-94c4-00a0989a1c8e",
        "name": "symmcon_fcnvme_vserver_0",
        "_links": {
          "self": {
            "href": "/api/svm/svms/f0f5b928-2593-11e9-94c4-00a0989a1c8e"
          }
        }
      },
      "subsystem": {
        "uuid": "14875240-2594-11e9-abde-00a098984313",
        "name": "symmcon_symmcon_fcnvme_vserver_0_subsystem_0",
        "_links": {
          "self": {
            "href": "/api/protocols/nvme/subsystems/14875240-2594-11e9-abde-00a098984313"
          }
        }
      },
      "id": "0040h",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/subsystem-controllers/14875240-2594-11e9-abde-00a098984313/0040h"
        }
      }
    },
    {
      "svm": {
        "uuid": "f0f5b928-2593-11e9-94c4-00a0989a1c8e",
        "name": "symmcon_fcnvme_vserver_0",
        "_links": {
          "self": {
            "href": "/api/svm/svms/f0f5b928-2593-11e9-94c4-00a0989a1c8e"
          }
        }
      },
      "subsystem": {
        "uuid": "14875240-2594-11e9-abde-00a098984313",
        "name": "symmcon_symmcon_fcnvme_vserver_0_subsystem_0",
        "_links": {
          "self": {
            "href": "/api/protocols/nvme/subsystems/14875240-2594-11e9-abde-00a098984313"
          }
        }
      },
      "id": "0041h",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/subsystem-controllers/14875240-2594-11e9-abde-00a098984313/0041h"
        }
      }
    },
    {
      "svm": {
        "uuid": "f0f5b928-2593-11e9-94c4-00a0989a1c8e",
        "name": "symmcon_fcnvme_vserver_0",
        "_links": {
          "self": {
            "href": "/api/svm/svms/f0f5b928-2593-11e9-94c4-00a0989a1c8e"
          }
        }
      },
      "subsystem": {
        "uuid": "1489d0d5-2594-11e9-94c4-00a0989a1c8e",
        "name": "symmcon_symmcon_fcnvme_vserver_0_subsystem_1",
        "_links": {
          "self": {
            "href": "/api/protocols/nvme/subsystems/1489d0d5-2594-11e9-94c4-00a0989a1c8e"
          }
        }
      },
      "id": "0040h",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/subsystem-controllers/1489d0d5-2594-11e9-94c4-00a0989a1c8e/0040h"
        }
      }
    },
    {
      "svm": {
        "uuid": "f0f5b928-2593-11e9-94c4-00a0989a1c8e",
        "name": "symmcon_fcnvme_vserver_0",
        "_links": {
          "self": {
            "href": "/api/svm/svms/f0f5b928-2593-11e9-94c4-00a0989a1c8e"
          }
        }
      },
      "subsystem": {
        "uuid": "1489d0d5-2594-11e9-94c4-00a0989a1c8e",
        "name": "symmcon_symmcon_fcnvme_vserver_0_subsystem_1",
        "_links": {
          "self": {
            "href": "/api/protocols/nvme/subsystems/1489d0d5-2594-11e9-94c4-00a0989a1c8e"
          }
        }
      },
      "id": "0041h",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/subsystem-controllers/1489d0d5-2594-11e9-94c4-00a0989a1c8e/0041h"
        }
      }
    }
  ],
  "num_records": 4,
  "_links": {
    "self": {
      "href": "/api/protocols/nvme/subsystem-controllers"
    }
  }
}
```
---
### Retrieving the NVMe subsystem controllers for a specific subsystem
```
# The API:
GET /api/protocols/nvme/subsystem-controllers/{subsystem.uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/nvme/subsystem-controllers/14875240-2594-11e9-abde-00a098984313' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "f0f5b928-2593-11e9-94c4-00a0989a1c8e",
        "name": "symmcon_fcnvme_vserver_0",
        "_links": {
          "self": {
            "href": "/api/svm/svms/f0f5b928-2593-11e9-94c4-00a0989a1c8e"
          }
        }
      },
      "subsystem": {
        "uuid": "14875240-2594-11e9-abde-00a098984313",
        "name": "symmcon_symmcon_fcnvme_vserver_0_subsystem_0",
        "_links": {
          "self": {
            "href": "/api/protocols/nvme/subsystems/14875240-2594-11e9-abde-00a098984313"
          }
        }
      },
      "id": "0040h",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/subsystem-controllers/14875240-2594-11e9-abde-00a098984313/0040h"
        }
      }
    },
    {
      "svm": {
        "uuid": "f0f5b928-2593-11e9-94c4-00a0989a1c8e",
        "name": "symmcon_fcnvme_vserver_0",
        "_links": {
          "self": {
            "href": "/api/svm/svms/f0f5b928-2593-11e9-94c4-00a0989a1c8e"
          }
        }
      },
      "subsystem": {
        "uuid": "14875240-2594-11e9-abde-00a098984313",
        "name": "symmcon_symmcon_fcnvme_vserver_0_subsystem_0",
        "_links": {
          "self": {
            "href": "/api/protocols/nvme/subsystems/14875240-2594-11e9-abde-00a098984313"
          }
        }
      },
      "id": "0041h",
      "_links": {
        "self": {
          "href": "/api/protocols/nvme/subsystem-controllers/14875240-2594-11e9-abde-00a098984313/0041h"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/nvme/subsystem-controllers/14875240-2594-11e9-abde-00a098984313"
    }
  }
}
```
---
### Retrieving a specific NVMe subsystem controller
```
# The API:
GET /api/protocols/nvme/subsystem-controllers/{subsystem.uuid}/{id}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/nvme/subsystem-controllers/14875240-2594-11e9-abde-00a098984313/0040h' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "f0f5b928-2593-11e9-94c4-00a0989a1c8e",
    "name": "symmcon_fcnvme_vserver_0",
    "_links": {
      "self": {
        "href": "/api/svm/svms/f0f5b928-2593-11e9-94c4-00a0989a1c8e"
      }
    }
  },
  "subsystem": {
    "uuid": "14875240-2594-11e9-abde-00a098984313",
    "name": "symmcon_symmcon_fcnvme_vserver_0_subsystem_0",
    "_links": {
      "self": {
        "href": "/api/protocols/nvme/subsystems/14875240-2594-11e9-abde-00a098984313"
      }
    }
  },
  "id": "0040h",
  "interface": {
    "name": "symmcon_lif_fcnvme_symmcon_fcnvme_vserver_0_3a_0",
    "uuid": "fa1c5941-2593-11e9-94c4-00a0989a1c8e",
    "transport_address": "nn-0x200400a0989a1c8d:pn-0x200500a0989a1c8d",
    "_links": {
      "self": {
        "href": "/api/protocols/nvme/interfaces/fa1c5941-2593-11e9-94c4-00a0989a1c8e"
      }
    }
  },
  "node": {
    "name": "ssan-8040-94a",
    "uuid": "ebf66f05-2590-11e9-abde-00a098984313",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/ebf66f05-2590-11e9-abde-00a098984313"
      }
    }
  },
  "host": {
    "transport_address": "nn-0x20000090fae00806:pn-0x10000090fae00806",
    "nqn": "nqn.2014-08.org.nvmexpress:uuid:c2846cb1-89d2-4020-a3b0-71ce907b4eef",
    "id": "b8546ca6097349e5b1558dc154fc073b"
  },
  "io_queue": {
    "count": 4,
    "depth": [
      32,
      32,
      32,
      32
    ]
  },
  "admin_queue": {
    "depth": 32
  },
  "_links": {
    "self": {
      "href": "/api/protocols/nvme/subsystem-controllers/14875240-2594-11e9-abde-00a098984313/0040h"
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


__all__ = ["NvmeSubsystemController", "NvmeSubsystemControllerSchema"]
__pdoc__ = {
    "NvmeSubsystemControllerSchema.resource": False,
    "NvmeSubsystemControllerSchema.patchable_fields": False,
    "NvmeSubsystemControllerSchema.postable_fields": False,
}


class NvmeSubsystemControllerSchema(ResourceSchema):
    """The fields of the NvmeSubsystemController object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the nvme_subsystem_controller. """

    admin_queue = fields.Nested("netapp_ontap.models.nvme_subsystem_controller_admin_queue.NvmeSubsystemControllerAdminQueueSchema", data_key="admin_queue", unknown=EXCLUDE)
    r""" The admin_queue field of the nvme_subsystem_controller. """

    host = fields.Nested("netapp_ontap.models.nvme_subsystem_controller_host.NvmeSubsystemControllerHostSchema", data_key="host", unknown=EXCLUDE)
    r""" The host field of the nvme_subsystem_controller. """

    id = fields.Str(
        data_key="id",
    )
    r""" The identifier of the subsystem controller. This field consists of 4 zero-filled hexadecimal digits followed by an 'h'.


Example: 0040h """

    interface = fields.Nested("netapp_ontap.models.nvme_subsystem_controller_interface.NvmeSubsystemControllerInterfaceSchema", data_key="interface", unknown=EXCLUDE)
    r""" The interface field of the nvme_subsystem_controller. """

    io_queue = fields.Nested("netapp_ontap.models.nvme_subsystem_controller_io_queue.NvmeSubsystemControllerIoQueueSchema", data_key="io_queue", unknown=EXCLUDE)
    r""" The io_queue field of the nvme_subsystem_controller. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the nvme_subsystem_controller. """

    subsystem = fields.Nested("netapp_ontap.resources.nvme_subsystem.NvmeSubsystemSchema", data_key="subsystem", unknown=EXCLUDE)
    r""" The subsystem field of the nvme_subsystem_controller. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the nvme_subsystem_controller. """

    @property
    def resource(self):
        return NvmeSubsystemController

    @property
    def patchable_fields(self):
        return [
            "admin_queue",
            "host",
            "interface",
            "io_queue",
            "node.name",
            "node.uuid",
            "subsystem.name",
            "subsystem.uuid",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "admin_queue",
            "host",
            "interface",
            "io_queue",
            "node.name",
            "node.uuid",
            "subsystem.name",
            "subsystem.uuid",
            "svm.name",
            "svm.uuid",
        ]

class NvmeSubsystemController(Resource):
    r""" A Non-Volatile Memory Express (NVMe) subsystem controller represents a connection between a host and a storage solution.<br/>
An NVMe subsystem controller is identified by the NVMe subsystem UUID and the controller ID. """

    _schema = NvmeSubsystemControllerSchema
    _path = "/api/protocols/nvme/subsystem-controllers"
    @property
    def _keys(self):
        return ["subsystem.uuid", "id"]

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
        r"""Retrieves NVMe subsystem controllers.
### Related ONTAP commands
* `vserver nvme subsystem controller show`
### Learn more
* [`DOC /protocols/nvme/subsystem-controllers`](#docs-NVMe-protocols_nvme_subsystem-controllers)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves NVMe subsystem controllers.
### Related ONTAP commands
* `vserver nvme subsystem controller show`
### Learn more
* [`DOC /protocols/nvme/subsystem-controllers`](#docs-NVMe-protocols_nvme_subsystem-controllers)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an NVMe subsystem controller.
### Related ONTAP commands
* `vserver nvme subsystem controller show`
### Learn more
* [`DOC /protocols/nvme/subsystem-controllers`](#docs-NVMe-protocols_nvme_subsystem-controllers)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





