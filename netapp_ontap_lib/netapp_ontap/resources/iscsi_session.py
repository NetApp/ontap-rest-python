# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An iSCSI session is one or more TCP connections that link an iSCSI initiator with an iSCSI target. TCP connections can be added and removed from an iSCSI session by the iSCSI initiator. Across all TCP connections within an iSCSI session, an initiator sees one and the same target. After the connection is established, iSCSI control, data, and status messages are communicated over the session.<br/>
The iSCSI sessions REST API provides information about iSCSI initiators that have successfully logged in to ONTAP.
## Examples
### Retrieving all iSCSI sessions
```
# The API:
GET /api/protocols/san/iscsi/sessions
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/san/iscsi/sessions" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "a009a9e7-4081-b576-7575-ada21efcaf16",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/a009a9e7-4081-b576-7575-ada21efcaf16"
          }
        }
      },
      "target_portal_group": "iscsi_lif1",
      "tsih": 10,
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/sessions/a009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif1/10"
        }
      }
    },
    {
      "svm": {
        "uuid": "b009a9e7-4081-b576-7575-ada21efcaf16",
        "name": "svm2",
        "_links": {
          "self": {
            "href": "/api/svm/svms/b009a9e7-4081-b576-7575-ada21efcaf16"
          }
        }
      },
      "target_portal_group": "iscsi_lif2",
      "tsih": 11,
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/sessions/b009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif2/11"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/san/iscsi/sessions"
    }
  }
}
```
---
### Retrieving all of the iSCSI sessions under the target portal group _iscsi_lif1_
The `tpgroup` query parameter is used to perform the query.
<br/>
```
# The API:
GET /api/protocols/san/iscsi/sessions
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/san/iscsi/sessions?tpgroup=iscsi_lif1" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "a009a9e7-4081-b576-7575-ada21efcaf16",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/a009a9e7-4081-b576-7575-ada21efcaf16"
          }
        }
      },
      "target_portal_group": "iscsi_lif1",
      "tsih": 10,
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/sessions/a009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif1/10"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/protocols/san/iscsi/sessions"
    }
  }
}
```
---
### Retrieving an iSCSI session
```
# The API:
GET /api/protocols/san/iscsi/sessions/{svm.uuid}/{target_portal_group}/{tsih}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/san/iscsi/sessions/a009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif1/10" -H "accept: application/hal+json"
# The response:
{
  "svm": {
    "uuid": "a009a9e7-4081-b576-7575-ada21efcaf16",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/a009a9e7-4081-b576-7575-ada21efcaf16"
      }
    }
  },
  "target_portal_group": "iscsi_lif1",
  "tsih": 10,
  "initiator": {
    "name": "iqn.1994-05.com.example:string"
  },
  "isid": "61:62:63:64:65:00",
  "target_portal_group_tag": 1027,
  "connections": [
    {
      "cid": 1,
      "authentication_type": "chap",
      "initiator_address": {
        "address": "10.224.123.85",
        "port": 43827
      },
      "interface": {
        "name": "iscsi_lif1",
        "uuid": "c15439b4-dbb4-11e8-90ac-005056bba882",
        "ip": {
          "address": "192.168.0.1",
          "port": 3260
        },
        "_links": {
          "self": {
            "href": "/api/network/ip/interfaces/c15439b4-dbb4-11e8-90ac-005056bba882"
          }
        }
      }
    }
  ],
  "igroups": [
    {
      "uuid": "af7838cd-f993-4faf-90b7-5524787ae1e8",
      "name": "igroup1",
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/af7838cd-f993-4faf-90b7-5524787ae1e8"
        }
      }
    },
    {
      "uuid": "bf7838cd-f993-4faf-90b7-5524787ae1e8",
      "name": "igroup2",
      "_links": {
        "self": {
          "href": "/api/protocols/san/igroups/bf7838cd-f993-4faf-90b7-5524787ae1e8"
        }
      }
    }
  ],
  "_links": {
    "self": {
      "href": "/api/protocols/san/iscsi/sessions/a009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif1/10"
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


__all__ = ["IscsiSession", "IscsiSessionSchema"]
__pdoc__ = {
    "IscsiSessionSchema.resource": False,
    "IscsiSessionSchema.patchable_fields": False,
    "IscsiSessionSchema.postable_fields": False,
}


class IscsiSessionSchema(ResourceSchema):
    """The fields of the IscsiSession object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the iscsi_session. """

    connections = fields.List(fields.Nested("netapp_ontap.models.iscsi_connection.IscsiConnectionSchema", unknown=EXCLUDE), data_key="connections")
    r""" The iSCSI connections that make up the iSCSI session. """

    igroups = fields.List(fields.Nested("netapp_ontap.resources.igroup.IgroupSchema", unknown=EXCLUDE), data_key="igroups")
    r""" The initiator groups in which the initiator is a member. """

    initiator = fields.Nested("netapp_ontap.models.iscsi_session_initiator.IscsiSessionInitiatorSchema", data_key="initiator", unknown=EXCLUDE)
    r""" The initiator field of the iscsi_session. """

    isid = fields.Str(
        data_key="isid",
    )
    r""" The initiator portion of the session identifier specified by the initiator during login.


Example: 61:62:63:64:65:00 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the iscsi_session. """

    target_portal_group = fields.Str(
        data_key="target_portal_group",
    )
    r""" The target portal group to which the session belongs.


Example: tpgroup1 """

    target_portal_group_tag = fields.Integer(
        data_key="target_portal_group_tag",
    )
    r""" The target portal group tag of the session. """

    tsih = fields.Integer(
        data_key="tsih",
    )
    r""" The target session identifier handle (TSIH) of the session. """

    @property
    def resource(self):
        return IscsiSession

    @property
    def patchable_fields(self):
        return [
            "initiator",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "initiator",
            "svm.name",
            "svm.uuid",
        ]

class IscsiSession(Resource):
    r""" An iSCSI session is one or more TCP connections that link an iSCSI initiator with an iSCSI target. TCP connections can be added and removed from an iSCSI session by the iSCSI initiator. Across all TCP connections within an iSCSI session, an initiator sees one and the same target. After the connection is established, iSCSI control, data, and status messages are communicated over the session. """

    _schema = IscsiSessionSchema
    _path = "/api/protocols/san/iscsi/sessions"
    @property
    def _keys(self):
        return ["svm.uuid", "tpgroup", "tsih"]

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
        r"""Retrieves iSCSI sessions.
### Related ONTAP commands
* `vserver iscsi connection show`
* `vserver iscsi session parameter show`
* `vserver iscsi session show`
### Learn more
* [`DOC /protocols/san/iscsi/sessions`](#docs-SAN-protocols_san_iscsi_sessions)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves iSCSI sessions.
### Related ONTAP commands
* `vserver iscsi connection show`
* `vserver iscsi session parameter show`
* `vserver iscsi session show`
### Learn more
* [`DOC /protocols/san/iscsi/sessions`](#docs-SAN-protocols_san_iscsi_sessions)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an iSCSI session.
### Related ONTAP commands
* `vserver iscsi connection show`
* `vserver iscsi session parameter show`
* `vserver iscsi session show`
### Learn more
* [`DOC /protocols/san/iscsi/sessions`](#docs-SAN-protocols_san_iscsi_sessions)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





