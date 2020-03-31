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


__all__ = ["ClusterPeerRemote", "ClusterPeerRemoteSchema"]
__pdoc__ = {
    "ClusterPeerRemoteSchema.resource": False,
    "ClusterPeerRemote": False,
}


class ClusterPeerRemoteSchema(ResourceSchema):
    """The fields of the ClusterPeerRemote object"""

    ip_addresses = fields.List(fields.Str, data_key="ip_addresses")
    r""" The IPv4 addresses, IPv6 addresses, or hostnames of the peers. """

    name = fields.Str(data_key="name")
    r""" The name of the remote cluster.

Example: cluster2 """

    serial_number = fields.Str(data_key="serial_number")
    r""" The serial number of the remote cluster.

Example: 4048820-60-9 """

    @property
    def resource(self):
        return ClusterPeerRemote

    @property
    def patchable_fields(self):
        return [
            "ip_addresses",
        ]

    @property
    def postable_fields(self):
        return [
            "ip_addresses",
        ]


class ClusterPeerRemote(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterPeerRemoteSchema
