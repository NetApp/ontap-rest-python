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


__all__ = ["ApplicationCifsPropertiesServer", "ApplicationCifsPropertiesServerSchema"]
__pdoc__ = {
    "ApplicationCifsPropertiesServerSchema.resource": False,
    "ApplicationCifsPropertiesServer": False,
}


class ApplicationCifsPropertiesServerSchema(ResourceSchema):
    """The fields of the ApplicationCifsPropertiesServer object"""

    name = fields.Str(data_key="name")
    r""" Server name """

    @property
    def resource(self):
        return ApplicationCifsPropertiesServer

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationCifsPropertiesServer(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationCifsPropertiesServerSchema
