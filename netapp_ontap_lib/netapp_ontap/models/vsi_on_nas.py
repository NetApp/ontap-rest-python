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


__all__ = ["VsiOnNas", "VsiOnNasSchema"]
__pdoc__ = {
    "VsiOnNasSchema.resource": False,
    "VsiOnNas": False,
}


class VsiOnNasSchema(ResourceSchema):
    """The fields of the VsiOnNas object"""

    datastore = fields.Nested("netapp_ontap.models.vsi_on_nas_datastore.VsiOnNasDatastoreSchema", unknown=EXCLUDE, data_key="datastore")
    r""" The datastore field of the vsi_on_nas. """

    hyper_v_access = fields.Nested("netapp_ontap.models.vdi_on_nas_hyper_v_access.VdiOnNasHyperVAccessSchema", unknown=EXCLUDE, data_key="hyper_v_access")
    r""" The hyper_v_access field of the vsi_on_nas. """

    nfs_access = fields.List(fields.Nested("netapp_ontap.models.app_nfs_access.AppNfsAccessSchema", unknown=EXCLUDE), data_key="nfs_access")
    r""" The list of NFS access controls. """

    protection_type = fields.Nested("netapp_ontap.models.mongo_db_on_san_protection_type.MongoDbOnSanProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the vsi_on_nas. """

    @property
    def resource(self):
        return VsiOnNas

    @property
    def patchable_fields(self):
        return [
            "datastore",
            "protection_type",
        ]

    @property
    def postable_fields(self):
        return [
            "datastore",
            "hyper_v_access",
            "nfs_access",
            "protection_type",
        ]


class VsiOnNas(Resource):  # pylint: disable=missing-docstring

    _schema = VsiOnNasSchema
