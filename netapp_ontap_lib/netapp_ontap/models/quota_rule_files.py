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


__all__ = ["QuotaRuleFiles", "QuotaRuleFilesSchema"]
__pdoc__ = {
    "QuotaRuleFilesSchema.resource": False,
    "QuotaRuleFiles": False,
}


class QuotaRuleFilesSchema(ResourceSchema):
    """The fields of the QuotaRuleFiles object"""

    hard_limit = fields.Integer(data_key="hard_limit")
    r""" This parameter specifies the hard limit for files. This is valid in POST or PATCH. """

    soft_limit = fields.Integer(data_key="soft_limit")
    r""" This parameter specifies the soft limit for files. This is valid in POST or PATCH. """

    @property
    def resource(self):
        return QuotaRuleFiles

    @property
    def patchable_fields(self):
        return [
            "hard_limit",
            "soft_limit",
        ]

    @property
    def postable_fields(self):
        return [
            "hard_limit",
            "soft_limit",
        ]


class QuotaRuleFiles(Resource):  # pylint: disable=missing-docstring

    _schema = QuotaRuleFilesSchema
