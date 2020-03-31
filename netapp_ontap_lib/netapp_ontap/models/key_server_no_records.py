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


__all__ = ["KeyServerNoRecords", "KeyServerNoRecordsSchema"]
__pdoc__ = {
    "KeyServerNoRecordsSchema.resource": False,
    "KeyServerNoRecords": False,
}


class KeyServerNoRecordsSchema(ResourceSchema):
    """The fields of the KeyServerNoRecords object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the key_server_no_records. """

    connectivity = fields.Nested("netapp_ontap.models.key_server_state_array.KeyServerStateArraySchema", unknown=EXCLUDE, data_key="connectivity")
    r""" The connectivity field of the key_server_no_records. """

    password = fields.Str(data_key="password")
    r""" Password credentials for connecting with the key server. This is not audited.

Example: password """

    server = fields.Str(data_key="server")
    r""" External key server for key management. If no port is provided, a default port of 5696 is used. Not valid in POST if `records` is provided.

Example: keyserver1.com:5698 """

    timeout = fields.Integer(data_key="timeout")
    r""" I/O timeout in seconds for communicating with the key server.

Example: 60 """

    username = fields.Str(data_key="username")
    r""" KMIP username credentials for connecting with the key server.

Example: username """

    @property
    def resource(self):
        return KeyServerNoRecords

    @property
    def patchable_fields(self):
        return [
            "password",
            "timeout",
            "username",
        ]

    @property
    def postable_fields(self):
        return [
            "server",
        ]


class KeyServerNoRecords(Resource):  # pylint: disable=missing-docstring

    _schema = KeyServerNoRecordsSchema
