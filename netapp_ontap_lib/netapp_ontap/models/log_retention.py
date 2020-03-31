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


__all__ = ["LogRetention", "LogRetentionSchema"]
__pdoc__ = {
    "LogRetentionSchema.resource": False,
    "LogRetention": False,
}


class LogRetentionSchema(ResourceSchema):
    """The fields of the LogRetention object"""

    count = fields.Integer(data_key="count")
    r""" Determines how many audit log files to retain before
rotating the oldest log file out. This is mutually exclusive with
duration. """

    duration = fields.Str(data_key="duration")
    r""" Specifies an ISO-8601 format date and time to retain the audit log file. The audit log files are
deleted once they reach the specified date/time. This is mutually exclusive with count.


Example: P4DT12H30M5S """

    @property
    def resource(self):
        return LogRetention

    @property
    def patchable_fields(self):
        return [
            "count",
            "duration",
        ]

    @property
    def postable_fields(self):
        return [
            "count",
            "duration",
        ]


class LogRetention(Resource):  # pylint: disable=missing-docstring

    _schema = LogRetentionSchema
