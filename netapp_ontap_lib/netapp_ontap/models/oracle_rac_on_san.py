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


__all__ = ["OracleRacOnSan", "OracleRacOnSanSchema"]
__pdoc__ = {
    "OracleRacOnSanSchema.resource": False,
    "OracleRacOnSan": False,
}


class OracleRacOnSanSchema(ResourceSchema):
    """The fields of the OracleRacOnSan object"""

    archive_log = fields.Nested("netapp_ontap.models.oracle_on_nfs_archive_log.OracleOnNfsArchiveLogSchema", unknown=EXCLUDE, data_key="archive_log")
    r""" The archive_log field of the oracle_rac_on_san. """

    db = fields.Nested("netapp_ontap.models.oracle_on_nfs_db.OracleOnNfsDbSchema", unknown=EXCLUDE, data_key="db")
    r""" The db field of the oracle_rac_on_san. """

    db_sids = fields.List(fields.Nested("netapp_ontap.models.oracle_rac_on_san_db_sids.OracleRacOnSanDbSidsSchema", unknown=EXCLUDE), data_key="db_sids")
    r""" The db_sids field of the oracle_rac_on_san. """

    grid_binary = fields.Nested("netapp_ontap.models.oracle_rac_on_nfs_grid_binary.OracleRacOnNfsGridBinarySchema", unknown=EXCLUDE, data_key="grid_binary")
    r""" The grid_binary field of the oracle_rac_on_san. """

    new_igroups = fields.List(fields.Nested("netapp_ontap.models.oracle_rac_on_san_new_igroups.OracleRacOnSanNewIgroupsSchema", unknown=EXCLUDE), data_key="new_igroups")
    r""" The list of initiator groups to create. """

    ora_home = fields.Nested("netapp_ontap.models.oracle_on_nfs_ora_home.OracleOnNfsOraHomeSchema", unknown=EXCLUDE, data_key="ora_home")
    r""" The ora_home field of the oracle_rac_on_san. """

    oracle_crs = fields.Nested("netapp_ontap.models.oracle_rac_on_nfs_oracle_crs.OracleRacOnNfsOracleCrsSchema", unknown=EXCLUDE, data_key="oracle_crs")
    r""" The oracle_crs field of the oracle_rac_on_san. """

    os_type = fields.Str(data_key="os_type")
    r""" The name of the host OS running the application.

Valid choices:

* aix
* hpux
* hyper_v
* linux
* solaris
* solaris_efi
* vmware
* windows
* windows_2008
* windows_gpt
* xen """

    protection_type = fields.Nested("netapp_ontap.models.mongo_db_on_san_protection_type.MongoDbOnSanProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the oracle_rac_on_san. """

    redo_log = fields.Nested("netapp_ontap.models.oracle_on_nfs_redo_log.OracleOnNfsRedoLogSchema", unknown=EXCLUDE, data_key="redo_log")
    r""" The redo_log field of the oracle_rac_on_san. """

    @property
    def resource(self):
        return OracleRacOnSan

    @property
    def patchable_fields(self):
        return [
            "archive_log",
            "db",
            "db_sids",
            "grid_binary",
            "new_igroups",
            "ora_home",
            "oracle_crs",
            "protection_type",
            "redo_log",
        ]

    @property
    def postable_fields(self):
        return [
            "archive_log",
            "db",
            "db_sids",
            "grid_binary",
            "new_igroups",
            "ora_home",
            "oracle_crs",
            "os_type",
            "protection_type",
            "redo_log",
        ]


class OracleRacOnSan(Resource):  # pylint: disable=missing-docstring

    _schema = OracleRacOnSanSchema
