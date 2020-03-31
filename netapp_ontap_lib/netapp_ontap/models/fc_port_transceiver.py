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


__all__ = ["FcPortTransceiver", "FcPortTransceiverSchema"]
__pdoc__ = {
    "FcPortTransceiverSchema.resource": False,
    "FcPortTransceiver": False,
}


class FcPortTransceiverSchema(ResourceSchema):
    """The fields of the FcPortTransceiver object"""

    capabilities = fields.List(fields.Integer, data_key="capabilities")
    r""" The speeds of which the transceiver is capable in gigabits per second. """

    form_factor = fields.Str(data_key="form-factor")
    r""" The form factor of the transceiver. Possible values are:
- _sfp_ - Small Form Factor - Pluggable
- _sff_ - Small Form Factor
- _unk_ - Unknown


Valid choices:

* sfp
* sff
* unk """

    manufacturer = fields.Str(data_key="manufacturer")
    r""" The manufacturer of the transceiver.


Example: Acme, Inc. """

    part_number = fields.Str(data_key="part_number")
    r""" The part number of the transceiver. """

    @property
    def resource(self):
        return FcPortTransceiver

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class FcPortTransceiver(Resource):  # pylint: disable=missing-docstring

    _schema = FcPortTransceiverSchema
