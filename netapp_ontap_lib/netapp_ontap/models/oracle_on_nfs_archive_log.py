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


__all__ = ["OracleOnNfsArchiveLog", "OracleOnNfsArchiveLogSchema"]
__pdoc__ = {
    "OracleOnNfsArchiveLogSchema.resource": False,
    "OracleOnNfsArchiveLog": False,
}


class OracleOnNfsArchiveLogSchema(ResourceSchema):
    """The fields of the OracleOnNfsArchiveLog object"""

    size = fields.Integer(data_key="size")
    r""" The size of the archive log. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = fields.Nested("netapp_ontap.models.oracle_on_nfs_archive_log_storage_service.OracleOnNfsArchiveLogStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the oracle_on_nfs_archive_log. """

    @property
    def resource(self):
        return OracleOnNfsArchiveLog

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


class OracleOnNfsArchiveLog(Resource):  # pylint: disable=missing-docstring

    _schema = OracleOnNfsArchiveLogSchema
