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


__all__ = ["ApplicationBackingStorage", "ApplicationBackingStorageSchema"]
__pdoc__ = {
    "ApplicationBackingStorageSchema.resource": False,
    "ApplicationBackingStorage": False,
}


class ApplicationBackingStorageSchema(ResourceSchema):
    """The fields of the ApplicationBackingStorage object"""

    luns = fields.List(fields.Nested("netapp_ontap.models.application_lun_object.ApplicationLunObjectSchema", unknown=EXCLUDE), data_key="luns")
    r""" The luns field of the application_backing_storage. """

    namespaces = fields.List(fields.Nested("netapp_ontap.models.application_namespace_object.ApplicationNamespaceObjectSchema", unknown=EXCLUDE), data_key="namespaces")
    r""" The namespaces field of the application_backing_storage. """

    volumes = fields.List(fields.Nested("netapp_ontap.models.application_volume_object.ApplicationVolumeObjectSchema", unknown=EXCLUDE), data_key="volumes")
    r""" The volumes field of the application_backing_storage. """

    @property
    def resource(self):
        return ApplicationBackingStorage

    @property
    def patchable_fields(self):
        return [
            "luns",
            "namespaces",
            "volumes",
        ]

    @property
    def postable_fields(self):
        return [
            "luns",
            "namespaces",
            "volumes",
        ]


class ApplicationBackingStorage(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationBackingStorageSchema
