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


__all__ = ["PerformanceSvmNfsMetricHistorical", "PerformanceSvmNfsMetricHistoricalSchema"]
__pdoc__ = {
    "PerformanceSvmNfsMetricHistoricalSchema.resource": False,
    "PerformanceSvmNfsMetricHistorical": False,
}


class PerformanceSvmNfsMetricHistoricalSchema(ResourceSchema):
    """The fields of the PerformanceSvmNfsMetricHistorical object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the performance_svm_nfs_metric_historical. """

    timestamp = fields.DateTime(data_key="timestamp")
    r""" The timestamp of the performance data.

Example: 2017-01-25T11:20:13.000+0000 """

    v3 = fields.Nested("netapp_ontap.models.performance_svm_nfs_metric_historical_v3.PerformanceSvmNfsMetricHistoricalV3Schema", unknown=EXCLUDE, data_key="v3")
    r""" The v3 field of the performance_svm_nfs_metric_historical. """

    @property
    def resource(self):
        return PerformanceSvmNfsMetricHistorical

    @property
    def patchable_fields(self):
        return [
            "v3",
        ]

    @property
    def postable_fields(self):
        return [
            "v3",
        ]


class PerformanceSvmNfsMetricHistorical(Resource):  # pylint: disable=missing-docstring

    _schema = PerformanceSvmNfsMetricHistoricalSchema
