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


__all__ = ["VolumeSnapmirror", "VolumeSnapmirrorSchema"]
__pdoc__ = {
    "VolumeSnapmirrorSchema.resource": False,
    "VolumeSnapmirror": False,
}


class VolumeSnapmirrorSchema(ResourceSchema):
    """The fields of the VolumeSnapmirror object"""

    is_protected = fields.Boolean(data_key="is_protected")
    r""" Specifies whether a volume is a SnapMirror source volume, using SnapMirror to protect its data. """

    @property
    def resource(self):
        return VolumeSnapmirror

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class VolumeSnapmirror(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeSnapmirrorSchema
