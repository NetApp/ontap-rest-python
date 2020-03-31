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


__all__ = ["ZappNvmeComponents", "ZappNvmeComponentsSchema"]
__pdoc__ = {
    "ZappNvmeComponentsSchema.resource": False,
    "ZappNvmeComponents": False,
}


class ZappNvmeComponentsSchema(ResourceSchema):
    """The fields of the ZappNvmeComponents object"""

    name = fields.Str(data_key="name")
    r""" The name of the application component. """

    namespace_count = fields.Integer(data_key="namespace_count")
    r""" The number of namespaces in the component """

    performance = fields.Nested("netapp_ontap.models.zapp_nvme_performance.ZappNvmePerformanceSchema", unknown=EXCLUDE, data_key="performance")
    r""" The performance field of the zapp_nvme_components. """

    subsystem = fields.Nested("netapp_ontap.models.zapp_nvme_components_subsystem.ZappNvmeComponentsSubsystemSchema", unknown=EXCLUDE, data_key="subsystem")
    r""" The subsystem field of the zapp_nvme_components. """

    tiering = fields.Nested("netapp_ontap.models.zapp_nvme_components_tiering.ZappNvmeComponentsTieringSchema", unknown=EXCLUDE, data_key="tiering")
    r""" The tiering field of the zapp_nvme_components. """

    total_size = fields.Integer(data_key="total_size")
    r""" The total size of the component, spread across member namespaces. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    @property
    def resource(self):
        return ZappNvmeComponents

    @property
    def patchable_fields(self):
        return [
            "name",
            "performance",
            "subsystem",
            "tiering",
            "total_size",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "namespace_count",
            "performance",
            "subsystem",
            "tiering",
            "total_size",
        ]


class ZappNvmeComponents(Resource):  # pylint: disable=missing-docstring

    _schema = ZappNvmeComponentsSchema
