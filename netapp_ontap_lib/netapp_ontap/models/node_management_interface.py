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


__all__ = ["NodeManagementInterface", "NodeManagementInterfaceSchema"]
__pdoc__ = {
    "NodeManagementInterfaceSchema.resource": False,
    "NodeManagementInterface": False,
}


class NodeManagementInterfaceSchema(ResourceSchema):
    """The fields of the NodeManagementInterface object"""

    ip = fields.Nested("netapp_ontap.models.node_setup_ip.NodeSetupIpSchema", unknown=EXCLUDE, data_key="ip")
    r""" The ip field of the node_management_interface. """

    @property
    def resource(self):
        return NodeManagementInterface

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "ip",
        ]


class NodeManagementInterface(Resource):  # pylint: disable=missing-docstring

    _schema = NodeManagementInterfaceSchema
