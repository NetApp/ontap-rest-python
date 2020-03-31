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


__all__ = ["SoftwareStatusDetailsReferenceNode", "SoftwareStatusDetailsReferenceNodeSchema"]
__pdoc__ = {
    "SoftwareStatusDetailsReferenceNodeSchema.resource": False,
    "SoftwareStatusDetailsReferenceNode": False,
}


class SoftwareStatusDetailsReferenceNodeSchema(ResourceSchema):
    """The fields of the SoftwareStatusDetailsReferenceNode object"""

    name = fields.Str(data_key="name")
    r""" Name of the node to be retrieved for status details.

Example: node1 """

    @property
    def resource(self):
        return SoftwareStatusDetailsReferenceNode

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class SoftwareStatusDetailsReferenceNode(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareStatusDetailsReferenceNodeSchema
