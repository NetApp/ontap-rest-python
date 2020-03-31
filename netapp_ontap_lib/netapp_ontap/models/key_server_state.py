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


__all__ = ["KeyServerState", "KeyServerStateSchema"]
__pdoc__ = {
    "KeyServerStateSchema.resource": False,
    "KeyServerState": False,
}


class KeyServerStateSchema(ResourceSchema):
    """The fields of the KeyServerState object"""

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, data_key="node")
    r""" The node field of the key_server_state. """

    state = fields.Str(data_key="state")
    r""" Key server connectivity state

Valid choices:

* not_responding
* unknown """

    @property
    def resource(self):
        return KeyServerState

    @property
    def patchable_fields(self):
        return [
            "node.name",
            "node.uuid",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "node.name",
            "node.uuid",
            "state",
        ]


class KeyServerState(Resource):  # pylint: disable=missing-docstring

    _schema = KeyServerStateSchema
