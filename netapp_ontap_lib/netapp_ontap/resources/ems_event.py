# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Queries a live collection of observed events on the system.
## Example
### Querying for the latest event received by EMS
```JSON
# API
GET /api/support/ems/events?fields=message.name&max_records=1
# Response
200 OK
# JSON Body
{
  "records": [
    {
      "node": {
        "name": "node1",
        "uuid": "f087b8e3-99ac-11e8-b5a5-005056bb4ec7",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/f087b8e3-99ac-11e8-b5a5-005056bb4ec7"
          }
        }
      },
      "index": 661,
      "message": {
        "name": "raid.aggr.log.CP.count"
      },
      "_links": {
        "self": {
          "href": "/api/support/ems/events/node1/661"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/support/ems/events?fields=message.name&max_records=1"
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


__all__ = ["EmsEvent", "EmsEventSchema"]
__pdoc__ = {
    "EmsEventSchema.resource": False,
    "EmsEventSchema.patchable_fields": False,
    "EmsEventSchema.postable_fields": False,
}


class EmsEventSchema(ResourceSchema):
    """The fields of the EmsEvent object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ems_event. """

    index = fields.Integer(
        data_key="index",
    )
    r""" Index of the event. Returned by default.

Example: 1 """

    log_message = fields.Str(
        data_key="log_message",
    )
    r""" A formatted text string populated with parameter details. Returned by default. """

    message = fields.Nested("netapp_ontap.models.ems_event_message.EmsEventMessageSchema", data_key="message", unknown=EXCLUDE)
    r""" The message field of the ems_event. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the ems_event. """

    parameters = fields.List(fields.Nested("netapp_ontap.models.ems_event_parameter.EmsEventParameterSchema", unknown=EXCLUDE), data_key="parameters")
    r""" A list of parameters provided with the EMS event. """

    source = fields.Str(
        data_key="source",
    )
    r""" Source """

    time = fields.Str(
        data_key="time",
    )
    r""" Timestamp of the event. Returned by default. """

    @property
    def resource(self):
        return EmsEvent

    @property
    def patchable_fields(self):
        return [
            "message",
            "node.name",
            "node.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "message",
            "node.name",
            "node.uuid",
        ]

class EmsEvent(Resource):
    """Allows interaction with EmsEvent objects on the host"""

    _schema = EmsEventSchema
    _path = "/api/support/ems/events"

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
        r"""Retrieves a collection of observed events.
### Related ONTAP commands
* `event log show`

### Learn more
* [`DOC /support/ems/events`](#docs-support-support_ems_events)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of observed events.
### Related ONTAP commands
* `event log show`

### Learn more
* [`DOC /support/ems/events`](#docs-support-support_ems_events)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






