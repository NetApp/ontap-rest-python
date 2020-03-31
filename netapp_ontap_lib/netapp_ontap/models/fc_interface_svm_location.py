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


__all__ = ["FcInterfaceSvmLocation", "FcInterfaceSvmLocationSchema"]
__pdoc__ = {
    "FcInterfaceSvmLocationSchema.resource": False,
    "FcInterfaceSvmLocation": False,
}


class FcInterfaceSvmLocationSchema(ResourceSchema):
    """The fields of the FcInterfaceSvmLocation object"""

    port = fields.Nested("netapp_ontap.resources.fc_port.FcPortSchema", unknown=EXCLUDE, data_key="port")
    r""" The port field of the fc_interface_svm_location. """

    @property
    def resource(self):
        return FcInterfaceSvmLocation

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


class FcInterfaceSvmLocation(Resource):  # pylint: disable=missing-docstring

    _schema = FcInterfaceSvmLocationSchema
