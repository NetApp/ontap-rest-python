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


__all__ = ["RaidGroup", "RaidGroupSchema"]
__pdoc__ = {
    "RaidGroupSchema.resource": False,
    "RaidGroup": False,
}


class RaidGroupSchema(ResourceSchema):
    """The fields of the RaidGroup object"""

    cache_tier = fields.Boolean(data_key="cache_tier")
    r""" RAID group is a cache tier """

    degraded = fields.Boolean(data_key="degraded")
    r""" RAID group is degraded. A RAID group is degraded when at least one disk from that group has failed or is offline. """

    disks = fields.List(fields.Nested("netapp_ontap.models.raid_group_disk.RaidGroupDiskSchema", unknown=EXCLUDE), data_key="disks")
    r""" The disks field of the raid_group. """

    name = fields.Str(data_key="name")
    r""" RAID group name

Example: rg0 """

    recomputing_parity = fields.Nested("netapp_ontap.models.raid_group_recomputing_parity.RaidGroupRecomputingParitySchema", unknown=EXCLUDE, data_key="recomputing_parity")
    r""" The recomputing_parity field of the raid_group. """

    reconstruct = fields.Nested("netapp_ontap.models.raid_group_reconstruct.RaidGroupReconstructSchema", unknown=EXCLUDE, data_key="reconstruct")
    r""" The reconstruct field of the raid_group. """

    @property
    def resource(self):
        return RaidGroup

    @property
    def patchable_fields(self):
        return [
            "recomputing_parity",
            "reconstruct",
        ]

    @property
    def postable_fields(self):
        return [
            "recomputing_parity",
            "reconstruct",
        ]


class RaidGroup(Resource):  # pylint: disable=missing-docstring

    _schema = RaidGroupSchema
