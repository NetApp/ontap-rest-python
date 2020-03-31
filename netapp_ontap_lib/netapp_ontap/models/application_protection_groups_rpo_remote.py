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


__all__ = ["ApplicationProtectionGroupsRpoRemote", "ApplicationProtectionGroupsRpoRemoteSchema"]
__pdoc__ = {
    "ApplicationProtectionGroupsRpoRemoteSchema.resource": False,
    "ApplicationProtectionGroupsRpoRemote": False,
}


class ApplicationProtectionGroupsRpoRemoteSchema(ResourceSchema):
    """The fields of the ApplicationProtectionGroupsRpoRemote object"""

    description = fields.Str(data_key="description")
    r""" A detailed description of the remote RPO. """

    name = fields.Str(data_key="name")
    r""" The remote RPO of the component. A remote RPO of zero indicates that the component is synchronously replicated to another cluster.

Valid choices:

* none
* zero
* hourly
* 6_hourly
* 15_minutely """

    @property
    def resource(self):
        return ApplicationProtectionGroupsRpoRemote

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationProtectionGroupsRpoRemote(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationProtectionGroupsRpoRemoteSchema
