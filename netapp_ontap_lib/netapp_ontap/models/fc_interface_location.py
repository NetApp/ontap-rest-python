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


__all__ = ["FcInterfaceLocation", "FcInterfaceLocationSchema"]
__pdoc__ = {
    "FcInterfaceLocationSchema.resource": False,
    "FcInterfaceLocation": False,
}


class FcInterfaceLocationSchema(ResourceSchema):
    """The fields of the FcInterfaceLocation object"""

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, data_key="node")
    r""" The node field of the fc_interface_location. """

    port = fields.Nested("netapp_ontap.resources.fc_port.FcPortSchema", unknown=EXCLUDE, data_key="port")
    r""" The port field of the fc_interface_location. """

    @property
    def resource(self):
        return FcInterfaceLocation

    @property
    def patchable_fields(self):
        return [
            "node.name",
            "node.uuid",
            "port.name",
            "port.node",
            "port.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "node.name",
            "node.uuid",
            "port.name",
            "port.node",
            "port.uuid",
        ]


class FcInterfaceLocation(Resource):  # pylint: disable=missing-docstring

    _schema = FcInterfaceLocationSchema
