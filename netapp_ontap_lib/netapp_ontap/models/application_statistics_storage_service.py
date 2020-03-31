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


__all__ = ["ApplicationStatisticsStorageService", "ApplicationStatisticsStorageServiceSchema"]
__pdoc__ = {
    "ApplicationStatisticsStorageServiceSchema.resource": False,
    "ApplicationStatisticsStorageService": False,
}


class ApplicationStatisticsStorageServiceSchema(ResourceSchema):
    """The fields of the ApplicationStatisticsStorageService object"""

    name = fields.Str(data_key="name")
    r""" The storage service name. AFF systems support the extreme storage service. All other systems only support value. """

    uuid = fields.Str(data_key="uuid")
    r""" The storage service UUID. """

    @property
    def resource(self):
        return ApplicationStatisticsStorageService

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationStatisticsStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationStatisticsStorageServiceSchema
