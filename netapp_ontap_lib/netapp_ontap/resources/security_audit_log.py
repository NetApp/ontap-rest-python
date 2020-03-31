# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
These APIs return audit log records. The GET requests retrieves all audit log records. An audit log record contains information such as timestamp, node name, index and so on.
<br />
---
## Example
### Retrieving audit log records
The following example shows the audit log records.
<br />
---
```
# The API:
/api/security/audit/messages
# The call:
curl -X GET "https://<cluster-ip>/api/security/audit/messages"
# The response:
{
  "records": [
    {
      "timestamp": "2019-03-08T11:03:32-05:00",
      "node": {
        "name": "node1",
        "uuid": "bc9af9da-41bb-11e9-a3db-005056bb27cf",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/bc9af9da-41bb-11e9-a3db-005056bb27cf"
          }
        }
      },
      "index": 4294967299,
      "application": "http",
      "location": "172.21.16.89",
      "user": "admin",
      "input": "GET /api/security/audit/destinations/",
      "state": "pending",
      "scope": "cluster"
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/security/audit/messages"
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


__all__ = ["SecurityAuditLog", "SecurityAuditLogSchema"]
__pdoc__ = {
    "SecurityAuditLogSchema.resource": False,
    "SecurityAuditLogSchema.patchable_fields": False,
    "SecurityAuditLogSchema.postable_fields": False,
}


class SecurityAuditLogSchema(ResourceSchema):
    """The fields of the SecurityAuditLog object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the security_audit_log. """

    application = fields.Str(
        data_key="application",
        validate=enum_validation(['internal', 'console', 'rsh', 'telnet', 'ssh', 'ontapi', 'http']),
    )
    r""" This identifies the "application" by which the request was processed.


Valid choices:

* internal
* console
* rsh
* telnet
* ssh
* ontapi
* http """

    command_id = fields.Str(
        data_key="command_id",
    )
    r""" This is the command ID for this request.
Each command received on a CLI session is assigned a command ID. This enables you to correlate a request and response. """

    index = fields.Integer(
        data_key="index",
    )
    r""" Internal index for accessing records with same time/node. This is a 64 bit unsigned value. """

    input = fields.Str(
        data_key="input",
    )
    r""" The request. """

    location = fields.Str(
        data_key="location",
    )
    r""" This identifies the location of the remote user. This is an IP address or "console". """

    message = fields.Str(
        data_key="message",
    )
    r""" This is an optional field that might contain "error" or "additional information" about the status of a command. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the security_audit_log. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" when the request is on a data SVM; otherwise set to "cluster".

Valid choices:

* svm
* cluster """

    session_id = fields.Str(
        data_key="session_id",
    )
    r""" This is the session ID on which the request is received. Each SSH session is assigned a session ID.
Each http/ontapi/snmp request is assigned a unique session ID. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['pending', 'success', 'error']),
    )
    r""" State of of this request.

Valid choices:

* pending
* success
* error """

    svm = fields.Nested("netapp_ontap.models.security_audit_log_svm.SecurityAuditLogSvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the security_audit_log. """

    timestamp = fields.Str(
        data_key="timestamp",
    )
    r""" Log entry timestamp. Valid in URL """

    user = fields.Str(
        data_key="user",
    )
    r""" Username of the remote user. """

    @property
    def resource(self):
        return SecurityAuditLog

    @property
    def patchable_fields(self):
        return [
            "node.name",
            "node.uuid",
            "scope",
            "svm",
        ]

    @property
    def postable_fields(self):
        return [
            "node.name",
            "node.uuid",
            "scope",
            "svm",
        ]

class SecurityAuditLog(Resource):
    """Allows interaction with SecurityAuditLog objects on the host"""

    _schema = SecurityAuditLogSchema
    _path = "/api/security/audit/messages"

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
        r"""Retrieves the administrative audit log viewer.
### Learn more
* [`DOC /security/audit/messages`](#docs-security-security_audit_messages)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the administrative audit log viewer.
### Learn more
* [`DOC /security/audit/messages`](#docs-security-security_audit_messages)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






