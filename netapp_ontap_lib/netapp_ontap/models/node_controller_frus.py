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


__all__ = ["NodeControllerFrus", "NodeControllerFrusSchema"]
__pdoc__ = {
    "NodeControllerFrusSchema.resource": False,
    "NodeControllerFrus": False,
}


class NodeControllerFrusSchema(ResourceSchema):
    """The fields of the NodeControllerFrus object"""

    id = fields.Integer(data_key="id")
    r""" The id field of the node_controller_frus. """

    state = fields.Str(data_key="state")
    r""" The state field of the node_controller_frus.

Valid choices:

* ok
* error """

    type = fields.Str(data_key="type")
    r""" The type field of the node_controller_frus.

Valid choices:

* fan
* psu
* pcie
* disk
* nvs
* dimm
* controller """

    @property
    def resource(self):
        return NodeControllerFrus

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class NodeControllerFrus(Resource):  # pylint: disable=missing-docstring

    _schema = NodeControllerFrusSchema
