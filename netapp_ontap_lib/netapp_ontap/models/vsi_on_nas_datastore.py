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


__all__ = ["VsiOnNasDatastore", "VsiOnNasDatastoreSchema"]
__pdoc__ = {
    "VsiOnNasDatastoreSchema.resource": False,
    "VsiOnNasDatastore": False,
}


class VsiOnNasDatastoreSchema(ResourceSchema):
    """The fields of the VsiOnNasDatastore object"""

    count = fields.Integer(data_key="count")
    r""" The number of datastores to support. """

    size = fields.Integer(data_key="size")
    r""" The size of the datastore. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = fields.Nested("netapp_ontap.models.vsi_on_nas_datastore_storage_service.VsiOnNasDatastoreStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the vsi_on_nas_datastore. """

    @property
    def resource(self):
        return VsiOnNasDatastore

    @property
    def patchable_fields(self):
        return [
            "count",
            "storage_service",
        ]

    @property
    def postable_fields(self):
        return [
            "count",
            "size",
            "storage_service",
        ]


class VsiOnNasDatastore(Resource):  # pylint: disable=missing-docstring

    _schema = VsiOnNasDatastoreSchema
