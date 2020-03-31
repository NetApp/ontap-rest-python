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


__all__ = ["NvmeSubsystemControllerIoQueue", "NvmeSubsystemControllerIoQueueSchema"]
__pdoc__ = {
    "NvmeSubsystemControllerIoQueueSchema.resource": False,
    "NvmeSubsystemControllerIoQueue": False,
}


class NvmeSubsystemControllerIoQueueSchema(ResourceSchema):
    """The fields of the NvmeSubsystemControllerIoQueue object"""

    count = fields.Integer(data_key="count")
    r""" The number of I/O queues available to the controller. """

    depth = fields.List(fields.Integer, data_key="depth")
    r""" The depths of the I/O queues. """

    @property
    def resource(self):
        return NvmeSubsystemControllerIoQueue

    @property
    def patchable_fields(self):
        return [
            "depth",
        ]

    @property
    def postable_fields(self):
        return [
            "depth",
        ]


class NvmeSubsystemControllerIoQueue(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeSubsystemControllerIoQueueSchema
