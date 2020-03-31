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


__all__ = ["SnapmirrorDestinationCreationTiering", "SnapmirrorDestinationCreationTieringSchema"]
__pdoc__ = {
    "SnapmirrorDestinationCreationTieringSchema.resource": False,
    "SnapmirrorDestinationCreationTiering": False,
}


class SnapmirrorDestinationCreationTieringSchema(ResourceSchema):
    """The fields of the SnapmirrorDestinationCreationTiering object"""

    policy = fields.Str(data_key="policy")
    r""" Optional property to specify the destination endpoint's tiering policy when "create_destination.tiering.supported" is set to "true". This property is applicable to FlexVol volume and FlexGroup volume endpoints. This property determines whether the user data blocks of the destination endpoint in a FabricPool will be tiered to the cloud store when they become cold. FabricPool combines flash (performance tier) with a cloud store into a single aggregate. Temperature of the destination endpoint volume blocks increases if they are accessed frequently and decreases when they are not.<br>all &dash; This policy allows tiering of both destination endpoint Snapshot copies and the user transfered data blocks to the cloud store as soon as possible by ignoring the temperature on the volume blocks. This tiering policy is not applicable for synchronous relationships.<br>auto &dash; This policy allows tiering of both destination endpoint Snapshot copies and the active file system user data to the cloud store<br>none &dash; Destination endpoint volume blocks will not be tiered to the cloud store.<br>snapshot_only &dash; This policy allows tiering of only the destination endpoint volume Snapshot copies not associated with the active file system. The default tiering policy is "snapshot_only" for a FlexVol volume and "none" for a FlexGroup volume.

Valid choices:

* all
* auto
* none
* snapshot_only """

    supported = fields.Boolean(data_key="supported")
    r""" Optional property to enable provisioning of the destination endpoint volumes on FabricPool aggregates. This property is applicable to FlexVol volume and FlexGroup volume endpoints. Only FabricPool aggregates are used if this property is set to "true" and only non FabricPool aggregates are used if this property is set to "false". Tiering support for a FlexGroup volume can be changed by moving all of the constituents to the required aggregates. Note that in order to tier data, not only do the destination endpoint volumes need to support tiering by using FabricPools, the "create_destination.tiering.policy" must not be "none". A destination endpoint that uses FabricPools but has a tiering "policy" of "none" supports tiering but will not tier any data. """

    @property
    def resource(self):
        return SnapmirrorDestinationCreationTiering

    @property
    def patchable_fields(self):
        return [
            "policy",
            "supported",
        ]

    @property
    def postable_fields(self):
        return [
            "policy",
            "supported",
        ]


class SnapmirrorDestinationCreationTiering(Resource):  # pylint: disable=missing-docstring

    _schema = SnapmirrorDestinationCreationTieringSchema
