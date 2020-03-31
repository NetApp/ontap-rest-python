# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Allows access to the EMS event catalog. The catalog contains a list of all events supported by the system and their corresponding descriptions, the reason for an event occurrence, and how to correct issues related to the event.
## Example
### Querying for the first event that has a message name beginning with 'C'
```JSON
# API
GET /api/support/ems/messages?fields=name&max_records=1&name=C*
# Response
200 OK
# JSON Body
{
  "records": [
    {
      "name": "CR.Data.File.Inaccessible",
      "_links": {
        "self": {
          "href": "/api/support/ems/messages/CR.Data.File.Inaccessible"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/support/ems/messages?fields=name&max_records=1&name=C*"
    },
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


__all__ = ["EmsMessage", "EmsMessageSchema"]
__pdoc__ = {
    "EmsMessageSchema.resource": False,
    "EmsMessageSchema.patchable_fields": False,
    "EmsMessageSchema.postable_fields": False,
}


class EmsMessageSchema(ResourceSchema):
    """The fields of the EmsMessage object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ems_message. """

    corrective_action = fields.Str(
        data_key="corrective_action",
    )
    r""" Corrective action """

    deprecated = fields.Boolean(
        data_key="deprecated",
    )
    r""" Is deprecated?

Example: true """

    description = fields.Str(
        data_key="description",
    )
    r""" Description """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the event.

Example: callhome.spares.low """

    severity = fields.Str(
        data_key="severity",
        validate=enum_validation(['emergency', 'alert', 'error', 'notice', 'informational', 'debug']),
    )
    r""" Severity

Valid choices:

* emergency
* alert
* error
* notice
* informational
* debug """

    snmp_trap_type = fields.Str(
        data_key="snmp_trap_type",
        validate=enum_validation(['standard', 'built_in', 'severity_based']),
    )
    r""" SNMP trap type

Valid choices:

* standard
* built_in
* severity_based """

    @property
    def resource(self):
        return EmsMessage

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]

class EmsMessage(Resource):
    """Allows interaction with EmsMessage objects on the host"""

    _schema = EmsMessageSchema
    _path = "/api/support/ems/messages"

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
        r"""Retrieves the event catalog definitions.
### Related ONTAP commands
* `event catalog show`

### Learn more
* [`DOC /support/ems/messages`](#docs-support-support_ems_messages)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the event catalog definitions.
### Related ONTAP commands
* `event catalog show`

### Learn more
* [`DOC /support/ems/messages`](#docs-support-support_ems_messages)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






