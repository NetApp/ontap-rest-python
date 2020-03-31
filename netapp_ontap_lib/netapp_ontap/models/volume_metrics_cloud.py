# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema


__all__ = ["VolumeMetricsCloud", "VolumeMetricsCloudSchema"]
__pdoc__ = {
    "VolumeMetricsCloudSchema.resource": False,
    "VolumeMetricsCloud": False,
}


class VolumeMetricsCloudSchema(ResourceSchema):
    """The fields of the VolumeMetricsCloud object"""

    duration = fields.Str(data_key="duration")
    r""" The duration over which this sample is calculated. The time durations are represented in the ISO-8601 standard format. Samples can be calculated over the following durations:


Valid choices:

* PT15S
* PT4M
* PT30M
* PT2H
* P1D
* PT5M """

    iops = fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", unknown=EXCLUDE, data_key="iops")
    r""" The iops field of the volume_metrics_cloud. """

    latency = fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", unknown=EXCLUDE, data_key="latency")
    r""" The latency field of the volume_metrics_cloud. """

    status = fields.Str(data_key="status")
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

    timestamp = fields.DateTime(data_key="timestamp")
    r""" The timestamp of the performance data.

Example: 2017-01-25T11:20:13.000+0000 """

    @property
    def resource(self):
        return VolumeMetricsCloud

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
        ]


class VolumeMetricsCloud(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeMetricsCloudSchema
