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


__all__ = ["BgpPeerGroupPeer", "BgpPeerGroupPeerSchema"]
__pdoc__ = {
    "BgpPeerGroupPeerSchema.resource": False,
    "BgpPeerGroupPeer": False,
}


class BgpPeerGroupPeerSchema(ResourceSchema):
    """The fields of the BgpPeerGroupPeer object"""

    address = fields.Str(data_key="address")
    r""" Peer router address

Example: 10.10.10.7 """

    asn = fields.Integer(data_key="asn")
    r""" Autonomous system number of peer """

    @property
    def resource(self):
        return BgpPeerGroupPeer

    @property
    def patchable_fields(self):
        return [
            "address",
        ]

    @property
    def postable_fields(self):
        return [
            "address",
            "asn",
        ]


class BgpPeerGroupPeer(Resource):  # pylint: disable=missing-docstring

    _schema = BgpPeerGroupPeerSchema
