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


__all__ = ["IscsiCredentialsChapOutbound", "IscsiCredentialsChapOutboundSchema"]
__pdoc__ = {
    "IscsiCredentialsChapOutboundSchema.resource": False,
    "IscsiCredentialsChapOutbound": False,
}


class IscsiCredentialsChapOutboundSchema(ResourceSchema):
    """The fields of the IscsiCredentialsChapOutbound object"""

    password = fields.Str(data_key="password")
    r""" The outbound CHAP password. Write-only; optional in POST and PATCH. """

    user = fields.Str(data_key="user")
    r""" The outbound CHAP user name. Optional in POST and PATCH. """

    @property
    def resource(self):
        return IscsiCredentialsChapOutbound

    @property
    def patchable_fields(self):
        return [
            "password",
            "user",
        ]

    @property
    def postable_fields(self):
        return [
            "password",
            "user",
        ]


class IscsiCredentialsChapOutbound(Resource):  # pylint: disable=missing-docstring

    _schema = IscsiCredentialsChapOutboundSchema
