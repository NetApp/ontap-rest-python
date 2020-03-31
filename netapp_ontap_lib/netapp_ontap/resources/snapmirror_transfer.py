# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API is used to manage transfers on an existing SnapMirror relationship.</br>
You can initiate SnapMirror operations such as "initialize", "update", "restore-transfer", and "abort" using this API and it only manages the active transfers on the specified relationship. For the restore relationships, the POST on transfers API triggers "restore-transfer". Successful completion of "restore"  also deletes the restore relationship. If the "restore" fails, DELETE on relationships must be called to delete the restore relationship.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnapmirrorTransfer", "SnapmirrorTransferSchema"]
__pdoc__ = {
    "SnapmirrorTransferSchema.resource": False,
    "SnapmirrorTransferSchema.patchable_fields": False,
    "SnapmirrorTransferSchema.postable_fields": False,
}


class SnapmirrorTransferSchema(ResourceSchema):
    """The fields of the SnapmirrorTransfer object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snapmirror_transfer. """

    bytes_transferred = fields.Integer(
        data_key="bytes_transferred",
    )
    r""" Bytes transferred """

    checkpoint_size = fields.Integer(
        data_key="checkpoint_size",
    )
    r""" Amount of data transferred in bytes as recorded in the restart checkpoint. """

    files = fields.List(fields.Nested("netapp_ontap.models.snapmirror_transfer_files.SnapmirrorTransferFilesSchema", unknown=EXCLUDE), data_key="files")
    r""" This is supported for transfer of restore relationship only. This specifies the list of files or LUNs to be restored. Can contain up to eight files or LUNs. """

    relationship = fields.Nested("netapp_ontap.models.snapmirror_transfer_relationship.SnapmirrorTransferRelationshipSchema", data_key="relationship", unknown=EXCLUDE)
    r""" The relationship field of the snapmirror_transfer. """

    snapshot = fields.Str(
        data_key="snapshot",
    )
    r""" Name of Snapshot copy being transferred. """

    source_snapshot = fields.Str(
        data_key="source_snapshot",
    )
    r""" Specifies the Snapshot copy on the source to be transferred to the destination. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['aborted', 'failed', 'hard_aborted', 'queued', 'success', 'transferring']),
    )
    r""" Status of the transfer. Set PATCH state to "aborted" to abort the transfer. Set PATCH state to "hard_aborted" to abort the transfer and discard the restart checkpoint.

Valid choices:

* aborted
* failed
* hard_aborted
* queued
* success
* transferring """

    storage_efficiency_enabled = fields.Boolean(
        data_key="storage_efficiency_enabled",
    )
    r""" This is supported for transfer of restore relationship only. Set this property to "false" to turn off storage efficiency for data transferred over the wire and written to the destination. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the snapmirror_transfer.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return SnapmirrorTransfer

    @property
    def patchable_fields(self):
        return [
            "relationship",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "files",
            "relationship",
            "source_snapshot",
            "storage_efficiency_enabled",
        ]

class SnapmirrorTransfer(Resource):
    r""" SnapMirror transfer information """

    _schema = SnapmirrorTransferSchema
    _path = "/api/snapmirror/relationships/{relationship[uuid]}/transfers"
    @property
    def _keys(self):
        return ["relationship.uuid", "uuid"]

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
        r"""Retrieves the list of ongoing SnapMirror transfers for the specified relationship.
### Related ONTAP commands
* `snapmirror show`
### Example
<br/>
```
GET "/api/snapmirror/relationships/293baa53-e63d-11e8-bff1-005056a793dd/transfers"
```
### Learn more
* [`DOC /snapmirror/relationships/{relationship.uuid}/transfers`](#docs-snapmirror-snapmirror_relationships_{relationship.uuid}_transfers)
<br/>
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member

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
        r"""Aborts an ongoing SnapMirror transfer.
### Related ONTAP commands
* `snapmirror abort`
### Example
<br/>
```
PATCH "/api/snapmirror/relationships/293baa53-e63d-11e8-bff1-005056a793dd/transfers/293baa53-e63d-11e8-bff1-005056a793dd" '{"state":"aborted"}'
```
<br/>
### Learn more
* [`DOC /snapmirror/relationships/{relationship.uuid}/transfers`](#docs-snapmirror-snapmirror_relationships_{relationship.uuid}_transfers)
"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the list of ongoing SnapMirror transfers for the specified relationship.
### Related ONTAP commands
* `snapmirror show`
### Example
<br/>
```
GET "/api/snapmirror/relationships/293baa53-e63d-11e8-bff1-005056a793dd/transfers"
```
### Learn more
* [`DOC /snapmirror/relationships/{relationship.uuid}/transfers`](#docs-snapmirror-snapmirror_relationships_{relationship.uuid}_transfers)
<br/>
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the attributes of a specific ongoing SnapMirror transfer.
### Related ONTAP commands
* `snapmirror show`
### Example
<br/>
```
GET "/api/snapmirror/relationships/293baa53-e63d-11e8-bff1-005056a793dd/transfers/293baa53-e63d-11e8-bff1-005056a793dd"
```
<br/>
### Learn more
* [`DOC /snapmirror/relationships/{relationship.uuid}/transfers`](#docs-snapmirror-snapmirror_relationships_{relationship.uuid}_transfers)
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
        r"""Starts a SnapMirror transfer operation. This API initiates a restore operation if the SnapMirror relationship is of type "restore". Otherwise, it intiates a SnapMirror "initialize" operation or "update" operation based on the current SnapMirror state.
### Default property values
* `storage_efficiency_enabled` - _true_
### Related ONTAP commands
* `snapmirror update`
* `snapmirror initialize`
* `snapmirror restore`
### Examples
The following examples show how to perform SnapMirror "initialize", "update", and "restore" operations.
<br/>
   Performing a SnapMirror initialize or update
   <br/>
   ```
   POST "/api/snapmirror/relationships/e4e7e130-0279-11e9-b566-0050568e9909/transfers" '{}'
   ```
   <br/>
   Performing a SnapMirror restore transfer
   <br/>
   ```
   POST "/api/snapmirror/relationships/c8c62a90-0fef-11e9-b09e-0050568e7067/transfers" '{"source-snapshot": "src", "files": {"source_path": ["/a1.txt.0"], "destination_path": ["/a1-renamed.txt.0"]}}'
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/relationships/{relationship.uuid}/transfers`](#docs-snapmirror-snapmirror_relationships_{relationship.uuid}_transfers)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member

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
        r"""Aborts an ongoing SnapMirror transfer.
### Related ONTAP commands
* `snapmirror abort`
### Example
<br/>
```
PATCH "/api/snapmirror/relationships/293baa53-e63d-11e8-bff1-005056a793dd/transfers/293baa53-e63d-11e8-bff1-005056a793dd" '{"state":"aborted"}'
```
<br/>
### Learn more
* [`DOC /snapmirror/relationships/{relationship.uuid}/transfers`](#docs-snapmirror-snapmirror_relationships_{relationship.uuid}_transfers)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



