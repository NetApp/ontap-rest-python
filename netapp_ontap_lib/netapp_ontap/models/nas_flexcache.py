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


__all__ = ["NasFlexcache", "NasFlexcacheSchema"]
__pdoc__ = {
    "NasFlexcacheSchema.resource": False,
    "NasFlexcache": False,
}


class NasFlexcacheSchema(ResourceSchema):
    """The fields of the NasFlexcache object"""

    origin = fields.Nested("netapp_ontap.models.nas_flexcache_origin.NasFlexcacheOriginSchema", unknown=EXCLUDE, data_key="origin")
    r""" The origin field of the nas_flexcache. """

    @property
    def resource(self):
        return NasFlexcache

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "origin",
        ]


class NasFlexcache(Resource):  # pylint: disable=missing-docstring

    _schema = NasFlexcacheSchema
