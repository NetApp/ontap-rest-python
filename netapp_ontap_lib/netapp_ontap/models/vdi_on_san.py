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


__all__ = ["VdiOnSan", "VdiOnSanSchema"]
__pdoc__ = {
    "VdiOnSanSchema.resource": False,
    "VdiOnSan": False,
}


class VdiOnSanSchema(ResourceSchema):
    """The fields of the VdiOnSan object"""

    desktops = fields.Nested("netapp_ontap.models.vdi_on_nas_desktops.VdiOnNasDesktopsSchema", unknown=EXCLUDE, data_key="desktops")
    r""" The desktops field of the vdi_on_san. """

    hypervisor = fields.Str(data_key="hypervisor")
    r""" The name of the hypervisor hosting the application.

Valid choices:

* hyper_v
* vmware
* xen """

    igroup_name = fields.Str(data_key="igroup_name")
    r""" The name of the initiator group through which the contents of this application will be accessed. Modification of this parameter is a disruptive operation. All LUNs in the application component will be unmapped from the current igroup and re-mapped to the new igroup. """

    new_igroups = fields.List(fields.Nested("netapp_ontap.models.vdi_on_san_new_igroups.VdiOnSanNewIgroupsSchema", unknown=EXCLUDE), data_key="new_igroups")
    r""" The list of initiator groups to create. """

    protection_type = fields.Nested("netapp_ontap.models.mongo_db_on_san_protection_type.MongoDbOnSanProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the vdi_on_san. """

    @property
    def resource(self):
        return VdiOnSan

    @property
    def patchable_fields(self):
        return [
            "desktops",
            "igroup_name",
            "new_igroups",
            "protection_type",
        ]

    @property
    def postable_fields(self):
        return [
            "desktops",
            "hypervisor",
            "igroup_name",
            "new_igroups",
            "protection_type",
        ]


class VdiOnSan(Resource):  # pylint: disable=missing-docstring

    _schema = VdiOnSanSchema
