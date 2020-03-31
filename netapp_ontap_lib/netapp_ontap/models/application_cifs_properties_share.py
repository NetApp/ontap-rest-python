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


__all__ = ["ApplicationCifsPropertiesShare", "ApplicationCifsPropertiesShareSchema"]
__pdoc__ = {
    "ApplicationCifsPropertiesShareSchema.resource": False,
    "ApplicationCifsPropertiesShare": False,
}


class ApplicationCifsPropertiesShareSchema(ResourceSchema):
    """The fields of the ApplicationCifsPropertiesShare object"""

    name = fields.Str(data_key="name")
    r""" Share name """

    @property
    def resource(self):
        return ApplicationCifsPropertiesShare

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationCifsPropertiesShare(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationCifsPropertiesShareSchema
