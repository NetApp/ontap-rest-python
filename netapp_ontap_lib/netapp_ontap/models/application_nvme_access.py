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


__all__ = ["ApplicationNvmeAccess", "ApplicationNvmeAccessSchema"]
__pdoc__ = {
    "ApplicationNvmeAccessSchema.resource": False,
    "ApplicationNvmeAccess": False,
}


class ApplicationNvmeAccessSchema(ResourceSchema):
    """The fields of the ApplicationNvmeAccess object"""

    backing_storage = fields.Nested("netapp_ontap.models.application_nvme_access_backing_storage.ApplicationNvmeAccessBackingStorageSchema", unknown=EXCLUDE, data_key="backing_storage")
    r""" The backing_storage field of the application_nvme_access. """

    is_clone = fields.Boolean(data_key="is_clone")
    r""" Clone """

    subsystem_map = fields.Nested("netapp_ontap.models.application_subsystem_map_object.ApplicationSubsystemMapObjectSchema", unknown=EXCLUDE, data_key="subsystem_map")
    r""" The subsystem_map field of the application_nvme_access. """

    @property
    def resource(self):
        return ApplicationNvmeAccess

    @property
    def patchable_fields(self):
        return [
            "backing_storage",
        ]

    @property
    def postable_fields(self):
        return [
            "backing_storage",
        ]


class ApplicationNvmeAccess(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationNvmeAccessSchema
