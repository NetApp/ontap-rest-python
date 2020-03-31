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


__all__ = ["QuotaReportFiles", "QuotaReportFilesSchema"]
__pdoc__ = {
    "QuotaReportFilesSchema.resource": False,
    "QuotaReportFiles": False,
}


class QuotaReportFilesSchema(ResourceSchema):
    """The fields of the QuotaReportFiles object"""

    hard_limit = fields.Integer(data_key="hard_limit")
    r""" File hard limit """

    soft_limit = fields.Integer(data_key="soft_limit")
    r""" File soft limit """

    used = fields.Nested("netapp_ontap.models.quota_report_files_used.QuotaReportFilesUsedSchema", unknown=EXCLUDE, data_key="used")
    r""" The used field of the quota_report_files. """

    @property
    def resource(self):
        return QuotaReportFiles

    @property
    def patchable_fields(self):
        return [
            "used",
        ]

    @property
    def postable_fields(self):
        return [
            "used",
        ]


class QuotaReportFiles(Resource):  # pylint: disable=missing-docstring

    _schema = QuotaReportFilesSchema
