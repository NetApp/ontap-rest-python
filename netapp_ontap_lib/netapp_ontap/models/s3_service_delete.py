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


__all__ = ["S3ServiceDelete", "S3ServiceDeleteSchema"]
__pdoc__ = {
    "S3ServiceDeleteSchema.resource": False,
    "S3ServiceDelete": False,
}


class S3ServiceDeleteSchema(ResourceSchema):
    """The fields of the S3ServiceDelete object"""

    num_records = fields.Integer(data_key="num_records")
    r""" Number of Records """

    records = fields.List(fields.Nested("netapp_ontap.models.s3_service_delete_response_records.S3ServiceDeleteResponseRecordsSchema", unknown=EXCLUDE), data_key="records")
    r""" The records field of the s3_service_delete. """

    @property
    def resource(self):
        return S3ServiceDelete

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


class S3ServiceDelete(Resource):  # pylint: disable=missing-docstring

    _schema = S3ServiceDeleteSchema
