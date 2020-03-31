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


__all__ = ["LunQosPolicy", "LunQosPolicySchema"]
__pdoc__ = {
    "LunQosPolicySchema.resource": False,
    "LunQosPolicy": False,
}


class LunQosPolicySchema(ResourceSchema):
    """The fields of the LunQosPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the lun_qos_policy. """

    name = fields.Str(data_key="name")
    r""" The name of the QoS policy. To remove the QoS policy from a LUN, leaving it with no QoS policy, set this property to an empty string ("") in a PATCH request. Valid in POST and PATCH.


Example: qos1 """

    uuid = fields.Str(data_key="uuid")
    r""" The unique identifier of the QoS policy. Valid in POST and PATCH.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return LunQosPolicy

    @property
    def patchable_fields(self):
        return [
            "name",
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "uuid",
        ]


class LunQosPolicy(Resource):  # pylint: disable=missing-docstring

    _schema = LunQosPolicySchema
