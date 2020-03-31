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


__all__ = ["PerformanceSvmNfsStatistics", "PerformanceSvmNfsStatisticsSchema"]
__pdoc__ = {
    "PerformanceSvmNfsStatisticsSchema.resource": False,
    "PerformanceSvmNfsStatistics": False,
}


class PerformanceSvmNfsStatisticsSchema(ResourceSchema):
    """The fields of the PerformanceSvmNfsStatistics object"""

    v3 = fields.Nested("netapp_ontap.models.performance_metric_raw_svm.PerformanceMetricRawSvmSchema", unknown=EXCLUDE, data_key="v3")
    r""" The v3 field of the performance_svm_nfs_statistics. """

    @property
    def resource(self):
        return PerformanceSvmNfsStatistics

    @property
    def patchable_fields(self):
        return [
            "v3.iops_raw",
            "v3.latency_raw",
            "v3.throughput_raw",
        ]

    @property
    def postable_fields(self):
        return [
            "v3.iops_raw",
            "v3.latency_raw",
            "v3.throughput_raw",
        ]


class PerformanceSvmNfsStatistics(Resource):  # pylint: disable=missing-docstring

    _schema = PerformanceSvmNfsStatisticsSchema
