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


__all__ = ["ScopeIpspace", "ScopeIpspaceSchema"]
__pdoc__ = {
    "ScopeIpspaceSchema.resource": False,
    "ScopeIpspace": False,
}


class ScopeIpspaceSchema(ResourceSchema):
    """The fields of the ScopeIpspace object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the scope_ipspace. """

    name = fields.Str(data_key="name")
    r""" IPspace name

Example: exchange """

    uuid = fields.Str(data_key="uuid")
    r""" IPspace UUID

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return ScopeIpspace

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


class ScopeIpspace(Resource):  # pylint: disable=missing-docstring

    _schema = ScopeIpspaceSchema
