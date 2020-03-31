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


__all__ = ["NvmeSubsystemHostNoRecords", "NvmeSubsystemHostNoRecordsSchema"]
__pdoc__ = {
    "NvmeSubsystemHostNoRecordsSchema.resource": False,
    "NvmeSubsystemHostNoRecords": False,
}


class NvmeSubsystemHostNoRecordsSchema(ResourceSchema):
    """The fields of the NvmeSubsystemHostNoRecords object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the nvme_subsystem_host_no_records. """

    io_queue = fields.Nested("netapp_ontap.models.nvme_subsystem_host_io_queue.NvmeSubsystemHostIoQueueSchema", unknown=EXCLUDE, data_key="io_queue")
    r""" The io_queue field of the nvme_subsystem_host_no_records. """

    nqn = fields.Str(data_key="nqn")
    r""" The NVMe qualified name (NQN) used to identify the NVMe storage target. Not allowed in POST when the `records` property is used.


Example: nqn.1992-01.example.com:string """

    subsystem = fields.Nested("netapp_ontap.models.nvme_subsystem_host_subsystem.NvmeSubsystemHostSubsystemSchema", unknown=EXCLUDE, data_key="subsystem")
    r""" The subsystem field of the nvme_subsystem_host_no_records. """

    @property
    def resource(self):
        return NvmeSubsystemHostNoRecords

    @property
    def patchable_fields(self):
        return [
            "io_queue",
            "subsystem",
        ]

    @property
    def postable_fields(self):
        return [
            "io_queue",
            "nqn",
            "subsystem",
        ]


class NvmeSubsystemHostNoRecords(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeSubsystemHostNoRecordsSchema
