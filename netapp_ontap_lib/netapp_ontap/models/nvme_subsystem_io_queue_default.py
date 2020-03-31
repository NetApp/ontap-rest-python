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


__all__ = ["NvmeSubsystemIoQueueDefault", "NvmeSubsystemIoQueueDefaultSchema"]
__pdoc__ = {
    "NvmeSubsystemIoQueueDefaultSchema.resource": False,
    "NvmeSubsystemIoQueueDefault": False,
}


class NvmeSubsystemIoQueueDefaultSchema(ResourceSchema):
    """The fields of the NvmeSubsystemIoQueueDefault object"""

    count = fields.Integer(data_key="count")
    r""" The number of host I/O queue pairs.


Example: 4 """

    depth = fields.Integer(data_key="depth")
    r""" The host I/O queue depth.


Example: 16 """

    @property
    def resource(self):
        return NvmeSubsystemIoQueueDefault

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class NvmeSubsystemIoQueueDefault(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeSubsystemIoQueueDefaultSchema
