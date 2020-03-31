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


__all__ = ["IscsiCredentialsChap", "IscsiCredentialsChapSchema"]
__pdoc__ = {
    "IscsiCredentialsChapSchema.resource": False,
    "IscsiCredentialsChap": False,
}


class IscsiCredentialsChapSchema(ResourceSchema):
    """The fields of the IscsiCredentialsChap object"""

    inbound = fields.Nested("netapp_ontap.models.iscsi_credentials_chap_inbound.IscsiCredentialsChapInboundSchema", unknown=EXCLUDE, data_key="inbound")
    r""" The inbound field of the iscsi_credentials_chap. """

    outbound = fields.Nested("netapp_ontap.models.iscsi_credentials_chap_outbound.IscsiCredentialsChapOutboundSchema", unknown=EXCLUDE, data_key="outbound")
    r""" The outbound field of the iscsi_credentials_chap. """

    @property
    def resource(self):
        return IscsiCredentialsChap

    @property
    def patchable_fields(self):
        return [
            "inbound",
            "outbound",
        ]

    @property
    def postable_fields(self):
        return [
            "inbound",
            "outbound",
        ]


class IscsiCredentialsChap(Resource):  # pylint: disable=missing-docstring

    _schema = IscsiCredentialsChapSchema
