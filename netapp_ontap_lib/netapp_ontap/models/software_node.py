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


__all__ = ["SoftwareNode", "SoftwareNodeSchema"]
__pdoc__ = {
    "SoftwareNodeSchema.resource": False,
    "SoftwareNode": False,
}


class SoftwareNodeSchema(ResourceSchema):
    """The fields of the SoftwareNode object"""

    name = fields.Str(data_key="name")
    r""" Name of the node.

Example: node1 """

    version = fields.Str(data_key="version")
    r""" ONTAP version of the node.

Example: ONTAP_X """

    @property
    def resource(self):
        return SoftwareNode

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class SoftwareNode(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareNodeSchema
