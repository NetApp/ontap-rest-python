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


__all__ = ["VolumeFiles", "VolumeFilesSchema"]
__pdoc__ = {
    "VolumeFilesSchema.resource": False,
    "VolumeFiles": False,
}


class VolumeFilesSchema(ResourceSchema):
    """The fields of the VolumeFiles object"""

    maximum = fields.Integer(data_key="maximum")
    r""" The maximum number of files (inodes) for user-visible data allowed on the volume. This value can be increased or decreased. Increasing the maximum number of files does not immediately cause additional disk space to be used to track files. Instead, as more files are created on the volume, the system dynamically increases the number of disk blocks that are used to track files. The space assigned to track files is never freed, and this value cannot be decreased below the current number of files that can be tracked within the assigned space for the volume. Valid in PATCH. """

    used = fields.Integer(data_key="used")
    r""" Number of files (inodes) used for user-visible data permitted on the volume. This field is valid only when the volume is online. """

    @property
    def resource(self):
        return VolumeFiles

    @property
    def patchable_fields(self):
        return [
            "maximum",
        ]

    @property
    def postable_fields(self):
        return [
            "maximum",
        ]


class VolumeFiles(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeFilesSchema
