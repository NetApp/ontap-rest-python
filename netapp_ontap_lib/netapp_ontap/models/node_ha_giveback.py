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


__all__ = ["NodeHaGiveback", "NodeHaGivebackSchema"]
__pdoc__ = {
    "NodeHaGivebackSchema.resource": False,
    "NodeHaGiveback": False,
}


class NodeHaGivebackSchema(ResourceSchema):
    """The fields of the NodeHaGiveback object"""

    failure = fields.Nested("netapp_ontap.models.node_ha_giveback_failure.NodeHaGivebackFailureSchema", unknown=EXCLUDE, data_key="failure")
    r""" The failure field of the node_ha_giveback. """

    state = fields.Str(data_key="state")
    r""" The state field of the node_ha_giveback.

Valid choices:

* nothing_to_giveback
* not_attempted
* in_progress
* failed """

    @property
    def resource(self):
        return NodeHaGiveback

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


class NodeHaGiveback(Resource):  # pylint: disable=missing-docstring

    _schema = NodeHaGivebackSchema
