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


__all__ = ["RaidGroupDisk", "RaidGroupDiskSchema"]
__pdoc__ = {
    "RaidGroupDiskSchema.resource": False,
    "RaidGroupDisk": False,
}


class RaidGroupDiskSchema(ResourceSchema):
    """The fields of the RaidGroupDisk object"""

    disk = fields.Nested("netapp_ontap.resources.disk.DiskSchema", unknown=EXCLUDE, data_key="disk")
    r""" The disk field of the raid_group_disk. """

    position = fields.Str(data_key="position")
    r""" The position of the disk within the RAID group.

Valid choices:

* data
* parity
* dparity
* tparity
* copy """

    state = fields.Str(data_key="state")
    r""" The state of the disk within the RAID group.

Valid choices:

* normal
* failed
* zeroing
* copy
* replacing
* evacuating
* prefail
* offline
* reconstructing """

    type = fields.Str(data_key="type")
    r""" Disk interface type

Valid choices:

* ata
* bsas
* fcal
* fsas
* lun
* sas
* msata
* ssd
* vmdisk
* unknown
* ssd_nvm """

    usable_size = fields.Integer(data_key="usable_size")
    r""" Size in bytes that is usable by the aggregate.

Example: 947912704 """

    @property
    def resource(self):
        return RaidGroupDisk

    @property
    def patchable_fields(self):
        return [
            "disk.name",
        ]

    @property
    def postable_fields(self):
        return [
            "disk.name",
        ]


class RaidGroupDisk(Resource):  # pylint: disable=missing-docstring

    _schema = RaidGroupDiskSchema
