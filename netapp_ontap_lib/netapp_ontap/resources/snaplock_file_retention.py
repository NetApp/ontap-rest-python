# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

This API manages the SnapLock retention time of a file. You can perform a privileged-delete operation by executing this API.
### Examples
1. Sets the SnapLock retention time of a file:
   <br/>
   ```
   PATCH "/api/storage/snaplock/file/000dc5fd-4175-11e9-b937-0050568e3f82/%2Ffile2.txt" '{"expiry_time": "2030-02-14T18:30:00+5:30"}'
   ```
   <br/>
2. Extends the retention time of a WORM file:
   <br/>
   ```
   PATCH "/api/storage/snaplock/file/000dc5fd-4175-11e9-b937-0050568e3f82/%2Ffile2.txt" '{"expiry_time": "infinite"}'
   ```
   <br/>
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnaplockFileRetention", "SnaplockFileRetentionSchema"]
__pdoc__ = {
    "SnaplockFileRetentionSchema.resource": False,
    "SnaplockFileRetentionSchema.patchable_fields": False,
    "SnaplockFileRetentionSchema.postable_fields": False,
}


class SnaplockFileRetentionSchema(ResourceSchema):
    """The fields of the SnaplockFileRetention object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snaplock_file_retention. """

    expiry_time = fields.DateTime(
        data_key="expiry_time",
    )
    r""" Expiry time of the file in date-time format.

Example: 2058-06-04T19:00:00.000+0000 """

    file_path = fields.Str(
        data_key="file_path",
    )
    r""" Specifies the volume relative path of the file

Example: /dir1/file """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the snaplock_file_retention. """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the snaplock_file_retention. """

    @property
    def resource(self):
        return SnaplockFileRetention

    @property
    def patchable_fields(self):
        return [
            "expiry_time",
        ]

    @property
    def postable_fields(self):
        return [
            "file_path",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

class SnaplockFileRetention(Resource):
    """Allows interaction with SnaplockFileRetention objects on the host"""

    _schema = SnaplockFileRetentionSchema
    _path = "/api/storage/snaplock/file"
    @property
    def _keys(self):
        return ["volume.uuid", "path"]


    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the SnapLock retention time of a file or extends the retention time of a WORM file. Input parameter expiry_time expects the date in ISO 8601 format or infinite.
### Related ONTAP commands
* `volume file retention set`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def delete_collection(
        cls,
        *args,
        body: Union[Resource, dict] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes unexpired WORM files of a SnapLock Enterprise volume. This is a privileged-delete operation. The only built-in role that has access to the command is vsadmin-snaplock.
### Related ONTAP commands
* `volume file privileged-delete`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the SnapLock retention details of the specified file. An indefinite expiry time indicates the file is under a Legal-Hold.
### Related ONTAP commands
* `volume file retention show`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the SnapLock retention time of a file or extends the retention time of a WORM file. Input parameter expiry_time expects the date in ISO 8601 format or infinite.
### Related ONTAP commands
* `volume file retention set`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes unexpired WORM files of a SnapLock Enterprise volume. This is a privileged-delete operation. The only built-in role that has access to the command is vsadmin-snaplock.
### Related ONTAP commands
* `volume file privileged-delete`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


