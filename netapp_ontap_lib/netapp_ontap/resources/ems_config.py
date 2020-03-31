# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
The Event Management System (EMS) collects and processes events, and sends notification of the events through various reporting mechanisms. The following endpoints defined under '/support/ems', allow you to query a list of observed events, and configure which events you handle and how you are notified:
- /support/ems
- /support/ems/events
- /support/ems/messages
- /support/ems/filters
- /support/ems/filters/{name}/rules
- /support/ems/filters/{name}/rules/{index}
- /support/ems/destinations
- /support/ems/destinations/{name}
## Examples
### Configuring an email destination
The following example configures EMS to send a support email when a WAFL event is observed with an error severity.
#### Configure the system-wide email parameters
```JSON
# API
PATCH /support/ems
# JSON Body
{
  "mail_from": "administrator@mycompany.com",
  "mail_server": "smtp@mycompany.com"
}
# Response
200 OK
```
### Configuring a filter with an enclosed rule
```JSON
# API
POST /support/ems/filters
# JSON Body
{
  "name": "critical-wafl",
  "rules": [
    {
      "index": 1,
      "type": "include",
      "message_criteria": {
        "name_pattern": "wafl.*",
        "severities": "emergency,error,alert"
      }
    }
  ]
}
# Response
201 Created
```
### Setting up an email destination
```JSON
# API
POST /support/ems/destinations
# JSON Body
{
  "name": "Technician_Email",
  "type": "email",
  "destination": "technician@mycompany.com",
  "filters": [
    { "name" : "critical-wafl" }
  ]
}
# Response
201 Created
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["EmsConfig", "EmsConfigSchema"]
__pdoc__ = {
    "EmsConfigSchema.resource": False,
    "EmsConfigSchema.patchable_fields": False,
    "EmsConfigSchema.postable_fields": False,
}


class EmsConfigSchema(ResourceSchema):
    """The fields of the EmsConfig object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ems_config. """

    mail_from = fields.Str(
        data_key="mail_from",
    )
    r""" Mail from

Example: administrator@mycompany.com """

    mail_server = fields.Str(
        data_key="mail_server",
    )
    r""" Mail server (SMTP)

Example: mail@mycompany.com """

    proxy_password = fields.Str(
        data_key="proxy_password",
    )
    r""" Password for HTTP/HTTPS proxy

Example: password """

    proxy_url = fields.Str(
        data_key="proxy_url",
    )
    r""" HTTP/HTTPS proxy URL

Example: https://proxyserver.mycompany.com """

    proxy_user = fields.Str(
        data_key="proxy_user",
    )
    r""" User name for HTTP/HTTPS proxy

Example: proxy_user """

    @property
    def resource(self):
        return EmsConfig

    @property
    def patchable_fields(self):
        return [
            "mail_from",
            "mail_server",
            "proxy_password",
            "proxy_url",
            "proxy_user",
        ]

    @property
    def postable_fields(self):
        return [
        ]

class EmsConfig(Resource):
    """Allows interaction with EmsConfig objects on the host"""

    _schema = EmsConfigSchema
    _path = "/api/support/ems"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the EMS configuration.
### Related ONTAP commands
* `event config show`

### Learn more
* [`DOC /support/ems`](#docs-support-support_ems)"""
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
        r"""Updates the EMS configuration.
### Related ONTAP commands
* `event config modify`

### Learn more
* [`DOC /support/ems`](#docs-support-support_ems)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



