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


__all__ = ["SqlOnSan", "SqlOnSanSchema"]
__pdoc__ = {
    "SqlOnSanSchema.resource": False,
    "SqlOnSan": False,
}


class SqlOnSanSchema(ResourceSchema):
    """The fields of the SqlOnSan object"""

    db = fields.Nested("netapp_ontap.models.sql_on_san_db.SqlOnSanDbSchema", unknown=EXCLUDE, data_key="db")
    r""" The db field of the sql_on_san. """

    igroup_name = fields.Str(data_key="igroup_name")
    r""" The name of the initiator group through which the contents of this application will be accessed. Modification of this parameter is a disruptive operation. All LUNs in the application component will be unmapped from the current igroup and re-mapped to the new igroup. """

    log = fields.Nested("netapp_ontap.models.sql_on_san_log.SqlOnSanLogSchema", unknown=EXCLUDE, data_key="log")
    r""" The log field of the sql_on_san. """

    new_igroups = fields.List(fields.Nested("netapp_ontap.models.sql_on_san_new_igroups.SqlOnSanNewIgroupsSchema", unknown=EXCLUDE), data_key="new_igroups")
    r""" The list of initiator groups to create. """

    os_type = fields.Str(data_key="os_type")
    r""" The name of the host OS running the application.

Valid choices:

* windows
* windows_2008
* windows_gpt """

    protection_type = fields.Nested("netapp_ontap.models.mongo_db_on_san_protection_type.MongoDbOnSanProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the sql_on_san. """

    server_cores_count = fields.Integer(data_key="server_cores_count")
    r""" The number of server cores for the DB. """

    temp_db = fields.Nested("netapp_ontap.models.sql_on_san_temp_db.SqlOnSanTempDbSchema", unknown=EXCLUDE, data_key="temp_db")
    r""" The temp_db field of the sql_on_san. """

    @property
    def resource(self):
        return SqlOnSan

    @property
    def patchable_fields(self):
        return [
            "db",
            "igroup_name",
            "log",
            "new_igroups",
            "protection_type",
            "temp_db",
        ]

    @property
    def postable_fields(self):
        return [
            "db",
            "igroup_name",
            "log",
            "new_igroups",
            "os_type",
            "protection_type",
            "server_cores_count",
            "temp_db",
        ]


class SqlOnSan(Resource):  # pylint: disable=missing-docstring

    _schema = SqlOnSanSchema
