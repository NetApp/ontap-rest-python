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


__all__ = ["ApplicationCifsProperties", "ApplicationCifsPropertiesSchema"]
__pdoc__ = {
    "ApplicationCifsPropertiesSchema.resource": False,
    "ApplicationCifsProperties": False,
}


class ApplicationCifsPropertiesSchema(ResourceSchema):
    """The fields of the ApplicationCifsProperties object"""

    backing_storage = fields.Nested("netapp_ontap.models.application_cifs_properties_backing_storage.ApplicationCifsPropertiesBackingStorageSchema", unknown=EXCLUDE, data_key="backing_storage")
    r""" The backing_storage field of the application_cifs_properties. """

    ips = fields.List(fields.Str, data_key="ips")
    r""" The ips field of the application_cifs_properties. """

    path = fields.Str(data_key="path")
    r""" Junction path """

    permissions = fields.List(fields.Nested("netapp_ontap.models.application_cifs_properties_permissions.ApplicationCifsPropertiesPermissionsSchema", unknown=EXCLUDE), data_key="permissions")
    r""" The permissions field of the application_cifs_properties. """

    server = fields.Nested("netapp_ontap.models.application_cifs_properties_server.ApplicationCifsPropertiesServerSchema", unknown=EXCLUDE, data_key="server")
    r""" The server field of the application_cifs_properties. """

    share = fields.Nested("netapp_ontap.models.application_cifs_properties_share.ApplicationCifsPropertiesShareSchema", unknown=EXCLUDE, data_key="share")
    r""" The share field of the application_cifs_properties. """

    @property
    def resource(self):
        return ApplicationCifsProperties

    @property
    def patchable_fields(self):
        return [
            "backing_storage",
            "ips",
            "server",
            "share",
        ]

    @property
    def postable_fields(self):
        return [
            "backing_storage",
            "ips",
            "server",
            "share",
        ]


class ApplicationCifsProperties(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationCifsPropertiesSchema
