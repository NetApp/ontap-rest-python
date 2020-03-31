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


__all__ = ["LicenseCapacity", "LicenseCapacitySchema"]
__pdoc__ = {
    "LicenseCapacitySchema.resource": False,
    "LicenseCapacity": False,
}


class LicenseCapacitySchema(ResourceSchema):
    """The fields of the LicenseCapacity object"""

    maximum_size = fields.Integer(data_key="maximum_size")
    r""" Licensed capacity size (in bytes) that can be used. """

    used_size = fields.Integer(data_key="used_size")
    r""" Capacity that is currently used (in bytes). """

    @property
    def resource(self):
        return LicenseCapacity

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class LicenseCapacity(Resource):  # pylint: disable=missing-docstring

    _schema = LicenseCapacitySchema
