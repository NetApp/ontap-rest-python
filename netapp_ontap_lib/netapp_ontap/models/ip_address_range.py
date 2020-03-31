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


__all__ = ["IpAddressRange", "IpAddressRangeSchema"]
__pdoc__ = {
    "IpAddressRangeSchema.resource": False,
    "IpAddressRange": False,
}


class IpAddressRangeSchema(ResourceSchema):
    """The fields of the IpAddressRange object"""

    end = fields.Str(data_key="end")
    r""" The end field of the ip_address_range. """

    family = fields.Str(data_key="family")
    r""" The family field of the ip_address_range. """

    start = fields.Str(data_key="start")
    r""" The start field of the ip_address_range. """

    @property
    def resource(self):
        return IpAddressRange

    @property
    def patchable_fields(self):
        return [
            "end",
            "family",
            "start",
        ]

    @property
    def postable_fields(self):
        return [
            "end",
            "family",
            "start",
        ]


class IpAddressRange(Resource):  # pylint: disable=missing-docstring

    _schema = IpAddressRangeSchema
