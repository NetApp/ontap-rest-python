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


__all__ = ["NvmeSubsystemIoQueue", "NvmeSubsystemIoQueueSchema"]
__pdoc__ = {
    "NvmeSubsystemIoQueueSchema.resource": False,
    "NvmeSubsystemIoQueue": False,
}


class NvmeSubsystemIoQueueSchema(ResourceSchema):
    """The fields of the NvmeSubsystemIoQueue object"""

    default = fields.Nested("netapp_ontap.models.nvme_subsystem_io_queue_default.NvmeSubsystemIoQueueDefaultSchema", unknown=EXCLUDE, data_key="default")
    r""" The default field of the nvme_subsystem_io_queue. """

    @property
    def resource(self):
        return NvmeSubsystemIoQueue

    @property
    def patchable_fields(self):
        return [
            "default",
        ]

    @property
    def postable_fields(self):
        return [
            "default",
        ]


class NvmeSubsystemIoQueue(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeSubsystemIoQueueSchema
