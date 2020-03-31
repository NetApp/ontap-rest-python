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


__all__ = ["NvmeNamespaceSpace", "NvmeNamespaceSpaceSchema"]
__pdoc__ = {
    "NvmeNamespaceSpaceSchema.resource": False,
    "NvmeNamespaceSpace": False,
}


class NvmeNamespaceSpaceSchema(ResourceSchema):
    """The fields of the NvmeNamespaceSpace object"""

    block_size = fields.Integer(data_key="block_size")
    r""" The size of blocks in the namespace in bytes.<br/>
Valid in POST when creating an NVMe namespace that is not a clone of another. Disallowed in POST when creating a namespace clone.
 Valid in POST. """

    guarantee = fields.Nested("netapp_ontap.models.nvme_namespace_space_guarantee.NvmeNamespaceSpaceGuaranteeSchema", unknown=EXCLUDE, data_key="guarantee")
    r""" The guarantee field of the nvme_namespace_space. """

    size = fields.Integer(data_key="size")
    r""" The total provisioned size of the NVMe namespace.<br/>
NVMe namespaces do not support resize.<br/>
For more information, see _Size properties_ in the _docs_ section of the ONTAP REST API documentation.


Example: 1073741824 """

    used = fields.Integer(data_key="used")
    r""" The amount of space consumed by the main data stream of the NVMe namespace.<br/>
This value is the total space consumed in the volume by the NVMe namespace, including filesystem overhead, but excluding prefix and suffix streams. Due to internal filesystem overhead and the many ways NVMe filesystems and applications utilize blocks within a namespace, this value does not necessarily reflect actual consumption/availability from the perspective of the filesystem or application. Without specific knowledge of how the namespace blocks are utilized outside of ONTAP, this property should not be used and an indicator for an out-of-space condition.<br/>
For more information, see _Size properties_ in the _docs_ section of the ONTAP REST API documentation. """

    @property
    def resource(self):
        return NvmeNamespaceSpace

    @property
    def patchable_fields(self):
        return [
            "guarantee",
        ]

    @property
    def postable_fields(self):
        return [
            "block_size",
            "guarantee",
            "size",
        ]


class NvmeNamespaceSpace(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeNamespaceSpaceSchema
