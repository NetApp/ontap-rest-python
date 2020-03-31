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


__all__ = ["IpInterfaceSvmLocation", "IpInterfaceSvmLocationSchema"]
__pdoc__ = {
    "IpInterfaceSvmLocationSchema.resource": False,
    "IpInterfaceSvmLocation": False,
}


class IpInterfaceSvmLocationSchema(ResourceSchema):
    """The fields of the IpInterfaceSvmLocation object"""

    broadcast_domain = fields.Nested("netapp_ontap.models.broadcast_domain_svm.BroadcastDomainSvmSchema", unknown=EXCLUDE, data_key="broadcast_domain")
    r""" The broadcast_domain field of the ip_interface_svm_location. """

    home_node = fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, data_key="home_node")
    r""" The home_node field of the ip_interface_svm_location. """

    @property
    def resource(self):
        return IpInterfaceSvmLocation

    @property
    def patchable_fields(self):
        return [
            "broadcast_domain.name",
            "broadcast_domain.uuid",
            "home_node.name",
            "home_node.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "broadcast_domain.name",
            "broadcast_domain.uuid",
            "home_node.name",
            "home_node.uuid",
        ]


class IpInterfaceSvmLocation(Resource):  # pylint: disable=missing-docstring

    _schema = IpInterfaceSvmLocationSchema
