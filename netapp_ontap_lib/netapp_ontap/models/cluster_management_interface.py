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


__all__ = ["ClusterManagementInterface", "ClusterManagementInterfaceSchema"]
__pdoc__ = {
    "ClusterManagementInterfaceSchema.resource": False,
    "ClusterManagementInterface": False,
}


class ClusterManagementInterfaceSchema(ResourceSchema):
    """The fields of the ClusterManagementInterface object"""

    ip = fields.Nested("netapp_ontap.models.ip_interface_and_gateway.IpInterfaceAndGatewaySchema", unknown=EXCLUDE, data_key="ip")
    r""" The ip field of the cluster_management_interface. """

    @property
    def resource(self):
        return ClusterManagementInterface

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ClusterManagementInterface(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterManagementInterfaceSchema
