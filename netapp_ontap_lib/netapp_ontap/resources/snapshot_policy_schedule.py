# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
In ONTAP, scheduled Snapshot copy creation works based on the schedules associated with Snapshot copy policies.
ONTAP provides six cluster-wide schedules: "5min", "8hour", "hourly", "daily", "weekly" and "monthly".
A Snapshot copy policy is created using at least one of these schedules and up to 5 schedules can be associated with a Snapshot copy policy.
A Snapshot copy policy can be linked to a storage object and based on the schedule in the policy, Snapshot copies are created on the object at that interval.
Each schedule in a Snapshot copy policy has a Snapshot copy name prefix attached to it. Every Snapshot copy created using this policy has this prefix in its name.
There is also a retention count associated with every schedule. This count indicates the maximum number of Snapshot copies that can exist for a given schedule.
Once the Snapshot copy count reaches the retention count, on the next create operation, the oldest Snapshot copy is deleted.
A schedule can be added, modified or deleted from a Snapshot copy policy.<br/>
## Snapshot copy policy schedule APIs
The following APIs are used to perform operations related to Snapshot copy policy schedules:

* POST      /api/storage/snapshot-policies/{snapshot-policy.uuid}/schedules/
* GET       /api/storage/snapshot-policies/{snapshot-policy.uuid}/schedules/
* GET       /api/storage/snapshot-policies/{snapshot-policy.uuid}/schedules/{uuid}
* PATCH     /api/storage/snapshot-policies/{snapshot-policy.uuid}/schedules/{uuid}
* DELETE    /api/storage/snapshot-policies/{snapshot-policy.uuid}/schedules/{uuid}
## Examples
### Adding schedule to a Snapshot copy policy
The POST operation is used to create a schedule for a Snapshot copy policy with the specified attributes.
```
# The API:
/api/storage/snapshot-policies/{snapshot-policy.uuid}/schedules/
# The call:
curl -X POST  "https://<mgmt-ip>/api/storage/snapshot-policies/32a0841a-818e-11e9-b4f4-005056bbab9c/schedules" -H "accept: application/hal+json" -d '{"schedule.uuid": "7c985d80-818a-11e9-b4f4-005056bbab9c", "count": "5", "prefix": "new_hourly" }'
# The response:
HTTP/1.1 201 Created
Date: Wed, 29 May 2019 22:41:33 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/storage/snapshot-policies/32a0841a-818e-11e9-b4f4-005056bbab9c/schedules
Content-Length: 271
Content-Type: application/json
{
  "num_records": 1,
  "records": [
    {
      "snapshot_policy": {
        "uuid": "32a0841a-818e-11e9-b4f4-005056bbab9c"
      },
      "schedule": {
        "uuid": "7c985d80-818a-11e9-b4f4-005056bbab9c"
      },
      "count": 5,
      "prefix": "new_monthly"
    }
  ]
}
```
### Retrieving Snapshot copy policy schedules
The GET operation is used to retrieve Snapshot copy policy schedules.
```
# The API:
/api/storage/snapshot-policies/{snapshot-policy.uuid}/schedules/
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/snapshot-policies/32a0841a-818e-11e9-b4f4-005056bbab9c/schedules" -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Wed, 29 May 2019 22:49:58 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 898
Content-Type: application/json
{
  "records": [
    {
      "snapshot_policy": {
        "uuid": "32a0841a-818e-11e9-b4f4-005056bbab9c"
      },
      "schedule": {
        "uuid": "63d017dc-818a-11e9-b4f4-005056bbab9c",
        "name": "5min"
      }
    },
    {
      "snapshot_policy": {
        "uuid": "32a0841a-818e-11e9-b4f4-005056bbab9c"
      },
      "schedule": {
        "uuid": "64a5c5da-818a-11e9-b4f4-005056bbab9c",
        "name": "8hour"
      }
    },
    {
      "snapshot_policy": {
        "uuid": "32a0841a-818e-11e9-b4f4-005056bbab9c"
      },
      "schedule": {
        "uuid": "63e21a3e-818a-11e9-b4f4-005056bbab9c",
        "name": "daily"
      }
    },
    {
      "snapshot_policy": {
        "uuid": "32a0841a-818e-11e9-b4f4-005056bbab9c"
      },
      "schedule": {
        "uuid": "7c985d80-818a-11e9-b4f4-005056bbab9c",
        "name": "monthly"
      }
    }
  ],
  "num_records": 4
}
```
### Retrieving the attributes of a specific Snapshot copy policy schedule
The GET operation is used to retrieve the attributes of a specific Snapshot copy policy schedule.
```
# The API:
/api/storage/snapshot-policies/{uuid}/schedules/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/snapshot-policies/32a0841a-818e-11e9-b4f4-005056bbab9c/schedules/7c985d80-818a-11e9-b4f4-005056bbab9c" -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Wed, 29 May 2019 22:54:06 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 238
Content-Type: application/json
{
  "snapshot_policy": {
    "uuid": "32a0841a-818e-11e9-b4f4-005056bbab9c"
  },
  "schedule": {
    "uuid": "7c985d80-818a-11e9-b4f4-005056bbab9c",
    "name": "monthly"
  },
  "count": 5,
  "prefix": "new_monthly",
  "snapmirror_label": "-"
}
```
### Updating a Snapshot copy policy schedule
The PATCH operation is used to update the specific attributes of a Snapshot copy policy.
```
# The API:
/api/storage/snapshot-policies/{uuid}/schedules/{uuid}
# The call:
  curl -X PATCH  "https://<mgmt-ip>/api/storage/snapshot-policies/32a0841a-818e-11e9-b4f4-005056bbab9c/schedules/7c985d80-818a-11e9-b4f4-005056bbab9c" -d '{"count": "10" }' -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Wed, 29 May 2019 23:08:00 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 3
Content-Type: application/json
```
### Deleting a Snapshot copy policy
The DELETE operation is used to delete a Snapshot copy policy.
```
# The API:
/api/storage/snapshot-policies/{uuid}/schedules/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/storage/snapshot-policies/32a0841a-818e-11e9-b4f4-005056bbab9c/schedules/7c985d80-818a-11e9-b4f4-005056bbab9c" -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Wed, 29 May 2019 23:12:32 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 3
Content-Type: application/json
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnapshotPolicySchedule", "SnapshotPolicyScheduleSchema"]
__pdoc__ = {
    "SnapshotPolicyScheduleSchema.resource": False,
    "SnapshotPolicyScheduleSchema.patchable_fields": False,
    "SnapshotPolicyScheduleSchema.postable_fields": False,
}


class SnapshotPolicyScheduleSchema(ResourceSchema):
    """The fields of the SnapshotPolicySchedule object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snapshot_policy_schedule. """

    count = fields.Integer(
        data_key="count",
    )
    r""" The number of Snapshot copies to maintain for this schedule. """

    prefix = fields.Str(
        data_key="prefix",
    )
    r""" The prefix to use while creating Snapshot copies at regular intervals. """

    schedule = fields.Nested("netapp_ontap.resources.schedule.ScheduleSchema", data_key="schedule", unknown=EXCLUDE)
    r""" The schedule field of the snapshot_policy_schedule. """

    snapmirror_label = fields.Str(
        data_key="snapmirror_label",
    )
    r""" Label for SnapMirror operations """

    snapshot_policy = fields.Nested("netapp_ontap.resources.snapshot_policy.SnapshotPolicySchema", data_key="snapshot_policy", unknown=EXCLUDE)
    r""" The snapshot_policy field of the snapshot_policy_schedule. """

    @property
    def resource(self):
        return SnapshotPolicySchedule

    @property
    def patchable_fields(self):
        return [
            "count",
            "schedule.name",
            "schedule.uuid",
            "snapmirror_label",
            "snapshot_policy.name",
            "snapshot_policy.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "count",
            "prefix",
            "schedule.name",
            "schedule.uuid",
            "snapmirror_label",
            "snapshot_policy.name",
            "snapshot_policy.uuid",
        ]

class SnapshotPolicySchedule(Resource):
    r""" The Snapshot copy policy schedule object is associated with a Snapshot copy policy and it defines the interval at which Snapshot copies are created and deleted. """

    _schema = SnapshotPolicyScheduleSchema
    _path = "/api/storage/snapshot-policies/{snapshot-policy[uuid]}/schedules"
    @property
    def _keys(self):
        return ["snapshot-policy.uuid", "uuid"]

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
        r"""Retrieves a collection of Snapshot copy policy schedules.
### Related ONTAP commands
* `snapshot policy show`
### Learn more
* [`DOC /storage/snapshot-policies/{snapshot-policy.uuid}/schedules`](#docs-storage-storage_snapshot-policies_{snapshot-policy.uuid}_schedules)
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
        r"""Updates a Snapshot copy policy schedule
### Related ONTAP commands
* `snapshot policy modify-schedule`
### Learn more
* [`DOC /storage/snapshot-policies/{snapshot-policy.uuid}/schedules`](#docs-storage-storage_snapshot-policies_{snapshot-policy.uuid}_schedules)
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
        r"""Deletes a schedule from a Snapshot copy policy
### Related ONTAP commands
* `snapshot policy remove-schedule`
### Learn more
* [`DOC /storage/snapshot-policies/{snapshot-policy.uuid}/schedules`](#docs-storage-storage_snapshot-policies_{snapshot-policy.uuid}_schedules)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of Snapshot copy policy schedules.
### Related ONTAP commands
* `snapshot policy show`
### Learn more
* [`DOC /storage/snapshot-policies/{snapshot-policy.uuid}/schedules`](#docs-storage-storage_snapshot-policies_{snapshot-policy.uuid}_schedules)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves details of a specific Snapshot copy policy schedule.
### Related ONTAP commands
* `snapshot policy show`
### Learn more
* [`DOC /storage/snapshot-policies/{snapshot-policy.uuid}/schedules`](#docs-storage-storage_snapshot-policies_{snapshot-policy.uuid}_schedules)
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
        r"""Adds a schedule to a Snapshot copy policy.
### Required properties
* `schedule.uuid` or `schedule.name` - Schedule at which Snapshot copies are captured on the volume.
* `count` - Number of Snapshot copies to maintain for this schedule.
### Recommended optional properties
* `prefix` - Prefix to use when creating Snapshot copies at regular intervals.
### Default property values
If not specified in POST, the following default property values are assigned:
* `prefix` - Value of `schedule.name`
### Related ONTAP commands
* `snapshot policy add-schedule`
### Learn more
* [`DOC /storage/snapshot-policies/{snapshot-policy.uuid}/schedules`](#docs-storage-storage_snapshot-policies_{snapshot-policy.uuid}_schedules)
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
        r"""Updates a Snapshot copy policy schedule
### Related ONTAP commands
* `snapshot policy modify-schedule`
### Learn more
* [`DOC /storage/snapshot-policies/{snapshot-policy.uuid}/schedules`](#docs-storage-storage_snapshot-policies_{snapshot-policy.uuid}_schedules)
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
        r"""Deletes a schedule from a Snapshot copy policy
### Related ONTAP commands
* `snapshot policy remove-schedule`
### Learn more
* [`DOC /storage/snapshot-policies/{snapshot-policy.uuid}/schedules`](#docs-storage-storage_snapshot-policies_{snapshot-policy.uuid}_schedules)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


