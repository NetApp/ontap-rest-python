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


__all__ = ["ApplicationVolumeObject", "ApplicationVolumeObjectSchema"]
__pdoc__ = {
    "ApplicationVolumeObjectSchema.resource": False,
    "ApplicationVolumeObject": False,
}


class ApplicationVolumeObjectSchema(ResourceSchema):
    """The fields of the ApplicationVolumeObject object"""

    creation_timestamp = fields.DateTime(data_key="creation_timestamp")
    r""" Creation time """

    name = fields.Str(data_key="name")
    r""" Name """

    size = fields.Integer(data_key="size")
    r""" Size """

    uuid = fields.Str(data_key="uuid")
    r""" UUID """

    @property
    def resource(self):
        return ApplicationVolumeObject

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationVolumeObject(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationVolumeObjectSchema
