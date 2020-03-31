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


__all__ = ["ScheduleCron", "ScheduleCronSchema"]
__pdoc__ = {
    "ScheduleCronSchema.resource": False,
    "ScheduleCron": False,
}


class ScheduleCronSchema(ResourceSchema):
    """The fields of the ScheduleCron object"""

    days = fields.List(fields.Integer, data_key="days")
    r""" The days of the month the schedule runs. Leave empty for all. """

    hours = fields.List(fields.Integer, data_key="hours")
    r""" The hours of the day the schedule runs. Leave empty for all. """

    minutes = fields.List(fields.Integer, data_key="minutes")
    r""" The minutes the schedule runs. Required on POST for a cron schedule. """

    months = fields.List(fields.Integer, data_key="months")
    r""" The months of the year the schedule runs. Leave empty for all. """

    weekdays = fields.List(fields.Integer, data_key="weekdays")
    r""" The weekdays the schedule runs. Leave empty for all. """

    @property
    def resource(self):
        return ScheduleCron

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


class ScheduleCron(Resource):  # pylint: disable=missing-docstring

    _schema = ScheduleCronSchema
