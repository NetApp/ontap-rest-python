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


__all__ = ["NasFlexcacheOriginComponent", "NasFlexcacheOriginComponentSchema"]
__pdoc__ = {
    "NasFlexcacheOriginComponentSchema.resource": False,
    "NasFlexcacheOriginComponent": False,
}


class NasFlexcacheOriginComponentSchema(ResourceSchema):
    """The fields of the NasFlexcacheOriginComponent object"""

    name = fields.Str(data_key="name")
    r""" Name of the source component. """

    @property
    def resource(self):
        return NasFlexcacheOriginComponent

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class NasFlexcacheOriginComponent(Resource):  # pylint: disable=missing-docstring

    _schema = NasFlexcacheOriginComponentSchema
