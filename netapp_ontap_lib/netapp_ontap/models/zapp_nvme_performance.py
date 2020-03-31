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


__all__ = ["ZappNvmePerformance", "ZappNvmePerformanceSchema"]
__pdoc__ = {
    "ZappNvmePerformanceSchema.resource": False,
    "ZappNvmePerformance": False,
}


class ZappNvmePerformanceSchema(ResourceSchema):
    """The fields of the ZappNvmePerformance object"""

    storage_service = fields.Nested("netapp_ontap.models.nas_storage_service.NasStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the zapp_nvme_performance. """

    @property
    def resource(self):
        return ZappNvmePerformance

    @property
    def patchable_fields(self):
        return [
            "storage_service",
        ]

    @property
    def postable_fields(self):
        return [
            "storage_service",
        ]


class ZappNvmePerformance(Resource):  # pylint: disable=missing-docstring

    _schema = ZappNvmePerformanceSchema
