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


__all__ = ["CollectionLinks", "CollectionLinksSchema"]
__pdoc__ = {
    "CollectionLinksSchema.resource": False,
    "CollectionLinks": False,
}


class CollectionLinksSchema(ResourceSchema):
    """The fields of the CollectionLinks object"""

    next = fields.Nested("netapp_ontap.models.href.HrefSchema", unknown=EXCLUDE, data_key="next")
    r""" The next field of the collection_links. """

    self_ = fields.Nested("netapp_ontap.models.href.HrefSchema", unknown=EXCLUDE, data_key="self")
    r""" The self_ field of the collection_links. """

    @property
    def resource(self):
        return CollectionLinks

    @property
    def patchable_fields(self):
        return [
            "next",
            "self_",
        ]

    @property
    def postable_fields(self):
        return [
            "next",
            "self_",
        ]


class CollectionLinks(Resource):  # pylint: disable=missing-docstring

    _schema = CollectionLinksSchema
