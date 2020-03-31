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


__all__ = ["NvmeNamespaceClone", "NvmeNamespaceCloneSchema"]
__pdoc__ = {
    "NvmeNamespaceCloneSchema.resource": False,
    "NvmeNamespaceClone": False,
}


class NvmeNamespaceCloneSchema(ResourceSchema):
    """The fields of the NvmeNamespaceClone object"""

    source = fields.Nested("netapp_ontap.models.nvme_namespace_clone_source.NvmeNamespaceCloneSourceSchema", unknown=EXCLUDE, data_key="source")
    r""" The source field of the nvme_namespace_clone. """

    @property
    def resource(self):
        return NvmeNamespaceClone

    @property
    def patchable_fields(self):
        return [
            "source",
        ]

    @property
    def postable_fields(self):
        return [
            "source",
        ]


class NvmeNamespaceClone(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeNamespaceCloneSchema
