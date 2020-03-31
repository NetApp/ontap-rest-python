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


__all__ = ["AggregateDataEncryption", "AggregateDataEncryptionSchema"]
__pdoc__ = {
    "AggregateDataEncryptionSchema.resource": False,
    "AggregateDataEncryption": False,
}


class AggregateDataEncryptionSchema(ResourceSchema):
    """The fields of the AggregateDataEncryption object"""

    drive_protection_enabled = fields.Boolean(data_key="drive_protection_enabled")
    r""" Aggregate uses self-encrypting drives with data protection enabled. """

    software_encryption_enabled = fields.Boolean(data_key="software_encryption_enabled")
    r""" NetApp Aggregate Encryption enabled. All data in the aggregate is encrypted. """

    @property
    def resource(self):
        return AggregateDataEncryption

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class AggregateDataEncryption(Resource):  # pylint: disable=missing-docstring

    _schema = AggregateDataEncryptionSchema
