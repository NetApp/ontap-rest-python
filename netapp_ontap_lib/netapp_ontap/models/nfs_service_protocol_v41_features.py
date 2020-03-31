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


__all__ = ["NfsServiceProtocolV41Features", "NfsServiceProtocolV41FeaturesSchema"]
__pdoc__ = {
    "NfsServiceProtocolV41FeaturesSchema.resource": False,
    "NfsServiceProtocolV41Features": False,
}


class NfsServiceProtocolV41FeaturesSchema(ResourceSchema):
    """The fields of the NfsServiceProtocolV41Features object"""

    acl_enabled = fields.Boolean(data_key="acl_enabled")
    r""" Specifies whether NFSv4.1 ACLs is enabled. """

    pnfs_enabled = fields.Boolean(data_key="pnfs_enabled")
    r""" Specifies whether NFSv4.1 Parallel NFS is enabled. """

    read_delegation_enabled = fields.Boolean(data_key="read_delegation_enabled")
    r""" Specifies whether NFSv4.1 Read Delegation is enabled. """

    write_delegation_enabled = fields.Boolean(data_key="write_delegation_enabled")
    r""" Specifies whether NFSv4.1 Write Delegation is enabled. """

    @property
    def resource(self):
        return NfsServiceProtocolV41Features

    @property
    def patchable_fields(self):
        return [
            "acl_enabled",
            "pnfs_enabled",
            "read_delegation_enabled",
            "write_delegation_enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "acl_enabled",
            "pnfs_enabled",
            "read_delegation_enabled",
            "write_delegation_enabled",
        ]


class NfsServiceProtocolV41Features(Resource):  # pylint: disable=missing-docstring

    _schema = NfsServiceProtocolV41FeaturesSchema
