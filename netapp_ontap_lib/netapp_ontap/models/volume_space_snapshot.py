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


__all__ = ["VolumeSpaceSnapshot", "VolumeSpaceSnapshotSchema"]
__pdoc__ = {
    "VolumeSpaceSnapshotSchema.resource": False,
    "VolumeSpaceSnapshot": False,
}


class VolumeSpaceSnapshotSchema(ResourceSchema):
    """The fields of the VolumeSpaceSnapshot object"""

    autodelete_enabled = fields.Boolean(data_key="autodelete_enabled")
    r""" Specifies whether Snapshot copy autodelete is currently enabled on this volume. """

    reserve_percent = fields.Integer(data_key="reserve_percent")
    r""" The space that has been set aside as a reserve for Snapshot copy usage, in percent. """

    used = fields.Integer(data_key="used")
    r""" The total space used by Snapshot copies in the volume, in bytes. """

    @property
    def resource(self):
        return VolumeSpaceSnapshot

    @property
    def patchable_fields(self):
        return [
            "autodelete_enabled",
            "reserve_percent",
        ]

    @property
    def postable_fields(self):
        return [
            "reserve_percent",
        ]


class VolumeSpaceSnapshot(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeSpaceSnapshotSchema
