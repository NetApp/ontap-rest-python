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


__all__ = ["FcPortFabric", "FcPortFabricSchema"]
__pdoc__ = {
    "FcPortFabricSchema.resource": False,
    "FcPortFabric": False,
}


class FcPortFabricSchema(ResourceSchema):
    """The fields of the FcPortFabric object"""

    connected = fields.Boolean(data_key="connected")
    r""" Reports if the physical port has established a connection with the FC fabric. """

    connected_speed = fields.Integer(data_key="connected_speed")
    r""" The negotiated data rate between the target FC port and the fabric in gigabits per second.


Example: 16 """

    name = fields.Str(data_key="name")
    r""" The name of the fabric to which the port is connected. This is only available when the FC port is connected to a fabric.<br/>
There is an added cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more. """

    port_address = fields.Str(data_key="port_address")
    r""" The FC port address of the host bus adapter (HBA) physical port.<br/>
Each FC port in an FC switched fabric has its own unique FC port address for routing purposes. The FC port address is assigned by a switch in the fabric when that port logs in to the fabric. This property refers to the FC port address given to the physical host bus adapter (HBA) port when the port performs a fabric login (FLOGI).<br/>
This is useful for obtaining statistics and diagnostic information from FC switches.<br/>
This is a six-digit hexadecimal encoded numeric value.


Example: 52100A """

    switch_port = fields.Str(data_key="switch_port")
    r""" The switch port to which the FC port is connected.


Example: ssan-g620-03:33 """

    @property
    def resource(self):
        return FcPortFabric

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class FcPortFabric(Resource):  # pylint: disable=missing-docstring

    _schema = FcPortFabricSchema
