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


__all__ = ["AutosupportConnectivityIssue", "AutosupportConnectivityIssueSchema"]
__pdoc__ = {
    "AutosupportConnectivityIssueSchema.resource": False,
    "AutosupportConnectivityIssue": False,
}


class AutosupportConnectivityIssueSchema(ResourceSchema):
    """The fields of the AutosupportConnectivityIssue object"""

    code = fields.Str(data_key="code")
    r""" Error code

Example: 53149746 """

    message = fields.Str(data_key="message")
    r""" Error message

Example: SMTP connectivity check failed for destination: mailhost. Error: Could not resolve host - 'mailhost' """

    @property
    def resource(self):
        return AutosupportConnectivityIssue

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class AutosupportConnectivityIssue(Resource):  # pylint: disable=missing-docstring

    _schema = AutosupportConnectivityIssueSchema
