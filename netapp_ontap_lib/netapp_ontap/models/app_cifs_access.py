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


__all__ = ["AppCifsAccess", "AppCifsAccessSchema"]
__pdoc__ = {
    "AppCifsAccessSchema.resource": False,
    "AppCifsAccess": False,
}


class AppCifsAccessSchema(ResourceSchema):
    """The fields of the AppCifsAccess object"""

    access = fields.Str(data_key="access")
    r""" The CIFS access granted to the user or group.

Valid choices:

* change
* full_control
* no_access
* read """

    user_or_group = fields.Str(data_key="user_or_group")
    r""" The name of the CIFS user or group that will be granted access. """

    @property
    def resource(self):
        return AppCifsAccess

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "access",
            "user_or_group",
        ]


class AppCifsAccess(Resource):  # pylint: disable=missing-docstring

    _schema = AppCifsAccessSchema
