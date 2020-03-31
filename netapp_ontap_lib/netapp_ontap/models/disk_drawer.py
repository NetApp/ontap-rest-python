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


__all__ = ["DiskDrawer", "DiskDrawerSchema"]
__pdoc__ = {
    "DiskDrawerSchema.resource": False,
    "DiskDrawer": False,
}


class DiskDrawerSchema(ResourceSchema):
    """The fields of the DiskDrawer object"""

    id = fields.Integer(data_key="id")
    r""" The id field of the disk_drawer. """

    slot = fields.Integer(data_key="slot")
    r""" The slot field of the disk_drawer. """

    @property
    def resource(self):
        return DiskDrawer

    @property
    def patchable_fields(self):
        return [
            "id",
            "slot",
        ]

    @property
    def postable_fields(self):
        return [
            "id",
            "slot",
        ]


class DiskDrawer(Resource):  # pylint: disable=missing-docstring

    _schema = DiskDrawerSchema
