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


__all__ = ["IgroupInitiatorIgroup", "IgroupInitiatorIgroupSchema"]
__pdoc__ = {
    "IgroupInitiatorIgroupSchema.resource": False,
    "IgroupInitiatorIgroup": False,
}


class IgroupInitiatorIgroupSchema(ResourceSchema):
    """The fields of the IgroupInitiatorIgroup object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the igroup_initiator_igroup. """

    uuid = fields.Str(data_key="uuid")
    r""" The unique identifier of the initiator group.


Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return IgroupInitiatorIgroup

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class IgroupInitiatorIgroup(Resource):  # pylint: disable=missing-docstring

    _schema = IgroupInitiatorIgroupSchema
