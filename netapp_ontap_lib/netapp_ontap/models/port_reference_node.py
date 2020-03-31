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


__all__ = ["PortReferenceNode", "PortReferenceNodeSchema"]
__pdoc__ = {
    "PortReferenceNodeSchema.resource": False,
    "PortReferenceNode": False,
}


class PortReferenceNodeSchema(ResourceSchema):
    """The fields of the PortReferenceNode object"""

    name = fields.Str(data_key="name")
    r""" Name of node on which the port is located.

Example: node1 """

    @property
    def resource(self):
        return PortReferenceNode

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


class PortReferenceNode(Resource):  # pylint: disable=missing-docstring

    _schema = PortReferenceNodeSchema
