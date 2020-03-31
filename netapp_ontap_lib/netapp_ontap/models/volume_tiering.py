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


__all__ = ["VolumeTiering", "VolumeTieringSchema"]
__pdoc__ = {
    "VolumeTieringSchema.resource": False,
    "VolumeTiering": False,
}


class VolumeTieringSchema(ResourceSchema):
    """The fields of the VolumeTiering object"""

    policy = fields.Str(data_key="policy")
    r""" Policy that determines whether the user data blocks of a volume in a FabricPool will be tiered to the cloud store when they become cold. FabricPool combines flash (performance tier) with a cloud store into a single aggregate. Temperature of a volume block increases if it is accessed frequently and decreases when it is not. Valid in POST or PATCH.<br>all &dash; This policy allows tiering of both Snapshot copies and active file system user data to the cloud store as soon as possible by ignoring the temperature on the volume blocks.<br>auto &dash; This policy allows tiering of both snapshot and active file system user data to the cloud store<br>none &dash; Volume blocks will not be tiered to the cloud store.<br>snapshot_only &dash; This policy allows tiering of only the volume Snapshot copies not associated with the active file system. The default tiering policy is "snapshot-only" for a FlexVol and "none" for a FlexGroup.

Valid choices:

* all
* auto
* backup
* none
* snapshot_only """

    supported = fields.Boolean(data_key="supported")
    r""" This parameter specifies whether or not FabricPools are selected when provisioning a FlexGroup without specifying "aggregates.name" or "aggregates.uuid". Only FabricPool aggregates are used if this parameter is set to true and only non FabricPool aggregates are used if this parameter is set to false. Tiering support for a FlexGroup can be changed by moving all of the constituents to the required aggregates. Note that in order to tier data, not only does the volume need to support tiering by using FabricPools, the tiering "policy" must not be 'none'. A volume that uses FabricPools but has a tiering "policy" of 'none' supports tiering, but will not tier any data. """

    @property
    def resource(self):
        return VolumeTiering

    @property
    def patchable_fields(self):
        return [
            "policy",
        ]

    @property
    def postable_fields(self):
        return [
            "policy",
            "supported",
        ]


class VolumeTiering(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeTieringSchema
