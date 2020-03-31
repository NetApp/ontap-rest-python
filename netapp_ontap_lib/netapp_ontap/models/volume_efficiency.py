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


__all__ = ["VolumeEfficiency", "VolumeEfficiencySchema"]
__pdoc__ = {
    "VolumeEfficiencySchema.resource": False,
    "VolumeEfficiency": False,
}


class VolumeEfficiencySchema(ResourceSchema):
    """The fields of the VolumeEfficiency object"""

    compaction = fields.Str(data_key="compaction")
    r""" The system can be enabled/disabled compaction.<br>inline &dash; Data will be compacted first and written to the volume.<br>none &dash; None<br>mixed &dash; Read only field for FlexGroups, where some of the constituent volumes are compaction enabled and some are disabled.

Valid choices:

* inline
* none
* mixed """

    compression = fields.Str(data_key="compression")
    r""" The system can be enabled/disabled compression.<br>inline &dash; Data will be compressed first and written to the volume.<br>background &dash; Data will be written to the volume and compressed later.<br>both &dash; Inline compression compresses the data and write to the volume, background compression compresses only the blocks on which inline compression is not run.<br>none &dash; None<br>mixed &dash; Read only field for FlexGroups, where some of the constituent volumes are compression enabled and some are disabled.

Valid choices:

* inline
* background
* both
* none
* mixed """

    cross_volume_dedupe = fields.Str(data_key="cross_volume_dedupe")
    r""" The system can be enabled/disabled cross volume dedupe. it can be enabled only when dedupe is enabled.<br>inline &dash; Data will be cross volume deduped first and written to the volume.<br>background &dash; Data will be written to the volume and cross volume deduped later.<br>both &dash; Inline cross volume dedupe dedupes the data and write to the volume, background cross volume dedupe dedupes only the blocks on which inline dedupe is not run.<br>none &dash; None<br>mixed &dash; Read only field for FlexGroups, where some of the constituent volumes are cross volume dedupe enabled and some are disabled.

Valid choices:

* inline
* background
* both
* none
* mixed """

    dedupe = fields.Str(data_key="dedupe")
    r""" The system can be enabled/disabled dedupe.<br>inline &dash; Data will be deduped first and written to the volume.<br>background &dash; Data will be written to the volume and deduped later.<br>both &dash; Inline dedupe dedupes the data and write to the volume, background dedupe dedupes only the blocks on which inline dedupe is not run.<br>none &dash; None<br>mixed &dash; Read only field for FlexGroups, where some of the constituent volumes are dedupe enabled and some are disabled.

Valid choices:

* inline
* background
* both
* none
* mixed """

    policy = fields.Nested("netapp_ontap.models.volume_efficiency_policy.VolumeEfficiencyPolicySchema", unknown=EXCLUDE, data_key="policy")
    r""" The policy field of the volume_efficiency. """

    @property
    def resource(self):
        return VolumeEfficiency

    @property
    def patchable_fields(self):
        return [
            "compaction",
            "compression",
            "cross_volume_dedupe",
            "dedupe",
            "policy",
        ]

    @property
    def postable_fields(self):
        return [
            "compaction",
            "compression",
            "cross_volume_dedupe",
            "dedupe",
            "policy",
        ]


class VolumeEfficiency(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeEfficiencySchema
