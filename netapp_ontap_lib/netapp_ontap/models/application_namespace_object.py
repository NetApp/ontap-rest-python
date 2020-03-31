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


__all__ = ["ApplicationNamespaceObject", "ApplicationNamespaceObjectSchema"]
__pdoc__ = {
    "ApplicationNamespaceObjectSchema.resource": False,
    "ApplicationNamespaceObject": False,
}


class ApplicationNamespaceObjectSchema(ResourceSchema):
    """The fields of the ApplicationNamespaceObject object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_namespace_object. """

    creation_timestamp = fields.DateTime(data_key="creation_timestamp")
    r""" Namespace creation time """

    name = fields.Str(data_key="name")
    r""" Namespace name """

    size = fields.Integer(data_key="size")
    r""" Namespace size """

    uuid = fields.Str(data_key="uuid")
    r""" Namespace UUID """

    @property
    def resource(self):
        return ApplicationNamespaceObject

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationNamespaceObject(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationNamespaceObjectSchema
