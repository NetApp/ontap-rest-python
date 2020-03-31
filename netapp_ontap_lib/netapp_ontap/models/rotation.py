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


__all__ = ["Rotation", "RotationSchema"]
__pdoc__ = {
    "RotationSchema.resource": False,
    "Rotation": False,
}


class RotationSchema(ResourceSchema):
    """The fields of the Rotation object"""

    now = fields.Boolean(data_key="now")
    r""" Manually rotates the audit logs. Optional in PATCH only. Not available in POST. """

    schedule = fields.Nested("netapp_ontap.models.audit_schedule.AuditScheduleSchema", unknown=EXCLUDE, data_key="schedule")
    r""" The schedule field of the rotation. """

    size = fields.Integer(data_key="size")
    r""" Rotates logs based on log size in bytes. """

    @property
    def resource(self):
        return Rotation

    @property
    def patchable_fields(self):
        return [
            "now",
            "schedule",
            "size",
        ]

    @property
    def postable_fields(self):
        return [
            "schedule",
            "size",
        ]


class Rotation(Resource):  # pylint: disable=missing-docstring

    _schema = RotationSchema
