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


__all__ = ["NvmeNamespaceCloneSource", "NvmeNamespaceCloneSourceSchema"]
__pdoc__ = {
    "NvmeNamespaceCloneSourceSchema.resource": False,
    "NvmeNamespaceCloneSource": False,
}


class NvmeNamespaceCloneSourceSchema(ResourceSchema):
    """The fields of the NvmeNamespaceCloneSource object"""

    name = fields.Str(data_key="name")
    r""" The fully qualified path name of the clone source NVMe namespace composed of a "/vol" prefix, the volume name, the (optional) qtree name and base name of the namespace. Valid in POST and PATCH.


Example: /vol/volume1/namespace1 """

    uuid = fields.Str(data_key="uuid")
    r""" The unique identifier of the clone source NVMe namespace. Valid in POST and PATCH.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return NvmeNamespaceCloneSource

    @property
    def patchable_fields(self):
        return [
            "name",
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "uuid",
        ]


class NvmeNamespaceCloneSource(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeNamespaceCloneSourceSchema
