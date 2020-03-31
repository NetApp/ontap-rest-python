# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["FileClone", "FileCloneSchema"]
__pdoc__ = {
    "FileCloneSchema.resource": False,
    "FileCloneSchema.patchable_fields": False,
    "FileCloneSchema.postable_fields": False,
}


class FileCloneSchema(ResourceSchema):
    """The fields of the FileClone object"""

    autodelete = fields.Boolean(
        data_key="autodelete",
    )
    r""" Mark file clone for auto deletion. """

    destination_path = fields.Str(
        data_key="destination_path",
    )
    r""" Relative path of the clone/destination file in the volume.

Example: dest_file1, dir1/dest_file2 """

    range = fields.List(fields.Str, data_key="range")
    r""" List of block ranges for sub-file cloning in the format "source-file-block-number:destination-file-block-number:block-count"

Example: [36605,73210] """

    source_path = fields.Str(
        data_key="source_path",
    )
    r""" Relative path of the source file in the volume.

Example: src_file1, dir1/src_file2, ./.snapshot/snap1/src_file3 """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the file_clone. """

    @property
    def resource(self):
        return FileClone

    @property
    def patchable_fields(self):
        return [
            "autodelete",
            "destination_path",
            "range",
            "source_path",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "autodelete",
            "destination_path",
            "range",
            "source_path",
            "volume.name",
            "volume.uuid",
        ]

class FileClone(Resource):
    r""" File clone """

    _schema = FileCloneSchema
    _path = "/api/storage/file/clone"






    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a clone of the file."""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member




