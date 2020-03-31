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


__all__ = ["S3BucketEncryption", "S3BucketEncryptionSchema"]
__pdoc__ = {
    "S3BucketEncryptionSchema.resource": False,
    "S3BucketEncryption": False,
}


class S3BucketEncryptionSchema(ResourceSchema):
    """The fields of the S3BucketEncryption object"""

    enabled = fields.Boolean(data_key="enabled")
    r""" Specifies whether encryption is enabled on the bucket. By default, encryption is disabled on a bucket. """

    @property
    def resource(self):
        return S3BucketEncryption

    @property
    def patchable_fields(self):
        return [
            "enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
        ]


class S3BucketEncryption(Resource):  # pylint: disable=missing-docstring

    _schema = S3BucketEncryptionSchema
