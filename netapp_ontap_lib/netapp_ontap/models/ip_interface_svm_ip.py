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


__all__ = ["IpInterfaceSvmIp", "IpInterfaceSvmIpSchema"]
__pdoc__ = {
    "IpInterfaceSvmIpSchema.resource": False,
    "IpInterfaceSvmIp": False,
}


class IpInterfaceSvmIpSchema(ResourceSchema):
    """The fields of the IpInterfaceSvmIp object"""

    address = fields.Str(data_key="address")
    r""" The address field of the ip_interface_svm_ip. """

    netmask = fields.Str(data_key="netmask")
    r""" The netmask field of the ip_interface_svm_ip. """

    @property
    def resource(self):
        return IpInterfaceSvmIp

    @property
    def patchable_fields(self):
        return [
            "address",
            "netmask",
        ]

    @property
    def postable_fields(self):
        return [
            "address",
            "netmask",
        ]


class IpInterfaceSvmIp(Resource):  # pylint: disable=missing-docstring

    _schema = IpInterfaceSvmIpSchema
