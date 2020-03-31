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


__all__ = ["AuditSchedule", "AuditScheduleSchema"]
__pdoc__ = {
    "AuditScheduleSchema.resource": False,
    "AuditSchedule": False,
}


class AuditScheduleSchema(ResourceSchema):
    """The fields of the AuditSchedule object"""

    days = fields.List(fields.Integer, data_key="days")
    r""" Specifies the day of the month schedule to rotate audit log. Leave empty for all. """

    hours = fields.List(fields.Integer, data_key="hours")
    r""" Specifies the hourly schedule to rotate audit log. Leave empty for all. """

    minutes = fields.List(fields.Integer, data_key="minutes")
    r""" Specifies the minutes schedule to rotate the audit log. """

    months = fields.List(fields.Integer, data_key="months")
    r""" Specifies the months schedule to rotate audit log. Leave empty for all. """

    weekdays = fields.List(fields.Integer, data_key="weekdays")
    r""" Specifies the weekdays schedule to rotate audit log. Leave empty for all. """

    @property
    def resource(self):
        return AuditSchedule

    @property
    def patchable_fields(self):
        return [
            "days",
            "hours",
            "minutes",
            "months",
            "weekdays",
        ]

    @property
    def postable_fields(self):
        return [
            "days",
            "hours",
            "minutes",
            "months",
            "weekdays",
        ]


class AuditSchedule(Resource):  # pylint: disable=missing-docstring

    _schema = AuditScheduleSchema
