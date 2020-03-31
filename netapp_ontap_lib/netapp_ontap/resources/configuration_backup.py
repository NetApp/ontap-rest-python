# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API retrieves the current settings for the configuration and updates configuration backup settings. The GET operation retrieves the current settings for the configuration and the PATCH operation updates the configuration backup settings.
## Examples
These examples show how to retrieve and update the configuration backup settings.
### Retrieving the configuration backup settings
---
```
# The API:
/api/support/configuration-backup
# The call:
curl -X GET "https://<mgmt-ip>/api/support/configuration-backup" -H "accept: application/hal+json"
# The response:
{
    "url": "http://10.224.65.198/backups",
    "username": "me",
    "_links": {
        "self": {
            "href": "/api/support/configuration-backup"
        }
    }
}
```
---
### Updating the configuration backup settings
---
```
# The API:
/api/support/configuration-backup
# The call:
curl -X PATCH "https://<mgmt-ip>/api/support/configuration-backup" -H "accept: application/hal+json"
# The body:
{
    "url": "https://10.224.65.198/new_backups",
    "username": "new_me",
    "password": "new_pass",
    "validate_certificate": "true"
}
# The response header:
HTTP/1.1 200 OK
Date: Tue, 05 Jun 2018 18:17:48 GMT
Server: libzapid-httpd
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 3
Content-Type: application/hal+json
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


__all__ = ["ConfigurationBackup", "ConfigurationBackupSchema"]
__pdoc__ = {
    "ConfigurationBackupSchema.resource": False,
    "ConfigurationBackupSchema.patchable_fields": False,
    "ConfigurationBackupSchema.postable_fields": False,
}


class ConfigurationBackupSchema(ResourceSchema):
    """The fields of the ConfigurationBackup object"""

    password = fields.Str(
        data_key="password",
    )
    r""" The password field of the configuration_backup.

Example: yourpassword """

    url = fields.Str(
        data_key="url",
    )
    r""" An external backup location for the cluster configuration. This is mostly required for single node clusters where node and cluster configuration backups cannot be copied to other nodes in the cluster.

Example: http://10.224.65.198/backups """

    username = fields.Str(
        data_key="username",
    )
    r""" The username field of the configuration_backup.

Example: me """

    validate_certificate = fields.Boolean(
        data_key="validate_certificate",
    )
    r""" Use this parameter with the value "true" to validate the digital certificate of the remote server. Digital certificate validation is available only when the HTTPS protocol is used in the URL; it is disabled by default. """

    @property
    def resource(self):
        return ConfigurationBackup

    @property
    def patchable_fields(self):
        return [
            "password",
            "url",
            "username",
            "validate_certificate",
        ]

    @property
    def postable_fields(self):
        return [
            "url",
            "username",
            "validate_certificate",
        ]

class ConfigurationBackup(Resource):
    """Allows interaction with ConfigurationBackup objects on the host"""

    _schema = ConfigurationBackupSchema
    _path = "/api/support/configuration-backup"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the cluster configuration backup information.
### Learn more
* [`DOC /support/configuration-backup`](#docs-support-support_configuration-backup)"""
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
        r"""Updates the cluster configuration backup information.

### Learn more
* [`DOC /support/configuration-backup`](#docs-support-support_configuration-backup)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



