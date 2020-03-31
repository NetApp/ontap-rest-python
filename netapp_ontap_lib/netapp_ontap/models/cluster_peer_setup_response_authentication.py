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


__all__ = ["ClusterPeerSetupResponseAuthentication", "ClusterPeerSetupResponseAuthenticationSchema"]
__pdoc__ = {
    "ClusterPeerSetupResponseAuthenticationSchema.resource": False,
    "ClusterPeerSetupResponseAuthentication": False,
}


class ClusterPeerSetupResponseAuthenticationSchema(ResourceSchema):
    """The fields of the ClusterPeerSetupResponseAuthentication object"""

    expiry_time = fields.DateTime(data_key="expiry_time")
    r""" The date and time the passphrase will expire.  The default expiry time is one hour.

Example: 2017-01-25T11:20:13.000+0000 """

    passphrase = fields.Str(data_key="passphrase")
    r""" A password to authenticate the cluster peer relationship. """

    @property
    def resource(self):
        return ClusterPeerSetupResponseAuthentication

    @property
    def patchable_fields(self):
        return [
            "expiry_time",
            "passphrase",
        ]

    @property
    def postable_fields(self):
        return [
            "expiry_time",
            "passphrase",
        ]


class ClusterPeerSetupResponseAuthentication(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterPeerSetupResponseAuthenticationSchema
