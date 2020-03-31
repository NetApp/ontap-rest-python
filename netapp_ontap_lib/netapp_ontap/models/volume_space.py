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


__all__ = ["VolumeSpace", "VolumeSpaceSchema"]
__pdoc__ = {
    "VolumeSpaceSchema.resource": False,
    "VolumeSpace": False,
}


class VolumeSpaceSchema(ResourceSchema):
    """The fields of the VolumeSpace object"""

    available = fields.Integer(data_key="available")
    r""" The available space, in bytes. """

    block_storage_inactive_user_data = fields.Integer(data_key="block_storage_inactive_user_data")
    r""" The size that is physically used in the block storage of the volume and has a cold temperature. In bytes. This parameter is only supported if the volume is in an aggregate that is either attached to a cloud store or could be attached to a cloud store. """

    capacity_tier_footprint = fields.Integer(data_key="capacity_tier_footprint")
    r""" The space used by capacity tier for this volume in the aggregate, in bytes. """

    footprint = fields.Integer(data_key="footprint")
    r""" Data and metadata used for this volume in the aggregate, in bytes. """

    logical_space = fields.Nested("netapp_ontap.models.volume_space_logical_space.VolumeSpaceLogicalSpaceSchema", unknown=EXCLUDE, data_key="logical_space")
    r""" The logical_space field of the volume_space. """

    metadata = fields.Integer(data_key="metadata")
    r""" The space used by the total metadata in the volume, in bytes. """

    over_provisioned = fields.Integer(data_key="over_provisioned")
    r""" The amount of space not available for this volume in the aggregate, in bytes. """

    size = fields.Integer(data_key="size")
    r""" Total provisioned size. The default size is equal to the minimum size of 20MB, in bytes. """

    snapshot = fields.Nested("netapp_ontap.models.volume_space_snapshot.VolumeSpaceSnapshotSchema", unknown=EXCLUDE, data_key="snapshot")
    r""" The snapshot field of the volume_space. """

    used = fields.Integer(data_key="used")
    r""" The virtual space used (includes volume reserves) before storage efficiency, in bytes. """

    @property
    def resource(self):
        return VolumeSpace

    @property
    def patchable_fields(self):
        return [
            "logical_space",
            "size",
            "snapshot",
        ]

    @property
    def postable_fields(self):
        return [
            "logical_space",
            "size",
            "snapshot",
        ]


class VolumeSpace(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeSpaceSchema
