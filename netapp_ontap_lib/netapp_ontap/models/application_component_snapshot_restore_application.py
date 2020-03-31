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


__all__ = ["ApplicationComponentSnapshotRestoreApplication", "ApplicationComponentSnapshotRestoreApplicationSchema"]
__pdoc__ = {
    "ApplicationComponentSnapshotRestoreApplicationSchema.resource": False,
    "ApplicationComponentSnapshotRestoreApplication": False,
}


class ApplicationComponentSnapshotRestoreApplicationSchema(ResourceSchema):
    """The fields of the ApplicationComponentSnapshotRestoreApplication object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_component_snapshot_restore_application. """

    uuid = fields.Str(data_key="uuid")
    r""" Application UUID. Valid in URL or POST """

    @property
    def resource(self):
        return ApplicationComponentSnapshotRestoreApplication

    @property
    def patchable_fields(self):
        return [
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "uuid",
        ]


class ApplicationComponentSnapshotRestoreApplication(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationComponentSnapshotRestoreApplicationSchema
