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


__all__ = ["AutosupportIssues", "AutosupportIssuesSchema"]
__pdoc__ = {
    "AutosupportIssuesSchema.resource": False,
    "AutosupportIssues": False,
}


class AutosupportIssuesSchema(ResourceSchema):
    """The fields of the AutosupportIssues object"""

    corrective_action = fields.Nested("netapp_ontap.models.autosupport_connectivity_corrective_action.AutosupportConnectivityCorrectiveActionSchema", unknown=EXCLUDE, data_key="corrective_action")
    r""" The corrective_action field of the autosupport_issues. """

    issue = fields.Nested("netapp_ontap.models.autosupport_connectivity_issue.AutosupportConnectivityIssueSchema", unknown=EXCLUDE, data_key="issue")
    r""" The issue field of the autosupport_issues. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, data_key="node")
    r""" The node field of the autosupport_issues. """

    @property
    def resource(self):
        return AutosupportIssues

    @property
    def patchable_fields(self):
        return [
            "corrective_action",
            "issue",
            "node.name",
            "node.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "corrective_action",
            "issue",
            "node.name",
            "node.uuid",
        ]


class AutosupportIssues(Resource):  # pylint: disable=missing-docstring

    _schema = AutosupportIssuesSchema
