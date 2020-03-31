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


__all__ = ["PerformanceSvm", "PerformanceSvmSchema"]
__pdoc__ = {
    "PerformanceSvmSchema.resource": False,
    "PerformanceSvm": False,
}


class PerformanceSvmSchema(ResourceSchema):
    """The fields of the PerformanceSvm object"""

    links = fields.Nested("netapp_ontap.models.collection_links.CollectionLinksSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the performance_svm. """

    num_records = fields.Integer(data_key="num_records")
    r""" Number of records """

    records = fields.List(fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", unknown=EXCLUDE), data_key="records")
    r""" The records field of the performance_svm. """

    @property
    def resource(self):
        return PerformanceSvm

    @property
    def patchable_fields(self):
        return [
            "num_records",
            "records.iops",
            "records.latency",
            "records.throughput",
        ]

    @property
    def postable_fields(self):
        return [
            "num_records",
            "records.iops",
            "records.latency",
            "records.throughput",
        ]


class PerformanceSvm(Resource):  # pylint: disable=missing-docstring

    _schema = PerformanceSvmSchema
