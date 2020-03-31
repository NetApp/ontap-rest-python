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


__all__ = ["SvmS3Service", "SvmS3ServiceSchema"]
__pdoc__ = {
    "SvmS3ServiceSchema.resource": False,
    "SvmS3Service": False,
}


class SvmS3ServiceSchema(ResourceSchema):
    """The fields of the SvmS3Service object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the svm_s3_service. """

    enabled = fields.Boolean(data_key="enabled")
    r""" Specifies whether or not to enable S3. Setting this value to true creates a service if one is not yet created. """

    name = fields.Str(data_key="name")
    r""" Specifies the name of the S3 server. A server name length can range from 1 to 15 characters and can only contain the following combination of characters 0-9, A-Z, a-z, ".", and "-".

Example: s3-server-1 """

    @property
    def resource(self):
        return SvmS3Service

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "name",
        ]


class SvmS3Service(Resource):  # pylint: disable=missing-docstring

    _schema = SvmS3ServiceSchema
