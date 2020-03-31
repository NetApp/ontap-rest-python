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


__all__ = ["ClusterPeerStatus", "ClusterPeerStatusSchema"]
__pdoc__ = {
    "ClusterPeerStatusSchema.resource": False,
    "ClusterPeerStatus": False,
}


class ClusterPeerStatusSchema(ResourceSchema):
    """The fields of the ClusterPeerStatus object"""

    state = fields.Str(data_key="state")
    r""" The state field of the cluster_peer_status.

Valid choices:

* available
* partial
* unavailable
* pending
* unidentified """

    update_time = fields.DateTime(data_key="update_time")
    r""" The last time the state was updated.

Example: 2017-01-25T11:20:13.000+0000 """

    @property
    def resource(self):
        return ClusterPeerStatus

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ClusterPeerStatus(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterPeerStatusSchema
