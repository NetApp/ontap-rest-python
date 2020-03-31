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


__all__ = ["ApplicationStatisticsSnapshot", "ApplicationStatisticsSnapshotSchema"]
__pdoc__ = {
    "ApplicationStatisticsSnapshotSchema.resource": False,
    "ApplicationStatisticsSnapshot": False,
}


class ApplicationStatisticsSnapshotSchema(ResourceSchema):
    """The fields of the ApplicationStatisticsSnapshot object"""

    reserve = fields.Integer(data_key="reserve")
    r""" The amount of space reserved by the system for Snapshot copies. """

    used = fields.Integer(data_key="used")
    r""" The amount of spacing currently in use by the system to store Snapshot copies. """

    @property
    def resource(self):
        return ApplicationStatisticsSnapshot

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationStatisticsSnapshot(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationStatisticsSnapshotSchema
