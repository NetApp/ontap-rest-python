# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
You can  use the /cluster/schedules API to view, create, and modify job schedules in a cluster.
## Retrieving a job schedule
You can retrieve job schedules by issuing a GET request to /cluster/schedules. It is also possible to retrieve a specific schedule when qualified by its UUID to /cluster/schedules/{uuid}. You can apply queries on fields to retrieve all schedules that match the combined query.
### Example
```
# The API:
/api/cluster/schedules/
# The call:
curl -X GET 'https://<mgmt-ip>/api/cluster/schedules?type=interval'
# The response:
{
  "records": [
    {
      "uuid": "08ceae53-0158-11e9-a82c-005056bb4301",
      "name": "RepositoryBalanceMonitorJobSchedule",
      "type": "interval",
      "interval": "PT10M",
      "_links": {
        "self": {
          "href": "/api/cluster/schedules/08ceae53-0158-11e9-a82c-005056bb4301"
        }
      }
    },
    {
      "uuid": "0941e980-0158-11e9-a82c-005056bb4301",
      "name": "Balanced Placement Model Cache Update",
      "type": "interval",
      "interval": "PT7M30S",
      "_links": {
        "self": {
          "href": "/api/cluster/schedules/0941e980-0158-11e9-a82c-005056bb4301"
        }
      }
    },
    {
      "uuid": "0944b975-0158-11e9-a82c-005056bb4301",
      "name": "Auto Balance Aggregate Scheduler",
      "type": "interval",
      "interval": "PT1H",
      "_links": {
        "self": {
          "href": "/api/cluster/schedules/0944b975-0158-11e9-a82c-005056bb4301"
        }
      }
    },
    {
      "uuid": "0c65f1fb-0158-11e9-a82c-005056bb4301",
      "name": "Application Templates ASUP Dump",
      "type": "interval",
      "interval": "P1D",
      "_links": {
        "self": {
          "href": "/api/cluster/schedules/0c65f1fb-0158-11e9-a82c-005056bb4301"
        }
      }
    }
  ],
  "num_records": 4,
  "_links": {
    "self": {
      "href": "/api/cluster/schedules?type=interval"
    }
  }
}
```
```
# The API:
/api/cluster/schedules/{uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/cluster/schedules/25312bd8-0158-11e9-a82c-005056bb4301'
# The response:
{
  "uuid": "25312bd8-0158-11e9-a82c-005056bb4301",
  "name": "monthly",
  "cluster": {
    "name": "rodan-tsundere",
    "uuid": "f3f9bbfa-0157-11e9-a82c-005056bb4301"
  },
  "type": "cron",
  "cron": {
    "minutes": [
      20
    ],
    "hours": [
      0
    ],
    "days": [
      1
    ]
  },
  "_links": {
    "self": {
      "href": "/api/cluster/schedules/25312bd8-0158-11e9-a82c-005056bb4301"
    }
  }
}
```
---
## Creating a job schedule
You can create a job schedule by issuing a POST request to /cluster/schedules to a node in the cluster. For a successful request, the POST request returns a status code of 201.
Job schedules can be of either type "cron" or type "interval". A cron schedule is run at specific minutes within the hour, or hours of the day, days of the week, days of the month, or months of the year. An interval schedule runs repeatedly at fixed intervals.
### Required fields

* name - Name of the job schedule
You are required to provide a "minutes" field for a cron schedule. An "interval" field is required for an interval schedule. Do not provide both a "cron" field and an "interval" field.
The schedule UUID is created by the system.
### Cron schedule fields

* cron.minutes - Minutes within the hour (0 through 59)
* cron.hours -  Hours of the day (0 through 23)
* cron.weekdays - Weekdays (0 through 6, where 0 is Sunday and 6 is Saturday.)
* cron.days - Days of the month (1 through 31)
* cron.months - Months of the year (1 through 12)
### Interval schedule field

* interval - Length of time in ISO 8601 duration format.
### Example
```
# The API:
/api/cluster/schedules
# The call:
curl -X POST "https://<mgmt-ip>/api/cluster/schedules" -d body
# The response of a successful POST is empty.
Example body to create an interval schedule with a 1-week interval:
{
    "name": "test_interval_1",
    "interval": "P1W"
}
Example body to create a cron schedule that runs daily at 12:05 :
{
    "name": "test_cron_1",
    "cron":
    {
        "minutes": [ 5 ],
        "hours": [ 12 ]
    }
}
```
### Optional fields
By default, the schedule is owned by the local cluster. In a MetroCluster configuration, you can specify the partner cluster if the local cluster is in the switchover state.

* cluster.name - Name of the cluster owning the schedule.
* cluster.uuid - UUID of the cluster owning the schedule.
### Records field
You can create multiple schedules in one request by providing an array of named records with schedule entries. Each entry must follow the required and optional fields listed above.
<br/>
---
## Updating a job schedule
The following fields of an existing schedule can be modified:

