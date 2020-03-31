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


__all__ = ["OracleRacOnNfsGridBinary", "OracleRacOnNfsGridBinarySchema"]
__pdoc__ = {
    "OracleRacOnNfsGridBinarySchema.resource": False,
    "OracleRacOnNfsGridBinary": False,
}


class OracleRacOnNfsGridBinarySchema(ResourceSchema):
    """The fields of the OracleRacOnNfsGridBinary object"""

    size = fields.Integer(data_key="size")
    r""" The size of the Oracle grid binary storage volume. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = fields.Nested("netapp_ontap.models.oracle_rac_on_nfs_grid_binary_storage_service.OracleRacOnNfsGridBinaryStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the oracle_rac_on_nfs_grid_binary. """

    @property
    def resource(self):
        return OracleRacOnNfsGridBinary

    @property
    def patchable_fields(self):
        return [
            "size",
            "storage_service",
        ]

    @property
    def postable_fields(self):
        return [
            "size",
            "storage_service",
        ]


class OracleRacOnNfsGridBinary(Resource):  # pylint: disable=missing-docstring

    _schema = OracleRacOnNfsGridBinarySchema
