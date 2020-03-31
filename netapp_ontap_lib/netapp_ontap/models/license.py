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


__all__ = ["License", "LicenseSchema"]
__pdoc__ = {
    "LicenseSchema.resource": False,
    "License": False,
}


class LicenseSchema(ResourceSchema):
    """The fields of the License object"""

    active = fields.Boolean(data_key="active")
    r""" A flag indicating whether the license is currently being enforced. """

    capacity = fields.Nested("netapp_ontap.models.license_capacity.LicenseCapacitySchema", unknown=EXCLUDE, data_key="capacity")
    r""" The capacity field of the license. """

    compliance = fields.Nested("netapp_ontap.models.license_compliance.LicenseComplianceSchema", unknown=EXCLUDE, data_key="compliance")
    r""" The compliance field of the license. """

    evaluation = fields.Boolean(data_key="evaluation")
    r""" A flag indicating whether the license is in evaluation mode. """

    expiry_time = fields.DateTime(data_key="expiry_time")
    r""" Date and time when the license expires.

Example: 2019-03-02T19:00:00.000+0000 """

    owner = fields.Str(data_key="owner")
    r""" Cluster, node or license manager that owns the license.

Example: cluster1 """

    serial_number = fields.Str(data_key="serial_number")
    r""" Serial number of the license.

Example: 123456789 """

    start_time = fields.DateTime(data_key="start_time")
    r""" Date and time when the license starts.

Example: 2019-02-02T19:00:00.000+0000 """

    @property
    def resource(self):
        return License

    @property
    def patchable_fields(self):
        return [
            "capacity",
            "compliance",
        ]

    @property
    def postable_fields(self):
        return [
            "capacity",
            "compliance",
        ]


class License(Resource):  # pylint: disable=missing-docstring

    _schema = LicenseSchema
