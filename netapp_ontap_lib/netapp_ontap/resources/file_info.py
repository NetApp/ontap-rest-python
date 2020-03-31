# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

This API is used to retrieve a list of files and directories for a given directory of a volume.
## Examples
###  Retrieving the list of files in a directory
```
# The API:
GET /api/storage/volumes/{volume.uuid}/files/{path}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/volumes/cb6b1b39-8d21-11e9-b926-05056aca658/files/d1%2Fd2%2Fd3"  -H 'accept: application/hal+json'
# Response for file records:
{
  "records": [
    {
      "path": "d1/d2/d3",
      "name": ".",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/cb6b1b39-8d21-11e9-b926-005056aca658/files/d1%2Fd2%2Fd3%2F%2E"
        }
      }
    },
    {
      "path": "d1/d2/d3",
      "name": "..",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/cb6b1b39-8d21-11e9-b926-005056aca658/files/d1%2Fd2%2Fd3%2F%2E%2E"
        }
      }
    },
    {
      "path": "d1/d2/d3",
      "name": "f1"
    },
    {
      "path": "d1/d2/d3",
      "name": "d5",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/cb6b1b39-8d21-11e9-b926-005056aca658/files/d1%2Fd2%2Fd3%2Fd5"
        }
      }
    }
  ],
  "num_records": 4,
  "_links": {
    "self": {
      "href": "/api/storage/volumes/cb6b1b39-8d21-11e9-b926-005056aca658/files/d1%2Fd2%2Fd3"
    }
  }
}
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["FileInfo", "FileInfoSchema"]
__pdoc__ = {
    "FileInfoSchema.resource": False,
    "FileInfoSchema.patchable_fields": False,
    "FileInfoSchema.postable_fields": False,
}


class FileInfoSchema(ResourceSchema):
    """The fields of the FileInfo object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the file_info. """

    accessed_time = fields.DateTime(
        data_key="accessed_time",
    )
    r""" Last access time of the file in date-time format.

Example: 2019-06-12T15:00:16.000+0000 """

    bytes_used = fields.Integer(
        data_key="bytes_used",
    )
    r""" The actual number of bytes used on disk by this file.

Example: 4096 """

    changed_time = fields.DateTime(
        data_key="changed_time",
    )
    r""" Last time data or attributes changed on the file in date-time format.

Example: 2019-06-12T15:00:16.000+0000 """

    creation_time = fields.DateTime(
        data_key="creation_time",
    )
    r""" Creation time of the file in date-time format.

Example: 2019-06-12T15:00:16.000+0000 """

    group_id = fields.Integer(
        data_key="group_id",
    )
    r""" The integer ID of the group of the file owner.

Example: 30 """

    hard_links_count = fields.Integer(
        data_key="hard_links_count",
    )
    r""" The number of hard links to the file.

Example: 1 """

    inode_generation = fields.Integer(
        data_key="inode_generation",
    )
    r""" Inode generation number.

Example: 214753547 """

    inode_number = fields.Integer(
        data_key="inode_number",
    )
    r""" The file inode number.

Example: 1695 """

    is_empty = fields.Boolean(
        data_key="is_empty",
    )
    r""" Specifies whether or not a directory is empty. A directory is considered empty if it only contains entries for "." and "..". This element is present if the file is a directory. In some special error cases, such as when the volume goes offline or when the directory is moved while retrieving this info, this field might not get set.

Example: false """

    is_junction = fields.Boolean(
        data_key="is_junction",
    )
    r""" Returns "true" if the directory is a junction.

Example: false """

    is_vm_aligned = fields.Boolean(
        data_key="is_vm_aligned",
    )
    r""" Returns true if the file is vm-aligned. A vm-aligned file is a file that is initially padded with zero-filled data so that its actual data starts at an offset other then zero. This is done in a VM environment so that read/write operations to this file are aligned to WAFL's 4k block boundary. The amount by which the start offset is adjusted depends on the vm-align setting of the hosting volume.

Example: false """

    modified_time = fields.DateTime(
        data_key="modified_time",
    )
    r""" Last data modification time of the file in date-time format.

Example: 2019-06-12T15:00:16.000+0000 """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the file.

Example: test_file """

    owner_id = fields.Integer(
        data_key="owner_id",
    )
    r""" The integer ID of the file owner.

Example: 54738 """

    path = fields.Str(
        data_key="path",
    )
    r""" Path of the file.

Example: d1/d2/d3 """

    size = fields.Integer(
        data_key="size",
    )
    r""" The size of the file, in bytes.

Example: 200 """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['file', 'directory', 'blockdev', 'chardev', 'symlink', 'socket', 'fifo', 'stream', 'lun']),
    )
    r""" Type of the file.

Valid choices:

* file
* directory
* blockdev
* chardev
* symlink
* socket
* fifo
* stream
* lun """

    unix_permissions = fields.Integer(
        data_key="unix_permissions",
    )
    r""" UNIX permissions to be viewed as an octal number. It consists of 4 digits derived by adding up bits 4 (read), 2 (write) and 1 (execute). The first digit selects the set user ID(4), set group ID (2) and sticky (1) attributes. The second digit selects permission for the owner of the file; the third selects permissions for other users in the same group; the fourth for other users not in the group.

Example: 493 """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the file_info. """

    @property
    def resource(self):
        return FileInfo

    @property
    def patchable_fields(self):
        return [
            "accessed_time",
            "bytes_used",
            "changed_time",
            "creation_time",
            "group_id",
            "hard_links_count",
            "inode_generation",
            "inode_number",
            "is_empty",
            "is_junction",
            "is_vm_aligned",
            "modified_time",
            "name",
            "owner_id",
            "path",
            "size",
            "type",
            "unix_permissions",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "accessed_time",
            "bytes_used",
            "changed_time",
            "creation_time",
            "group_id",
            "hard_links_count",
            "inode_generation",
            "inode_number",
            "is_empty",
            "is_junction",
            "is_vm_aligned",
            "modified_time",
            "name",
            "owner_id",
            "path",
            "size",
            "type",
            "unix_permissions",
            "volume.name",
            "volume.uuid",
        ]

class FileInfo(Resource):
    r""" Information about a single file. """

    _schema = FileInfoSchema
    _path = "/api/storage/volumes/{volume[uuid]}/files"
    @property
    def _keys(self):
        return ["volume.uuid", "path"]





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a list of files and directories for a given directory of a volume.
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/files/{path}`](#docs-storage-storage_volumes_{volume.uuid}_files_{path})"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





