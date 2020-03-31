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


__all__ = ["VolumeConsistencyGroup", "VolumeConsistencyGroupSchema"]
__pdoc__ = {
    "VolumeConsistencyGroupSchema.resource": False,
    "VolumeConsistencyGroup": False,
}


class VolumeConsistencyGroupSchema(ResourceSchema):
    """The fields of the VolumeConsistencyGroup object"""

    name = fields.Str(data_key="name")
    r""" Name of the consistency group.

Example: consistency_group_1 """

    @property
    def resource(self):
        return VolumeConsistencyGroup

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


class VolumeConsistencyGroup(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeConsistencyGroupSchema
