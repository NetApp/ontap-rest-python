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


__all__ = ["ApplicationStatisticsComponents", "ApplicationStatisticsComponentsSchema"]
__pdoc__ = {
    "ApplicationStatisticsComponentsSchema.resource": False,
    "ApplicationStatisticsComponents": False,
}


class ApplicationStatisticsComponentsSchema(ResourceSchema):
    """The fields of the ApplicationStatisticsComponents object"""

    iops = fields.Nested("netapp_ontap.models.application_statistics_iops.ApplicationStatisticsIopsSchema", unknown=EXCLUDE, data_key="iops")
    r""" The iops field of the application_statistics_components. """

    latency = fields.Nested("netapp_ontap.models.application_statistics_latency.ApplicationStatisticsLatencySchema", unknown=EXCLUDE, data_key="latency")
    r""" The latency field of the application_statistics_components. """

    name = fields.Str(data_key="name")
    r""" Component Name. """

    shared_storage_pool = fields.Boolean(data_key="shared_storage_pool")
    r""" An application component is considered to use a shared storage pool if storage elements for for other components reside on the same aggregate as storage elements for this component. """

    snapshot = fields.Nested("netapp_ontap.models.application_statistics_snapshot.ApplicationStatisticsSnapshotSchema", unknown=EXCLUDE, data_key="snapshot")
    r""" The snapshot field of the application_statistics_components. """

    space = fields.Nested("netapp_ontap.models.application_statistics_space.ApplicationStatisticsSpaceSchema", unknown=EXCLUDE, data_key="space")
    r""" The space field of the application_statistics_components. """

    statistics_incomplete = fields.Boolean(data_key="statistics_incomplete")
    r""" If not all storage elements of the application component are currently available, the returned statistics might only include data from those elements that were available. """

    storage_service = fields.Nested("netapp_ontap.models.application_statistics_storage_service.ApplicationStatisticsStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the application_statistics_components. """

    uuid = fields.Str(data_key="uuid")
    r""" Component UUID. """

    @property
    def resource(self):
        return ApplicationStatisticsComponents

    @property
    def patchable_fields(self):
        return [
            "iops",
            "latency",
            "snapshot",
            "space",
            "storage_service",
        ]

    @property
    def postable_fields(self):
        return [
            "iops",
            "latency",
            "snapshot",
            "space",
            "storage_service",
        ]


class ApplicationStatisticsComponents(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationStatisticsComponentsSchema
