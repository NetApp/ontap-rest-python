# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Managing SnapMirror policies
This API is used to manage SnapMirror policies of type "mirror-vault", "sync-mirror" and "strict-sync-mirror". When applied to a SnapMirror relationship, the SnapMirror policy controls the behavior of the relationship and specifies the configuration attributes for that relationship.<br/>
Mapping of SnapMirror policies from CLI to REST
| CLI                | REST                |
|--------------------|---------------------|
|mirror-vault        | async               |
|                    |       |  sync_type  |
|                    |       |-------------|
|sync-mirror         | sync  |  sync       |
|strict-sync-mirror  | sync  | strict_sync |
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnapmirrorPolicy", "SnapmirrorPolicySchema"]
__pdoc__ = {
    "SnapmirrorPolicySchema.resource": False,
    "SnapmirrorPolicySchema.patchable_fields": False,
    "SnapmirrorPolicySchema.postable_fields": False,
}


class SnapmirrorPolicySchema(ResourceSchema):
    """The fields of the SnapmirrorPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snapmirror_policy. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" Comment associated with the policy. """

    identity_preservation = fields.Str(
        data_key="identity_preservation",
        validate=enum_validation(['full', 'exclude_network_config', 'exclude_network_and_protocol_config']),
    )
    r""" Specifies which configuration of the source SVM is replicated to the destination. This property is applicable only for SVM data protection and async policies.

Valid choices:

* full
* exclude_network_config
* exclude_network_and_protocol_config """

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the snapmirror_policy.

Example: Asynchronous """

    network_compression_enabled = fields.Boolean(
        data_key="network_compression_enabled",
    )
    r""" Specifies whether network compression is enabled for transfers. This is applicable only to async policies. """

    retention = fields.List(fields.Nested("netapp_ontap.models.snapmirror_policy_rule.SnapmirrorPolicyRuleSchema", unknown=EXCLUDE), data_key="retention")
    r""" Policy on Snapshot copy retention. This is applicable only to async policies. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" for policies owned by an SVM, otherwise set to "cluster".

Valid choices:

* svm
* cluster """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the snapmirror_policy. """

    sync_common_snapshot_schedule = fields.Nested("netapp_ontap.resources.schedule.ScheduleSchema", data_key="sync_common_snapshot_schedule", unknown=EXCLUDE)
    r""" The sync_common_snapshot_schedule field of the snapmirror_policy. """

    sync_type = fields.Str(
        data_key="sync_type",
        validate=enum_validation(['sync', 'strict_sync', 'active_sync']),
    )
    r""" The sync_type field of the snapmirror_policy.

Valid choices:

* sync
* strict_sync
* active_sync """

    throttle = fields.Integer(
        data_key="throttle",
    )
    r""" Throttle in KB/s. Default to unlimited. """

    transfer_schedule = fields.Nested("netapp_ontap.resources.schedule.ScheduleSchema", data_key="transfer_schedule", unknown=EXCLUDE)
    r""" The transfer_schedule field of the snapmirror_policy. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['async', 'sync']),
    )
    r""" The type field of the snapmirror_policy.

Valid choices:

* async
* sync """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the snapmirror_policy.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return SnapmirrorPolicy

    @property
    def patchable_fields(self):
        return [
            "comment",
            "identity_preservation",
            "network_compression_enabled",
            "retention",
            "sync_common_snapshot_schedule.name",
            "sync_common_snapshot_schedule.uuid",
            "throttle",
            "transfer_schedule.name",
            "transfer_schedule.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "comment",
            "identity_preservation",
            "name",
            "network_compression_enabled",
            "retention",
            "svm.name",
            "svm.uuid",
            "sync_common_snapshot_schedule.name",
            "sync_common_snapshot_schedule.uuid",
            "sync_type",
            "throttle",
            "transfer_schedule.name",
            "transfer_schedule.uuid",
            "type",
        ]

class SnapmirrorPolicy(Resource):
    r""" SnapMirror policy information """

    _schema = SnapmirrorPolicySchema
    _path = "/api/snapmirror/policies"
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
        r"""Retrieves SnapMirror policies of type "mirror-vault", "sync-mirror" and "strict-sync-mirror".
