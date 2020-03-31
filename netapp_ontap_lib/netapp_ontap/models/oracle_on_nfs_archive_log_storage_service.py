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


__all__ = ["OracleOnNfsArchiveLogStorageService", "OracleOnNfsArchiveLogStorageServiceSchema"]
__pdoc__ = {
    "OracleOnNfsArchiveLogStorageServiceSchema.resource": False,
    "OracleOnNfsArchiveLogStorageService": False,
}


class OracleOnNfsArchiveLogStorageServiceSchema(ResourceSchema):
    """The fields of the OracleOnNfsArchiveLogStorageService object"""

    name = fields.Str(data_key="name")
    r""" The storage service of the archive log.

Valid choices:

* extreme
* performance
* value """

    @property
    def resource(self):
        return OracleOnNfsArchiveLogStorageService

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


class OracleOnNfsArchiveLogStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = OracleOnNfsArchiveLogStorageServiceSchema
