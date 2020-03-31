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


__all__ = ["PerformanceMetricRawSvm", "PerformanceMetricRawSvmSchema"]
__pdoc__ = {
    "PerformanceMetricRawSvmSchema.resource": False,
    "PerformanceMetricRawSvm": False,
}


class PerformanceMetricRawSvmSchema(ResourceSchema):
    """The fields of the PerformanceMetricRawSvm object"""

    iops_raw = fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", unknown=EXCLUDE, data_key="iops_raw")
    r""" The iops_raw field of the performance_metric_raw_svm. """

    latency_raw = fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", unknown=EXCLUDE, data_key="latency_raw")
    r""" The latency_raw field of the performance_metric_raw_svm. """

    status = fields.Str(data_key="status")
    r""" Any errors associated with the sample. For example, if the aggregation of data over multiple nodes fails then any of the partial errors might be returned, "ok" on success, or "error" on any internal uncategorized failure. Whenever a sample collection is missed but done at a later time, it is back filled to the previous 15 second timestamp and tagged with "backfilled_data". "Inconsistent_delta_time" is encountered when the time between two collections is not the same for all nodes. Therefore, the aggregated value might be over or under inflated. "Negative_delta" is returned when an expected monotonically increasing value has decreased in value. "Inconsistent_old_data" is returned when one or more nodes do not have the latest data.

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

    throughput_raw = fields.Nested("netapp_ontap.models.performance_metric_io_type_rwt.PerformanceMetricIoTypeRwtSchema", unknown=EXCLUDE, data_key="throughput_raw")
    r""" The throughput_raw field of the performance_metric_raw_svm. """

    timestamp = fields.DateTime(data_key="timestamp")
    r""" The timestamp of the performance data.

Example: 2017-01-25T11:20:13.000+0000 """

    @property
    def resource(self):
        return PerformanceMetricRawSvm

    @property
    def patchable_fields(self):
        return [
            "iops_raw.other",
            "iops_raw.read",
            "iops_raw.total",
            "iops_raw.write",
            "latency_raw.other",
            "latency_raw.read",
            "latency_raw.total",
            "latency_raw.write",
            "throughput_raw.read",
            "throughput_raw.total",
            "throughput_raw.write",
        ]

    @property
    def postable_fields(self):
        return [
            "iops_raw.other",
            "iops_raw.read",
            "iops_raw.total",
            "iops_raw.write",
            "latency_raw.other",
            "latency_raw.read",
            "latency_raw.total",
            "latency_raw.write",
            "throughput_raw.read",
            "throughput_raw.total",
            "throughput_raw.write",
        ]


class PerformanceMetricRawSvm(Resource):  # pylint: disable=missing-docstring

    _schema = PerformanceMetricRawSvmSchema
