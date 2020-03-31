# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API manages asynchronous extended data protection (XDP) relationships for FlexVols, FlexGroups, or SVMs. It is also used to create a synchronous relationship between FlexVol volumes, which provides zero RPO data protection. It supports the SnapMirror policy types "mirror-vault", "sync-mirror", and "strict-sync-mirror". You can create a relationship between the source and destination which can be used to transfer APIs to perform SnapMirror "restore" operations.<br/>
To create FlexVol or FlexGroup SnapMirror relationships, the source volume must be in the "online" state and be a read-write type; the destination volume must be in the "online" state and be a data protection type.
To create SnapMirror relationships between SVMs, the source SVM must be of subtype "default" and the destination SVM of subtype "dp_destination". Additionally, SVMs must be peered before a relationship can be established between them.
The SnapMirror functionality is subdivided into relationship APIs and transfer APIs:
- SnapMirror relationship APIs are used to create and manage the SnapMirror relationships.
- SnapMirror transfer APIs are used to manage data transfers.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnapmirrorRelationship", "SnapmirrorRelationshipSchema"]
__pdoc__ = {
    "SnapmirrorRelationshipSchema.resource": False,
    "SnapmirrorRelationshipSchema.patchable_fields": False,
    "SnapmirrorRelationshipSchema.postable_fields": False,
}


class SnapmirrorRelationshipSchema(ResourceSchema):
    """The fields of the SnapmirrorRelationship object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snapmirror_relationship. """

    create_destination = fields.Nested("netapp_ontap.models.snapmirror_destination_creation.SnapmirrorDestinationCreationSchema", data_key="create_destination", unknown=EXCLUDE)
    r""" The create_destination field of the snapmirror_relationship. """

    destination = fields.Nested("netapp_ontap.models.snapmirror_endpoint.SnapmirrorEndpointSchema", data_key="destination", unknown=EXCLUDE)
    r""" This property is the destination endpoint of the relationship. The destination endpoint can be a FlexVol volume, FlexGroup volume, or SVM. For the POST request, the destination endpoint must be of type "DP" when the endpoint is a FlexVol volume or a FlexGroup volume. The POST request for SVM must have a destination endpoint of type "dp-destination". The destination endpoint path name must be specified in the "destination.path" property. The destination endpoint for FlexVol volume or FlexGroup volume will change to type "RW" when the relationship status is "broken_off" and will revert to type "DP" when the relationship status is "snapmirrored" using the PATCH request. The destination endpoint for SVM will change from "dp-destination" to type "default" when the relationship status is "broken_off" and will revert to type "dp-destination" when the relationship status is "snapmirrored" using the PATCH request. """

    exported_snapshot = fields.Str(
        data_key="exported_snapshot",
    )
    r""" Snapshot copy exported to clients on destination. """

    healthy = fields.Boolean(
        data_key="healthy",
    )
    r""" Is the relationship healthy? """

    lag_time = fields.Str(
        data_key="lag_time",
    )
    r""" Time since the exported Snapshot copy was created.

Example: PT8H35M42S """

    policy = fields.Nested("netapp_ontap.models.snapmirror_relationship_policy.SnapmirrorRelationshipPolicySchema", data_key="policy", unknown=EXCLUDE)
    r""" The policy field of the snapmirror_relationship. """

    preserve = fields.Boolean(
        data_key="preserve",
    )
    r""" Set to true on resync to preserve Snapshot copies on the destination that are newer than the latest common Snapshot copy. This property is applicable only for relationships with FlexGroup or FlexVol endpoints and when the PATCH state is being changed to "snapmirrored". """

    quick_resync = fields.Boolean(
        data_key="quick_resync",
    )
    r""" Set to true to reduce resync time by not preserving storage efficiency. This property is applicable only for relationships with FlexVol endpoints and when the PATCH state is being changed to "snapmirrored". """

    recover_after_break = fields.Boolean(
        data_key="recover_after_break",
    )
    r""" Set to true to recover from a failed SnapMirror break operation on a FlexGroup relationship. This restores all destination FlexGroup constituents to the latest Snapshot copy, and any writes to the read-write constituents are lost. This property is applicable only for SnapMirror relationships with FlexGroup endpoints and when the PATCH state is being changed to "broken_off". """

    restore = fields.Boolean(
        data_key="restore",
    )
    r""" Set to true to create a relationship for restore. To trigger restore-transfer, use transfers POST on the restore relationship. """

    restore_to_snapshot = fields.Str(
        data_key="restore_to_snapshot",
    )
    r""" Specifies the Snapshot copy to restore to on the destination during the break operation. This property is applicable only for SnapMirror relationships with FlexVol endpoints and when the PATCH state is being changed to "broken_off". """

    source = fields.Nested("netapp_ontap.models.snapmirror_endpoint.SnapmirrorEndpointSchema", data_key="source", unknown=EXCLUDE)
    r""" This property is the source endpoint of the relationship. The source endpoint can be a FlexVol volume, FlexGroup volume, or SVM. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['broken_off', 'paused', 'snapmirrored', 'uninitialized', 'in_sync', 'out_of_sync', 'synchronizing']),
    )
    r""" State of the relationship. To initialize the relationship, PATCH the state to "snapmirrored" for relationships with a policy of type "async" or "in-sync" for relationships with a policy of type "sync". To break the relationship, PATCH the state to "broken_off". To resync the broken relationship, PATCH the state to "snapmirrored" for relationships with a policy of type "async" or "in_sync" for relationships with a policy of type "sync". To pause the relationship, suspending further transfers, PATCH the state to "paused". To resume transfers for a paused relationship, PATCH the state to "snapmirrored" or "in_sync". The entries "in_sync", "out_of_sync", and "synchronizing" are only applicable to relationships with a policy of type "sync". A PATCH call on the state change only triggers the transition to the specified state. You must poll on the "state", "healthy" and "unhealthy_reason" properties using a GET request to determine if the transition is successful. To automatically initialize the relationship when specifying “create_destination”, set the state to “snapmirrored” for relationships with a policy of type "async" or "in_sync" for relationships with a policy of type "sync".

Valid choices:

* broken_off
* paused
* snapmirrored
* uninitialized
* in_sync
* out_of_sync
* synchronizing """

    transfer = fields.Nested("netapp_ontap.models.snapmirror_relationship_transfer.SnapmirrorRelationshipTransferSchema", data_key="transfer", unknown=EXCLUDE)
    r""" The transfer field of the snapmirror_relationship. """

    unhealthy_reason = fields.List(fields.Nested("netapp_ontap.models.snapmirror_error.SnapmirrorErrorSchema", unknown=EXCLUDE), data_key="unhealthy_reason")
    r""" Reason the relationship is not healthy. It is a concatenation of up to four levels of error messages.

Example: [{"code":"6621444","message":"Failed to complete update operation on one or more item relationships.","parameters":[]},{"code":"6621445","message":"Group Update failed","parameters":[]}] """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the snapmirror_relationship.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return SnapmirrorRelationship

    @property
    def patchable_fields(self):
        return [
            "destination",
            "policy",
            "preserve",
            "quick_resync",
            "recover_after_break",
            "restore_to_snapshot",
            "source",
            "state",
            "transfer",
        ]

    @property
    def postable_fields(self):
        return [
            "create_destination",
            "destination",
            "policy",
            "restore",
            "source",
            "state",
            "transfer",
        ]

class SnapmirrorRelationship(Resource):
    r""" SnapMirror relationship information """

    _schema = SnapmirrorRelationshipSchema
    _path = "/api/snapmirror/relationships"
    @property
    def _keys(self):
        return ["uuid"]

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
        r"""Retrieves information for SnapMirror relationships whose destination endpoints are in the current SVM or the current cluster, depending on the cluster context.
