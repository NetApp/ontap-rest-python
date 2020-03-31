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


__all__ = ["AutosupportConnectivityCorrectiveAction", "AutosupportConnectivityCorrectiveActionSchema"]
__pdoc__ = {
    "AutosupportConnectivityCorrectiveActionSchema.resource": False,
    "AutosupportConnectivityCorrectiveAction": False,
}


class AutosupportConnectivityCorrectiveActionSchema(ResourceSchema):
    """The fields of the AutosupportConnectivityCorrectiveAction object"""

    code = fields.Str(data_key="code")
    r""" Corrective action code

Example: 53149746 """

    message = fields.Str(data_key="message")
    r""" Corrective action message. The corrective action might contain commands which needs to be executed on the ONTAP CLI.

Example: Check the hostname of the SMTP server """

    @property
    def resource(self):
        return AutosupportConnectivityCorrectiveAction

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class AutosupportConnectivityCorrectiveAction(Resource):  # pylint: disable=missing-docstring

    _schema = AutosupportConnectivityCorrectiveActionSchema
