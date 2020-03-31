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


__all__ = ["ShelfDrawers", "ShelfDrawersSchema"]
__pdoc__ = {
    "ShelfDrawersSchema.resource": False,
    "ShelfDrawers": False,
}


class ShelfDrawersSchema(ResourceSchema):
    """The fields of the ShelfDrawers object"""

    closed = fields.Boolean(data_key="closed")
    r""" The closed field of the shelf_drawers. """

    disk_count = fields.Integer(data_key="disk_count")
    r""" The disk_count field of the shelf_drawers.

Example: 12 """

    error = fields.Str(data_key="error")
    r""" The error field of the shelf_drawers. """

    id = fields.Integer(data_key="id")
    r""" The id field of the shelf_drawers. """

    part_number = fields.Str(data_key="part_number")
    r""" The part_number field of the shelf_drawers.

Example: 111-03071 """

    serial_number = fields.Str(data_key="serial_number")
    r""" The serial_number field of the shelf_drawers.

Example: 2.1604008263E10 """

    state = fields.Str(data_key="state")
    r""" The state field of the shelf_drawers.

Valid choices:

* ok
* error """

    @property
    def resource(self):
        return ShelfDrawers

    @property
    def patchable_fields(self):
        return [
            "closed",
            "disk_count",
            "error",
            "id",
            "part_number",
            "serial_number",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "closed",
            "disk_count",
            "error",
            "id",
            "part_number",
            "serial_number",
            "state",
        ]


class ShelfDrawers(Resource):  # pylint: disable=missing-docstring

    _schema = ShelfDrawersSchema
