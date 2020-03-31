# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema


__all__ = ["EmsEventMessage", "EmsEventMessageSchema"]
__pdoc__ = {
    "EmsEventMessageSchema.resource": False,
    "EmsEventMessage": False,
}


class EmsEventMessageSchema(ResourceSchema):
    """The fields of the EmsEventMessage object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the ems_event_message. """

    name = fields.Str(data_key="name")
    r""" Message name of the event. Returned by default.

Example: callhome.spares.low """

    severity = fields.Str(data_key="severity")
    r""" Severity of the event. Returned by default.

Valid choices:

* emergency
* alert
* error
* notice
* informational
* debug """

    @property
    def resource(self):
        return EmsEventMessage

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class EmsEventMessage(Resource):  # pylint: disable=missing-docstring

    _schema = EmsEventMessageSchema
