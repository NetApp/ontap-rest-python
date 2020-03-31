# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Fibre Channel (FC) logins represent connections formed by FC initiators that have successfully logged in to ONTAP. This represents the FC login on which higher-level protocols such as Fibre Channel Protocol and NVMe over FC (NVMe/FC) rely.<br/>
The Fibre Channel logins REST API provides information about active FC logins.
## Examples
### Retrieving all FC logins
```
# The API:
GET /api/network/fc/logins
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/logins" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "056403da-83a7-4b13-bc78-6a93e8ea3596",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/056403da-83a7-4b13-bc78-6a93e8ea3596"
          }
        }
      },
      "interface": {
        "uuid": "01056403-1383-bc4b-786a-93e8ea35969d",
        "name": "lif1",
        "_links": {
          "self": {
            "href": "/api/network/fc/interfaces/01056403-1383-bc4b-786a-93e8ea35969d"
          }
        }
      },
      "initiator": {
        "wwpn": "8b:21:2f:07:00:00:00:00"
      },
      "_links": {
        "self": {
          "href": "/api/network/fc/logins/01056403-1383-bc4b-786a-93e8ea35969d/8b%3A21%3A2f%3A07%3A00%3A00%3A00%3A00"
        }
      }
    },
    {
      "svm": {
        "uuid": "056403da-83a7-4b13-bc78-6a93e8ea3596",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/056403da-83a7-4b13-bc78-6a93e8ea3596"
          }
        }
      },
      "interface": {
        "uuid": "02056403-1383-bc4b-786a-93e8ea35969d",
        "name": "lif2",
        "_links": {
          "self": {
            "href": "/api/network/fc/interfaces/02056403-1383-bc4b-786a-93e8ea35969d"
          }
        }
      },
      "initiator": {
        "wwpn": "8c:21:2f:07:00:00:00:00"
      },
      "_links": {
        "self": {
          "href": "/api/network/fc/logins/02056403-1383-bc4b-786a-93e8ea35969d/8c%3A21%3A2f%3A07%3A00%3A00%3A00%3A00"
        }
      }
    },
    {
      "svm": {
        "uuid": "156403da-83a7-4b13-bc78-6a93e8ea3596",
        "name": "svm2",
        "_links": {
          "self": {
            "href": "/api/svm/svms/156403da-83a7-4b13-bc78-6a93e8ea3596"
          }
        }
      },
      "interface": {
        "uuid": "03056403-1383-bc4b-786a-93e8ea35969d",
        "name": "lif3",
        "_links": {
          "self": {
            "href": "/api/network/fc/interfaces/00056403-1383-bc4b-786a-93e8ea35969d"
          }
        }
      },
      "initiator": {
        "wwpn": "8a:21:2f:07:00:00:00:00"
      },
      "_links": {
        "self": {
          "href": "/api/network/fc/logins/00056403-1383-bc4b-786a-93e8ea35969d/8a%3A21%3A2f%3A07%3A00%3A00%3A00%3A00"
        }
      }
    }
  ],
  "num_records": 3,
  "_links": {
    "self": {
      "href": "/api/network/fc/logins"
    }
  }
}
```
---
### Retrieving all FC logins with data protocol _fcp_ in SVM _svm1_
The `svm.name` and `protocol` query parameters are used to perform the query.
<br/>
```
# The API:
GET /api/network/fc/logins
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/logins?svm.name=svm1&protocol=fcp" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "056403da-83a7-4b13-bc78-6a93e8ea3596",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/056403da-83a7-4b13-bc78-6a93e8ea3596"
          }
        }
      },
      "interface": {
        "uuid": "01056403-1383-bc4b-786a-93e8ea35969d",
        "name": "lif2",
        "_links": {
          "self": {
            "href": "/api/network/fc/interfaces/01056403-1383-bc4b-786a-93e8ea35969d"
          }
        }
      },
      "initiator": {
        "wwpn": "8b:21:2f:07:00:00:00:00"
      },
      "protocol": "fcp",
      "_links": {
        "self": {
          "href": "/api/network/fc/logins/01056403-1383-bc4b-786a-93e8ea35969d/8b%3A21%3A2f%3A07%3A00%3A00%3A00%3A00"
        }
      }
    },
    {
      "svm": {
        "uuid": "056403da-83a7-4b13-bc78-6a93e8ea3596",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/056403da-83a7-4b13-bc78-6a93e8ea3596"
          }
        }
      },
      "interface": {
        "uuid": "02056403-1383-bc4b-786a-93e8ea35969d",
        "name": "lif3",
        "_links": {
          "self": {
            "href": "/api/network/fc/interfaces/02056403-1383-bc4b-786a-93e8ea35969d"
          }
        }
      },
      "initiator": {
        "wwpn": "8c:21:2f:07:00:00:00:00"
      },
      "protocol": "fcp",
      "_links": {
        "self": {
          "href": "/api/network/fc/logins/02056403-1383-bc4b-786a-93e8ea35969d/8c%3A21%3A2f%3A07%3A00%3A00%3A00%3A00"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/network/fc/logins?svm.name=svm1&protocol=fcp"
    }
  }
}
```
---
### Retrieving all FC logins for initiators belonging to _igroup1_ and returning all of their properties
The `igroups.name` query parameter is used to perform the query. The `fields` query parameter is used to return all of the properties.
<br/>
```
# The API:
GET /api/network/fc/logins
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/logins?igroups.name=igroup1&fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "056403da-83a7-4b13-bc78-6a93e8ea3596",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/056403da-83a7-4b13-bc78-6a93e8ea3596"
          }
        }
      },
      "interface": {
        "uuid": "01056403-1383-bc4b-786a-93e8ea35969d",
        "name": "lif2",
        "wwpn": "8b:21:2f:07:00:00:00:00",
        "_links": {
          "self": {
            "href": "/api/network/fc/interfaces/01056403-1383-bc4b-786a-93e8ea35969d"
          }
        }
      },
      "initiator": {
        "wwpn": "8b:21:2f:07:00:00:00:00",
        "wwnn": "95:21:2f:07:00:00:00:00"
      },
      "igroups": [
        {
          "uuid": "243bbb8a-46e9-4b2d-a508-a62dc93df9d1",
          "name": "igroup1",
          "_links": {
            "self": {
              "href": "/api/protocols/san/igroups/243bbb8a-46e9-4b2d-a508-a62dc93df9d1"
            }
          }
        }
      ],
      "port_address": "8aa53",
      "protocol": "fcp",
      "_links": {
        "self": {
          "href": "/api/network/fc/logins/01056403-1383-bc4b-786a-93e8ea35969d/8b%3A21%3A2f%3A07%3A00%3A00%3A00%3A00"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/network/fc/logins?igroups.name=igroup1&fields=*"
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


__all__ = ["FcLogin", "FcLoginSchema"]
__pdoc__ = {
    "FcLoginSchema.resource": False,
    "FcLoginSchema.patchable_fields": False,
    "FcLoginSchema.postable_fields": False,
}


class FcLoginSchema(ResourceSchema):
    """The fields of the FcLogin object"""

    links = fields.Nested("netapp_ontap.models.collection_links.CollectionLinksSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the fc_login. """

    igroups = fields.List(fields.Nested("netapp_ontap.resources.igroup.IgroupSchema", unknown=EXCLUDE), data_key="igroups")
    r""" The initiator groups in which the initiator is a member. """

    initiator = fields.Nested("netapp_ontap.models.fc_login_initiator.FcLoginInitiatorSchema", data_key="initiator", unknown=EXCLUDE)
    r""" The initiator field of the fc_login. """

    interface = fields.Nested("netapp_ontap.resources.fc_interface.FcInterfaceSchema", data_key="interface", unknown=EXCLUDE)
    r""" The interface field of the fc_login. """

    protocol = fields.Str(
        data_key="protocol",
        validate=enum_validation(['fc_nvme', 'fcp']),
    )
    r""" The data protocol used to perform the login.


Valid choices:

* fc_nvme
* fcp """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the fc_login. """

    @property
    def resource(self):
        return FcLogin

    @property
    def patchable_fields(self):
        return [
            "initiator",
            "interface.name",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "initiator",
            "interface.name",
            "svm.name",
            "svm.uuid",
        ]

class FcLogin(Resource):
    r""" A Fibre Channel (FC) login represents a connection formed by an FC initiator that has successfully logged in to ONTAP. This represents the FC login on which higher-level protocols such as Fibre Channel Protocol and NVMe over Fibre Channel (NVMe/FC) rely. """

    _schema = FcLoginSchema
    _path = "/api/network/fc/logins"
    @property
    def _keys(self):
        return ["interface.uuid", "initiator.wwpn"]

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
        r"""Retrieves FC logins.
### Related ONTAP commands
* `vserver fcp initiator show`
### Learn more
* SAN: [`DOC /network/fc/logins`](#docs-SAN-network_fc_logins)
* NVMe: [`DOC /network/fc/logins`](#docs-NVMe-network_fc_logins)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves FC logins.
### Related ONTAP commands
* `vserver fcp initiator show`
### Learn more
* SAN: [`DOC /network/fc/logins`](#docs-SAN-network_fc_logins)
* NVMe: [`DOC /network/fc/logins`](#docs-NVMe-network_fc_logins)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an FC login.
### Related ONTAP commands
* `vserver fcp initiator show`
### Learn more
* SAN: [`DOC /network/fc/logins`](#docs-SAN-network_fc_logins)
* NVMe: [`DOC /network/fc/logins`](#docs-NVMe-network_fc_logins)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





