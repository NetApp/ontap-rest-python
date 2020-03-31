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


__all__ = ["VolumeErrorState", "VolumeErrorStateSchema"]
__pdoc__ = {
    "VolumeErrorStateSchema.resource": False,
    "VolumeErrorState": False,
}


class VolumeErrorStateSchema(ResourceSchema):
    """The fields of the VolumeErrorState object"""

    has_bad_blocks = fields.Boolean(data_key="has_bad_blocks")
    r""" Indicates whether the volume has any corrupt data blocks. If the damaged data block is accessed, an IO error, such as EIO for NFS or STATUS_FILE_CORRUPT for CIFS, is returned. """

    is_inconsistent = fields.Boolean(data_key="is_inconsistent")
    r""" Indicates whether the file system has any inconsistencies.<br>true &dash; File system is inconsistent.<br>false &dash; File system in not inconsistent. """

    @property
    def resource(self):
        return VolumeErrorState

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class VolumeErrorState(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeErrorStateSchema
