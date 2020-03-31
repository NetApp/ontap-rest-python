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


__all__ = ["VolumeAutosize", "VolumeAutosizeSchema"]
__pdoc__ = {
    "VolumeAutosizeSchema.resource": False,
    "VolumeAutosize": False,
}


class VolumeAutosizeSchema(ResourceSchema):
    """The fields of the VolumeAutosize object"""

    grow_threshold = fields.Integer(data_key="grow_threshold")
    r""" Used space threshold size, in percentage, for the automatic growth of the volume. When the amount of used space in the volume becomes greater than this threhold, the volume automatically grows unless it has reached the maximum size. The volume grows when 'space.used' is greater than this percent of 'space.size'. The 'grow_threshold' size cannot be less than or equal to the 'shrink_threshold' size.. """

    maximum = fields.Integer(data_key="maximum")
    r""" Maximum size in bytes up to which a volume grows automatically. This size cannot be less than the current volume size, or less than or equal to the minimum size of volume. """

    minimum = fields.Integer(data_key="minimum")
    r""" Minimum size in bytes up to which the volume shrinks automatically. This size cannot be greater than or equal to the maximum size of volume. """

    mode = fields.Str(data_key="mode")
    r""" Autosize mode for the volume.<br>grow &dash; Volume automatically grows when the amount of used space is above the 'grow_threshold' value.<br>grow_shrink &dash; Volume grows or shrinks in response to the amount of space used.<br>off &dash; Autosizing of the volume is disabled.

Valid choices:

* grow
* grow_shrink
* off """

    shrink_threshold = fields.Integer(data_key="shrink_threshold")
    r""" Used space threshold size, in percentage, for the automatic shrinkage of the volume.  When the amount of used space in the volume drops below this threshold, the volume automatically shrinks unless it has reached the minimum size. The volume shrinks when the 'space.used' is less than the 'shrink_threshold' percent of 'space.size'. The 'shrink_threshold' size cannot be greater than or equal to the 'grow_threshold' size. """

    @property
    def resource(self):
        return VolumeAutosize

    @property
    def patchable_fields(self):
        return [
            "grow_threshold",
            "maximum",
            "minimum",
            "mode",
            "shrink_threshold",
        ]

    @property
    def postable_fields(self):
        return [
            "grow_threshold",
            "maximum",
            "minimum",
            "mode",
            "shrink_threshold",
        ]


class VolumeAutosize(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeAutosizeSchema
