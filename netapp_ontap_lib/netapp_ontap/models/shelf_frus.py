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


__all__ = ["ShelfFrus", "ShelfFrusSchema"]
__pdoc__ = {
    "ShelfFrusSchema.resource": False,
    "ShelfFrus": False,
}


class ShelfFrusSchema(ResourceSchema):
    """The fields of the ShelfFrus object"""

    firmware_version = fields.Str(data_key="firmware_version")
    r""" The firmware_version field of the shelf_frus.

Example: 191.0 """

    id = fields.Integer(data_key="id")
    r""" The id field of the shelf_frus. """

    part_number = fields.Str(data_key="part_number")
    r""" The part_number field of the shelf_frus.

Example: 111-00690+A2 """

    serial_number = fields.Str(data_key="serial_number")
    r""" The serial_number field of the shelf_frus.

Example: 8000166294 """

    state = fields.Str(data_key="state")
    r""" The state field of the shelf_frus.

Valid choices:

* ok
* error """

    type = fields.Str(data_key="type")
    r""" The type field of the shelf_frus.

Valid choices:

* module
* psu """

    @property
    def resource(self):
        return ShelfFrus

    @property
    def patchable_fields(self):
        return [
            "firmware_version",
            "id",
            "part_number",
            "serial_number",
            "state",
            "type",
        ]

    @property
    def postable_fields(self):
        return [
            "firmware_version",
            "id",
            "part_number",
            "serial_number",
            "state",
            "type",
        ]


class ShelfFrus(Resource):  # pylint: disable=missing-docstring

    _schema = ShelfFrusSchema
