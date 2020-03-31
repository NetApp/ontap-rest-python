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


__all__ = ["ApplicationProtectionGroupsRpoLocal", "ApplicationProtectionGroupsRpoLocalSchema"]
__pdoc__ = {
    "ApplicationProtectionGroupsRpoLocalSchema.resource": False,
    "ApplicationProtectionGroupsRpoLocal": False,
}


class ApplicationProtectionGroupsRpoLocalSchema(ResourceSchema):
    """The fields of the ApplicationProtectionGroupsRpoLocal object"""

    description = fields.Str(data_key="description")
    r""" A detailed description of the local RPO. This includes details on the Snapshot copy schedule. """

    name = fields.Str(data_key="name")
    r""" The local RPO of the component. This indicates how often component Snapshot copies are automatically created.

Valid choices:

* none
* hourly
* 6_hourly
* 15_minutely """

    @property
    def resource(self):
        return ApplicationProtectionGroupsRpoLocal

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationProtectionGroupsRpoLocal(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationProtectionGroupsRpoLocalSchema
