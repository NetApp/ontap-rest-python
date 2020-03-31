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


__all__ = ["NvmeSubsystemHostIoQueue", "NvmeSubsystemHostIoQueueSchema"]
__pdoc__ = {
    "NvmeSubsystemHostIoQueueSchema.resource": False,
    "NvmeSubsystemHostIoQueue": False,
}


class NvmeSubsystemHostIoQueueSchema(ResourceSchema):
    """The fields of the NvmeSubsystemHostIoQueue object"""

    count = fields.Integer(data_key="count")
    r""" The number of I/O queue pairs. The default value is inherited from the owning NVMe subsystem.


Example: 4 """

    depth = fields.Integer(data_key="depth")
    r""" The I/O queue depth. The default value is inherited from the owning NVMe subsystem.


Example: 32 """

    @property
    def resource(self):
        return NvmeSubsystemHostIoQueue

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class NvmeSubsystemHostIoQueue(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeSubsystemHostIoQueueSchema
