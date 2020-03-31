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


__all__ = ["FcPortReferenceNode", "FcPortReferenceNodeSchema"]
__pdoc__ = {
    "FcPortReferenceNodeSchema.resource": False,
    "FcPortReferenceNode": False,
}


class FcPortReferenceNodeSchema(ResourceSchema):
    """The fields of the FcPortReferenceNode object"""

    name = fields.Str(data_key="name")
    r""" The name of the node on which the FC port is located.


Example: node1 """

    @property
    def resource(self):
        return FcPortReferenceNode

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class FcPortReferenceNode(Resource):  # pylint: disable=missing-docstring

    _schema = FcPortReferenceNodeSchema
