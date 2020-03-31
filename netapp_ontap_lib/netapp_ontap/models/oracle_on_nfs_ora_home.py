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


__all__ = ["OracleOnNfsOraHome", "OracleOnNfsOraHomeSchema"]
__pdoc__ = {
    "OracleOnNfsOraHomeSchema.resource": False,
    "OracleOnNfsOraHome": False,
}


class OracleOnNfsOraHomeSchema(ResourceSchema):
    """The fields of the OracleOnNfsOraHome object"""

    size = fields.Integer(data_key="size")
    r""" The size of the ORACLE_HOME storage volume. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = fields.Nested("netapp_ontap.models.oracle_on_nfs_ora_home_storage_service.OracleOnNfsOraHomeStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the oracle_on_nfs_ora_home. """

    @property
    def resource(self):
        return OracleOnNfsOraHome

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


class OracleOnNfsOraHome(Resource):  # pylint: disable=missing-docstring

    _schema = OracleOnNfsOraHomeSchema
