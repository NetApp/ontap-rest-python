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


__all__ = ["NasFlexcacheOrigin", "NasFlexcacheOriginSchema"]
__pdoc__ = {
    "NasFlexcacheOriginSchema.resource": False,
    "NasFlexcacheOrigin": False,
}


class NasFlexcacheOriginSchema(ResourceSchema):
    """The fields of the NasFlexcacheOrigin object"""

    component = fields.Nested("netapp_ontap.models.nas_flexcache_origin_component.NasFlexcacheOriginComponentSchema", unknown=EXCLUDE, data_key="component")
    r""" The component field of the nas_flexcache_origin. """

    svm = fields.Nested("netapp_ontap.models.nas_flexcache_origin_svm.NasFlexcacheOriginSvmSchema", unknown=EXCLUDE, data_key="svm")
    r""" The svm field of the nas_flexcache_origin. """

    @property
    def resource(self):
        return NasFlexcacheOrigin

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "component",
            "svm",
        ]


class NasFlexcacheOrigin(Resource):  # pylint: disable=missing-docstring

    _schema = NasFlexcacheOriginSchema
