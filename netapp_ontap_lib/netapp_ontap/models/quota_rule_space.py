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


__all__ = ["QuotaRuleSpace", "QuotaRuleSpaceSchema"]
__pdoc__ = {
    "QuotaRuleSpaceSchema.resource": False,
    "QuotaRuleSpace": False,
}


class QuotaRuleSpaceSchema(ResourceSchema):
    """The fields of the QuotaRuleSpace object"""

    hard_limit = fields.Integer(data_key="hard_limit")
    r""" This parameter specifies the space hard limit, in bytes. If less than 1024 bytes, the value is rounded up to 1024 bytes. Valid in POST or PATCH. For a POST operation where the parameter is either empty or set to -1, no limit is applied. For a PATCH operation where a limit is configured, use a value of -1 to clear the limit. """

    soft_limit = fields.Integer(data_key="soft_limit")
    r""" This parameter specifies the space soft limit, in bytes. If less than 1024 bytes, the value is rounded up to 1024 bytes. Valid in POST or PATCH. For a POST operation where the parameter is either empty or set to -1, no limit is applied. For a PATCH operation where a limit is configured, use a value of -1 to clear the limit. """

    @property
    def resource(self):
        return QuotaRuleSpace

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


class QuotaRuleSpace(Resource):  # pylint: disable=missing-docstring

    _schema = QuotaRuleSpaceSchema
