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


__all__ = ["NvmeInterfaceFcInterface", "NvmeInterfaceFcInterfaceSchema"]
__pdoc__ = {
    "NvmeInterfaceFcInterfaceSchema.resource": False,
    "NvmeInterfaceFcInterface": False,
}


class NvmeInterfaceFcInterfaceSchema(ResourceSchema):
    """The fields of the NvmeInterfaceFcInterface object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the nvme_interface_fc_interface. """

    port = fields.Nested("netapp_ontap.resources.fc_port.FcPortSchema", unknown=EXCLUDE, data_key="port")
    r""" The port field of the nvme_interface_fc_interface. """

    wwnn = fields.Str(data_key="wwnn")
    r""" The WWNN (world wide node name) of the Fibre Channel NVMe interface.


Example: 20:00:00:50:56:b4:13:a9 """

    wwpn = fields.Str(data_key="wwpn")
    r""" The WWPN (world wide port name) of the Fibre Channel NVMe interface.


Example: 20:00:00:50:56:b4:13:a8 """

    @property
    def resource(self):
        return NvmeInterfaceFcInterface

    @property
    def patchable_fields(self):
        return [
            "port.name",
            "port.node",
            "port.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "port.name",
            "port.node",
            "port.uuid",
        ]


class NvmeInterfaceFcInterface(Resource):  # pylint: disable=missing-docstring

    _schema = NvmeInterfaceFcInterfaceSchema
