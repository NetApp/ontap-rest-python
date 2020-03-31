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


__all__ = ["RaidGroupRecomputingParity", "RaidGroupRecomputingParitySchema"]
__pdoc__ = {
    "RaidGroupRecomputingParitySchema.resource": False,
    "RaidGroupRecomputingParity": False,
}


class RaidGroupRecomputingParitySchema(ResourceSchema):
    """The fields of the RaidGroupRecomputingParity object"""

    active = fields.Boolean(data_key="active")
    r""" RAID group is recomputing parity """

    percent = fields.Integer(data_key="percent")
    r""" Recomputing parity percentage

Example: 10 """

    @property
    def resource(self):
        return RaidGroupRecomputingParity

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class RaidGroupRecomputingParity(Resource):  # pylint: disable=missing-docstring

    _schema = RaidGroupRecomputingParitySchema
