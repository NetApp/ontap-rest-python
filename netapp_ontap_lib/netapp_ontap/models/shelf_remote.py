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


__all__ = ["ShelfRemote", "ShelfRemoteSchema"]
__pdoc__ = {
    "ShelfRemoteSchema.resource": False,
    "ShelfRemote": False,
}


class ShelfRemoteSchema(ResourceSchema):
    """The fields of the ShelfRemote object"""

    chassis = fields.Str(data_key="chassis")
    r""" The chassis field of the shelf_remote. """

    mac_address = fields.Str(data_key="mac_address")
    r""" The mac_address field of the shelf_remote. """

    phy = fields.Str(data_key="phy")
    r""" The phy field of the shelf_remote.

Example: 12 """

    port = fields.Str(data_key="port")
    r""" The port field of the shelf_remote. """

    wwn = fields.Str(data_key="wwn")
    r""" The wwn field of the shelf_remote.

Example: 50000D1703544B80 """

    @property
    def resource(self):
        return ShelfRemote

    @property
    def patchable_fields(self):
        return [
            "chassis",
            "mac_address",
            "phy",
            "port",
            "wwn",
        ]

    @property
    def postable_fields(self):
        return [
            "chassis",
            "mac_address",
            "phy",
            "port",
            "wwn",
        ]


class ShelfRemote(Resource):  # pylint: disable=missing-docstring

    _schema = ShelfRemoteSchema
