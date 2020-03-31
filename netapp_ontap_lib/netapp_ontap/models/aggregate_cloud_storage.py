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


__all__ = ["AggregateCloudStorage", "AggregateCloudStorageSchema"]
__pdoc__ = {
    "AggregateCloudStorageSchema.resource": False,
    "AggregateCloudStorage": False,
}


class AggregateCloudStorageSchema(ResourceSchema):
    """The fields of the AggregateCloudStorage object"""

    attach_eligible = fields.Boolean(data_key="attach_eligible")
    r""" Aggregate is eligible for a cloud store to be attached. """

    stores = fields.List(fields.Nested("netapp_ontap.models.cloud_storage_tier.CloudStorageTierSchema", unknown=EXCLUDE), data_key="stores")
    r""" Configuration information for each cloud storage portion of the aggregate. """

    tiering_fullness_threshold = fields.Integer(data_key="tiering_fullness_threshold")
    r""" The percentage of space in the performance tier that must be used before data is tiered out to the cloud store. Only valid for PATCH operations. """

    @property
    def resource(self):
        return AggregateCloudStorage

    @property
    def patchable_fields(self):
        return [
            "tiering_fullness_threshold",
        ]

    @property
    def postable_fields(self):
        return [
        ]


class AggregateCloudStorage(Resource):  # pylint: disable=missing-docstring

    _schema = AggregateCloudStorageSchema
