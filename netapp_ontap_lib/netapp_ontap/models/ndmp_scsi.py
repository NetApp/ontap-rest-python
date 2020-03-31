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


__all__ = ["NdmpScsi", "NdmpScsiSchema"]
__pdoc__ = {
    "NdmpScsiSchema.resource": False,
    "NdmpScsi": False,
}


class NdmpScsiSchema(ResourceSchema):
    """The fields of the NdmpScsi object"""

    device_id = fields.Str(data_key="device_id")
    r""" Indicates the NDMP SCSI device ID. """

    host_adapter = fields.Integer(data_key="host_adapter")
    r""" Indicates the NDMP SCSI host adapter. """

    lun_id = fields.Integer(data_key="lun_id")
    r""" Indicates the NDMP SCSI LUN ID. """

    target_id = fields.Integer(data_key="target_id")
    r""" Indicates the NDMP SCSI target ID. """

    @property
    def resource(self):
        return NdmpScsi

    @property
    def patchable_fields(self):
        return [
            "device_id",
            "host_adapter",
            "lun_id",
            "target_id",
        ]

    @property
    def postable_fields(self):
        return [
            "device_id",
            "host_adapter",
            "lun_id",
            "target_id",
        ]


class NdmpScsi(Resource):  # pylint: disable=missing-docstring

    _schema = NdmpScsiSchema
