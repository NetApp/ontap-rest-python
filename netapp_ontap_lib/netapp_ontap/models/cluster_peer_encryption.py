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


__all__ = ["ClusterPeerEncryption", "ClusterPeerEncryptionSchema"]
__pdoc__ = {
    "ClusterPeerEncryptionSchema.resource": False,
    "ClusterPeerEncryption": False,
}


class ClusterPeerEncryptionSchema(ResourceSchema):
    """The fields of the ClusterPeerEncryption object"""

    proposed = fields.Str(data_key="proposed")
    r""" The proposed field of the cluster_peer_encryption.

Valid choices:

* none
* tls_psk """

    state = fields.Str(data_key="state")
    r""" The state field of the cluster_peer_encryption.

Valid choices:

* none
* tls_psk """

    @property
    def resource(self):
        return ClusterPeerEncryption

    @property
    def patchable_fields(self):
        return [
            "proposed",
        ]

    @property
    def postable_fields(self):
        return [
            "proposed",
        ]


class ClusterPeerEncryption(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterPeerEncryptionSchema
