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


__all__ = ["SqlOnSanTempDb", "SqlOnSanTempDbSchema"]
__pdoc__ = {
    "SqlOnSanTempDbSchema.resource": False,
    "SqlOnSanTempDb": False,
}


class SqlOnSanTempDbSchema(ResourceSchema):
    """The fields of the SqlOnSanTempDb object"""

    size = fields.Integer(data_key="size")
    r""" The size of the temp DB. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = fields.Nested("netapp_ontap.models.sql_on_san_temp_db_storage_service.SqlOnSanTempDbStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the sql_on_san_temp_db. """

    @property
    def resource(self):
        return SqlOnSanTempDb

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


class SqlOnSanTempDb(Resource):  # pylint: disable=missing-docstring

    _schema = SqlOnSanTempDbSchema
