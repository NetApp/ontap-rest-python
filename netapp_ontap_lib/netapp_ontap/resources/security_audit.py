# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API controls what is logged to the audit log files. All operations that make changes are always logged and cannot be disabled. The PATCH request updates administrative audit settings for GET requests. All fields are optional for a PATCH request. A GET request retrieves administrative audit settings for GET requests.
<br />
---
## Examples
### Retrieving administrative audit settings for GET requests
The following example shows the administrative audit settings for GET requests.
<br />
---
```
# The API:
/api/security/audit
# The call:
curl -X GET "https://<cluster-ip>/api/security/audit"
# The response:
{
  "cli": false,
  "http": false,
  "ontapi": false,
  "_links": {
      "self": {
          "href": "/api/security/audit"
      }
  }
}
```
---
### Updating administrative audit settings for GET requests
The following example updates the administrative audit settings for GET requests
<br />
---
```
# The API:
/api/security/audit
# The call:
curl -X PATCH "https://<cluster-ip>/api/security/audit" -d '{"cli":"false", "http": "true", "ontapi": "true"}'
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


__all__ = ["SecurityAudit", "SecurityAuditSchema"]
__pdoc__ = {
    "SecurityAuditSchema.resource": False,
    "SecurityAuditSchema.patchable_fields": False,
    "SecurityAuditSchema.postable_fields": False,
}


class SecurityAuditSchema(ResourceSchema):
    """The fields of the SecurityAudit object"""

    cli = fields.Boolean(
        data_key="cli",
    )
    r""" Enable auditing of CLI GET Operations. Valid in PATCH """

    http = fields.Boolean(
        data_key="http",
    )
    r""" Enable auditing of HTTP GET Operations. Valid in PATCH """

    ontapi = fields.Boolean(
        data_key="ontapi",
    )
    r""" Enable auditing of ONTAP API GET operations. Valid in PATCH """

    @property
    def resource(self):
        return SecurityAudit

    @property
    def patchable_fields(self):
        return [
            "cli",
            "http",
            "ontapi",
        ]

    @property
    def postable_fields(self):
        return [
            "cli",
            "http",
            "ontapi",
        ]

class SecurityAudit(Resource):
    """Allows interaction with SecurityAudit objects on the host"""

    _schema = SecurityAuditSchema
    _path = "/api/security/audit"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves administrative audit settings for GET requests.
### Learn more
* [`DOC /security/audit`](#docs-security-security_audit)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member


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
        r"""Updates administrative audit settings for GET requests.
All of the fields are optional. An empty body will make no changes.

### Learn more
* [`DOC /security/audit`](#docs-security-security_audit)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



