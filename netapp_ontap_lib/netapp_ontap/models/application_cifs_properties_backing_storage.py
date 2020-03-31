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


__all__ = ["ApplicationCifsPropertiesBackingStorage", "ApplicationCifsPropertiesBackingStorageSchema"]
__pdoc__ = {
    "ApplicationCifsPropertiesBackingStorageSchema.resource": False,
    "ApplicationCifsPropertiesBackingStorage": False,
}


class ApplicationCifsPropertiesBackingStorageSchema(ResourceSchema):
    """The fields of the ApplicationCifsPropertiesBackingStorage object"""

    type = fields.Str(data_key="type")
    r""" Backing storage type

Valid choices:

* volume """

    uuid = fields.Str(data_key="uuid")
    r""" Backing storage UUID """

    @property
    def resource(self):
        return ApplicationCifsPropertiesBackingStorage

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationCifsPropertiesBackingStorage(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationCifsPropertiesBackingStorageSchema
