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


__all__ = ["NdmpMover", "NdmpMoverSchema"]
__pdoc__ = {
    "NdmpMoverSchema.resource": False,
    "NdmpMover": False,
}


class NdmpMoverSchema(ResourceSchema):
    """The fields of the NdmpMover object"""

    bytes_moved = fields.Integer(data_key="bytes_moved")
    r""" Indicates the NDMP mover bytes moved.

Example: 645120 """

    connection = fields.Nested("netapp_ontap.models.ndmp_connect.NdmpConnectSchema", unknown=EXCLUDE, data_key="connection")
    r""" Indicates the NDMP connection attributes. """

    mode = fields.Str(data_key="mode")
    r""" Indicates the NDMP mover mode of operation. """

    reason = fields.Str(data_key="reason")
    r""" Indicates the reason for the NDMP mover pause or halt. """

    state = fields.Str(data_key="state")
    r""" Indicates the NDMP mover state. """

    @property
    def resource(self):
        return NdmpMover

    @property
    def patchable_fields(self):
        return [
            "bytes_moved",
            "connection",
            "mode",
            "reason",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "bytes_moved",
            "connection",
            "mode",
            "reason",
            "state",
        ]


class NdmpMover(Resource):  # pylint: disable=missing-docstring

    _schema = NdmpMoverSchema
