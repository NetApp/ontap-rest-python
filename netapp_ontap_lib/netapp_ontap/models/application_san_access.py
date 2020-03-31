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


__all__ = ["ApplicationSanAccess", "ApplicationSanAccessSchema"]
__pdoc__ = {
    "ApplicationSanAccessSchema.resource": False,
    "ApplicationSanAccess": False,
}


class ApplicationSanAccessSchema(ResourceSchema):
    """The fields of the ApplicationSanAccess object"""

    backing_storage = fields.Nested("netapp_ontap.models.application_san_access_backing_storage.ApplicationSanAccessBackingStorageSchema", unknown=EXCLUDE, data_key="backing_storage")
    r""" The backing_storage field of the application_san_access. """

    is_clone = fields.Boolean(data_key="is_clone")
    r""" Clone """

    lun_mappings = fields.List(fields.Nested("netapp_ontap.models.application_lun_mapping_object.ApplicationLunMappingObjectSchema", unknown=EXCLUDE), data_key="lun_mappings")
    r""" The lun_mappings field of the application_san_access. """

    serial_number = fields.Str(data_key="serial_number")
    r""" LUN serial number """

    @property
    def resource(self):
        return ApplicationSanAccess

    @property
    def patchable_fields(self):
        return [
            "backing_storage",
            "lun_mappings",
        ]

    @property
    def postable_fields(self):
        return [
            "backing_storage",
            "lun_mappings",
        ]


class ApplicationSanAccess(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSanAccessSchema
