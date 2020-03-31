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


__all__ = ["SanApplicationComponents", "SanApplicationComponentsSchema"]
__pdoc__ = {
    "SanApplicationComponentsSchema.resource": False,
    "SanApplicationComponents": False,
}


class SanApplicationComponentsSchema(ResourceSchema):
    """The fields of the SanApplicationComponents object"""

    igroup_name = fields.Str(data_key="igroup_name")
    r""" The name of the initiator group through which the contents of this application will be accessed. Modification of this parameter is a disruptive operation. All LUNs in the application component will be unmapped from the current igroup and re-mapped to the new igroup. """

    lun_count = fields.Integer(data_key="lun_count")
    r""" The number of LUNs in the application component. """

    name = fields.Str(data_key="name")
    r""" The name of the application component. """

    storage_service = fields.Nested("netapp_ontap.models.nas_storage_service.NasStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the san_application_components. """

    tiering = fields.Nested("netapp_ontap.models.san_application_components_tiering.SanApplicationComponentsTieringSchema", unknown=EXCLUDE, data_key="tiering")
    r""" The tiering field of the san_application_components. """

    total_size = fields.Integer(data_key="total_size")
    r""" The total size of the application component, split across the member LUNs. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    @property
    def resource(self):
        return SanApplicationComponents

    @property
    def patchable_fields(self):
        return [
            "igroup_name",
            "name",
            "storage_service",
            "tiering",
            "total_size",
        ]

    @property
    def postable_fields(self):
        return [
            "igroup_name",
            "lun_count",
            "name",
            "storage_service",
            "tiering",
            "total_size",
        ]


class SanApplicationComponents(Resource):  # pylint: disable=missing-docstring

    _schema = SanApplicationComponentsSchema
