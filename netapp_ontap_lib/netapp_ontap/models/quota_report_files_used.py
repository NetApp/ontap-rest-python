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


__all__ = ["QuotaReportFilesUsed", "QuotaReportFilesUsedSchema"]
__pdoc__ = {
    "QuotaReportFilesUsedSchema.resource": False,
    "QuotaReportFilesUsed": False,
}


class QuotaReportFilesUsedSchema(ResourceSchema):
    """The fields of the QuotaReportFilesUsed object"""

    hard_limit_percent = fields.Integer(data_key="hard_limit_percent")
    r""" Total files used as a percentage of file hard limit """

    soft_limit_percent = fields.Integer(data_key="soft_limit_percent")
    r""" Total files used as a percentage of file soft limit """

    total = fields.Integer(data_key="total")
    r""" Total files used """

    @property
    def resource(self):
        return QuotaReportFilesUsed

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class QuotaReportFilesUsed(Resource):  # pylint: disable=missing-docstring

    _schema = QuotaReportFilesUsedSchema
