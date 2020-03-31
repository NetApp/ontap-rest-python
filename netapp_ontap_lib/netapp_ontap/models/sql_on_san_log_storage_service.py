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


__all__ = ["SqlOnSanLogStorageService", "SqlOnSanLogStorageServiceSchema"]
__pdoc__ = {
    "SqlOnSanLogStorageServiceSchema.resource": False,
    "SqlOnSanLogStorageService": False,
}


class SqlOnSanLogStorageServiceSchema(ResourceSchema):
    """The fields of the SqlOnSanLogStorageService object"""

    name = fields.Str(data_key="name")
    r""" The storage service of the log DB.

Valid choices:

* extreme
* performance
* value """

    @property
    def resource(self):
        return SqlOnSanLogStorageService

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


class SqlOnSanLogStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = SqlOnSanLogStorageServiceSchema
