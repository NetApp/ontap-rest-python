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


__all__ = ["RaidGroupReconstruct", "RaidGroupReconstructSchema"]
__pdoc__ = {
    "RaidGroupReconstructSchema.resource": False,
    "RaidGroupReconstruct": False,
}


class RaidGroupReconstructSchema(ResourceSchema):
    """The fields of the RaidGroupReconstruct object"""

    active = fields.Boolean(data_key="active")
    r""" One or more disks in this RAID group are being reconstructed. """

    percent = fields.Integer(data_key="percent")
    r""" Reconstruct percentage

Example: 10 """

    @property
    def resource(self):
        return RaidGroupReconstruct

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class RaidGroupReconstruct(Resource):  # pylint: disable=missing-docstring

    _schema = RaidGroupReconstructSchema
