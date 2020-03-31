# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Auditing for NAS events is a security measure that enables you to track and log certain CIFS and NFS events on storage virtual machines (SVMs). This helps you track potential security problems and provides evidence of any security breaches.
## Examples
---
### Creating an audit entry with log rotation size and log retention count
To create an audit entry with log rotation size and log retention count, use the following API. Note the <i>return_records=true</i> query parameter is used to obtain the newly created entry in the response.
<br/>
---
```
# The API:
POST /api/protocols/audit/
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/audit" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": true, \"events\": { \"authorization_policy\": false, \"cap_staging\": false, \"cifs_logon_logoff\": true, \"file_operations\": true, \"file_share\": false, \"security_group\": false, \"user_account\": false }, \"log\": { \"format\": \"evtx\", \"retention\": { \"count\": 10 }, \"rotation\": { \"size\": 2048000 }}, \"log_path\": \"/\", \"svm\": { \"name\": \"vs1\", \"uuid\": \"ec650e97-156e-11e9-abcb-005056bbd0bf\" }}"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "ec650e97-156e-11e9-abcb-005056bbd0bf",
        "name": "vs1"
      },
      "enabled": true,
      "events": {
        "authorization_policy": false,
        "cap_staging": false,
        "cifs_logon_logoff": true,
        "file_operations": true,
        "file_share": false,
        "security_group": false,
        "user_account": false
      },
      "log": {
        "format": "evtx",
        "rotation": {
          "size": 2048000
        },
        "retention": {
          "count": 10,
          "duration": "0s"
        }
      },
      "log_path": "/"
    }
  ],
  "num_records": 1
}
```
---
### Creating an audit entry with log rotation schedule and log retention duration
To create an audit entry with log rotation schedule and log retention duration, use the following API. Note that the <i>return_records=true</i> query parameter is used to obtain the newly created entry in the response.
<br/>
---
```
# The API:
POST /api/protocols/audit/
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/audit" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": false, \"events\": { \"authorization_policy\": false, \"cap_staging\": false, \"cifs_logon_logoff\": true, \"file_operations\": true, \"file_share\": false, \"security_group\": false, \"user_account\": false }, \"log\": { \"format\": \"xml\", \"retention\": { \"duration\": \"P4DT12H30M5S\" }, \"rotation\": { \"schedule\": { \"days\": [1, 5, 10, 15], \"hours\": [0, 1, 6, 12, 18, 23], \"minutes\": [10, 15, 30, 45, 59], \"months\": [0], \"weekdays\": [0, 2, 5] } } }, \"log_path\": \"/\", \"svm\": { \"name\": \"vs3\", \"uuid\": \"a8d64674-13fc-11e9-87b1-005056a7ae7e\" }}"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "a8d64674-13fc-11e9-87b1-005056a7ae7e",
        "name": "vs3"
      },
      "enabled": true,
      "events": {
        "authorization_policy": false,
        "cap_staging": false,
        "cifs_logon_logoff": true,
        "file_operations": true,
        "file_share": false,
        "security_group": false,
        "user_account": false
      },
      "log": {
        "format": "xml",
        "rotation": {
          "schedule": {
            "minutes": [
              10,
              15,
              30,
              45,
              59
            ],
            "hours": [
              0,
              1,
              6,
              12,
              18,
              23
            ],
            "weekdays": [
              0,
              2,
              5
            ],
            "days": [
              1,
              5,
              10,
              15
            ],
            "months": [
              0
            ]
          }
        },
        "retention": {
          "count": 0,
          "duration": "P4DT12H30M5S"
        }
      },
      "log_path": "/"
    }
  ],
  "num_records": 1
}
```
---
### Retrieving an audit configuration for all SVMs in the cluster
---
```
# The API:
GET /api/protocols/audit/
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/audit?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "ec650e97-156e-11e9-abcb-005056bbd0bf",
        "name": "vs1"
      },
      "enabled": true,
      "events": {
        "authorization_policy": false,
        "cap_staging": false,
        "cifs_logon_logoff": true,
        "file_operations": true,
        "file_share": false,
        "security_group": false,
        "user_account": false
      },
      "log": {
        "format": "evtx",
        "rotation": {
          "size": 2048000
        },
        "retention": {
          "count": 10,
          "duration": "0s"
        }
      },
      "log_path": "/"
    },
    {
      "svm": {
        "uuid": "a8d64674-13fc-11e9-87b1-005056a7ae7e",
        "name": "vs3"
      },
      "enabled": true,
      "events": {
        "authorization_policy": false,
        "cap_staging": false,
        "cifs_logon_logoff": true,
        "file_operations": true,
        "file_share": false,
        "security_group": false,
        "user_account": false
      },
      "log": {
        "format": "xml",
        "rotation": {
          "schedule": {
            "minutes": [
              10,
              15,
              30,
              45,
              59
            ],
            "hours": [
              0,
              1,
              6,
              12,
              18,
              23
            ],
            "weekdays": [
              0,
              2,
              5
            ],
            "days": [
              1,
              5,
              10,
              15
            ],
            "months": [
              0
            ]
          }
        },
        "retention": {
          "count": 0,
          "duration": "P4DT12H30M5S"
        }
      },
      "log_path": "/"
    }
  ],
  "num_records": 2
}
```
---
### Retrieving specific entries with event list as cifs-logon-logoff, file-ops = true for an SVM
The configuration returned is identified by the events in the list of audit configurations for an SVM.
<br/>
---
```
# The API:
GET /api/protocols/audit/
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/audit?events.file_operations=true&events.cifs_logon_logoff=true&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "ec650e97-156e-11e9-abcb-005056bbd0bf",
        "name": "vs1"
      },
      "events": {
        "cifs_logon_logoff": true,
        "file_operations": true
      }
    },
    {
      "svm": {
        "uuid": "a8d64674-13fc-11e9-87b1-005056a7ae7e",
        "name": "vs3"
      },
      "events": {
        "cifs_logon_logoff": true,
        "file_operations": true
      }
    }
  ],
  "num_records": 2
}
```
---
### Retrieving a specific audit configuration for an SVM
The configuration returned is identified by the UUID of its SVM.
<br/>
---
```
# The API:
GET /api/protocols/audit/{svm.uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/audit/ec650e97-156e-11e9-abcb-005056bbd0bf" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "ec650e97-156e-11e9-abcb-005056bbd0bf",
    "name": "vs1"
  },
  "enabled": true,
  "events": {
    "authorization_policy": false,
    "cap_staging": false,
    "cifs_logon_logoff": true,
    "file_operations": true,
    "file_share" : false,
    "security_group": false,
    "user_account": false
  },
  "log": {
    "format": "evtx",
    "rotation": {
      "size": 2048000
    },
    "retention": {
      "count": 10,
      "duration": "0s"
    }
  },
  "log_path": "/"
}
```
---
### Updating a specific audit configuration of an SVM
The configuration is identified by the UUID of its SVM and the provided information is updated.
<br/>
---
```
# The API:
PATCH /api/protocols/audit/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/audit/ec650e97-156e-11e9-abcb-005056bbd0bf" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": false}"
```
---
### Deleting a specific audit configuration for an SVM
The entry to be deleted is identified by the UUID of its SVM.
<br/>
---
```
# The API:
DELETE /api/protocols/audit/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/audit/ec650e97-156e-11e9-abcb-005056bbd0bf" -H "accept: application/json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Audit", "AuditSchema"]
__pdoc__ = {
    "AuditSchema.resource": False,
    "AuditSchema.patchable_fields": False,
    "AuditSchema.postable_fields": False,
}


class AuditSchema(ResourceSchema):
    """The fields of the Audit object"""

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies whether or not auditing is enabled on the SVM. """

    events = fields.Nested("netapp_ontap.models.audit_events.AuditEventsSchema", data_key="events", unknown=EXCLUDE)
    r""" The events field of the audit. """

    log = fields.Nested("netapp_ontap.models.log.LogSchema", data_key="log", unknown=EXCLUDE)
    r""" The log field of the audit. """

    log_path = fields.Str(
        data_key="log_path",
    )
    r""" The audit log destination path where consolidated audit logs are stored. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the audit. """

    @property
    def resource(self):
        return Audit

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "events",
            "log",
            "log_path",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "events",
            "log",
            "log_path",
            "svm.name",
            "svm.uuid",
        ]

class Audit(Resource):
    r""" Auditing for NAS events is a security measure that enables you to track and log certain CIFS and NFS events on SVMs. """

    _schema = AuditSchema
    _path = "/api/protocols/audit"
    @property
    def _keys(self):
        return ["svm.uuid"]

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
        r"""Retrieves audit configurations.
### Related ONTAP commands
* `vserver audit show`
### Learn more
* [`DOC /protocols/audit`](#docs-NAS-protocols_audit)
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
        r"""Updates an audit configuration for an SVM.
### Related ONTAP commands
* `vserver audit modify`
### Learn more
* [`DOC /protocols/audit`](#docs-NAS-protocols_audit)
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
        r"""Deletes an audit configuration.
### Related ONTAP commands
* `vserver audit disable`
* `vserver audit delete`
### Learn more
* [`DOC /protocols/audit`](#docs-NAS-protocols_audit)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves audit configurations.
### Related ONTAP commands
* `vserver audit show`
### Learn more
* [`DOC /protocols/audit`](#docs-NAS-protocols_audit)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an audit configuration for an SVM.
### Related ONTAP commands
* `vserver audit show`
### Learn more
* [`DOC /protocols/audit`](#docs-NAS-protocols_audit)
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
        r"""Creates an audit configuration.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM to which audit configuration is to be created.
* `log_path` - Path in the owning SVM namespace that is used to store audit logs.
### Default property values
If not specified in POST, the following default property values are assigned:
* `enabled` - _true_
* `events.authorization_policy` - _false_
* `events.cap_staging` - _false_
* `events.file_share` - _false_
* `events.security_group` - _false_
* `events.user_account` - _false_
* `events.cifs_logon_logoff` - _true_
* `events.file_operations` - _true_
* `log.format` - _evtx_
* `log.retention.count` - _0_
* `log.retention.duration` - _PT0S_
* `log.rotation.size` - _100MB_
* `log.rotation.now` - _false_
### Related ONTAP commands
* `vserver audit create`
* `vserver audit enable`
### Learn more
* [`DOC /protocols/audit`](#docs-NAS-protocols_audit)
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
        r"""Updates an audit configuration for an SVM.
### Related ONTAP commands
* `vserver audit modify`
### Learn more
* [`DOC /protocols/audit`](#docs-NAS-protocols_audit)
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
        r"""Deletes an audit configuration.
### Related ONTAP commands
* `vserver audit disable`
* `vserver audit delete`
### Learn more
* [`DOC /protocols/audit`](#docs-NAS-protocols_audit)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


