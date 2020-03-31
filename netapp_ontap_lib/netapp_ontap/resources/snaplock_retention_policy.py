# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

An event retention policy consists of a policy-name and a retention-period. The policy can be applied to a single file or files in a directory. Only a user with the security login role vsadmin-snaplock can perform the operation. EBR policies cannot be applied to files under a Legal-Hold.
### Examples
1. Creates an EBR policy policy_name with a retention period of "10 years":
   <br/>
   ```
   POST "/api/storage/snaplock/event-retention/policies/" '{"name": "policy_name","retention_period": "P10Y"}'
   ```
   <br/>
2. Creates an EBR policy policy_name1 with a retention period of "infinite":
   <br/>
   ```
   POST "/api/storage/snaplock/event-retention/policies/" '{"name": "policy_name1","retention_period": "infinite"}'
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


__all__ = ["SnaplockRetentionPolicy", "SnaplockRetentionPolicySchema"]
__pdoc__ = {
    "SnaplockRetentionPolicySchema.resource": False,
    "SnaplockRetentionPolicySchema.patchable_fields": False,
    "SnaplockRetentionPolicySchema.postable_fields": False,
}


class SnaplockRetentionPolicySchema(ResourceSchema):
    """The fields of the SnaplockRetentionPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snaplock_retention_policy. """

    name = fields.Str(
        data_key="name",
    )
    r""" Specifies the EBR policy name """

    retention_period = fields.Str(
        data_key="retention_period",
    )
    r""" Specifies the retention period of an EBR policy. The retention period value represents a duration and must be specified in the ISO-8601 duration format. The retention period can be in years, months, days, hours or minutes. A period specified for years, months and days is represented in the ISO-8601 format as "P<num>Y", "P<num>M", "P<num>D" respectively. For example "P10Y" represents a duration of 10 years. Similarly, a duration in hours, minutes is represented by "PT<num>H", "PT<num>M" respectively. The period string must contain only a single time element i.e. either years, months, days, hours or minutes. A duration which combines different periods is not supported, example "P1Y10M" is not supported. Apart from the duration specified in the ISO-8601 format, the retention period field also accepts the string "infinite".

Example: P30M """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the snaplock_retention_policy. """

    @property
    def resource(self):
        return SnaplockRetentionPolicy

    @property
    def patchable_fields(self):
        return [
            "name",
            "retention_period",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "retention_period",
            "svm.name",
            "svm.uuid",
        ]

class SnaplockRetentionPolicy(Resource):
    """Allows interaction with SnaplockRetentionPolicy objects on the host"""

    _schema = SnaplockRetentionPolicySchema
    _path = "/api/storage/snaplock/event-retention/policies"
    @property
    def _keys(self):
        return ["policy.name"]

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
        r"""Retrieves all event retention policies for an SVM.
### Related ONTAP commands
* `snaplock event-retention policy show`
### Learn more
* [`DOC /storage/snaplock/event-retention/policies`](#docs-snaplock-storage_snaplock_event-retention_policies)
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
        r"""Updates the retention period of an Event Based Retention (EBR) policy.
### Related ONTAP commands
* `snaplock event-retention policy modify`
### Example
Updates the retention period of an EBR policy "policy_name":
<br/>
```
PATCH "/api/storage/snaplock/event-retention/policies/" '{"name": "policy_name","retention_period": "P20Y"}'
```
<br/>
### Learn more
* [`DOC /storage/snaplock/event-retention/policies`](#docs-snaplock-storage_snaplock_event-retention_policies)
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
        r"""Deletes the specified Event Based Retention (EBR) policy.
### Related ONTAP commands
* `snaplock event-retention policy delete`
### Learn more
* [`DOC /storage/snaplock/event-retention/policies`](#docs-snaplock-storage_snaplock_event-retention_policies)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves all event retention policies for an SVM.
### Related ONTAP commands
* `snaplock event-retention policy show`
### Learn more
* [`DOC /storage/snaplock/event-retention/policies`](#docs-snaplock-storage_snaplock_event-retention_policies)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a list of attributes of the specified Event Based Retention (EBR) policy.
### Related ONTAP commands
* `snaplock event-retention policy show`
### Learn more
* [`DOC /storage/snaplock/event-retention/policies`](#docs-snaplock-storage_snaplock_event-retention_policies)
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
        r"""Creates an Event Based Retention (EBR) policy for an SVM. The input parameter retention_period expects the duration in ISO 8601 format or infinite.
### Required properties
* `name` - Event retention policy name.
* `retention_period` - Retention period of the EBR policy.
### Related ONTAP commands
* `snaplock event-retention policy create`
### Learn more
* [`DOC /storage/snaplock/event-retention/policies`](#docs-snaplock-storage_snaplock_event-retention_policies)
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
        r"""Updates the retention period of an Event Based Retention (EBR) policy.
### Related ONTAP commands
* `snaplock event-retention policy modify`
### Example
Updates the retention period of an EBR policy "policy_name":
<br/>
```
PATCH "/api/storage/snaplock/event-retention/policies/" '{"name": "policy_name","retention_period": "P20Y"}'
```
<br/>
### Learn more
* [`DOC /storage/snaplock/event-retention/policies`](#docs-snaplock-storage_snaplock_event-retention_policies)
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
        r"""Deletes the specified Event Based Retention (EBR) policy.
### Related ONTAP commands
* `snaplock event-retention policy delete`
### Learn more
* [`DOC /storage/snaplock/event-retention/policies`](#docs-snaplock-storage_snaplock_event-retention_policies)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


