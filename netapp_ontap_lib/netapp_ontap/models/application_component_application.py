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


__all__ = ["ApplicationComponentApplication", "ApplicationComponentApplicationSchema"]
__pdoc__ = {
    "ApplicationComponentApplicationSchema.resource": False,
    "ApplicationComponentApplication": False,
}


class ApplicationComponentApplicationSchema(ResourceSchema):
    """The fields of the ApplicationComponentApplication object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_component_application. """

    name = fields.Str(data_key="name")
    r""" Application name """

    uuid = fields.Str(data_key="uuid")
    r""" The application UUID. Valid in URL. """

    @property
    def resource(self):
        return ApplicationComponentApplication

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationComponentApplication(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationComponentApplicationSchema
