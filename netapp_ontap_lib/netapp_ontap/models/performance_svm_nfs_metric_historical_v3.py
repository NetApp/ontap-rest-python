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


__all__ = ["PerformanceSvmNfsMetricHistoricalV3", "PerformanceSvmNfsMetricHistoricalV3Schema"]
__pdoc__ = {
    "PerformanceSvmNfsMetricHistoricalV3Schema.resource": False,
    "PerformanceSvmNfsMetricHistoricalV3": False,
}


class PerformanceSvmNfsMetricHistoricalV3Schema(ResourceSchema):
    """The fields of the PerformanceSvmNfsMetricHistoricalV3 object"""

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
    r""" The iops field of the performance_svm_nfs_metric_historical_v3. """

    latency = fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", unknown=EXCLUDE, data_key="latency")
    r""" The latency field of the performance_svm_nfs_metric_historical_v3. """

    status = fields.Str(data_key="status")
    r""" Any errors associated with the sample. For example, if the aggregation of data over multiple nodes fails then any of the partial errors might be returned, "ok" on success, or "error" on any internal uncategorized failure. Whenever a sample collection is missed but done at a later time, it is back filled to the previous 15 second timestamp and tagged with "backfilled_data". "Inconsistent_ delta_time" is encountered when the time between two collections is not the same for all nodes. Therefore, the aggregated value might be over or under inflated. "Negative_delta" is returned when an expected monotonically increasing value has decreased in value. "Inconsistent_old_data" is returned when one or more nodes do not have the latest data.

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

    throughput = fields.Nested("netapp_ontap.models.performance_metric_io_type_rwt.PerformanceMetricIoTypeRwtSchema", unknown=EXCLUDE, data_key="throughput")
    r""" The throughput field of the performance_svm_nfs_metric_historical_v3. """

    @property
    def resource(self):
        return PerformanceSvmNfsMetricHistoricalV3

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
            "throughput.read",
            "throughput.total",
            "throughput.write",
        ]


class PerformanceSvmNfsMetricHistoricalV3(Resource):  # pylint: disable=missing-docstring

    _schema = PerformanceSvmNfsMetricHistoricalV3Schema
