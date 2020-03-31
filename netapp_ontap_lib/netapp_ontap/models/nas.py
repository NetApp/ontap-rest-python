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


__all__ = ["Nas", "NasSchema"]
__pdoc__ = {
    "NasSchema.resource": False,
    "Nas": False,
}


class NasSchema(ResourceSchema):
    """The fields of the Nas object"""

    application_components = fields.List(fields.Nested("netapp_ontap.models.nas_application_components.NasApplicationComponentsSchema", unknown=EXCLUDE), data_key="application_components")
    r""" The application_components field of the nas. """

    cifs_access = fields.List(fields.Nested("netapp_ontap.models.app_cifs_access.AppCifsAccessSchema", unknown=EXCLUDE), data_key="cifs_access")
    r""" The list of CIFS access controls. """

    nfs_access = fields.List(fields.Nested("netapp_ontap.models.app_nfs_access.AppNfsAccessSchema", unknown=EXCLUDE), data_key="nfs_access")
    r""" The list of NFS access controls. """

    protection_type = fields.Nested("netapp_ontap.models.nas_protection_type.NasProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the nas. """

    @property
    def resource(self):
        return Nas

    @property
    def patchable_fields(self):
        return [
            "application_components",
            "protection_type",
        ]

    @property
    def postable_fields(self):
        return [
            "application_components",
            "cifs_access",
            "nfs_access",
            "protection_type",
        ]


class Nas(Resource):  # pylint: disable=missing-docstring

    _schema = NasSchema
