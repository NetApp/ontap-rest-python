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


__all__ = ["LicenseKeys", "LicenseKeysSchema"]
__pdoc__ = {
    "LicenseKeysSchema.resource": False,
    "LicenseKeys": False,
}


class LicenseKeysSchema(ResourceSchema):
    """The fields of the LicenseKeys object"""

    keys = fields.List(fields.Str, data_key="keys")
    r""" The keys field of the license_keys. """

    @property
    def resource(self):
        return LicenseKeys

    @property
    def patchable_fields(self):
        return [
            "keys",
        ]

    @property
    def postable_fields(self):
        return [
            "keys",
        ]


class LicenseKeys(Resource):  # pylint: disable=missing-docstring

    _schema = LicenseKeysSchema
