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


__all__ = ["MaxdataOnSanApplicationComponents", "MaxdataOnSanApplicationComponentsSchema"]
__pdoc__ = {
    "MaxdataOnSanApplicationComponentsSchema.resource": False,
    "MaxdataOnSanApplicationComponents": False,
}


class MaxdataOnSanApplicationComponentsSchema(ResourceSchema):
    """The fields of the MaxdataOnSanApplicationComponents object"""

    file_system = fields.Str(data_key="file_system")
    r""" Defines the type of file system that will be installed on this application component.

Valid choices:

* generic
* m1fs
* xfs """

    host_management_url = fields.Str(data_key="host_management_url")
    r""" The host management URL for this application component. """

    host_name = fields.Str(data_key="host_name")
    r""" FQDN of the L2 host that contains the hot tier of this application component. """

    igroup_name = fields.Str(data_key="igroup_name")
    r""" The name of the initiator group through which the contents of this application will be accessed. Modification of this parameter is a disruptive operation. All LUNs in the application component will be unmapped from the current igroup and re-mapped to the new igroup. """

    lun_count = fields.Integer(data_key="lun_count")
    r""" The number of LUNs in the application component. """

    metadata = fields.List(fields.Nested("netapp_ontap.models.maxdata_on_san_application_components_metadata.MaxdataOnSanApplicationComponentsMetadataSchema", unknown=EXCLUDE), data_key="metadata")
    r""" The metadata field of the maxdata_on_san_application_components. """

    name = fields.Str(data_key="name")
    r""" The name of the application component. """

    protection_type = fields.Nested("netapp_ontap.models.maxdata_on_san_application_components_protection_type.MaxdataOnSanApplicationComponentsProtectionTypeSchema", unknown=EXCLUDE, data_key="protection_type")
    r""" The protection_type field of the maxdata_on_san_application_components. """

    storage_service = fields.Nested("netapp_ontap.models.maxdata_on_san_application_components_storage_service.MaxdataOnSanApplicationComponentsStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the maxdata_on_san_application_components. """

    total_size = fields.Integer(data_key="total_size")
    r""" The total size of the application component, split across the member LUNs. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    @property
    def resource(self):
        return MaxdataOnSanApplicationComponents

    @property
    def patchable_fields(self):
        return [
            "igroup_name",
            "lun_count",
            "name",
            "protection_type",
            "storage_service",
            "total_size",
        ]

    @property
    def postable_fields(self):
        return [
            "file_system",
            "host_name",
            "igroup_name",
            "lun_count",
            "metadata",
            "name",
            "protection_type",
            "storage_service",
            "total_size",
        ]


class MaxdataOnSanApplicationComponents(Resource):  # pylint: disable=missing-docstring

    _schema = MaxdataOnSanApplicationComponentsSchema
