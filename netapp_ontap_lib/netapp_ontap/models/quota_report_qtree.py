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


__all__ = ["QuotaReportQtree", "QuotaReportQtreeSchema"]
__pdoc__ = {
    "QuotaReportQtreeSchema.resource": False,
    "QuotaReportQtree": False,
}


class QuotaReportQtreeSchema(ResourceSchema):
    """The fields of the QuotaReportQtree object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the quota_report_qtree. """

    id = fields.Integer(data_key="id")
    r""" The unique identifier for a qtree.

Example: 1 """

    name = fields.Str(data_key="name")
    r""" The name of the qtree.

Example: qt1 """

    @property
    def resource(self):
        return QuotaReportQtree

    @property
    def patchable_fields(self):
        return [
            "id",
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "id",
            "name",
        ]


class QuotaReportQtree(Resource):  # pylint: disable=missing-docstring

    _schema = QuotaReportQtreeSchema
