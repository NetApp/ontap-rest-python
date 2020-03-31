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


__all__ = ["SnapmirrorTransferFiles", "SnapmirrorTransferFilesSchema"]
__pdoc__ = {
    "SnapmirrorTransferFilesSchema.resource": False,
    "SnapmirrorTransferFiles": False,
}


class SnapmirrorTransferFilesSchema(ResourceSchema):
    """The fields of the SnapmirrorTransferFiles object"""

    destination_path = fields.Str(data_key="destination_path")
    r""" The destination_path field of the snapmirror_transfer_files.

Example: /dirb/file2 """

    source_path = fields.Str(data_key="source_path")
    r""" The source_path field of the snapmirror_transfer_files.

Example: /dira/file1 """

    @property
    def resource(self):
        return SnapmirrorTransferFiles

    @property
    def patchable_fields(self):
        return [
            "destination_path",
            "source_path",
        ]

    @property
    def postable_fields(self):
        return [
            "destination_path",
            "source_path",
        ]


class SnapmirrorTransferFiles(Resource):  # pylint: disable=missing-docstring

    _schema = SnapmirrorTransferFilesSchema
