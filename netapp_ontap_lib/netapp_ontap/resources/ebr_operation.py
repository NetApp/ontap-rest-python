# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

Use this API to display all Event Based Retention (EBR) operations and to apply an EBR policy on a specified volume.
### Examples
1. Displays all of the EBR operations:
   <br/>
   ```
   GET "/api/storage/snaplock/event-retention/operations"
   ```
   <br/>
2. Displays all completed EBR operations:
   <br/>
   ```
   GET "/api/storage/snaplock/event-retention/operations?state=completed"
   ```
   <br/>
3. Displays all completed EBR operations with filter set as volume.uuid:
   <br/>
   ```
   GET "/api/storage/snaplock/event-retention/operations?volume.uuid=b96f976e-404b-11e9-bff2-0050568e4dbe"
   ```
   <br/>
4. Displays all of the EBR operations with filter set as volume.name:
   <br/>
   ```
   GET "/api/storage/snaplock/event-retention/operations?volume.name=SLCVOL"
   ```
   <br/>
### Examples
1. Applies an EBR policy on a specific path:
   <br/>
   ```
   POST "/api/storage/snaplock/event-retention/operations" '{"volume.name":"SLCVOL", "policy.name":"p1day", "path":"/dir1/file.txt"}'
   ```
   <br/>
2. Applies an EBR policy on the complete volume:
   <br/>
   ```
   POST "/api/storage/snaplock/event-retention/operations" '{"volume.name":"SLCVOL", "policy.name":"p1day", "path":"/"}'
   ```
   <br/>
### Example
<br/>
```
DELETE "/api/storage/snaplock/event-retention/operations/16842999"
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


__all__ = ["EbrOperation", "EbrOperationSchema"]
__pdoc__ = {
    "EbrOperationSchema.resource": False,
    "EbrOperationSchema.patchable_fields": False,
    "EbrOperationSchema.postable_fields": False,
}


class EbrOperationSchema(ResourceSchema):
    """The fields of the EbrOperation object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ebr_operation. """

    id = fields.Integer(
        data_key="id",
    )
    r""" Operation ID

Example: 16842759 """

    num_files_failed = fields.Integer(
        data_key="num_files_failed",
    )
    r""" Specifies the number of files on which the application of EBR policy failed.

Example: 0 """

    num_files_processed = fields.Integer(
        data_key="num_files_processed",
    )
    r""" Specifies the number of files on which EBR policy was applied successfully.

Example: 50 """

    num_files_skipped = fields.Integer(
        data_key="num_files_skipped",
    )
    r""" Specifies the number of files on which the application of EBR policy was skipped.

Example: 2 """

    num_inodes_ignored = fields.Integer(
        data_key="num_inodes_ignored",
    )
    r""" Specifies the number of inodes on which the application of EBR policy was not attempted because they were not regular files.

Example: 2 """

    path = fields.Str(
        data_key="path",
    )
    r""" The path for the EBR operation. Specifies the path relative to the output volume root, of the form "/path". The path can be path to a file or a directory.

Example: /dir1/file """

    policy = fields.Nested("netapp_ontap.resources.snaplock_retention_policy.SnaplockRetentionPolicySchema", data_key="policy", unknown=EXCLUDE)
    r""" The policy field of the ebr_operation. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['unknown', 'in_progress', 'failed', 'aborting', 'completed']),
    )
    r""" Specifies the operation status of an EBR operation.

Valid choices:

* unknown
* in_progress
* failed
* aborting
* completed """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the ebr_operation. """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the ebr_operation. """

    @property
    def resource(self):
        return EbrOperation

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "path",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

class EbrOperation(Resource):
    """Allows interaction with EbrOperation objects on the host"""

    _schema = EbrOperationSchema
    _path = "/api/storage/snaplock/event-retention/operations"
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
        r"""Retrieves a list of all EBR operations.
### Related ONTAP commands
* `snaplock event-retention show`
### Learn more
* [`DOC /storage/snaplock/event-retention/operations`](#docs-snaplock-storage_snaplock_event-retention_operations)
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
        r"""Aborts an ongoing EBR operation.
### Related ONTAP commands
* `snaplock event-retention abort`
### Learn more
* [`DOC /storage/snaplock/event-retention/operations`](#docs-snaplock-storage_snaplock_event-retention_operations)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of all EBR operations.
### Related ONTAP commands
* `snaplock event-retention show`
### Learn more
* [`DOC /storage/snaplock/event-retention/operations`](#docs-snaplock-storage_snaplock_event-retention_operations)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a list of attributes for an EBR operation.
### Related ONTAP commands
* `snaplock event-retention show`
### Learn more
* [`DOC /storage/snaplock/event-retention/operations`](#docs-snaplock-storage_snaplock_event-retention_operations)
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
        r"""Creates an EBR policy.
### Required properties
* `path` - Path of the file.
* `policy.name` - Name of the EBR policy.
### Related ONTAP commands
* `snaplock event-retention apply`
### Learn more
* [`DOC /storage/snaplock/event-retention/operations`](#docs-snaplock-storage_snaplock_event-retention_operations)
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
        r"""Aborts an ongoing EBR operation.
### Related ONTAP commands
* `snaplock event-retention abort`
### Learn more
* [`DOC /storage/snaplock/event-retention/operations`](#docs-snaplock-storage_snaplock_event-retention_operations)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


