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


__all__ = ["VsiOnNasDatastoreStorageService", "VsiOnNasDatastoreStorageServiceSchema"]
__pdoc__ = {
    "VsiOnNasDatastoreStorageServiceSchema.resource": False,
    "VsiOnNasDatastoreStorageService": False,
}


class VsiOnNasDatastoreStorageServiceSchema(ResourceSchema):
    """The fields of the VsiOnNasDatastoreStorageService object"""

    name = fields.Str(data_key="name")
    r""" The storage service of the datastore.

Valid choices:

* extreme
* performance
* value """

    @property
    def resource(self):
        return VsiOnNasDatastoreStorageService

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class VsiOnNasDatastoreStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = VsiOnNasDatastoreStorageServiceSchema
