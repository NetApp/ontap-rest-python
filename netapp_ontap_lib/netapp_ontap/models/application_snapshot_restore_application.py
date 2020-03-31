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


__all__ = ["ApplicationSnapshotRestoreApplication", "ApplicationSnapshotRestoreApplicationSchema"]
__pdoc__ = {
    "ApplicationSnapshotRestoreApplicationSchema.resource": False,
    "ApplicationSnapshotRestoreApplication": False,
}


class ApplicationSnapshotRestoreApplicationSchema(ResourceSchema):
    """The fields of the ApplicationSnapshotRestoreApplication object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_snapshot_restore_application. """

    uuid = fields.Str(data_key="uuid")
    r""" The application UUID. Valid in URL or POST. """

    @property
    def resource(self):
        return ApplicationSnapshotRestoreApplication

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


class ApplicationSnapshotRestoreApplication(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSnapshotRestoreApplicationSchema
