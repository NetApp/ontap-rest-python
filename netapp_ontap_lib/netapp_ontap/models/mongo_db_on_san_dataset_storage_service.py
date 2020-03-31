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


__all__ = ["MongoDbOnSanDatasetStorageService", "MongoDbOnSanDatasetStorageServiceSchema"]
__pdoc__ = {
    "MongoDbOnSanDatasetStorageServiceSchema.resource": False,
    "MongoDbOnSanDatasetStorageService": False,
}


class MongoDbOnSanDatasetStorageServiceSchema(ResourceSchema):
    """The fields of the MongoDbOnSanDatasetStorageService object"""

    name = fields.Str(data_key="name")
    r""" The storage service of the database.

Valid choices:

* extreme
* performance
* value """

    @property
    def resource(self):
        return MongoDbOnSanDatasetStorageService

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


class MongoDbOnSanDatasetStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = MongoDbOnSanDatasetStorageServiceSchema
