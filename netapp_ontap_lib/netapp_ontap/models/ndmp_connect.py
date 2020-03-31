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


__all__ = ["NdmpConnect", "NdmpConnectSchema"]
__pdoc__ = {
    "NdmpConnectSchema.resource": False,
    "NdmpConnect": False,
}


class NdmpConnectSchema(ResourceSchema):
    """The fields of the NdmpConnect object"""

    address = fields.Str(data_key="address")
    r""" Indicates the NDMP data connection address. """

    port = fields.Integer(data_key="port")
    r""" Indicates the NDMP data connection port.

Example: 18600 """

    type = fields.Str(data_key="type")
    r""" Indicates the NDMP data connection type. """

    @property
    def resource(self):
        return NdmpConnect

    @property
    def patchable_fields(self):
        return [
            "address",
            "port",
            "type",
        ]

    @property
    def postable_fields(self):
        return [
            "address",
            "port",
            "type",
        ]


class NdmpConnect(Resource):  # pylint: disable=missing-docstring

    _schema = NdmpConnectSchema
