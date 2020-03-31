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


__all__ = ["SoftwareUpdateDetailsReferenceNode", "SoftwareUpdateDetailsReferenceNodeSchema"]
__pdoc__ = {
    "SoftwareUpdateDetailsReferenceNodeSchema.resource": False,
    "SoftwareUpdateDetailsReferenceNode": False,
}


class SoftwareUpdateDetailsReferenceNodeSchema(ResourceSchema):
    """The fields of the SoftwareUpdateDetailsReferenceNode object"""

    name = fields.Str(data_key="name")
    r""" Name of the node to be retrieved for update details.

Example: node1 """

    @property
    def resource(self):
        return SoftwareUpdateDetailsReferenceNode

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class SoftwareUpdateDetailsReferenceNode(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareUpdateDetailsReferenceNodeSchema
