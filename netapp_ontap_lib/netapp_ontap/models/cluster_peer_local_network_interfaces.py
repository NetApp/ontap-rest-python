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


__all__ = ["ClusterPeerLocalNetworkInterfaces", "ClusterPeerLocalNetworkInterfacesSchema"]
__pdoc__ = {
    "ClusterPeerLocalNetworkInterfacesSchema.resource": False,
    "ClusterPeerLocalNetworkInterfaces": False,
}


class ClusterPeerLocalNetworkInterfacesSchema(ResourceSchema):
    """The fields of the ClusterPeerLocalNetworkInterfaces object"""

    ip_address = fields.Str(data_key="ip_address")
    r""" List of local intercluster IP addresses. """

    @property
    def resource(self):
        return ClusterPeerLocalNetworkInterfaces

    @property
    def patchable_fields(self):
        return [
            "ip_address",
        ]

    @property
    def postable_fields(self):
        return [
            "ip_address",
        ]


class ClusterPeerLocalNetworkInterfaces(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterPeerLocalNetworkInterfacesSchema
