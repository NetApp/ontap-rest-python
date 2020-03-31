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


__all__ = ["NodeHaPorts", "NodeHaPortsSchema"]
__pdoc__ = {
    "NodeHaPortsSchema.resource": False,
    "NodeHaPorts": False,
}


class NodeHaPortsSchema(ResourceSchema):
    """The fields of the NodeHaPorts object"""

    state = fields.Str(data_key="state")
    r""" HA port state:

* <i>down</i> - Logical HA link is down.
* <i>initialized</i> - Logical HA link is initialized. The physical link is up, but the subnet manager hasn’t started to configure the port.
* <i>armed</i> - Logical HA link is armed. The physical link is up and the subnet manager started but did not yet complete configuring the port.
* <i>active</i> - Logical HA link is active.
* <i>reserved</i> - Logical HA link is active, but the physical link is down.


Valid choices:

* down
* initialized
* armed
* active
* reserved """

    @property
    def resource(self):
        return NodeHaPorts

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class NodeHaPorts(Resource):  # pylint: disable=missing-docstring

    _schema = NodeHaPortsSchema
