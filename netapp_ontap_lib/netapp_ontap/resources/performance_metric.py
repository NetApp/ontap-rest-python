# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
The Storage Aggregate Metrics API provides historical performance metrics for the specified aggregate.
The collection GET operation retrieves read, write, other and total metrics for a given aggregate, in terms of IOPS, latency and throughput. The read and write categories display the I/O operations that service user reads and writes across all the hosted volumes on a given aggregate. The other category encompasses background I/O operations that implement data protection services currently running on the aggregate. IOPs are the number of I/O operations reported per second, throughput is the amount of I/O operations measured in bytes per second and latency is the average response time for an IOP, reported in microseconds.
Without a specified time interval, the output is limited to statistics collected at 15 second intervals over the last hour.
## Examples
### Retrieving metrics for an aggregate
In this example, the API returns a set of records that exist for the aggregate with the given UUID for the last hour.
```
# The API:
/api/storage/aggregates/{uuid}/metrics
#The call:
curl -X GET "https://<mgmt-ip>/api/storage/aggregates/538bf337-1b2c-11e8-bad0-005056b48388/metrics" -H "accept: application/json"
#The response:
{
  "records": [
    {
      "timestamp": "2019-01-14T23:33:45Z"
    },
    {
      "timestamp": "2019-01-14T23:33:30Z"
    },
    {
      "timestamp": "2019-01-14T23:33:15Z"
    },
    {
      "timestamp": "2019-01-14T23:33:00Z"
    },
    ...
  ],
  "num_records": 240
}
```
### Retrieving metrics for an aggregate with a set timestamp
In this example, the API returns metric values for latency, IOPS, and throughput properties such as read, write and total. The status and duration
for which the metrics are requested are also returned.
```
#The API:
/api/storage/aggregates/{uuid}/metrics/{timestamp}
#The call:
curl -X GET "https://<mgmt-ip>/api/storage/aggregates/538bf337-1b2c-11e8-bad0-005056b48388/metrics/2019-01-1T23:33:00Z" -H "accept: application/json"
#The response:
{
  "uuid": "538bf337-1b2c-11e8-bad0-005056b48388",
  "timestamp": "2019-01-01T23:33:00Z",
  "status": "ok",
  "duration": "PT15S",
  "throughput": {
    "read": 6826,
    "write": 205892,
    "other": 0,
    "total": 212718
  },
  "latency": {
    "read": 148,
    "write": 216,
    "other": 0,
    "total": 199
  },
  "iops": {
    "read": 1,
    "write": 5,
    "other": 0,
    "total": 6
  }
}
```
### Retrieving metrics for an aggregate for a set time interval
In this example, the API returns the requested metrics for the given time interval of 1 week. The interval value can be
1 hour, 1 day, 1 week, 1 month or 1 year. If the interval value is not set, a default value of 1 hour is used.
```
#The API:
/api/storage/aggregates/{uuid}/metrics
#The call:
    curl -X GET "https://<mgmt-ip>/api/storage/aggregates/538bf337-1b2c-11e8-bad0-005056b48388/metrics?return_timeout=15&fields=*&interval=1w"  -H "accept: application/json"
#The response:
{
  "records": [
    {
       "timestamp": "2019-01-01T23:30:00Z",
       "status": "ok",
       "duration": "PT30M",
       "throughput": {
         "read": 268328,
         "write": 5556255,
         "other": 0,
         "total": 5824584
       },
       "latency": {
         "read": 156,
         "write": 430,
         "other": 0,
         "total": 318
       },
       "iops": {
         "read": 18,
         "write": 26,
         "other": 0,
         "total": 45
       }
    },
    {
       "timestamp": "2019-01-01T23:00:00Z",
       "status": "ok",
       "duration": "PT30M",
       "throughput": {
         "read": 474266,
         "write": 6121908,
         "other": 0,
         "total": 6596175
       },
       "latency": {
         "read": 154,
         "write": 448,
         "other": 0,
         "total": 262
       },
       "iops": {
         "read": 48,
         "write": 28,
         "other": 0,
         "total": 76
       }
    },
    {
       "timestamp": "2019-01-01T22:30:00Z",
       "status": "ok",
       "duration": "PT30M",
       "throughput": {
         "read": 540164,
         "write": 2411356,
         "other": 26244685,
         "total": 29196206
       },
       "latency": {
         "read": 159,
         "write": 394,
         "other": 192,
         "total": 193
       },
       "iops": {
         "read": 94,
         "write": 16,
         "other": 437,
         "total": 548
       }
    },
    {
       "timestamp": "2019-01-01T22:00:00Z",
       "status": "ok",
       "duration": "PT30M",
       "throughput": {
         "read": 2842,
         "write": 2765407,
         "other": 0,
         "total": 2768249
       },
       "latency": {
         "read": 189,
         "write": 540,
         "other": 0,
         "total": 523
       },
       "iops": {
         "read": 0,
         "write": 13,
         "other": 0,
         "total": 13
       }
    },
    ...
  ],
  "num_records": 336
}
```
### Related ONTAP commands

* `statistics aggregate show`
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["PerformanceMetric", "PerformanceMetricSchema"]
__pdoc__ = {
    "PerformanceMetricSchema.resource": False,
    "PerformanceMetricSchema.patchable_fields": False,
    "PerformanceMetricSchema.postable_fields": False,
}


class PerformanceMetricSchema(ResourceSchema):
    """The fields of the PerformanceMetric object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the performance_metric. """

    duration = fields.Str(
        data_key="duration",
        validate=enum_validation(['PT15S', 'PT4M', 'PT30M', 'PT2H', 'P1D', 'PT5M']),
    )
    r""" The duration over which this sample is calculated. The time durations are represented in the ISO-8601 standard format. Samples can be calculated over the following durations:


Valid choices:

* PT15S
* PT4M
* PT30M
* PT2H
* P1D
* PT5M """

    iops = fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", data_key="iops", unknown=EXCLUDE)
    r""" The iops field of the performance_metric. """

    latency = fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", data_key="latency", unknown=EXCLUDE)
    r""" The latency field of the performance_metric. """

    status = fields.Str(
        data_key="status",
        validate=enum_validation(['ok', 'error', 'partial_no_data', 'partial_no_uuid', 'partial_no_response', 'partial_other_error', 'negative_delta', 'backfilled_data', 'inconsistent_delta_time', 'inconsistent_old_data']),
    )
    r""" Errors associated with the sample. For example, if the aggregation of data over multiple nodes fails, then any partial errors might return "ok" on success or "error" on an internal uncategorized failure. Whenever a sample collection is missed but done at a later time, it is back filled to the previous 15 second timestamp and tagged with "backfilled_data". "Inconsistent_ delta_time" is encountered when the time between two collections is not the same for all nodes. Therefore, the aggregated value might be over or under inflated. "Negative_delta" is returned when an expected monotonically increasing value has decreased in value. "Inconsistent_old_data" is returned when one or more nodes do not have the latest data.

Valid choices:

* ok
* error
* partial_no_data
* partial_no_uuid
* partial_no_response
* partial_other_error
* negative_delta
* backfilled_data
* inconsistent_delta_time
* inconsistent_old_data """

    throughput = fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", data_key="throughput", unknown=EXCLUDE)
    r""" The throughput field of the performance_metric. """

    timestamp = fields.DateTime(
        data_key="timestamp",
    )
    r""" The timestamp of the performance data.

Example: 2017-01-25T11:20:13.000+0000 """

    @property
    def resource(self):
        return PerformanceMetric

    @property
    def patchable_fields(self):
        return [
            "iops.other",
            "iops.read",
            "iops.total",
            "iops.write",
            "latency.other",
            "latency.read",
            "latency.total",
            "latency.write",
            "throughput.other",
            "throughput.read",
            "throughput.total",
            "throughput.write",
        ]

    @property
    def postable_fields(self):
        return [
            "iops.other",
            "iops.read",
            "iops.total",
            "iops.write",
            "latency.other",
            "latency.read",
            "latency.total",
            "latency.write",
            "throughput.other",
            "throughput.read",
            "throughput.total",
            "throughput.write",
        ]

class PerformanceMetric(Resource):
    r""" Performance numbers, such as IOPS latency and throughput. """

    _schema = PerformanceMetricSchema
    _path = "/api/storage/aggregates/{aggregate[uuid]}/metrics"
    @property
    def _keys(self):
        return ["aggregate.uuid"]

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
        r"""Retrieves historical performance metrics for an aggregate.
### Learn more
* [`DOC /storage/aggregates/{uuid}/metrics`](#docs-storage-storage_aggregates_{uuid}_metrics)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves historical performance metrics for an aggregate.
### Learn more
* [`DOC /storage/aggregates/{uuid}/metrics`](#docs-storage-storage_aggregates_{uuid}_metrics)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






