# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

Use this API to view key information about files and volumes, including the file type (regular, WORM, or WORM appendable), the volume expiration date, and so on.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnaplockFileFingerprint", "SnaplockFileFingerprintSchema"]
__pdoc__ = {
    "SnaplockFileFingerprintSchema.resource": False,
    "SnaplockFileFingerprintSchema.patchable_fields": False,
    "SnaplockFileFingerprintSchema.postable_fields": False,
}


class SnaplockFileFingerprintSchema(ResourceSchema):
    """The fields of the SnaplockFileFingerprint object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snaplock_file_fingerprint. """

    algorithm = fields.Str(
        data_key="algorithm",
        validate=enum_validation(['md5', 'sha256']),
    )
    r""" The digest algorithm which is used for the fingerprint computation

Valid choices:

* md5
* sha256 """

    data_fingerprint = fields.Str(
        data_key="data_fingerprint",
    )
    r""" The digest value of data of the file. The fingerprint is base64 encoded. This field is not included if the scope is metadata-only.

Example: MOFJVevxNSJm3C/4Bn5oEEYH51CrudOzZYK4r5Cfy1g= """

    file_size = fields.Integer(
        data_key="file_size",
    )
    r""" The size of the file in bytes.

Example: 1048576 """

    file_type = fields.Str(
        data_key="file_type",
        validate=enum_validation(['worm', 'worm_appendable', 'worm_active_log', 'worm_log', 'regular']),
    )
    r""" The type of the file.

Valid choices:

* worm
* worm_appendable
* worm_active_log
* worm_log
* regular """

    id = fields.Integer(
        data_key="id",
    )
    r""" A unique identifier for the fingerprint operation

Example: 17039367 """

    metadata_fingerprint = fields.Str(
        data_key="metadata_fingerprint",
    )
    r""" The digest value of metadata of the file. The metadata fingerprint is calculated for file size, file ctime, file mtime, file crtime, file retention time, file uid, file gid, and file type. The fingerprint is base64 encoded. This field is not included if the scope is data-only.

Example: 8iMjqJXiNcqgXT5XuRhLiEwIrJEihDmwS0hrexnjgmc= """

    path = fields.Str(
        data_key="path",
    )
    r""" Specifies the path on which file fingerprint operation is running or has completed. Specifies the path relative to the output volume root, of the form "/path". The path can be path to a file or a directory.

Example: /homedir/dir1 """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['data_and_metadata', 'data_only', 'metadata_only']),
    )
    r""" The scope of the file which is used for the fingerprint computation

Valid choices:

* data_and_metadata
* data_only
* metadata_only """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['in_progress', 'failed', 'aborting', 'completed']),
    )
    r""" Specifies the status of fingerprint operation.

Valid choices:

* in_progress
* failed
* aborting
* completed """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the snaplock_file_fingerprint. """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the snaplock_file_fingerprint. """

    @property
    def resource(self):
        return SnaplockFileFingerprint

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "algorithm",
            "path",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

class SnaplockFileFingerprint(Resource):
    """Allows interaction with SnaplockFileFingerprint objects on the host"""

    _schema = SnaplockFileFingerprintSchema
    _path = "/api/storage/snaplock/file-fingerprints"
    @property
    def _keys(self):
        return ["id"]

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a list of all the fingerprint operations of the specified SVM and volume.
### Related ONTAP commands
* `volume file fingerprint show`
### Example
<br/>
```
GET "/api/storage/snaplock/file-fingerprints/?svm.uuid=23940494-3f3a-11e9-8675-0050568e8f89&volume.uuid=36cdb58c-3f3a-11e9-8675-0050568e8f89"
```
<br/>
### Learn more
* [`DOC /storage/snaplock/file-fingerprints`](#docs-snaplock-storage_snaplock_file-fingerprints)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member


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
        r"""Aborts an in-progress fingerprint operation. This API takes session-id as input and aborts the fingerprint operation that is associated with the specified session-id.
### Related ONTAP commands
* `volume file fingerprint abort`
### Learn more
* [`DOC /storage/snaplock/file-fingerprints`](#docs-snaplock-storage_snaplock_file-fingerprints)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of all the fingerprint operations of the specified SVM and volume.
### Related ONTAP commands
* `volume file fingerprint show`
### Example
<br/>
```
GET "/api/storage/snaplock/file-fingerprints/?svm.uuid=23940494-3f3a-11e9-8675-0050568e8f89&volume.uuid=36cdb58c-3f3a-11e9-8675-0050568e8f89"
```
<br/>
### Learn more
* [`DOC /storage/snaplock/file-fingerprints`](#docs-snaplock-storage_snaplock_file-fingerprints)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the file fingerprint information for a specific session ID.
### Related ONTAP commands
* `volume file fingerprint dump`
### Learn more
* [`DOC /storage/snaplock/file-fingerprints`](#docs-snaplock-storage_snaplock_file-fingerprints)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member

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
        r"""Creates a fingerprint computation session on the file and returns a session-id. This session-id is a unique identifier that you can use to retrieve the progress of an ongoing fingerprint operation. When the operation is complete, you can use the session-id to retrieve the complete fingerprint output for the file .
### Required properties
* `svm.uuid` or `svm.name` - Name or UUID of the SVM.
* `volume.name` or `volume.uuid` - Name or UUID of the volume.
* `path` - Path of the file.
### Default property values
If not specified in POST, the follow default property values are assigned:
* `algorithm` - _md5_
### Related ONTAP commands
* `volume file fingerprint start`
### Example
<br/>
```
POST "/api/storage/snaplock/file-fingerprints" '{"svm":{"uuid":"23940494-3f3a-11e9-8675-0050568e8f89"},"volume": {"uuid":"26cdb58c-3f3a-11e9-8675-0050568e8f89"},"path":"/vol/a1.txt","algorithm":"md5"}'
```
<br/>
### Learn more
* [`DOC /storage/snaplock/file-fingerprints`](#docs-snaplock-storage_snaplock_file-fingerprints)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member


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
        r"""Aborts an in-progress fingerprint operation. This API takes session-id as input and aborts the fingerprint operation that is associated with the specified session-id.
### Related ONTAP commands
* `volume file fingerprint abort`
### Learn more
* [`DOC /storage/snaplock/file-fingerprints`](#docs-snaplock-storage_snaplock_file-fingerprints)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


