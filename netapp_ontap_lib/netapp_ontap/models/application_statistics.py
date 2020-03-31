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


__all__ = ["ApplicationStatistics", "ApplicationStatisticsSchema"]
__pdoc__ = {
    "ApplicationStatisticsSchema.resource": False,
    "ApplicationStatistics": False,
}


class ApplicationStatisticsSchema(ResourceSchema):
    """The fields of the ApplicationStatistics object"""

    components = fields.List(fields.Nested("netapp_ontap.models.application_statistics_components.ApplicationStatisticsComponentsSchema", unknown=EXCLUDE), data_key="components")
    r""" The components field of the application_statistics. """

    iops = fields.Nested("netapp_ontap.models.application_statistics_iops1.ApplicationStatisticsIops1Schema", unknown=EXCLUDE, data_key="iops")
    r""" The iops field of the application_statistics. """

    latency = fields.Nested("netapp_ontap.models.application_statistics_latency1.ApplicationStatisticsLatency1Schema", unknown=EXCLUDE, data_key="latency")
    r""" The latency field of the application_statistics. """

    shared_storage_pool = fields.Boolean(data_key="shared_storage_pool")
    r""" An application is considered to use a shared storage pool if storage elements for multiple components reside on the same aggregate. """

    snapshot = fields.Nested("netapp_ontap.models.application_statistics_snapshot.ApplicationStatisticsSnapshotSchema", unknown=EXCLUDE, data_key="snapshot")
    r""" The snapshot field of the application_statistics. """

    space = fields.Nested("netapp_ontap.models.application_statistics_space1.ApplicationStatisticsSpace1Schema", unknown=EXCLUDE, data_key="space")
    r""" The space field of the application_statistics. """

    statistics_incomplete = fields.Boolean(data_key="statistics_incomplete")
    r""" If not all storage elements of the application are currently available, the returned statistics might only include data from those elements that were available. """

    @property
    def resource(self):
        return ApplicationStatistics

    @property
    def patchable_fields(self):
        return [
            "iops",
            "latency",
            "snapshot",
            "space",
        ]

    @property
    def postable_fields(self):
        return [
            "iops",
            "latency",
            "snapshot",
            "space",
        ]


class ApplicationStatistics(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationStatisticsSchema
