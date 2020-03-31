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


__all__ = ["ApplicationComponentSnapshotApplication", "ApplicationComponentSnapshotApplicationSchema"]
__pdoc__ = {
    "ApplicationComponentSnapshotApplicationSchema.resource": False,
    "ApplicationComponentSnapshotApplication": False,
}


class ApplicationComponentSnapshotApplicationSchema(ResourceSchema):
    """The fields of the ApplicationComponentSnapshotApplication object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_component_snapshot_application. """

    name = fields.Str(data_key="name")
    r""" Application Name """

    uuid = fields.Str(data_key="uuid")
    r""" Application UUID. Valid in URL """

    @property
    def resource(self):
        return ApplicationComponentSnapshotApplication

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationComponentSnapshotApplication(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationComponentSnapshotApplicationSchema
