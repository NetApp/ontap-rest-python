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


__all__ = ["NodeSetupIp", "NodeSetupIpSchema"]
__pdoc__ = {
    "NodeSetupIpSchema.resource": False,
    "NodeSetupIp": False,
}


class NodeSetupIpSchema(ResourceSchema):
    """The fields of the NodeSetupIp object"""

    address = fields.Str(data_key="address")
    r""" The address field of the node_setup_ip. """

    @property
    def resource(self):
        return NodeSetupIp

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "address",
        ]


class NodeSetupIp(Resource):  # pylint: disable=missing-docstring

    _schema = NodeSetupIpSchema
