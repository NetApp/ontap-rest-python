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


__all__ = ["QuotaReportSpace", "QuotaReportSpaceSchema"]
__pdoc__ = {
    "QuotaReportSpaceSchema.resource": False,
    "QuotaReportSpace": False,
}


class QuotaReportSpaceSchema(ResourceSchema):
    """The fields of the QuotaReportSpace object"""

    hard_limit = fields.Integer(data_key="hard_limit")
    r""" Space hard limit in bytes """

    soft_limit = fields.Integer(data_key="soft_limit")
    r""" Space soft limit in bytes """

    used = fields.Nested("netapp_ontap.models.quota_report_space_used.QuotaReportSpaceUsedSchema", unknown=EXCLUDE, data_key="used")
    r""" The used field of the quota_report_space. """

    @property
    def resource(self):
        return QuotaReportSpace

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


class QuotaReportSpace(Resource):  # pylint: disable=missing-docstring

    _schema = QuotaReportSpaceSchema