### Related ONTAP commands
* `snapmirror show`
* `snapmirror list-destinations`
### Examples
The following examples show how to retrieve the list of SnapMirror relationships and the list of SnapMirror destinations.
   1. Retrieving the list of SnapMirror relationships. This API must be run on the cluster containing the destination endpoint.
   <br/>
   ```
   GET "/api/snapmirror/relationships/"
   ```
   <br/>
  2.  Retrieving the list of SnapMirror destinations on source. This must be run on the cluster containing the source endpoint.
   <br/>
   ```
   GET "/api/snapmirror/relationships/?list_destinations_only=true"
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/relationships`](#docs-snapmirror-snapmirror_relationships)
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
        r"""Updates a SnapMirror relationship. This API is used to initiate SnapMirror operations such as "initialize", "resync", "break", "quiesce", and "resume" by specifying the appropriate value for the "state" field. It is also used to modify the SnapMirror policy associated with the specified relationship.
### Related ONTAP commands
* `snapmirror modify`
* `snapmirror initialize`
* `snapmirror resync`
* `snapmirror break`
* `snapmirror quiesce`
* `snapmirror resume`
### Examples
The following examples show how to perform the SnapMirror "resync", "initialize", "resume", "quiesce", and "break" operations.
<br/>
   Performing a SnapMirror "resync"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff/" '{"state":"snapmirrored"}'
   ```
   <br/>
   Performing a SnapMirror "initialize"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff/" '{"state":"snapmirrored"}'
   ```
   <br/>
   Performing a SnapMirror "resume"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff/" '{"state":"snapmirrored"}'
   ```
   <br/>
   Performing a SnapMirror "quiesce"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff" '{"state":"paused"}'
   ```
   <br/>
   Performing a SnapMirror "break"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff" '{"state":"broken_off"}'
   ```
   <br/>
   Updating an associated SnapMirror policy
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/9e922e65-1818-11e9-8b22-005056bbee73/" '{"policy": { "name" : "MirrorAndVaultDiscardNetwork"}}'
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/relationships`](#docs-snapmirror-snapmirror_relationships)
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
        r"""Deletes a SnapMirror relationship.
### Important notes
* The "destination_only", "source_only", and "source_info_only" flags are mutually exclusive. If no flag is specified, the relationship is deleted from both the source and destination and all common Snapshot copies between the source and destination are also deleted.
* For a restore relationship, the call must be executed on the cluster containing the destination endpoint without specifying the destination_only, source_only, or source_info_only parameters.
* Additionally, ensure that there are no ongoing transfers on a restore relationship before calling this API.
### Related ONTAP commands
* `snapmirror delete`
* `snapmirror release`
### Examples
The following examples show how to delete the relationship from both the source and destination, the destination only, and the source only.
<br/>
   Deleting the relationship from both the source and destination. This API must be run on the cluster containing the destination endpoint.
   <br/>
   ```
   DELETE "/api/snapmirror/relationships/4512b2d2-fd60-11e8-8929-005056bbfe52"
   ```
   <br/>
   Deleting the relationship on the destination only. This API must be run on the cluster containing the destination endpoint.
   <br/>
   ```
   DELETE "/api/snapmirror/relationships/fd1e0697-02ba-11e9-acc7-005056a7697f/?destination_only=true"
   ```
   <br/>
   Deleting the relationship on the source only. This API must be run on the cluster containing the source endpoint.
   <br/>
   ```
   DELETE "/api/snapmirror/relationships/93e828ba-02bc-11e9-acc7-005056a7697f/?source_only=true"
   ```
   <br/>
   Deleting the source information only. This API must be run on the cluster containing the source endpoint. This does not delete the common Snapshot copies between the source and destination.
   <br/>
   ```
   DELETE "/api/snapmirror/relationships/caf545a2-fc60-11e8-aa13-005056a707ff/?source_info_only=true"
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/relationships`](#docs-snapmirror-snapmirror_relationships)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves information for SnapMirror relationships whose destination endpoints are in the current SVM or the current cluster, depending on the cluster context.
### Related ONTAP commands
* `snapmirror show`
* `snapmirror list-destinations`
### Examples
The following examples show how to retrieve the list of SnapMirror relationships and the list of SnapMirror destinations.
   1. Retrieving the list of SnapMirror relationships. This API must be run on the cluster containing the destination endpoint.
   <br/>
   ```
   GET "/api/snapmirror/relationships/"
   ```
   <br/>
  2.  Retrieving the list of SnapMirror destinations on source. This must be run on the cluster containing the source endpoint.
   <br/>
   ```
   GET "/api/snapmirror/relationships/?list_destinations_only=true"
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/relationships`](#docs-snapmirror-snapmirror_relationships)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a SnapMirror relationship.
### Related ONTAP commands
* `snapmirror show`
* `snapmirror list-destinations`
### Example
<br/>
```
GET "/api/snapmirror/relationships/caf545a2-fc60-11e8-aa13-005056a707ff/"
```
<br/>
### Learn more
* [`DOC /snapmirror/relationships`](#docs-snapmirror-snapmirror_relationships)
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
        r"""Creates a SnapMirror relationship. This API can optionally provision the destination endpoint when it does not exist. This API must be executed on the cluster containing the destination endpoint unless the destination endpoint is being provisioned. When the destination endpoint is being provisioned, this API can also be executed from the cluster containing the source endpoint.
### Required properties
* `source.path` - Path to the source endpoint of the SnapMirror relationship.
* `destination.path` - Path to the destination endpoint of the SnapMirror relationship.
### Recommended optional properties
* `policy.name` or `policy.uuid` - Policy governing the SnapMirror relationship.
* `state` - Set the state to "snapmirrored" to automatically initialize the relationship.
* `create_destination.enabled` - Enable this property to provision the destination endpoint.
### Default property values
If not specified in POST, the following default property values are assigned:
* `policy.name` - _Asynchronous_
* `restore` - _false_
* `create_destination.tiering.policy` - `_snapshot_only_` (when `create_destination.tiering.supported` is _true_ for FlexVol volume)
* `create_destination.tiering.policy` - `_none_` (when `create_destination.tiering.supported` is _true_ for FlexGroup volume)
* `create_destination.storage_service.enforce_performance` - `_false_`
* `source.ipspace` - `_Default_`
* `destination.ipspace` - `_Default_`
### Related ONTAP commands
* `snapmirror create`
* `snapmirror protect`
### Examples
The following examples show how to create FlexVol, FlexGroup and SVM SnapMirror relationships. Note that the source SVM name should be the local name of the peer SVM.</br>
   Creating a FlexVol SnapMirror relationship of type XDP.
   <br/>
   ```
   POST "/api/snapmirror/relationships/" '{"source": {"path": "test_vserv_src:src_vol_rw"}, "destination": { "path": "test_vserv_dst:dst_vol_rw"}}'
   ```
   <br/>
   Creating a FlexGroup SnapMirror relationship of type XDP.
   <br/>
   ```
   POST "/api/snapmirror/relationships/" '{"source": {"path": "test_vserv_src:source_flexgrp"}, "destination": { "path": "test_vserv_dst:dest_flexgrp"}}'
   ```
   <br/>
   Creating a SVM SnapMirror relationship of type XDP.
   <br/>
   ```
   POST "/api/snapmirror/relationships/" '{"source": { "path": "src_svm:"}, "destination": { "path": "dst_svm:"}}'
   ```
   <br/>
   Creating a SnapMirror relationship in order to restore from a destination.
   <br/>
   ```
   POST "/api/snapmirror/relationships/" '{"source": {"path": "test_vserv_src:src_vol_rw"}, "destination": { "path": "test_vserv_dst:dst_vol_rw"}, "restore": "true"}'
   ```
   <br/>
   Creating a FlexVol SnapMirror relationship of type XDP.
   <br/>
   ```
   POST "/api/snapmirror/relationships/" '{"source": {"path": "test_vserv_src:src_vol_rw"}, "destination": { "path": "test_vserv_dst:dst_vol_rw"}, "create_destination": { "enable": "true" }}'
   ```
   <br/>
   ```
   POST "/api/snapmirror/relationships/" '{"source": {"path": "test_vserv_src:src_vol_rw"}, "destination": { "path": "test_vserv_dst:dst_vol_rw"}, "create_destination": { "enable": "true", "tiering": { "supported": "true", "policy": "auto" } } }'
   ```
   <br/>
   ```
   POST "/api/snapmirror/relationships/" '{"source": {"path": "test_vserv_src:src_vol_rw"}, "destination": { "path": "test_vserv_dst:dst_vol_rw"}, "create_destination": { "enable": "true", "storage_service": { "enabled": "true", "name": "extreme", "enforce_performance": "true" } } }'
   ```
   <br/>
   ```
   POST "/api/snapmirror/relationships/" '{"source": {"path": "src_svm:", "cluster": { "name": "cluster_src" }}, "destination": { "path": "dst_svm:"}, "create_destination": { "enable": "true" }}'
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/relationships`](#docs-snapmirror-snapmirror_relationships)
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
        r"""Updates a SnapMirror relationship. This API is used to initiate SnapMirror operations such as "initialize", "resync", "break", "quiesce", and "resume" by specifying the appropriate value for the "state" field. It is also used to modify the SnapMirror policy associated with the specified relationship.
### Related ONTAP commands
* `snapmirror modify`
* `snapmirror initialize`
* `snapmirror resync`
* `snapmirror break`
* `snapmirror quiesce`
* `snapmirror resume`
### Examples
The following examples show how to perform the SnapMirror "resync", "initialize", "resume", "quiesce", and "break" operations.
<br/>
   Performing a SnapMirror "resync"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff/" '{"state":"snapmirrored"}'
   ```
   <br/>
   Performing a SnapMirror "initialize"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff/" '{"state":"snapmirrored"}'
   ```
   <br/>
   Performing a SnapMirror "resume"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff/" '{"state":"snapmirrored"}'
   ```
   <br/>
   Performing a SnapMirror "quiesce"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff" '{"state":"paused"}'
   ```
   <br/>
   Performing a SnapMirror "break"
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/98bb2608-fc60-11e8-aa13-005056a707ff" '{"state":"broken_off"}'
   ```
   <br/>
   Updating an associated SnapMirror policy
   <br/>
   ```
   PATCH "/api/snapmirror/relationships/9e922e65-1818-11e9-8b22-005056bbee73/" '{"policy": { "name" : "MirrorAndVaultDiscardNetwork"}}'
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/relationships`](#docs-snapmirror-snapmirror_relationships)
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
        r"""Deletes a SnapMirror relationship.
### Important notes
* The "destination_only", "source_only", and "source_info_only" flags are mutually exclusive. If no flag is specified, the relationship is deleted from both the source and destination and all common Snapshot copies between the source and destination are also deleted.
* For a restore relationship, the call must be executed on the cluster containing the destination endpoint without specifying the destination_only, source_only, or source_info_only parameters.
* Additionally, ensure that there are no ongoing transfers on a restore relationship before calling this API.
### Related ONTAP commands
* `snapmirror delete`
* `snapmirror release`
### Examples
The following examples show how to delete the relationship from both the source and destination, the destination only, and the source only.
<br/>
   Deleting the relationship from both the source and destination. This API must be run on the cluster containing the destination endpoint.
   <br/>
   ```
   DELETE "/api/snapmirror/relationships/4512b2d2-fd60-11e8-8929-005056bbfe52"
   ```
   <br/>
   Deleting the relationship on the destination only. This API must be run on the cluster containing the destination endpoint.
   <br/>
   ```
   DELETE "/api/snapmirror/relationships/fd1e0697-02ba-11e9-acc7-005056a7697f/?destination_only=true"
   ```
   <br/>
   Deleting the relationship on the source only. This API must be run on the cluster containing the source endpoint.
   <br/>
   ```
   DELETE "/api/snapmirror/relationships/93e828ba-02bc-11e9-acc7-005056a7697f/?source_only=true"
   ```
   <br/>
   Deleting the source information only. This API must be run on the cluster containing the source endpoint. This does not delete the common Snapshot copies between the source and destination.
   <br/>
   ```
   DELETE "/api/snapmirror/relationships/caf545a2-fc60-11e8-aa13-005056a707ff/?source_info_only=true"
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/relationships`](#docs-snapmirror-snapmirror_relationships)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


