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


__all__ = ["ApplicationProtectionGroupsRpo", "ApplicationProtectionGroupsRpoSchema"]
__pdoc__ = {
    "ApplicationProtectionGroupsRpoSchema.resource": False,
    "ApplicationProtectionGroupsRpo": False,
}


class ApplicationProtectionGroupsRpoSchema(ResourceSchema):
    """The fields of the ApplicationProtectionGroupsRpo object"""

    local = fields.Nested("netapp_ontap.models.application_protection_groups_rpo_local.ApplicationProtectionGroupsRpoLocalSchema", unknown=EXCLUDE, data_key="local")
    r""" The local field of the application_protection_groups_rpo. """

    remote = fields.Nested("netapp_ontap.models.application_protection_groups_rpo_remote.ApplicationProtectionGroupsRpoRemoteSchema", unknown=EXCLUDE, data_key="remote")
    r""" The remote field of the application_protection_groups_rpo. """

    @property
    def resource(self):
        return ApplicationProtectionGroupsRpo

    @property
    def patchable_fields(self):
        return [
            "local",
            "remote",
        ]

    @property
    def postable_fields(self):
        return [
            "local",
            "remote",
        ]


class ApplicationProtectionGroupsRpo(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationProtectionGroupsRpoSchema
