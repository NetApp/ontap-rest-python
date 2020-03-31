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


__all__ = ["AggregateSpaceCloudStorage", "AggregateSpaceCloudStorageSchema"]
__pdoc__ = {
    "AggregateSpaceCloudStorageSchema.resource": False,
    "AggregateSpaceCloudStorage": False,
}


class AggregateSpaceCloudStorageSchema(ResourceSchema):
    """The fields of the AggregateSpaceCloudStorage object"""

    used = fields.Integer(data_key="used")
    r""" Used space in bytes in the cloud store. Only applicable for aggregate with a cloud store tier.

Example: 402743264 """

    @property
    def resource(self):
        return AggregateSpaceCloudStorage

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class AggregateSpaceCloudStorage(Resource):  # pylint: disable=missing-docstring

    _schema = AggregateSpaceCloudStorageSchema
