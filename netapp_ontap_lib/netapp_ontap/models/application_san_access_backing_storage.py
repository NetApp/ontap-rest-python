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


__all__ = ["ApplicationSanAccessBackingStorage", "ApplicationSanAccessBackingStorageSchema"]
__pdoc__ = {
    "ApplicationSanAccessBackingStorageSchema.resource": False,
    "ApplicationSanAccessBackingStorage": False,
}


class ApplicationSanAccessBackingStorageSchema(ResourceSchema):
    """The fields of the ApplicationSanAccessBackingStorage object"""

    type = fields.Str(data_key="type")
    r""" Backing storage type

Valid choices:

* lun """

    uuid = fields.Str(data_key="uuid")
    r""" Backing storage UUID """

    @property
    def resource(self):
        return ApplicationSanAccessBackingStorage

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationSanAccessBackingStorage(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSanAccessBackingStorageSchema
