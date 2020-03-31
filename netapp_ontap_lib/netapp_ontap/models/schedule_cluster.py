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


__all__ = ["ScheduleCluster", "ScheduleClusterSchema"]
__pdoc__ = {
    "ScheduleClusterSchema.resource": False,
    "ScheduleCluster": False,
}


class ScheduleClusterSchema(ResourceSchema):
    """The fields of the ScheduleCluster object"""

    name = fields.Str(data_key="name")
    r""" Cluster name

Example: cluster1 """

    uuid = fields.Str(data_key="uuid")
    r""" Cluster UUID

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return ScheduleCluster

    @property
    def patchable_fields(self):
        return [
            "name",
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "uuid",
        ]


class ScheduleCluster(Resource):  # pylint: disable=missing-docstring

    _schema = ScheduleClusterSchema
