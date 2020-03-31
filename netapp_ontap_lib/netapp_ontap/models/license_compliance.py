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


__all__ = ["LicenseCompliance", "LicenseComplianceSchema"]
__pdoc__ = {
    "LicenseComplianceSchema.resource": False,
    "LicenseCompliance": False,
}


class LicenseComplianceSchema(ResourceSchema):
    """The fields of the LicenseCompliance object"""

    state = fields.Str(data_key="state")
    r""" Compliance state of the license.

Valid choices:

* compliant
* noncompliant
* unlicensed
* unknown """

    @property
    def resource(self):
        return LicenseCompliance

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class LicenseCompliance(Resource):  # pylint: disable=missing-docstring

    _schema = LicenseComplianceSchema
