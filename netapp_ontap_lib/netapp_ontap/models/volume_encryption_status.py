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


__all__ = ["VolumeEncryptionStatus", "VolumeEncryptionStatusSchema"]
__pdoc__ = {
    "VolumeEncryptionStatusSchema.resource": False,
    "VolumeEncryptionStatus": False,
}


class VolumeEncryptionStatusSchema(ResourceSchema):
    """The fields of the VolumeEncryptionStatus object"""

    code = fields.Str(data_key="code")
    r""" Encryption progress message code. """

    message = fields.Str(data_key="message")
    r""" Encryption progress message. """

    @property
    def resource(self):
        return VolumeEncryptionStatus

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class VolumeEncryptionStatus(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeEncryptionStatusSchema
