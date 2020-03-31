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


__all__ = ["ClusterPeerAuthentication", "ClusterPeerAuthenticationSchema"]
__pdoc__ = {
    "ClusterPeerAuthenticationSchema.resource": False,
    "ClusterPeerAuthentication": False,
}


class ClusterPeerAuthenticationSchema(ResourceSchema):
    """The fields of the ClusterPeerAuthentication object"""

    expiry_time = fields.Str(data_key="expiry_time")
    r""" The time when the passphrase will expire, in ISO 8601 duration format or date and time format.  The default is 1 hour.

Example: P1DT2H3M4S or '2017-01-25T11:20:13Z' """

    generate_passphrase = fields.Boolean(data_key="generate_passphrase")
    r""" Auto generate a passphrase when true. """

    in_use = fields.Str(data_key="in_use")
    r""" The in_use field of the cluster_peer_authentication.

Valid choices:

* ok
* absent
* revoked """

    passphrase = fields.Str(data_key="passphrase")
    r""" A password to authenticate the cluster peer relationship. """

    state = fields.Str(data_key="state")
    r""" The state field of the cluster_peer_authentication.

Valid choices:

* ok
* absent
* pending
* problem """

    @property
    def resource(self):
        return ClusterPeerAuthentication

    @property
    def patchable_fields(self):
        return [
            "expiry_time",
            "generate_passphrase",
            "in_use",
            "passphrase",
        ]

    @property
    def postable_fields(self):
        return [
            "expiry_time",
            "generate_passphrase",
            "in_use",
            "passphrase",
        ]


class ClusterPeerAuthentication(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterPeerAuthenticationSchema
