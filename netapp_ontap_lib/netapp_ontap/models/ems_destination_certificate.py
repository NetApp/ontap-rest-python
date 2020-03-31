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


__all__ = ["EmsDestinationCertificate", "EmsDestinationCertificateSchema"]
__pdoc__ = {
    "EmsDestinationCertificateSchema.resource": False,
    "EmsDestinationCertificate": False,
}


class EmsDestinationCertificateSchema(ResourceSchema):
    """The fields of the EmsDestinationCertificate object"""

    ca = fields.Str(data_key="ca")
    r""" Client certificate issuing CA

Example: VeriSign """

    serial_number = fields.Str(data_key="serial_number")
    r""" Client certificate serial number

Example: 1234567890 """

    @property
    def resource(self):
        return EmsDestinationCertificate

    @property
    def patchable_fields(self):
        return [
            "ca",
            "serial_number",
        ]

    @property
    def postable_fields(self):
        return [
            "ca",
            "serial_number",
        ]


class EmsDestinationCertificate(Resource):  # pylint: disable=missing-docstring

    _schema = EmsDestinationCertificateSchema
