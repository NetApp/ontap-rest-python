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


__all__ = ["ClusterSpaceBlockStorageMedias", "ClusterSpaceBlockStorageMediasSchema"]
__pdoc__ = {
    "ClusterSpaceBlockStorageMediasSchema.resource": False,
    "ClusterSpaceBlockStorageMedias": False,
}


class ClusterSpaceBlockStorageMediasSchema(ResourceSchema):
    """The fields of the ClusterSpaceBlockStorageMedias object"""

    available = fields.Integer(data_key="available")
    r""" Available space """

    efficiency = fields.Nested("netapp_ontap.models.space_efficiency.SpaceEfficiencySchema", unknown=EXCLUDE, data_key="efficiency")
    r""" The efficiency field of the cluster_space_block_storage_medias. """

    size = fields.Integer(data_key="size")
    r""" Total space """

    type = fields.Str(data_key="type")
    r""" The type of media being used

Valid choices:

* hdd
* hybrid
* lun
* ssd
* vmdisk """

    used = fields.Integer(data_key="used")
    r""" Used space """

    @property
    def resource(self):
        return ClusterSpaceBlockStorageMedias

    @property
    def patchable_fields(self):
        return [
            "available",
            "efficiency",
            "size",
            "type",
            "used",
        ]

    @property
    def postable_fields(self):
        return [
            "available",
            "efficiency",
            "size",
            "type",
            "used",
        ]


class ClusterSpaceBlockStorageMedias(Resource):  # pylint: disable=missing-docstring

    _schema = ClusterSpaceBlockStorageMediasSchema
