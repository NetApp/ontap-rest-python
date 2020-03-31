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


__all__ = ["VdiOnNas", "VdiOnNasSchema"]
__pdoc__ = {
    "VdiOnNasSchema.resource": False,
    "VdiOnNas": False,
}


class VdiOnNasSchema(ResourceSchema):
    """The fields of the VdiOnNas object"""

    desktops = fields.Nested("netapp_ontap.models.vdi_on_nas_desktops.VdiOnNasDesktopsSchema", unknown=EXCLUDE, data_key="desktops")
    r""" The desktops field of the vdi_on_nas. """

    hyper_v_access = fields.Nested("netapp_ontap.models.vdi_on_nas_hyper_v_access.VdiOnNasHyperVAccessSchema", unknown=EXCLUDE, data_key="hyper_v_access")
    r""" The hyper_v_access field of the vdi_on_nas. """

    nfs_access = fields.List(fields.Nested("netapp_ontap.models.app_nfs_access.AppNfsAccessSchema", unknown=EXCLUDE), data_key="nfs_access")
    r""" The list of NFS access controls. """

    protection_type = fields.Nested("netapp_ontap.models.mongo_db_on_san_protection_type.MongoDbOnSanProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the vdi_on_nas. """

    @property
    def resource(self):
        return VdiOnNas

    @property
    def patchable_fields(self):
        return [
            "desktops",
            "protection_type",
        ]

    @property
    def postable_fields(self):
        return [
            "desktops",
            "hyper_v_access",
            "nfs_access",
            "protection_type",
        ]


class VdiOnNas(Resource):  # pylint: disable=missing-docstring

    _schema = VdiOnNasSchema
