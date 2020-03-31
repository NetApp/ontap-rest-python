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


__all__ = ["EmsFilterRuleMessageCriteria", "EmsFilterRuleMessageCriteriaSchema"]
__pdoc__ = {
    "EmsFilterRuleMessageCriteriaSchema.resource": False,
    "EmsFilterRuleMessageCriteria": False,
}


class EmsFilterRuleMessageCriteriaSchema(ResourceSchema):
    """The fields of the EmsFilterRuleMessageCriteria object"""

    links = fields.Nested("netapp_ontap.models.related_link.RelatedLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the ems_filter_rule_message_criteria. """

    name_pattern = fields.Str(data_key="name_pattern")
    r""" Message name filter on which to match. Supports wildcards. Defaults to * if not specified.

Example: callhome.* """

    severities = fields.Str(data_key="severities")
    r""" A comma-separated list of severities or a wildcard.

Example: error,informational """

    snmp_trap_types = fields.Str(data_key="snmp_trap_types")
    r""" A comma separated list of snmp_trap_types or a wildcard.

Example: standard|built_in """

    @property
    def resource(self):
        return EmsFilterRuleMessageCriteria

    @property
    def patchable_fields(self):
        return [
            "name_pattern",
            "severities",
            "snmp_trap_types",
        ]

    @property
    def postable_fields(self):
        return [
            "name_pattern",
            "severities",
            "snmp_trap_types",
        ]


class EmsFilterRuleMessageCriteria(Resource):  # pylint: disable=missing-docstring

    _schema = EmsFilterRuleMessageCriteriaSchema
