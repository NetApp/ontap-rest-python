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


__all__ = ["ClusterPeerLocalNetwork", "ClusterPeerLocalNetworkSchema"]
__pdoc__ = {
    "ClusterPeerLocalNetworkSchema.resource": False,
    "ClusterPeerLocalNetwork": False,
}


class ClusterPeerLocalNetworkSchema(ResourceSchema):
    """The fields of the ClusterPeerLocalNetwork object"""

    broadcast_domain = fields.Str(data_key="broadcast_domain")
    r""" Broadcast domain that is in use within the IPspace.

Example: bd1 """

    gateway = fields.Str(data_key="gateway")
    r""" The IPv4 or IPv6 address of the default router.

Example: 10.1.1.1 """

    interfaces = fields.List(fields.Nested("netapp_ontap.models.cluster_peer_local_network_interfaces.ClusterPeerLocalNetworkInterfacesSchema", unknown=EXCLUDE), data_key="interfaces")
    r""" The interfaces field of the cluster_peer_local_network. """

    netmask = fields.Str(data_key="netmask")
    r""" IPv4 mask or netmask length.

Example: 255.255.0.0 """

    @property
    def resource(self):
        return ClusterPeerLocalNetwork

    @property
    def patchable_fields(self):
        return [
            "broadcast_domain",
            "gateway",
            "interfaces",
            "netmask",
        ]

    @property
    def postable_fields(self):
        return [
            "broadcast_domain",
            "gateway",
            "interfaces",
            "netmask",
        ]


class ClusterPeerLocalNetwork(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterPeerLocalNetworkSchema
