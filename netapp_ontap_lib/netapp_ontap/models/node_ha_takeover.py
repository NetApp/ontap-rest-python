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


__all__ = ["NodeHaTakeover", "NodeHaTakeoverSchema"]
__pdoc__ = {
    "NodeHaTakeoverSchema.resource": False,
    "NodeHaTakeover": False,
}


class NodeHaTakeoverSchema(ResourceSchema):
    """The fields of the NodeHaTakeover object"""

    failure = fields.Nested("netapp_ontap.models.node_ha_takeover_failure.NodeHaTakeoverFailureSchema", unknown=EXCLUDE, data_key="failure")
    r""" The failure field of the node_ha_takeover. """

    state = fields.Str(data_key="state")
    r""" The state field of the node_ha_takeover.

Valid choices:

* not_possible
* not_attempted
* in_takeover
* in_progress
* failed """

    @property
    def resource(self):
        return NodeHaTakeover

    @property
    def patchable_fields(self):
        return [
            "failure",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "failure",
            "state",
        ]


class NodeHaTakeover(Resource):  # pylint: disable=missing-docstring

    _schema = NodeHaTakeoverSchema
