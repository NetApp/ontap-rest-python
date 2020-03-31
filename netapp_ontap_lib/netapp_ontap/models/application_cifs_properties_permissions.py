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


__all__ = ["ApplicationCifsPropertiesPermissions", "ApplicationCifsPropertiesPermissionsSchema"]
__pdoc__ = {
    "ApplicationCifsPropertiesPermissionsSchema.resource": False,
    "ApplicationCifsPropertiesPermissions": False,
}


class ApplicationCifsPropertiesPermissionsSchema(ResourceSchema):
    """The fields of the ApplicationCifsPropertiesPermissions object"""

    access = fields.Str(data_key="access")
    r""" Access granted to the user or group """

    user_or_group = fields.Str(data_key="user_or_group")
    r""" User or group """

    @property
    def resource(self):
        return ApplicationCifsPropertiesPermissions

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationCifsPropertiesPermissions(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationCifsPropertiesPermissionsSchema
