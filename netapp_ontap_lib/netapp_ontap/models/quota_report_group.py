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


__all__ = ["QuotaReportGroup", "QuotaReportGroupSchema"]
__pdoc__ = {
    "QuotaReportGroupSchema.resource": False,
    "QuotaReportGroup": False,
}


class QuotaReportGroupSchema(ResourceSchema):
    """The fields of the QuotaReportGroup object"""

    id = fields.Str(data_key="id")
    r""" Quota target group ID """

    name = fields.Str(data_key="name")
    r""" Quota target group name """

    @property
    def resource(self):
        return QuotaReportGroup

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class QuotaReportGroup(Resource):  # pylint: disable=missing-docstring

    _schema = QuotaReportGroupSchema
