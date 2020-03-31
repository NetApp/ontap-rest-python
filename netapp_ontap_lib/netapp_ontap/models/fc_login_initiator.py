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


__all__ = ["FcLoginInitiator", "FcLoginInitiatorSchema"]
__pdoc__ = {
    "FcLoginInitiatorSchema.resource": False,
    "FcLoginInitiator": False,
}


class FcLoginInitiatorSchema(ResourceSchema):
    """The fields of the FcLoginInitiator object"""

    aliases = fields.List(fields.Str, data_key="aliases")
    r""" The logged in initiator world wide port name (WWPN) aliases. """

    port_address = fields.Str(data_key="port_address")
    r""" The port address of the initiator's FC port.<br/>
Each port in an FC switched fabric has its own unique port address for routing purposes. The port address is assigned by a switch in the fabric when that port logs in to the fabric. This property refers to the address given by a switch to the initiator port.<br/>
This is useful for obtaining statistics and diagnostic information from FC switches.<br/>
This is a hexadecimal encoded numeric value.


Example: 5060A """

    wwnn = fields.Str(data_key="wwnn")
    r""" The logged in initiator world wide node name (WWNN).


Example: 2f:a0:00:a0:98:0b:56:13 """

    wwpn = fields.Str(data_key="wwpn")
    r""" The logged in initiator WWPN.


Example: 2f:a0:00:a0:98:0b:56:13 """

    @property
    def resource(self):
        return FcLoginInitiator

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class FcLoginInitiator(Resource):  # pylint: disable=missing-docstring

    _schema = FcLoginInitiatorSchema
