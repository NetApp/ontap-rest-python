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


__all__ = ["SnapshotPolicyCopies", "SnapshotPolicyCopiesSchema"]
__pdoc__ = {
    "SnapshotPolicyCopiesSchema.resource": False,
    "SnapshotPolicyCopies": False,
}


class SnapshotPolicyCopiesSchema(ResourceSchema):
    """The fields of the SnapshotPolicyCopies object"""

    count = fields.Integer(data_key="count")
    r""" The number of Snapshot copies to maintain for this schedule. """

    prefix = fields.Str(data_key="prefix")
    r""" The prefix to use while creating Snapshot copies at regular intervals. """

    schedule = fields.Nested("netapp_ontap.models.snapshot_policy_schedule1.SnapshotPolicySchedule1Schema", unknown=EXCLUDE, data_key="schedule")
    r""" The schedule field of the snapshot_policy_copies. """

    snapmirror_label = fields.Str(data_key="snapmirror_label")
    r""" Label for SnapMirror operations """

    @property
    def resource(self):
        return SnapshotPolicyCopies

    @property
    def patchable_fields(self):
        return [
            "count",
            "prefix",
            "schedule",
            "snapmirror_label",
        ]

    @property
    def postable_fields(self):
        return [
            "count",
            "prefix",
            "schedule",
            "snapmirror_label",
        ]


class SnapshotPolicyCopies(Resource):  # pylint: disable=missing-docstring

    _schema = SnapshotPolicyCopiesSchema
