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


__all__ = ["SpaceEfficiency", "SpaceEfficiencySchema"]
__pdoc__ = {
    "SpaceEfficiencySchema.resource": False,
    "SpaceEfficiency": False,
}


class SpaceEfficiencySchema(ResourceSchema):
    """The fields of the SpaceEfficiency object"""

    logical_used = fields.Integer(data_key="logical_used")
    r""" Logical used """

    ratio = fields.Number(data_key="ratio")
    r""" Data reduction ratio (logical_used / used) """

    savings = fields.Integer(data_key="savings")
    r""" Space saved by storage efficiencies (logical_used - used) """

    @property
    def resource(self):
        return SpaceEfficiency

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class SpaceEfficiency(Resource):  # pylint: disable=missing-docstring

    _schema = SpaceEfficiencySchema
