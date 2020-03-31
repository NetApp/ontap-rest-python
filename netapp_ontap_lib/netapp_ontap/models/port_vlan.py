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


__all__ = ["PortVlan", "PortVlanSchema"]
__pdoc__ = {
    "PortVlanSchema.resource": False,
    "PortVlan": False,
}


class PortVlanSchema(ResourceSchema):
    """The fields of the PortVlan object"""

    base_port = fields.Nested("netapp_ontap.resources.port.PortSchema", unknown=EXCLUDE, data_key="base_port")
    r""" The base_port field of the port_vlan. """

    tag = fields.Integer(data_key="tag")
    r""" VLAN ID

Example: 100 """

    @property
    def resource(self):
        return PortVlan

    @property
    def patchable_fields(self):
        return [
            "base_port.name",
            "base_port.node",
            "base_port.uuid",
            "tag",
        ]

    @property
    def postable_fields(self):
        return [
            "base_port.name",
            "base_port.node",
            "base_port.uuid",
            "tag",
        ]


class PortVlan(Resource):  # pylint: disable=missing-docstring

    _schema = PortVlanSchema
