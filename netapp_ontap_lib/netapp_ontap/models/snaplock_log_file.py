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


__all__ = ["SnaplockLogFile", "SnaplockLogFileSchema"]
__pdoc__ = {
    "SnaplockLogFileSchema.resource": False,
    "SnaplockLogFile": False,
}


class SnaplockLogFileSchema(ResourceSchema):
    """The fields of the SnaplockLogFile object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the snaplock_log_file. """

    archive = fields.Boolean(data_key="archive")
    r""" Archive the specified SnapLock log file for the given base_name, and create a new log file. If base_name is not mentioned, archive all log files. """

    base_name = fields.Str(data_key="base_name")
    r""" Base name of log file

Valid choices:

* legal_hold
* privileged_delete
* system """

    expiry_time = fields.DateTime(data_key="expiry_time")
    r""" Expiry time of the log file in date-time format. Value '9999-12-31T00:00:00Z' indicates infinite expiry time.

Example: 2058-06-04T19:00:00.000+0000 """

    path = fields.Str(data_key="path")
    r""" Absolute path of the log file in the volume

Example: /snaplock_log/system_logs/20180822_005947_GMT-present """

    size = fields.Integer(data_key="size")
    r""" Size of the log file in bytes

Example: 20000 """

    @property
    def resource(self):
        return SnaplockLogFile

    @property
    def patchable_fields(self):
        return [
            "archive",
            "base_name",
        ]

    @property
    def postable_fields(self):
        return [
            "base_name",
        ]


class SnaplockLogFile(Resource):  # pylint: disable=missing-docstring

    _schema = SnaplockLogFileSchema
