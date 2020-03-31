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


__all__ = ["BroadcastDomainReferenceIpspace", "BroadcastDomainReferenceIpspaceSchema"]
__pdoc__ = {
    "BroadcastDomainReferenceIpspaceSchema.resource": False,
    "BroadcastDomainReferenceIpspace": False,
}


class BroadcastDomainReferenceIpspaceSchema(ResourceSchema):
    """The fields of the BroadcastDomainReferenceIpspace object"""

    name = fields.Str(data_key="name")
    r""" Name of the broadcast domain's IPspace

Example: ipspace1 """

    @property
    def resource(self):
        return BroadcastDomainReferenceIpspace

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class BroadcastDomainReferenceIpspace(Resource):  # pylint: disable=missing-docstring

    _schema = BroadcastDomainReferenceIpspaceSchema
