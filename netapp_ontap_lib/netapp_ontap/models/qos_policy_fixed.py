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


__all__ = ["QosPolicyFixed", "QosPolicyFixedSchema"]
__pdoc__ = {
    "QosPolicyFixedSchema.resource": False,
    "QosPolicyFixed": False,
}


class QosPolicyFixedSchema(ResourceSchema):
    """The fields of the QosPolicyFixed object"""

    capacity_shared = fields.Boolean(data_key="capacity_shared")
    r""" Specifies whether the capacities are shared across all objects that use this QoS policy-group. Default is false. """

    max_throughput_iops = fields.Integer(data_key="max_throughput_iops")
    r""" Maximum throughput defined by this policy.  It is specified in terms of IOPS. 0 means no maximum throughput is enforced. """

    max_throughput_mbps = fields.Integer(data_key="max_throughput_mbps")
    r""" Maximum throughput defined by this policy.  It is specified in terms of Mbps. 0 means no maximum throughput is enforced. """

    min_throughput_iops = fields.Integer(data_key="min_throughput_iops")
    r""" Minimum throughput defined by this policy.  It is specified in terms of IOPS. 0 means no minimum throughput is enforced. These floors are not guaranteed on non-AFF platforms or when FabricPool tiering policies are set. """

    @property
    def resource(self):
        return QosPolicyFixed

    @property
    def patchable_fields(self):
        return [
            "max_throughput_iops",
            "max_throughput_mbps",
            "min_throughput_iops",
        ]

    @property
    def postable_fields(self):
        return [
            "capacity_shared",
            "max_throughput_iops",
            "max_throughput_mbps",
            "min_throughput_iops",
        ]


class QosPolicyFixed(Resource):  # pylint: disable=missing-docstring

    _schema = QosPolicyFixedSchema
