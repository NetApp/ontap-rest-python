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


__all__ = ["ClusterSpaceCloudStorage", "ClusterSpaceCloudStorageSchema"]
__pdoc__ = {
    "ClusterSpaceCloudStorageSchema.resource": False,
    "ClusterSpaceCloudStorage": False,
}


class ClusterSpaceCloudStorageSchema(ResourceSchema):
    """The fields of the ClusterSpaceCloudStorage object"""

    used = fields.Integer(data_key="used")
    r""" Total space used in cloud. """

    @property
    def resource(self):
        return ClusterSpaceCloudStorage

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ClusterSpaceCloudStorage(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterSpaceCloudStorageSchema
