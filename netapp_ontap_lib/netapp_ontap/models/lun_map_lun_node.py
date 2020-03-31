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


__all__ = ["LunMapLunNode", "LunMapLunNodeSchema"]
__pdoc__ = {
    "LunMapLunNodeSchema.resource": False,
    "LunMapLunNode": False,
}


class LunMapLunNodeSchema(ResourceSchema):
    """The fields of the LunMapLunNode object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the lun_map_lun_node. """

    name = fields.Str(data_key="name")
    r""" The name the LUN's node.


Example: node1 """

    uuid = fields.Str(data_key="uuid")
    r""" The unique identifier of the LUN node.


Example: 1cf8aa42-8cd1-12e0-a11c-423468563412 """

    @property
    def resource(self):
        return LunMapLunNode

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class LunMapLunNode(Resource):  # pylint: disable=missing-docstring

    _schema = LunMapLunNodeSchema
