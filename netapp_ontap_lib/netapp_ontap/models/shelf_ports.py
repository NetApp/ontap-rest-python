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


__all__ = ["ShelfPorts", "ShelfPortsSchema"]
__pdoc__ = {
    "ShelfPortsSchema.resource": False,
    "ShelfPorts": False,
}


class ShelfPortsSchema(ResourceSchema):
    """The fields of the ShelfPorts object"""

    cable = fields.Nested("netapp_ontap.models.shelf_cable.ShelfCableSchema", unknown=EXCLUDE, data_key="cable")
    r""" The cable field of the shelf_ports. """

    designator = fields.Str(data_key="designator")
    r""" The designator field of the shelf_ports.

Valid choices:

* circle
* square
* 1
* 2
* 3
* 4 """

    id = fields.Integer(data_key="id")
    r""" The id field of the shelf_ports.

Example: 0 """

    internal = fields.Boolean(data_key="internal")
    r""" The internal field of the shelf_ports. """

    mac_address = fields.Str(data_key="mac_address")
    r""" The mac_address field of the shelf_ports. """

    module_id = fields.Str(data_key="module_id")
    r""" The module_id field of the shelf_ports.

Valid choices:

* a
* b """

    remote = fields.Nested("netapp_ontap.models.shelf_remote.ShelfRemoteSchema", unknown=EXCLUDE, data_key="remote")
    r""" The remote field of the shelf_ports. """

    state = fields.Str(data_key="state")
    r""" The state field of the shelf_ports.

Valid choices:

* connected
* disconnected
* error """

    wwn = fields.Str(data_key="wwn")
    r""" The wwn field of the shelf_ports.

Example: 500A0980000B6C3F """

    @property
    def resource(self):
        return ShelfPorts

    @property
    def patchable_fields(self):
        return [
            "cable",
            "designator",
            "id",
            "internal",
            "mac_address",
            "module_id",
            "remote",
            "state",
            "wwn",
        ]

    @property
    def postable_fields(self):
        return [
            "cable",
            "designator",
            "id",
            "internal",
            "mac_address",
            "module_id",
            "remote",
            "state",
            "wwn",
        ]


class ShelfPorts(Resource):  # pylint: disable=missing-docstring

    _schema = ShelfPortsSchema
