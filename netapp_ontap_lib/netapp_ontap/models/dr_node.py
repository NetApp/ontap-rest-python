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


__all__ = ["DrNode", "DrNodeSchema"]
__pdoc__ = {
    "DrNodeSchema.resource": False,
    "DrNode": False,
}


class DrNodeSchema(ResourceSchema):
    """The fields of the DrNode object"""

    name = fields.Str(data_key="name")
    r""" The name field of the dr_node.

Example: node1 """

    uuid = fields.Str(data_key="uuid")
    r""" The uuid field of the dr_node.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return DrNode

    @property
    def patchable_fields(self):
        return [
            "name",
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "uuid",
        ]


class DrNode(Resource):  # pylint: disable=missing-docstring

    _schema = DrNodeSchema
