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


__all__ = ["ApplicationNfsPropertiesPermissions", "ApplicationNfsPropertiesPermissionsSchema"]
__pdoc__ = {
    "ApplicationNfsPropertiesPermissionsSchema.resource": False,
    "ApplicationNfsPropertiesPermissions": False,
}


class ApplicationNfsPropertiesPermissionsSchema(ResourceSchema):
    """The fields of the ApplicationNfsPropertiesPermissions object"""

    access = fields.Str(data_key="access")
    r""" Access granted to the host """

    host = fields.Str(data_key="host")
    r""" Host granted access """

    @property
    def resource(self):
        return ApplicationNfsPropertiesPermissions

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationNfsPropertiesPermissions(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationNfsPropertiesPermissionsSchema
