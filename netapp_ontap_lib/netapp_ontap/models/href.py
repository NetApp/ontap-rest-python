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


__all__ = ["Href", "HrefSchema"]
__pdoc__ = {
    "HrefSchema.resource": False,
    "Href": False,
}


class HrefSchema(ResourceSchema):
    """The fields of the Href object"""

    href = fields.Str(data_key="href")
    r""" The href field of the href.

Example: /api/resourcelink """

    @property
    def resource(self):
        return Href

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class Href(Resource):  # pylint: disable=missing-docstring

    _schema = HrefSchema
