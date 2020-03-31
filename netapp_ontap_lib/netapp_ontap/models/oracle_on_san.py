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


__all__ = ["OracleOnSan", "OracleOnSanSchema"]
__pdoc__ = {
    "OracleOnSanSchema.resource": False,
    "OracleOnSan": False,
}


class OracleOnSanSchema(ResourceSchema):
    """The fields of the OracleOnSan object"""

    archive_log = fields.Nested("netapp_ontap.models.oracle_on_nfs_archive_log.OracleOnNfsArchiveLogSchema", unknown=EXCLUDE, data_key="archive_log")
    r""" The archive_log field of the oracle_on_san. """

    db = fields.Nested("netapp_ontap.models.oracle_on_nfs_db.OracleOnNfsDbSchema", unknown=EXCLUDE, data_key="db")
    r""" The db field of the oracle_on_san. """

    igroup_name = fields.Str(data_key="igroup_name")
    r""" The name of the initiator group through which the contents of this application will be accessed. Modification of this parameter is a disruptive operation. All LUNs in the application component will be unmapped from the current igroup and re-mapped to the new igroup. """

    new_igroups = fields.List(fields.Nested("netapp_ontap.models.oracle_on_san_new_igroups.OracleOnSanNewIgroupsSchema", unknown=EXCLUDE), data_key="new_igroups")
    r""" The list of initiator groups to create. """

    ora_home = fields.Nested("netapp_ontap.models.oracle_on_nfs_ora_home.OracleOnNfsOraHomeSchema", unknown=EXCLUDE, data_key="ora_home")
    r""" The ora_home field of the oracle_on_san. """

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
    r""" The protection_type field of the oracle_on_san. """

    redo_log = fields.Nested("netapp_ontap.models.oracle_on_nfs_redo_log.OracleOnNfsRedoLogSchema", unknown=EXCLUDE, data_key="redo_log")
    r""" The redo_log field of the oracle_on_san. """

    @property
    def resource(self):
        return OracleOnSan

    @property
    def patchable_fields(self):
        return [
            "archive_log",
            "db",
            "igroup_name",
            "new_igroups",
            "ora_home",
            "protection_type",
            "redo_log",
        ]

    @property
    def postable_fields(self):
        return [
            "archive_log",
            "db",
            "igroup_name",
            "new_igroups",
            "ora_home",
            "os_type",
            "protection_type",
            "redo_log",
        ]


class OracleOnSan(Resource):  # pylint: disable=missing-docstring

    _schema = OracleOnSanSchema
