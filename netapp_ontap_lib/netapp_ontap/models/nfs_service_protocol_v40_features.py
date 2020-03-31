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


__all__ = ["NfsServiceProtocolV40Features", "NfsServiceProtocolV40FeaturesSchema"]
__pdoc__ = {
    "NfsServiceProtocolV40FeaturesSchema.resource": False,
    "NfsServiceProtocolV40Features": False,
}


class NfsServiceProtocolV40FeaturesSchema(ResourceSchema):
    """The fields of the NfsServiceProtocolV40Features object"""

    acl_enabled = fields.Boolean(data_key="acl_enabled")
    r""" Specifies whether NFSv4.0 ACLs is enabled. """

    read_delegation_enabled = fields.Boolean(data_key="read_delegation_enabled")
    r""" Specifies whether NFSv4.0 Read Delegation is enabled. """

    write_delegation_enabled = fields.Boolean(data_key="write_delegation_enabled")
    r""" Specifies whether NFSv4.0 Write Delegation is enabled. """

    @property
    def resource(self):
        return NfsServiceProtocolV40Features

    @property
    def patchable_fields(self):
        return [
            "acl_enabled",
            "read_delegation_enabled",
            "write_delegation_enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "acl_enabled",
            "read_delegation_enabled",
            "write_delegation_enabled",
        ]


class NfsServiceProtocolV40Features(Resource):  # pylint: disable=missing-docstring

    _schema = NfsServiceProtocolV40FeaturesSchema