### Related ONTAP commands
* `snapmirror policy show`
### Example
The following example shows how to retrieve a collection of SnapMirror policies.
<br/>
```
GET "/api/storage/snapmirror/policies"
```
<br/>
### Learn more
* [`DOC /snapmirror/policies`](#docs-snapmirror-snapmirror_policies)
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
        r"""Updates the SnapMirror policy.
### Important notes
* The properties "transfer_schedule" and "throttle" can be modified only if all the SnapMirror relationships associated with the specified SnapMirror policy have the same values.
* The properties "retention.label" and "retention.count" are mandatory if "retention" is provided in the input. The provided "retention.label" is the final list and is replaced with the existing values.
* The value of the "identity_preservation" property cannot be changed if the SnapMirror relationships associated with the policy have different identity_preservation configurations.
* If the SnapMirror policy "identity_preservation" value matches the "identity_preservation" value of the associated SnapMirror relationships, then the "identity_preservation" value can be changed from a higher "identity_preservation" threshold value to a lower "identity_preservation" threshold value but not vice-versa. For example, the threshold value of the "identity_preservation" property can be changed from "full" to "exclude_network_config" to "exclude_network_and_protocol_config", but could not be increased from "exclude_network_and_protocol_config" to "exclude_network_config" to "full".<br/>
### Related ONTAP commands
* `snapmirror policy modify`
### Example
  Updating the "retention" property
   <br/>
   ```
   PATCH "/api/snapmirror/policies/fe65686d-00dc-11e9-b5fb-0050568e3f83" '{"retention" : {"label" : ["sm_created", "lab2"], "count": ["1","2"], "creation_schedule": {"name": ["weekly"]}}}'
   ```
   <br/>
  Updating "transfer_schedule", "throttle", and "identity_preservation" properties
   <br/>
   ```
   PATCH "/api/snapmirror/policies/8aef950b-3bef-11e9-80ac-0050568ea591" '{"transfer_schedule.name" : "weekly", "throttle" : "100", "identity_preservation":"exclude_network_and_protocol_config"}'
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/policies`](#docs-snapmirror-snapmirror_policies)
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
        r"""Deletes a SnapMirror policy.
### Related ONTAP commands
* `snapmirror policy delete`
### Example
<br/>
```
DELETE "/api/snapmirror/policies/510c15d4-f9e6-11e8-bdb5-0050568e12c2"
```
<br/>
### Learn more
* [`DOC /snapmirror/policies`](#docs-snapmirror-snapmirror_policies)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves SnapMirror policies of type "mirror-vault", "sync-mirror" and "strict-sync-mirror".
### Related ONTAP commands
* `snapmirror policy show`
### Example
The following example shows how to retrieve a collection of SnapMirror policies.
<br/>
```
GET "/api/storage/snapmirror/policies"
```
<br/>
### Learn more
* [`DOC /snapmirror/policies`](#docs-snapmirror-snapmirror_policies)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific SnapMirror policy.
### Example
<br/>
```
GET "/api/snapmirror/policies/567aaac0-f863-11e8-a666-0050568e12c2"
```
<br/>
### Learn more
* [`DOC /snapmirror/policies`](#docs-snapmirror-snapmirror_policies)
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
        r"""Creates a SnapMirror policy. The property "identity_preservation" is applicable to only SnapMirror relationships with SVM endpoints and it indicates which configuration of the source SVM is replicated to the destination SVM.</br>
It takes the following values:
- `full` - indicates that the source SVM configuration is replicated to the destination SVM endpoint.
- `exclude_network_config` - indicates that the source SVM configuration other than network configuration is replicated to the destination SVM endpoint.
- `exclude_network_and_protocol_config` - indicates that the source SVM configuration is not replicated to the destination SVM endpoint.<br/>
### Important note
- The property "identity_preservation" is applicable to only SnapMirror relationships with SVM endpoints and it indicates which configuration of the source SVM is replicated to the destination SVM.
- The properties "identity_preservation", "retention" and "transfer_schedule" are not applicable for "sync" type policies.
- The property "sync_common_snapshot_schedule" is not applicable for an "async" type policy.
- The property "retention.count" specifies the maximum number of Snapshot copies that are retained on the SnapMirror destination volume.
- When the property "retention.label" is specified, the Snapshot copies that have a SnapMirror label matching this property is transferred to the SnapMirror destination.
- When the property "retention.creation_schedule" is specified, Snapshot copies are directly created on the SnapMirror destination. The Snapshot copies created have the same content as the latest Snapshot copy already present on the SnapMirror destination.
### Required properties
* `name` - Name of the new SnapMirror policy.
### Recommended optional properties
* `svm.name` or `svm.uuid` - Name or UUID of the SVM that owns the SnapMirror policy.
### Default property values
If not specified in POST, the following default property values are assigned:
* `type` - _async_
* `sync_type` - _sync_ (when `type` is _sync_)
* `network_compression_enabled` - _false_
* `throttle` - _0_
* `identity_preservation` - `_exclude_network_and_protocol_config_`
### Related ONTAP commands
* `snapmirror policy create`
### Examples
  Creating a SnapMirror policy of type "sync"
   <br/>
   ```
   POST "/api/snapmirror/policies/" '{"name": "policy1", "svm.name": "VS0", "type": "sync", "sync_type": "sync"}'
   ```
   <br/>
  Creating a SnapMirror policy of type "async" with retention values
   <br/>
   ```
   POST "/api/snapmirror/policies" '{"name": "policy_ret", "svm": {"name": "vs1"}, "retention": {"label": ["smcreate"], "count": ["2"], "creation_schedule": ["weekly"]}}'
   ```
   <br/>
  Creating a SnapMirror policy of type "async"
   ```
   POST "/api/snapmirror/policies" '{"name": "newPolicy", "svm":{"name" : "vs1"}, "type": "async"}'
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/policies`](#docs-snapmirror-snapmirror_policies)
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
        r"""Updates the SnapMirror policy.
### Important notes
* The properties "transfer_schedule" and "throttle" can be modified only if all the SnapMirror relationships associated with the specified SnapMirror policy have the same values.
* The properties "retention.label" and "retention.count" are mandatory if "retention" is provided in the input. The provided "retention.label" is the final list and is replaced with the existing values.
* The value of the "identity_preservation" property cannot be changed if the SnapMirror relationships associated with the policy have different identity_preservation configurations.
* If the SnapMirror policy "identity_preservation" value matches the "identity_preservation" value of the associated SnapMirror relationships, then the "identity_preservation" value can be changed from a higher "identity_preservation" threshold value to a lower "identity_preservation" threshold value but not vice-versa. For example, the threshold value of the "identity_preservation" property can be changed from "full" to "exclude_network_config" to "exclude_network_and_protocol_config", but could not be increased from "exclude_network_and_protocol_config" to "exclude_network_config" to "full".<br/>
### Related ONTAP commands
* `snapmirror policy modify`
### Example
  Updating the "retention" property
   <br/>
   ```
   PATCH "/api/snapmirror/policies/fe65686d-00dc-11e9-b5fb-0050568e3f83" '{"retention" : {"label" : ["sm_created", "lab2"], "count": ["1","2"], "creation_schedule": {"name": ["weekly"]}}}'
   ```
   <br/>
  Updating "transfer_schedule", "throttle", and "identity_preservation" properties
   <br/>
   ```
   PATCH "/api/snapmirror/policies/8aef950b-3bef-11e9-80ac-0050568ea591" '{"transfer_schedule.name" : "weekly", "throttle" : "100", "identity_preservation":"exclude_network_and_protocol_config"}'
   ```
   <br/>
### Learn more
* [`DOC /snapmirror/policies`](#docs-snapmirror-snapmirror_policies)
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
        r"""Deletes a SnapMirror policy.
### Related ONTAP commands
* `snapmirror policy delete`
### Example
<br/>
```
DELETE "/api/snapmirror/policies/510c15d4-f9e6-11e8-bdb5-0050568e12c2"
```
<br/>
### Learn more
* [`DOC /snapmirror/policies`](#docs-snapmirror-snapmirror_policies)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


