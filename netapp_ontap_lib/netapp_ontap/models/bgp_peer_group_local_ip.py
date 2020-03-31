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


__all__ = ["BgpPeerGroupLocalIp", "BgpPeerGroupLocalIpSchema"]
__pdoc__ = {
    "BgpPeerGroupLocalIpSchema.resource": False,
    "BgpPeerGroupLocalIp": False,
}


class BgpPeerGroupLocalIpSchema(ResourceSchema):
    """The fields of the BgpPeerGroupLocalIp object"""

    address = fields.Str(data_key="address")
    r""" The address field of the bgp_peer_group_local_ip. """

    netmask = fields.Str(data_key="netmask")
    r""" The netmask field of the bgp_peer_group_local_ip. """

    @property
    def resource(self):
        return BgpPeerGroupLocalIp

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


class BgpPeerGroupLocalIp(Resource):  # pylint: disable=missing-docstring

    _schema = BgpPeerGroupLocalIpSchema
