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


__all__ = ["ShelfCable", "ShelfCableSchema"]
__pdoc__ = {
    "ShelfCableSchema.resource": False,
    "ShelfCable": False,
}


class ShelfCableSchema(ResourceSchema):
    """The fields of the ShelfCable object"""

    identifier = fields.Str(data_key="identifier")
    r""" The identifier field of the shelf_cable.

Example: 500a0980000b6c3f-50000d1703544b80 """

    length = fields.Str(data_key="length")
    r""" The length field of the shelf_cable.

Example: 2m """

    part_number = fields.Str(data_key="part_number")
    r""" The part_number field of the shelf_cable.

Example: 112-00431+A0 """

    serial_number = fields.Str(data_key="serial_number")
    r""" The serial_number field of the shelf_cable.

Example: 616930439 """

    @property
    def resource(self):
        return ShelfCable

    @property
    def patchable_fields(self):
        return [
            "identifier",
            "length",
            "part_number",
            "serial_number",
        ]

    @property
    def postable_fields(self):
        return [
            "identifier",
            "length",
            "part_number",
            "serial_number",
        ]


class ShelfCable(Resource):  # pylint: disable=missing-docstring

    _schema = ShelfCableSchema
