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


__all__ = ["ApplicationComponentSnapshotRestore", "ApplicationComponentSnapshotRestoreSchema"]
__pdoc__ = {
    "ApplicationComponentSnapshotRestoreSchema.resource": False,
    "ApplicationComponentSnapshotRestore": False,
}


class ApplicationComponentSnapshotRestoreSchema(ResourceSchema):
    """The fields of the ApplicationComponentSnapshotRestore object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_component_snapshot_restore. """

    application = fields.Nested("netapp_ontap.models.application_component_snapshot_restore_application.ApplicationComponentSnapshotRestoreApplicationSchema", unknown=EXCLUDE, data_key="application")
    r""" The application field of the application_component_snapshot_restore. """

    component = fields.Nested("netapp_ontap.models.application_component_snapshot_restore_component.ApplicationComponentSnapshotRestoreComponentSchema", unknown=EXCLUDE, data_key="component")
    r""" The component field of the application_component_snapshot_restore. """

    uuid = fields.Str(data_key="uuid")
    r""" Snapshot UUID. Valid in URL or POST """

    @property
    def resource(self):
        return ApplicationComponentSnapshotRestore

    @property
    def patchable_fields(self):
        return [
            "application",
            "component",
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "application",
            "component",
            "uuid",
        ]


class ApplicationComponentSnapshotRestore(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationComponentSnapshotRestoreSchema
