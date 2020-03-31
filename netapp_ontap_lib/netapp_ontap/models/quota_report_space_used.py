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


__all__ = ["QuotaReportSpaceUsed", "QuotaReportSpaceUsedSchema"]
__pdoc__ = {
    "QuotaReportSpaceUsedSchema.resource": False,
    "QuotaReportSpaceUsed": False,
}


class QuotaReportSpaceUsedSchema(ResourceSchema):
    """The fields of the QuotaReportSpaceUsed object"""

    hard_limit_percent = fields.Integer(data_key="hard_limit_percent")
    r""" Total space used as a percentage of space hard limit """

    soft_limit_percent = fields.Integer(data_key="soft_limit_percent")
    r""" Total space used as a percentage of space soft limit """

    total = fields.Integer(data_key="total")
    r""" Total space used """

    @property
    def resource(self):
        return QuotaReportSpaceUsed

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class QuotaReportSpaceUsed(Resource):  # pylint: disable=missing-docstring

    _schema = QuotaReportSpaceUsedSchema
