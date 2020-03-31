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


__all__ = ["MongoDbOnSanDataset", "MongoDbOnSanDatasetSchema"]
__pdoc__ = {
    "MongoDbOnSanDatasetSchema.resource": False,
    "MongoDbOnSanDataset": False,
}


class MongoDbOnSanDatasetSchema(ResourceSchema):
    """The fields of the MongoDbOnSanDataset object"""

    element_count = fields.Integer(data_key="element_count")
    r""" The number of storage elements (LUNs for SAN) of the database to maintain.  Must be an even number between 2 and 16.  Odd numbers will be rounded up to the next even number within range. """

    replication_factor = fields.Integer(data_key="replication_factor")
    r""" The number of data bearing members of the replicaset, including 1 primary and at least 1 secondary. """

    size = fields.Integer(data_key="size")
    r""" The size of the database. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = fields.Nested("netapp_ontap.models.mongo_db_on_san_dataset_storage_service.MongoDbOnSanDatasetStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the mongo_db_on_san_dataset. """

    @property
    def resource(self):
        return MongoDbOnSanDataset

    @property
    def patchable_fields(self):
        return [
            "size",
            "storage_service",
        ]

    @property
    def postable_fields(self):
        return [
            "element_count",
            "replication_factor",
            "size",
            "storage_service",
        ]


class MongoDbOnSanDataset(Resource):  # pylint: disable=missing-docstring

    _schema = MongoDbOnSanDatasetSchema
