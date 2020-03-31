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


__all__ = ["OracleOnNfsRedoLog", "OracleOnNfsRedoLogSchema"]
__pdoc__ = {
    "OracleOnNfsRedoLogSchema.resource": False,
    "OracleOnNfsRedoLog": False,
}


class OracleOnNfsRedoLogSchema(ResourceSchema):
    """The fields of the OracleOnNfsRedoLog object"""

    mirrored = fields.Boolean(data_key="mirrored")
    r""" Specifies whether the redo log group should be mirrored. """

    size = fields.Integer(data_key="size")
    r""" The size of the redo log group. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = fields.Nested("netapp_ontap.models.oracle_on_nfs_redo_log_storage_service.OracleOnNfsRedoLogStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the oracle_on_nfs_redo_log. """

    @property
    def resource(self):
        return OracleOnNfsRedoLog

    @property
    def patchable_fields(self):
        return [
            "size",
            "storage_service",
        ]

    @property
    def postable_fields(self):
        return [
            "mirrored",
            "size",
            "storage_service",
        ]


class OracleOnNfsRedoLog(Resource):  # pylint: disable=missing-docstring

    _schema = OracleOnNfsRedoLogSchema
