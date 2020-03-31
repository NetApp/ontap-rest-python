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


__all__ = ["SnapshotPolicySchedule1", "SnapshotPolicySchedule1Schema"]
__pdoc__ = {
    "SnapshotPolicySchedule1Schema.resource": False,
    "SnapshotPolicySchedule1": False,
}


class SnapshotPolicySchedule1Schema(ResourceSchema):
    """The fields of the SnapshotPolicySchedule1 object"""

    name = fields.Str(data_key="name")
    r""" Schedule at which Snapshot copies are captured on the volume. Some common schedules already defined in the system are hourly, daily, weekly, at 15 minute intervals, and at 5 minute intervals. Snapshot copy policies with custom schedules can be referenced.

Example: hourly """

    @property
    def resource(self):
        return SnapshotPolicySchedule1

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class SnapshotPolicySchedule1(Resource):  # pylint: disable=missing-docstring

    _schema = SnapshotPolicySchedule1Schema
