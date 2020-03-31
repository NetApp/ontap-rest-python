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


__all__ = ["Peer", "PeerSchema"]
__pdoc__ = {
    "PeerSchema.resource": False,
    "Peer": False,
}


class PeerSchema(ResourceSchema):
    """The fields of the Peer object"""

    cluster = fields.Nested("netapp_ontap.resources.cluster_peer.ClusterPeerSchema", unknown=EXCLUDE, data_key="cluster")
    r""" The cluster field of the peer. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", unknown=EXCLUDE, data_key="svm")
    r""" The svm field of the peer. """

    @property
    def resource(self):
        return Peer

    @property
    def patchable_fields(self):
        return [
            "cluster.name",
            "cluster.uuid",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "cluster.name",
            "cluster.uuid",
            "svm.name",
            "svm.uuid",
        ]


class Peer(Resource):  # pylint: disable=missing-docstring

    _schema = PeerSchema
