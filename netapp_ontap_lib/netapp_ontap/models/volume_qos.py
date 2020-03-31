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


__all__ = ["VolumeQos", "VolumeQosSchema"]
__pdoc__ = {
    "VolumeQosSchema.resource": False,
    "VolumeQos": False,
}


class VolumeQosSchema(ResourceSchema):
    """The fields of the VolumeQos object"""

    policy = fields.Nested("netapp_ontap.resources.qos_policy.QosPolicySchema", unknown=EXCLUDE, data_key="policy")
    r""" The policy field of the volume_qos. """

    @property
    def resource(self):
        return VolumeQos

    @property
    def patchable_fields(self):
        return [
            "policy.max_throughput_iops",
            "policy.max_throughput_mbps",
            "policy.min_throughput_iops",
            "policy.name",
            "policy.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "policy.max_throughput_iops",
            "policy.max_throughput_mbps",
            "policy.min_throughput_iops",
            "policy.name",
            "policy.uuid",
        ]


class VolumeQos(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeQosSchema
