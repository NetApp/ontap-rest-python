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


__all__ = ["VolumeEfficiencyPolicy", "VolumeEfficiencyPolicySchema"]
__pdoc__ = {
    "VolumeEfficiencyPolicySchema.resource": False,
    "VolumeEfficiencyPolicy": False,
}


class VolumeEfficiencyPolicySchema(ResourceSchema):
    """The fields of the VolumeEfficiencyPolicy object"""

    name = fields.Str(data_key="name")
    r""" Specifies the name of the efficiency policy. """

    @property
    def resource(self):
        return VolumeEfficiencyPolicy

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class VolumeEfficiencyPolicy(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeEfficiencyPolicySchema
