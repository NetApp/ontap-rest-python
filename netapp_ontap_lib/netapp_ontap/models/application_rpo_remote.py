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


__all__ = ["ApplicationRpoRemote", "ApplicationRpoRemoteSchema"]
__pdoc__ = {
    "ApplicationRpoRemoteSchema.resource": False,
    "ApplicationRpoRemote": False,
}


class ApplicationRpoRemoteSchema(ResourceSchema):
    """The fields of the ApplicationRpoRemote object"""

    description = fields.Str(data_key="description")
    r""" A detailed description of the remote RPO. """

    name = fields.Str(data_key="name")
    r""" The remote RPO of the application. A remote RPO of zero indicates that the application is synchronously replicated to another cluster.

Valid choices:

* 6_hourly
* 15_minutely
* hourly
* none
* zero """

    @property
    def resource(self):
        return ApplicationRpoRemote

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationRpoRemote(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationRpoRemoteSchema
