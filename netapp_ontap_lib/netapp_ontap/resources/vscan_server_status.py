# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API is used to display connection status information for the external virus-scanning servers or \"Vscan servers\".
## Examples
### Retrieving all fields for the Vscan server status
---
```
# The API:
/api/protocols/vscan/server_status/
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/server_status?fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "86fbc414-f140-11e8-8e22-0050568e0945",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/86fbc414-f140-11e8-8e22-0050568e0945"
          }
        }
      },
      "node": {
        "uuid": "fe696362-f138-11e8-8e22-0050568e0945",
        "name": "Cluster-01",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/fe696362-f138-11e8-8e22-0050568e0945"
          }
        }
      },
      "ip": "10.141.46.173",
      "type": "primary",
      "state": "disconnected",
      "disconnected_reason": "unknown",
      "_links": {
        "self": {
          "href": "/api/protocols/vscan/server_status/86fbc414-f140-11e8-8e22-0050568e0945/Cluster-01/10.141.46.173"
        }
      }
    },
    {
      "svm": {
        "uuid": "86fbc414-f140-11e8-8e22-0050568e0945",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/86fbc414-f140-11e8-8e22-0050568e0945"
          }
        }
      },
      "node": {
        "uuid": "fe696362-f138-11e8-8e22-0050568e0945",
        "name": "Cluster-01",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/fe696362-f138-11e8-8e22-0050568e0945"
          }
        }
      },
      "ip": "fd20:8b1e:b255:5053::46:173",
      "type": "primary",
      "state": "disconnected",
      "disconnected_reason": "remote_closed",
      "_links": {
        "self": {
          "href": "/api/protocols/vscan/server_status/86fbc414-f140-11e8-8e22-0050568e0945/Cluster-01/fd20%3A8b1e%3Ab255%3A5053%3A%3A46%3A173"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/vscan/server_status?fields=*"
    }
  }
}
```
---
### Retrieving the server status information for the server with IP address 10.141.46.173
---
```
# The API:
/api/protocols/vscan/server_status
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/server_status?ip=10.141.46.173&fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "86fbc414-f140-11e8-8e22-0050568e0945",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/86fbc414-f140-11e8-8e22-0050568e0945"
          }
        }
      },
      "node": {
        "uuid": "fe696362-f138-11e8-8e22-0050568e0945",
        "name": "Cluster-01",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/fe696362-f138-11e8-8e22-0050568e0945"
          }
        }
      },
      "ip": "10.141.46.173",
      "type": "primary",
      "state": "connected",
      "update_time": "2018-12-19T08:03:40.988Z",
      "vendor": "XYZ",
      "version": "1.12.2",
      "_links": {
        "self": {
          "href": "/api/protocols/vscan/server_status/86fbc414-f140-11e8-8e22-0050568e0945/Cluster-01/10.141.46.173"
        }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/protocols/vscan/server_status?ip=10.141.46.173&fields=*"
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


__all__ = ["VscanServerStatus", "VscanServerStatusSchema"]
__pdoc__ = {
    "VscanServerStatusSchema.resource": False,
    "VscanServerStatusSchema.patchable_fields": False,
    "VscanServerStatusSchema.postable_fields": False,
}


class VscanServerStatusSchema(ResourceSchema):
    """The fields of the VscanServerStatus object"""

    disconnected_reason = fields.Str(
        data_key="disconnected_reason",
    )
    r""" Specifies the server disconnected reason.
The following is a list of the possible reasons:

* unknown                   - Disconnected, unknown reason.
* vscan_disabled            - Disconnected, Vscan is disabled on the SVM.
* no_data_lif               - Disconnected, SVM does not have data LIF.
* session_uninitialized     - Disconnected, session is not initialized.
* remote_closed             - Disconnected, server has closed the connection.
* invalid_protocol_msg      - Disconnected, invalid protocol message received.
* invalid_session_id        - Disconnected, invalid session ID received.
* inactive_connection       - Disconnected, no activity on connection.
* invalid_user              - Connection request by an invalid user.
* server_removed            - Disconnected, server has been removed from the active Scanners List.
enum:
  - unknown
  - vscan_disabled
  - no_data_lif
  - session_uninitialized
  - remote_closed
  - invalid_protocol_msg
  - invalid_session_id
  - inactive_connection
  - invalid_user
  - server_removed """

    ip = fields.Str(
        data_key="ip",
    )
    r""" IP address of the Vscan server. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the vscan_server_status. """

    state = fields.Str(
        data_key="state",
    )
    r""" Specifies the server connection state indicating if it is in the connected or disconnected state.
The following is a list of the possible states:

* connected                 - Connected
* disconnected              - Disconnected
enum:
  - connected
  - disconnected """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the vscan_server_status. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['primary', 'backup']),
    )
    r""" Server type. The possible values are:

  * primary - Primary server
  * backup  - Backup server


Valid choices:

* primary
* backup """

    update_time = fields.DateTime(
        data_key="update_time",
    )
    r""" Specifies the time the server is in the connected or disconnected state. """

    vendor = fields.Str(
        data_key="vendor",
    )
    r""" Name of the connected virus-scanner vendor. """

    version = fields.Str(
        data_key="version",
    )
    r""" Version of the connected virus-scanner. """

    @property
    def resource(self):
        return VscanServerStatus

    @property
    def patchable_fields(self):
        return [
            "disconnected_reason",
            "ip",
            "node.name",
            "node.uuid",
            "state",
            "svm.name",
            "svm.uuid",
            "type",
            "update_time",
            "vendor",
            "version",
        ]

    @property
    def postable_fields(self):
        return [
            "disconnected_reason",
            "ip",
            "node.name",
            "node.uuid",
            "state",
            "svm.name",
            "svm.uuid",
            "type",
            "update_time",
            "vendor",
            "version",
        ]

class VscanServerStatus(Resource):
    r""" Displays the connection status information of the external virus-scanning servers. """

    _schema = VscanServerStatusSchema
    _path = "/api/protocols/vscan/server-status"

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
        r"""Retrieves a Vscan server status.
### Related ONTAP commands
* `vserver vscan connection-status show-all`
### Learn more
* [`DOC /protocols/vscan/server-status`](#docs-NAS-protocols_vscan_server-status)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a Vscan server status.
### Related ONTAP commands
* `vserver vscan connection-status show-all`
### Learn more
* [`DOC /protocols/vscan/server-status`](#docs-NAS-protocols_vscan_server-status)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






