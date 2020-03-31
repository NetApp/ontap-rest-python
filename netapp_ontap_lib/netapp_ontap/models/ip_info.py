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


__all__ = ["IpInfo", "IpInfoSchema"]
__pdoc__ = {
    "IpInfoSchema.resource": False,
    "IpInfo": False,
}


class IpInfoSchema(ResourceSchema):
    """The fields of the IpInfo object"""

    address = fields.Str(data_key="address")
    r""" The address field of the ip_info. """

    family = fields.Str(data_key="family")
    r""" The family field of the ip_info. """

    netmask = fields.Str(data_key="netmask")
    r""" The netmask field of the ip_info. """

    @property
    def resource(self):
        return IpInfo

    @property
    def patchable_fields(self):
        return [
            "address",
            "family",
            "netmask",
        ]

    @property
    def postable_fields(self):
        return [
            "address",
            "family",
            "netmask",
        ]


class IpInfo(Resource):  # pylint: disable=missing-docstring

    _schema = IpInfoSchema
