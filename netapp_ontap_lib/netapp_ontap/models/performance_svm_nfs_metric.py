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


__all__ = ["PerformanceSvmNfsMetric", "PerformanceSvmNfsMetricSchema"]
__pdoc__ = {
    "PerformanceSvmNfsMetricSchema.resource": False,
    "PerformanceSvmNfsMetric": False,
}


class PerformanceSvmNfsMetricSchema(ResourceSchema):
    """The fields of the PerformanceSvmNfsMetric object"""

    v3 = fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", unknown=EXCLUDE, data_key="v3")
    r""" The v3 field of the performance_svm_nfs_metric. """

    @property
    def resource(self):
        return PerformanceSvmNfsMetric

    @property
    def patchable_fields(self):
        return [
            "v3.iops",
            "v3.latency",
            "v3.throughput",
        ]

    @property
    def postable_fields(self):
        return [
            "v3.iops",
            "v3.latency",
            "v3.throughput",
        ]


class PerformanceSvmNfsMetric(Resource):  # pylint: disable=missing-docstring

    _schema = PerformanceSvmNfsMetricSchema
