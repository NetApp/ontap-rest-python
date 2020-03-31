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


__all__ = ["OracleOnNfs", "OracleOnNfsSchema"]
__pdoc__ = {
    "OracleOnNfsSchema.resource": False,
    "OracleOnNfs": False,
}


class OracleOnNfsSchema(ResourceSchema):
    """The fields of the OracleOnNfs object"""

    archive_log = fields.Nested("netapp_ontap.models.oracle_on_nfs_archive_log.OracleOnNfsArchiveLogSchema", unknown=EXCLUDE, data_key="archive_log")
    r""" The archive_log field of the oracle_on_nfs. """

    db = fields.Nested("netapp_ontap.models.oracle_on_nfs_db.OracleOnNfsDbSchema", unknown=EXCLUDE, data_key="db")
    r""" The db field of the oracle_on_nfs. """

    nfs_access = fields.List(fields.Nested("netapp_ontap.models.app_nfs_access.AppNfsAccessSchema", unknown=EXCLUDE), data_key="nfs_access")
    r""" The list of NFS access controls. """

    ora_home = fields.Nested("netapp_ontap.models.oracle_on_nfs_ora_home.OracleOnNfsOraHomeSchema", unknown=EXCLUDE, data_key="ora_home")
    r""" The ora_home field of the oracle_on_nfs. """

    protection_type = fields.Nested("netapp_ontap.models.mongo_db_on_san_protection_type.MongoDbOnSanProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the oracle_on_nfs. """

    redo_log = fields.Nested("netapp_ontap.models.oracle_on_nfs_redo_log.OracleOnNfsRedoLogSchema", unknown=EXCLUDE, data_key="redo_log")
    r""" The redo_log field of the oracle_on_nfs. """

    @property
    def resource(self):
        return OracleOnNfs

    @property
    def patchable_fields(self):
        return [
            "archive_log",
            "db",
            "ora_home",
            "protection_type",
            "redo_log",
        ]

    @property
    def postable_fields(self):
        return [
            "archive_log",
            "db",
            "nfs_access",
            "ora_home",
            "protection_type",
            "redo_log",
        ]


class OracleOnNfs(Resource):  # pylint: disable=missing-docstring

    _schema = OracleOnNfsSchema
