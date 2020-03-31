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


__all__ = ["IscsiConnectionInitiatorAddress", "IscsiConnectionInitiatorAddressSchema"]
__pdoc__ = {
    "IscsiConnectionInitiatorAddressSchema.resource": False,
    "IscsiConnectionInitiatorAddress": False,
}


class IscsiConnectionInitiatorAddressSchema(ResourceSchema):
    """The fields of the IscsiConnectionInitiatorAddress object"""

    address = fields.Str(data_key="address")
    r""" The TCP IPv4 or IPv6 address of the initiator end of the iSCSI connection.


Example: 10.10.10.7 """

    port = fields.Integer(data_key="port")
    r""" The TCP port number of the initiator end of the iSCSI connection.


Example: 55432 """

    @property
    def resource(self):
        return IscsiConnectionInitiatorAddress

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class IscsiConnectionInitiatorAddress(Resource):  # pylint: disable=missing-docstring

    _schema = IscsiConnectionInitiatorAddressSchema
