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


__all__ = ["CloudStorageTier", "CloudStorageTierSchema"]
__pdoc__ = {
    "CloudStorageTierSchema.resource": False,
    "CloudStorageTier": False,
}


class CloudStorageTierSchema(ResourceSchema):
    """The fields of the CloudStorageTier object"""

    cloud_store = fields.Nested("netapp_ontap.resources.cloud_store.CloudStoreSchema", unknown=EXCLUDE, data_key="cloud_store")
    r""" The cloud_store field of the cloud_storage_tier. """

    used = fields.Integer(data_key="used")
    r""" Capacity used in bytes in the cloud store by this aggregate. This is a cached value calculated every 5 minutes. """

    @property
    def resource(self):
        return CloudStorageTier

    @property
    def patchable_fields(self):
        return [
            "cloud_store.name",
            "cloud_store.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "cloud_store.name",
            "cloud_store.uuid",
        ]


class CloudStorageTier(Resource):  # pylint: disable=missing-docstring

    _schema = CloudStorageTierSchema
