# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

Manages the legal-hold operations for the specified litigation ID.
### Examples
1. Adds a Legal-Hold.
   <br/>
   ```
   POST "/api/storage/snaplock/litigations/f8a67b60-4461-11e9-b327-0050568ebef5:l1/operations" '{"lh_operation.type" : "begin", "lh_operation.path" : "/a.txt"}'
   ```
   <br/>
2. Removes a Legal-Hold.
   <br/>
   ```
   POST "/api/storage/snaplock/litigations/f8a67b60-4461-11e9-b327-0050568ebef5:l1/operations" '{"lh_operation.type" : "end", "lh_operation.path" : "/a.txt"}'
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


__all__ = ["SnaplockLegalHoldOperation", "SnaplockLegalHoldOperationSchema"]
__pdoc__ = {
    "SnaplockLegalHoldOperationSchema.resource": False,
    "SnaplockLegalHoldOperationSchema.patchable_fields": False,
    "SnaplockLegalHoldOperationSchema.postable_fields": False,
}


class SnaplockLegalHoldOperationSchema(ResourceSchema):
    """The fields of the SnaplockLegalHoldOperation object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snaplock_legal_hold_operation. """

    id = fields.Integer(
        data_key="id",
    )
    r""" Operation ID.

Example: 16842759 """

    num_files_failed = fields.Str(
        data_key="num_files_failed",
    )
    r""" Specifies the number of files on which legal-hold operation failed.

Example: 0 """

    num_files_processed = fields.Str(
        data_key="num_files_processed",
    )
    r""" Specifies the number of files on which legal-hold operation was successful.

Example: 30 """

    num_files_skipped = fields.Str(
        data_key="num_files_skipped",
    )
    r""" Specifies the number of files on which legal-hold begin operation was skipped. The legal-hold begin operation is skipped on a file if it is already under hold for a given litigation.

Example: 10 """

    num_inodes_ignored = fields.Str(
        data_key="num_inodes_ignored",
    )
    r""" Specifies the number of inodes on which the legal-hold operation was not attempted because they were not regular files.

Example: 10 """

    path = fields.Str(
        data_key="path",
    )
    r""" Specifies the path on which legal-hold operation is applied.

Example: /dir1 """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['in_progress', 'failed', 'aborting', 'completed']),
    )
    r""" Specifies the status of legal-hold operation.

Valid choices:

* in_progress
* failed
* aborting
* completed """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['begin', 'end']),
    )
    r""" Specifies the type of legal-hold operation.

Valid choices:

* begin
* end """

    @property
    def resource(self):
        return SnaplockLegalHoldOperation

    @property
    def patchable_fields(self):
        return [
            "type",
        ]

    @property
    def postable_fields(self):
        return [
            "path",
        ]

class SnaplockLegalHoldOperation(Resource):
    """Allows interaction with SnaplockLegalHoldOperation objects on the host"""

    _schema = SnaplockLegalHoldOperationSchema
    _path = "/api/storage/snaplock/litigations/{litigation[id]}/operations"
    @property
    def _keys(self):
        return ["litigation.id", "id"]



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
        r"""Aborts the ongoing legal-hold operation. An abort does not rollback any changes already made. You must re-run begin or end for cleanup.
### Related ONTAP commands
* `snaplock legal-hold abort`
### Example
<br/>
```
DELETE "/api/storage/snaplock/litigations/f8a67b60-4461-11e9-b327-0050568ebef5:l1?lh_operation.id=16908292"
```
<br/>
### Learn more
* [`DOC /storage/snaplock/litigations/{litigation.id}/operations`](#docs-snaplock-storage_snaplock_litigations_{litigation.id}_operations)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the status of legal-hold for the specified operation ID.
### Related ONTAP commands
* `snaplock legal-hold show`
### Learn more
* [`DOC /storage/snaplock/litigations/{litigation.id}/operations`](#docs-snaplock-storage_snaplock_litigations_{litigation.id}_operations)
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
        r"""Creates or removes litigations for the specified path.
### Required properties
* `lh_operation.type` - Legal-Hold operation type.
* `lh.operation.path` - Litigation path.
### Related ONTAP commands
* `snaplock legal-hold begin`
* `snaplock legal-hold end`
### Learn more
* [`DOC /storage/snaplock/litigations/{litigation.id}/operations`](#docs-snaplock-storage_snaplock_litigations_{litigation.id}_operations)
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
        r"""Aborts the ongoing legal-hold operation. An abort does not rollback any changes already made. You must re-run begin or end for cleanup.
### Related ONTAP commands
* `snaplock legal-hold abort`
### Example
<br/>
```
DELETE "/api/storage/snaplock/litigations/f8a67b60-4461-11e9-b327-0050568ebef5:l1?lh_operation.id=16908292"
```
<br/>
### Learn more
* [`DOC /storage/snaplock/litigations/{litigation.id}/operations`](#docs-snaplock-storage_snaplock_litigations_{litigation.id}_operations)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


