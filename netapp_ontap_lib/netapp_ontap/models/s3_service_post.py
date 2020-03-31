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


__all__ = ["S3ServicePost", "S3ServicePostSchema"]
__pdoc__ = {
    "S3ServicePostSchema.resource": False,
    "S3ServicePost": False,
}


class S3ServicePostSchema(ResourceSchema):
    """The fields of the S3ServicePost object"""

    num_records = fields.Integer(data_key="num_records")
    r""" Number of Records """

    records = fields.List(fields.Nested("netapp_ontap.models.s3_service_post_response_records.S3ServicePostResponseRecordsSchema", unknown=EXCLUDE), data_key="records")
    r""" The records field of the s3_service_post. """

    @property
    def resource(self):
        return S3ServicePost

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


class S3ServicePost(Resource):  # pylint: disable=missing-docstring

    _schema = S3ServicePostSchema
