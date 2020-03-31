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


__all__ = ["RelatedLink", "RelatedLinkSchema"]
__pdoc__ = {
    "RelatedLinkSchema.resource": False,
    "RelatedLink": False,
}


class RelatedLinkSchema(ResourceSchema):
    """The fields of the RelatedLink object"""

    related = fields.Nested("netapp_ontap.models.href.HrefSchema", unknown=EXCLUDE, data_key="related")
    r""" The related field of the related_link. """

    @property
    def resource(self):
        return RelatedLink

    @property
    def patchable_fields(self):
        return [
            "related",
        ]

    @property
    def postable_fields(self):
        return [
            "related",
        ]


class RelatedLink(Resource):  # pylint: disable=missing-docstring

    _schema = RelatedLinkSchema
