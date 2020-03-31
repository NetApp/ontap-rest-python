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


__all__ = ["NvmeSubsystemControllerAdminQueue", "NvmeSubsystemControllerAdminQueueSchema"]
__pdoc__ = {
    "NvmeSubsystemControllerAdminQueueSchema.resource": False,
    "NvmeSubsystemControllerAdminQueue": False,
}


class NvmeSubsystemControllerAdminQueueSchema(ResourceSchema):
    """The fields of the NvmeSubsystemControllerAdminQueue object"""

    depth = fields.Integer(data_key="depth")
    r""" The depth of the admin queue for the controller. """

    @property
    def resource(self):
        return NvmeSubsystemControllerAdminQueue

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class NvmeSubsystemControllerAdminQueue(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeSubsystemControllerAdminQueueSchema
