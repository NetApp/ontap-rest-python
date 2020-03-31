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


__all__ = ["NfsServiceTransport", "NfsServiceTransportSchema"]
__pdoc__ = {
    "NfsServiceTransportSchema.resource": False,
    "NfsServiceTransport": False,
}


class NfsServiceTransportSchema(ResourceSchema):
    """The fields of the NfsServiceTransport object"""

    tcp_enabled = fields.Boolean(data_key="tcp_enabled")
    r""" Specifies whether TCP transports are enabled on the server. """

    udp_enabled = fields.Boolean(data_key="udp_enabled")
    r""" Specifies whether UDP transports are enabled on the server. """

    @property
    def resource(self):
        return NfsServiceTransport

    @property
    def patchable_fields(self):
        return [
            "tcp_enabled",
            "udp_enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "tcp_enabled",
            "udp_enabled",
        ]


class NfsServiceTransport(Resource):  # pylint: disable=missing-docstring

    _schema = NfsServiceTransportSchema
