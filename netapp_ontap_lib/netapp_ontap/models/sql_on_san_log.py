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


__all__ = ["SqlOnSanLog", "SqlOnSanLogSchema"]
__pdoc__ = {
    "SqlOnSanLogSchema.resource": False,
    "SqlOnSanLog": False,
}


class SqlOnSanLogSchema(ResourceSchema):
    """The fields of the SqlOnSanLog object"""

    size = fields.Integer(data_key="size")
    r""" The size of the log DB. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = fields.Nested("netapp_ontap.models.sql_on_san_log_storage_service.SqlOnSanLogStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the sql_on_san_log. """

    @property
    def resource(self):
        return SqlOnSanLog

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


class SqlOnSanLog(Resource):  # pylint: disable=missing-docstring

    _schema = SqlOnSanLogSchema
