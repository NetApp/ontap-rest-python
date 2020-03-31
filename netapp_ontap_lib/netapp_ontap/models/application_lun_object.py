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


__all__ = ["ApplicationLunObject", "ApplicationLunObjectSchema"]
__pdoc__ = {
    "ApplicationLunObjectSchema.resource": False,
    "ApplicationLunObject": False,
}


class ApplicationLunObjectSchema(ResourceSchema):
    """The fields of the ApplicationLunObject object"""

    creation_timestamp = fields.DateTime(data_key="creation_timestamp")
    r""" LUN creation time """

    path = fields.Str(data_key="path")
    r""" LUN path """

    size = fields.Integer(data_key="size")
    r""" LUN size """

    uuid = fields.Str(data_key="uuid")
    r""" LUN UUID """

    @property
    def resource(self):
        return ApplicationLunObject

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationLunObject(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationLunObjectSchema
