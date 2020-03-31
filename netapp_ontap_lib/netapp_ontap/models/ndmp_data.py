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


__all__ = ["NdmpData", "NdmpDataSchema"]
__pdoc__ = {
    "NdmpDataSchema.resource": False,
    "NdmpData": False,
}


class NdmpDataSchema(ResourceSchema):
    """The fields of the NdmpData object"""

    bytes_processed = fields.Integer(data_key="bytes_processed")
    r""" Indicates the NDMP data bytes processed.

Example: 5000 """

    connection = fields.Nested("netapp_ontap.models.ndmp_connect.NdmpConnectSchema", unknown=EXCLUDE, data_key="connection")
    r""" Indicates the NDMP connection attributes. """

    operation = fields.Str(data_key="operation")
    r""" Indicates the NDMP data server operation.

Valid choices:

* backup
* restore
* none """

    reason = fields.Str(data_key="reason")
    r""" Indicates the reason for the NDMP data server halt. """

    state = fields.Str(data_key="state")
    r""" Indicates the state of the NDMP data server. """

    @property
    def resource(self):
        return NdmpData

    @property
    def patchable_fields(self):
        return [
            "bytes_processed",
            "connection",
            "operation",
            "reason",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "bytes_processed",
            "connection",
            "operation",
            "reason",
            "state",
        ]


class NdmpData(Resource):  # pylint: disable=missing-docstring

    _schema = NdmpDataSchema
