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


__all__ = ["S3UserPostPatch", "S3UserPostPatchSchema"]
__pdoc__ = {
    "S3UserPostPatchSchema.resource": False,
    "S3UserPostPatch": False,
}


class S3UserPostPatchSchema(ResourceSchema):
    """The fields of the S3UserPostPatch object"""

    num_records = fields.Integer(data_key="num_records")
    r""" Number of records """

    records = fields.List(fields.Nested("netapp_ontap.models.s3_service_user_post_response.S3ServiceUserPostSchema", unknown=EXCLUDE), data_key="records")
    r""" The records field of the s3_user_post_patch. """

    @property
    def resource(self):
        return S3UserPostPatch

    @property
    def patchable_fields(self):
        return [
            "num_records",
            "records",
        ]

    @property
    def postable_fields(self):
        return [
            "num_records",
            "records",
        ]


class S3UserPostPatch(Resource):  # pylint: disable=missing-docstring

    _schema = S3UserPostPatchSchema
