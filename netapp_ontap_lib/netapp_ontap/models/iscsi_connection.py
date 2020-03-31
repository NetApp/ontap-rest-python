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


__all__ = ["IscsiConnection", "IscsiConnectionSchema"]
__pdoc__ = {
    "IscsiConnectionSchema.resource": False,
    "IscsiConnection": False,
}


class IscsiConnectionSchema(ResourceSchema):
    """The fields of the IscsiConnection object"""

    links = fields.Nested("netapp_ontap.models.collection_links.CollectionLinksSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the iscsi_connection. """

    authentication_type = fields.Str(data_key="authentication_type")
    r""" The iSCSI authentication type used to establish the connection.


Valid choices:

* chap
* none """

    cid = fields.Integer(data_key="cid")
    r""" The identifier of the connection within the session. """

    initiator_address = fields.Nested("netapp_ontap.models.iscsi_connection_initiator_address.IscsiConnectionInitiatorAddressSchema", unknown=EXCLUDE, data_key="initiator_address")
    r""" The initiator_address field of the iscsi_connection. """

    interface = fields.Nested("netapp_ontap.models.iscsi_connection_interface.IscsiConnectionInterfaceSchema", unknown=EXCLUDE, data_key="interface")
    r""" The interface field of the iscsi_connection. """

    @property
    def resource(self):
        return IscsiConnection

    @property
    def patchable_fields(self):
        return [
            "initiator_address",
            "interface",
        ]

    @property
    def postable_fields(self):
        return [
            "initiator_address",
            "interface",
        ]


class IscsiConnection(Resource):  # pylint: disable=missing-docstring

    _schema = IscsiConnectionSchema
