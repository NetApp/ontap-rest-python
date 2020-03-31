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


__all__ = ["MongoDbOnSanProtectionType", "MongoDbOnSanProtectionTypeSchema"]
__pdoc__ = {
    "MongoDbOnSanProtectionTypeSchema.resource": False,
    "MongoDbOnSanProtectionType": False,
}


class MongoDbOnSanProtectionTypeSchema(ResourceSchema):
    """The fields of the MongoDbOnSanProtectionType object"""

    local_rpo = fields.Str(data_key="local_rpo")
    r""" The local rpo of the application.

Valid choices:

* hourly
* none """

    remote_rpo = fields.Str(data_key="remote_rpo")
    r""" The remote rpo of the application.

Valid choices:

* none
* zero """

    @property
    def resource(self):
        return MongoDbOnSanProtectionType

    @property
    def patchable_fields(self):
        return [
            "local_rpo",
        ]

    @property
    def postable_fields(self):
        return [
            "local_rpo",
            "remote_rpo",
        ]


class MongoDbOnSanProtectionType(Resource):  # pylint: disable=missing-docstring

    _schema = MongoDbOnSanProtectionTypeSchema
