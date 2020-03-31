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


__all__ = ["SnapmirrorRelationshipPolicy", "SnapmirrorRelationshipPolicySchema"]
__pdoc__ = {
    "SnapmirrorRelationshipPolicySchema.resource": False,
    "SnapmirrorRelationshipPolicy": False,
}


class SnapmirrorRelationshipPolicySchema(ResourceSchema):
    """The fields of the SnapmirrorRelationshipPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the snapmirror_relationship_policy. """

    name = fields.Str(data_key="name")
    r""" The name field of the snapmirror_relationship_policy.

Example: Asynchronous """

    type = fields.Str(data_key="type")
    r""" The type field of the snapmirror_relationship_policy.

Valid choices:

* async
* sync """

    uuid = fields.Str(data_key="uuid")
    r""" The uuid field of the snapmirror_relationship_policy.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return SnapmirrorRelationshipPolicy

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


class SnapmirrorRelationshipPolicy(Resource):  # pylint: disable=missing-docstring

    _schema = SnapmirrorRelationshipPolicySchema
