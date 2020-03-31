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


__all__ = ["IpInterfaceReferenceIp", "IpInterfaceReferenceIpSchema"]
__pdoc__ = {
    "IpInterfaceReferenceIpSchema.resource": False,
    "IpInterfaceReferenceIp": False,
}


class IpInterfaceReferenceIpSchema(ResourceSchema):
    """The fields of the IpInterfaceReferenceIp object"""

    address = fields.Str(data_key="address")
    r""" The address field of the ip_interface_reference_ip. """

    @property
    def resource(self):
        return IpInterfaceReferenceIp

    @property
    def patchable_fields(self):
        return [
            "address",
        ]

    @property
    def postable_fields(self):
        return [
            "address",
        ]


class IpInterfaceReferenceIp(Resource):  # pylint: disable=missing-docstring

    _schema = IpInterfaceReferenceIpSchema
