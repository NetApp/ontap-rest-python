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


__all__ = ["SecurityKeyManagerExternal", "SecurityKeyManagerExternalSchema"]
__pdoc__ = {
    "SecurityKeyManagerExternalSchema.resource": False,
    "SecurityKeyManagerExternal": False,
}


class SecurityKeyManagerExternalSchema(ResourceSchema):
    """The fields of the SecurityKeyManagerExternal object"""

    client_certificate = fields.Nested("netapp_ontap.resources.security_certificate.SecurityCertificateSchema", unknown=EXCLUDE, data_key="client_certificate")
    r""" The client_certificate field of the security_key_manager_external. """

    server_ca_certificates = fields.List(fields.Nested("netapp_ontap.resources.security_certificate.SecurityCertificateSchema", unknown=EXCLUDE), data_key="server_ca_certificates")
    r""" The UUIDs of the server CA certificates already installed in the cluster or SVM. The array of certificates are common for all the keyservers per SVM. """

    servers = fields.List(fields.Nested("netapp_ontap.models.key_server_readcreate.KeyServerReadcreateSchema", unknown=EXCLUDE), data_key="servers")
    r""" The set of external key servers. """

    @property
    def resource(self):
        return SecurityKeyManagerExternal

    @property
    def patchable_fields(self):
        return [
            "client_certificate.uuid",
            "server_ca_certificates.uuid",
            "servers",
        ]

    @property
    def postable_fields(self):
        return [
            "client_certificate.uuid",
            "server_ca_certificates.uuid",
            "servers",
        ]


class SecurityKeyManagerExternal(Resource):  # pylint: disable=missing-docstring

    _schema = SecurityKeyManagerExternalSchema
