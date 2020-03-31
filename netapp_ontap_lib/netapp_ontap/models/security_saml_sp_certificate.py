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


__all__ = ["SecuritySamlSpCertificate", "SecuritySamlSpCertificateSchema"]
__pdoc__ = {
    "SecuritySamlSpCertificateSchema.resource": False,
    "SecuritySamlSpCertificate": False,
}


class SecuritySamlSpCertificateSchema(ResourceSchema):
    """The fields of the SecuritySamlSpCertificate object"""

    ca = fields.Str(data_key="ca")
    r""" Server certificate issuing certificate authority (CA).  This cannot be used with the server certificate common name. """

    common_name = fields.Str(data_key="common_name")
    r""" Server certificate common name.  This cannot be used with the certificate authority (CA) or serial_number.

Example: cluster1 """

    serial_number = fields.Str(data_key="serial_number")
    r""" Server certificate serial number.  This cannot be used with the server certificate common name.

Example: 1506B24A94F566BA """

    @property
    def resource(self):
        return SecuritySamlSpCertificate

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "ca",
            "common_name",
            "serial_number",
        ]


class SecuritySamlSpCertificate(Resource):  # pylint: disable=missing-docstring

    _schema = SecuritySamlSpCertificateSchema