* cron.minutes
* cron.hours
* cron.weekdays
* cron.days
* cron.months
* interval
Note that you cannot modify the name, cluster, and type of schedule. Also, you cannot modify a cron field of an interval schedule, or the interval field of a cron schedule. You can apply queries on fields to modify all schedules that match the combined query.
### Example
```
# The API:
/api/cluster/schedules/{uuid}
# The call:
curl  -X PATCH "https://<mgmt-ip>/api/cluster/schedules/{uuid}" -d body
# The response of a sucessful PATCH is empty.
Example body to modify an interval schedule with a 2-day and 5-minute interval:
{
    "interval": "P2DT5M"
}
Example body to modify a cron schedule to run Mondays at 2:
{
    "cron":
    {
        "hours": [ 2 ],
        "weekdays": [ 1 ]
    }
}
```
---
## Deleting a job schedule
You can delete job schedules based on their UUID. You can apply queries on fields to delete all schedules that match the combined query.
### Example
```
# The API:
/api/cluster/schedules/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/cluster/schedules/{uuid}"
# The response of a successful DELETE of one schedule is empty.
```
```
# The API:
/api/cluster/schedules/
# The call:
curl -X DELETE "https://<mgmt-ip>/api/cluster/schedules/?name=test*"
# The response of a successful DELETE indicates the number of schedules affected:
{
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/cluster/schedules?name=test*"
    }
  }
}
```
---
## MetroCluster configurations
In a MetroCluster configuration, user-created schedules owned by the local cluster are replicated to the partner cluster. Likewise, user-created schedules owned by the partner cluster are replicated to the local cluster. The owning cluster for a particular schedule is shown in the "cluster.name" and "cluster.uuid" fields.
Normally, only schedules owned by the local cluster can be created, modified, and deleted on the local cluster. However, when a MetroCluster configuration is in switchover, the cluster in switchover state can create, modify, and delete schedules owned by the partner cluster.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Schedule", "ScheduleSchema"]
__pdoc__ = {
    "ScheduleSchema.resource": False,
    "ScheduleSchema.patchable_fields": False,
    "ScheduleSchema.postable_fields": False,
}


class ScheduleSchema(ResourceSchema):
    """The fields of the Schedule object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the schedule. """

    cluster = fields.Nested("netapp_ontap.models.schedule_cluster.ScheduleClusterSchema", data_key="cluster", unknown=EXCLUDE)
    r""" The cluster field of the schedule. """

    cron = fields.Nested("netapp_ontap.models.schedule_cron.ScheduleCronSchema", data_key="cron", unknown=EXCLUDE)
    r""" The cron field of the schedule. """

    interval = fields.Str(
        data_key="interval",
    )
    r""" An ISO-8601 duration formatted string.

Example: P1DT2H3M4S """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=256),
    )
    r""" Schedule name. Required in the URL or POST body. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['cron', 'interval']),
    )
    r""" Schedule type

Valid choices:

* cron
* interval """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Job schedule UUID

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return Schedule

    @property
    def patchable_fields(self):
        return [
            "cron",
            "interval",
        ]

    @property
    def postable_fields(self):
        return [
            "cluster",
            "cron",
            "interval",
            "name",
        ]

class Schedule(Resource):
    r""" Complete schedule information """

    _schema = ScheduleSchema
    _path = "/api/cluster/schedules"
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
        r"""Retrieves a schedule.
### Learn more
* [`DOC /cluster/schedules`](#docs-cluster-cluster_schedules)"""
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
        r"""Updates a schedule. Note that you cannot modify a cron field of an interval schedule, or the interval field of a cron schedule.
### Learn more
* [`DOC /cluster/schedules`](#docs-cluster-cluster_schedules)"""
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
        r"""Deletes a schedule.
### Learn more
* [`DOC /cluster/schedules`](#docs-cluster-cluster_schedules)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a schedule.
### Learn more
* [`DOC /cluster/schedules`](#docs-cluster-cluster_schedules)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a schedule.
### Learn more
* [`DOC /cluster/schedules`](#docs-cluster-cluster_schedules)"""
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
        r"""Creates a schedule.
### Required Fields
* name - Name of the job schedule.
You must provide a minutes field for a cron schedule and an interval field for an interval schedule. Do not provide both a cron field and an interval field.

### Learn more
* [`DOC /cluster/schedules`](#docs-cluster-cluster_schedules)"""
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
        r"""Updates a schedule. Note that you cannot modify a cron field of an interval schedule, or the interval field of a cron schedule.
### Learn more
* [`DOC /cluster/schedules`](#docs-cluster-cluster_schedules)"""
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
        r"""Deletes a schedule.
### Learn more
* [`DOC /cluster/schedules`](#docs-cluster-cluster_schedules)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


