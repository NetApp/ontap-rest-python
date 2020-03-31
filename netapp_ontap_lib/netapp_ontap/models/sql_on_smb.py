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


__all__ = ["SqlOnSmb", "SqlOnSmbSchema"]
__pdoc__ = {
    "SqlOnSmbSchema.resource": False,
    "SqlOnSmb": False,
}


class SqlOnSmbSchema(ResourceSchema):
    """The fields of the SqlOnSmb object"""

    access = fields.Nested("netapp_ontap.models.sql_on_smb_access.SqlOnSmbAccessSchema", unknown=EXCLUDE, data_key="access")
    r""" The access field of the sql_on_smb. """

    db = fields.Nested("netapp_ontap.models.sql_on_san_db.SqlOnSanDbSchema", unknown=EXCLUDE, data_key="db")
    r""" The db field of the sql_on_smb. """

    log = fields.Nested("netapp_ontap.models.sql_on_san_log.SqlOnSanLogSchema", unknown=EXCLUDE, data_key="log")
    r""" The log field of the sql_on_smb. """

    protection_type = fields.Nested("netapp_ontap.models.mongo_db_on_san_protection_type.MongoDbOnSanProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the sql_on_smb. """

    server_cores_count = fields.Integer(data_key="server_cores_count")
    r""" The number of server cores for the DB. """

    temp_db = fields.Nested("netapp_ontap.models.sql_on_san_temp_db.SqlOnSanTempDbSchema", unknown=EXCLUDE, data_key="temp_db")
    r""" The temp_db field of the sql_on_smb. """

    @property
    def resource(self):
        return SqlOnSmb

    @property
    def patchable_fields(self):
        return [
            "db",
            "log",
            "protection_type",
            "temp_db",
        ]

    @property
    def postable_fields(self):
        return [
            "access",
            "db",
            "log",
            "protection_type",
            "server_cores_count",
            "temp_db",
        ]


class SqlOnSmb(Resource):  # pylint: disable=missing-docstring

    _schema = SqlOnSmbSchema
