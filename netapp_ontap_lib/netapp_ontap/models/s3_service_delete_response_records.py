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


__all__ = ["S3ServiceDeleteResponseRecords", "S3ServiceDeleteResponseRecordsSchema"]
__pdoc__ = {
    "S3ServiceDeleteResponseRecordsSchema.resource": False,
    "S3ServiceDeleteResponseRecords": False,
}


class S3ServiceDeleteResponseRecordsSchema(ResourceSchema):
    """The fields of the S3ServiceDeleteResponseRecords object"""

    job = fields.Nested("netapp_ontap.models.job_link.JobLinkSchema", unknown=EXCLUDE, data_key="job")
    r""" The job field of the s3_service_delete_response_records. """

    @property
    def resource(self):
        return S3ServiceDeleteResponseRecords

    @property
    def patchable_fields(self):
        return [
            "job",
        ]

    @property
    def postable_fields(self):
        return [
            "job",
        ]


class S3ServiceDeleteResponseRecords(Resource):  # pylint: disable=missing-docstring

    _schema = S3ServiceDeleteResponseRecordsSchema
