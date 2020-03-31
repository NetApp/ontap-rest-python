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


__all__ = ["OnboardKeyManagerConfigurableStatus", "OnboardKeyManagerConfigurableStatusSchema"]
__pdoc__ = {
    "OnboardKeyManagerConfigurableStatusSchema.resource": False,
    "OnboardKeyManagerConfigurableStatus": False,
}


class OnboardKeyManagerConfigurableStatusSchema(ResourceSchema):
    """The fields of the OnboardKeyManagerConfigurableStatus object"""

    code = fields.Integer(data_key="code")
    r""" Code corresponding to the status message. Returns a 0 if the Onboard Key Manager can be configured in the cluster.

Example: 65537300 """

    message = fields.Str(data_key="message")
    r""" Reason that Onboard Key Manager cannot be configured in the cluster.

Example: No platform support for volume encryption in following nodes - node1, node2. """

    supported = fields.Boolean(data_key="supported")
    r""" Set to true if the Onboard Key Manager can be configured in the cluster. """

    @property
    def resource(self):
        return OnboardKeyManagerConfigurableStatus

    @property
    def patchable_fields(self):
        return [
            "code",
            "message",
            "supported",
        ]

    @property
    def postable_fields(self):
        return [
            "code",
            "message",
            "supported",
        ]


class OnboardKeyManagerConfigurableStatus(Resource):  # pylint: disable=missing-docstring

    _schema = OnboardKeyManagerConfigurableStatusSchema
