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


__all__ = ["SoftwareStatusDetails", "SoftwareStatusDetailsSchema"]
__pdoc__ = {
    "SoftwareStatusDetailsSchema.resource": False,
    "SoftwareStatusDetails": False,
}


class SoftwareStatusDetailsSchema(ResourceSchema):
    """The fields of the SoftwareStatusDetails object"""

    action = fields.Nested("netapp_ontap.models.software_status_details_reference_action.SoftwareStatusDetailsReferenceActionSchema", unknown=EXCLUDE, data_key="action")
    r""" The action field of the software_status_details. """

    end_time = fields.DateTime(data_key="end_time")
    r""" End time for each status phase.

Example: 2019-02-02T19:00:00.000+0000 """

    issue = fields.Nested("netapp_ontap.models.software_status_details_reference_issue.SoftwareStatusDetailsReferenceIssueSchema", unknown=EXCLUDE, data_key="issue")
    r""" The issue field of the software_status_details. """

    name = fields.Str(data_key="name")
    r""" Name of the phase to be retrieved for status details.

Example: initialize """

    node = fields.Nested("netapp_ontap.models.software_status_details_reference_node.SoftwareStatusDetailsReferenceNodeSchema", unknown=EXCLUDE, data_key="node")
    r""" The node field of the software_status_details. """

    start_time = fields.DateTime(data_key="start_time")
    r""" Start time for each status phase.

Example: 2019-02-02T19:00:00.000+0000 """

    state = fields.Str(data_key="state")
    r""" Status of the phase

Valid choices:

* in_progress
* waiting
* paused_by_user
* paused_on_error
* completed
* canceled
* failed
* pause_pending
* cancel_pending """

    @property
    def resource(self):
        return SoftwareStatusDetails

    @property
    def patchable_fields(self):
        return [
            "action",
            "issue",
            "node",
        ]

    @property
    def postable_fields(self):
        return [
            "action",
            "issue",
            "node",
        ]


class SoftwareStatusDetails(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareStatusDetailsSchema
