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


__all__ = ["BgpPeerGroupLocal", "BgpPeerGroupLocalSchema"]
__pdoc__ = {
    "BgpPeerGroupLocalSchema.resource": False,
    "BgpPeerGroupLocal": False,
}


class BgpPeerGroupLocalSchema(ResourceSchema):
    """The fields of the BgpPeerGroupLocal object"""

    interface = fields.Nested("netapp_ontap.resources.ip_interface.IpInterfaceSchema", unknown=EXCLUDE, data_key="interface")
    r""" The interface field of the bgp_peer_group_local. """

    ip = fields.Nested("netapp_ontap.models.bgp_peer_group_local_ip.BgpPeerGroupLocalIpSchema", unknown=EXCLUDE, data_key="ip")
    r""" The ip field of the bgp_peer_group_local. """

    port = fields.Nested("netapp_ontap.resources.port.PortSchema", unknown=EXCLUDE, data_key="port")
    r""" The port field of the bgp_peer_group_local. """

    @property
    def resource(self):
        return BgpPeerGroupLocal

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "interface.ip",
            "interface.name",
            "interface.uuid",
            "ip",
            "port.name",
            "port.node",
            "port.uuid",
        ]


class BgpPeerGroupLocal(Resource):  # pylint: disable=missing-docstring

    _schema = BgpPeerGroupLocalSchema
