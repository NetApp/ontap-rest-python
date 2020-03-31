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


__all__ = ["ApplicationSnapshotRestore", "ApplicationSnapshotRestoreSchema"]
__pdoc__ = {
    "ApplicationSnapshotRestoreSchema.resource": False,
    "ApplicationSnapshotRestore": False,
}


class ApplicationSnapshotRestoreSchema(ResourceSchema):
    """The fields of the ApplicationSnapshotRestore object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_snapshot_restore. """

    application = fields.Nested("netapp_ontap.models.application_snapshot_restore_application.ApplicationSnapshotRestoreApplicationSchema", unknown=EXCLUDE, data_key="application")
    r""" The application field of the application_snapshot_restore. """

    uuid = fields.Str(data_key="uuid")
    r""" The Snapshot copy UUID. Valid in URL or POST. """

    @property
    def resource(self):
        return ApplicationSnapshotRestore

    @property
    def patchable_fields(self):
        return [
            "application",
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "application",
            "uuid",
        ]


class ApplicationSnapshotRestore(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSnapshotRestoreSchema
