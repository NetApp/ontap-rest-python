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


__all__ = ["IscsiCredentialsInitiatorAddress", "IscsiCredentialsInitiatorAddressSchema"]
__pdoc__ = {
    "IscsiCredentialsInitiatorAddressSchema.resource": False,
    "IscsiCredentialsInitiatorAddress": False,
}


class IscsiCredentialsInitiatorAddressSchema(ResourceSchema):
    """The fields of the IscsiCredentialsInitiatorAddress object"""

    masks = fields.List(fields.Nested("netapp_ontap.models.ip_info.IpInfoSchema", unknown=EXCLUDE), data_key="masks")
    r""" The masks field of the iscsi_credentials_initiator_address. """

    ranges = fields.List(fields.Nested("netapp_ontap.models.ip_address_range.IpAddressRangeSchema", unknown=EXCLUDE), data_key="ranges")
    r""" The ranges field of the iscsi_credentials_initiator_address. """

    @property
    def resource(self):
        return IscsiCredentialsInitiatorAddress

    @property
    def patchable_fields(self):
        return [
            "masks",
            "ranges",
        ]

    @property
    def postable_fields(self):
        return [
            "masks",
            "ranges",
        ]


class IscsiCredentialsInitiatorAddress(Resource):  # pylint: disable=missing-docstring

    _schema = IscsiCredentialsInitiatorAddressSchema
