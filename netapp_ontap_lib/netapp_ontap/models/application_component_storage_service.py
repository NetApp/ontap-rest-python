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


__all__ = ["ApplicationComponentStorageService", "ApplicationComponentStorageServiceSchema"]
__pdoc__ = {
    "ApplicationComponentStorageServiceSchema.resource": False,
    "ApplicationComponentStorageService": False,
}


class ApplicationComponentStorageServiceSchema(ResourceSchema):
    """The fields of the ApplicationComponentStorageService object"""

    name = fields.Str(data_key="name")
    r""" Storage service name """

    uuid = fields.Str(data_key="uuid")
    r""" Storage service UUID """

    @property
    def resource(self):
        return ApplicationComponentStorageService

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationComponentStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationComponentStorageServiceSchema
