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


__all__ = ["NvmeNamespaceSubsystemMap", "NvmeNamespaceSubsystemMapSchema"]
__pdoc__ = {
    "NvmeNamespaceSubsystemMapSchema.resource": False,
    "NvmeNamespaceSubsystemMap": False,
}


class NvmeNamespaceSubsystemMapSchema(ResourceSchema):
    """The fields of the NvmeNamespaceSubsystemMap object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the nvme_namespace_subsystem_map. """

    anagrpid = fields.Str(data_key="anagrpid")
    r""" The Asymmetric Namespace Access Group ID (ANAGRPID) of the NVMe namespace.<br/>
The format for an ANAGRPID is 8 hexadecimal digits (zero-filled) followed by a lower case "h".


Example: 00103050h """

    nsid = fields.Str(data_key="nsid")
    r""" The NVMe namespace identifier. This is an identifier used by an NVMe controller to provide access to the NVMe namespace.<br/>
The format for an NVMe namespace identifier is 8 hexadecimal digits (zero-filled) followed by a lower case "h".


Example: 00000001h """

    subsystem = fields.Nested("netapp_ontap.resources.nvme_subsystem.NvmeSubsystemSchema", unknown=EXCLUDE, data_key="subsystem")
    r""" The subsystem field of the nvme_namespace_subsystem_map. """

    @property
    def resource(self):
        return NvmeNamespaceSubsystemMap

    @property
    def patchable_fields(self):
        return [
            "subsystem.name",
            "subsystem.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "subsystem.name",
            "subsystem.uuid",
        ]


class NvmeNamespaceSubsystemMap(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeNamespaceSubsystemMapSchema
