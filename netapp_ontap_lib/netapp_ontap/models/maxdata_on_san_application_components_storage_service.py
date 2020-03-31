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


__all__ = ["MaxdataOnSanApplicationComponentsStorageService", "MaxdataOnSanApplicationComponentsStorageServiceSchema"]
__pdoc__ = {
    "MaxdataOnSanApplicationComponentsStorageServiceSchema.resource": False,
    "MaxdataOnSanApplicationComponentsStorageService": False,
}


class MaxdataOnSanApplicationComponentsStorageServiceSchema(ResourceSchema):
    """The fields of the MaxdataOnSanApplicationComponentsStorageService object"""

    name = fields.Str(data_key="name")
    r""" The storage service of the application component.

Valid choices:

* extreme
* maxdata
* performance
* value """

    @property
    def resource(self):
        return MaxdataOnSanApplicationComponentsStorageService

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class MaxdataOnSanApplicationComponentsStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = MaxdataOnSanApplicationComponentsStorageServiceSchema
