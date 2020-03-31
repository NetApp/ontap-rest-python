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


__all__ = ["MongoDbOnSanSecondaryIgroups", "MongoDbOnSanSecondaryIgroupsSchema"]
__pdoc__ = {
    "MongoDbOnSanSecondaryIgroupsSchema.resource": False,
    "MongoDbOnSanSecondaryIgroups": False,
}


class MongoDbOnSanSecondaryIgroupsSchema(ResourceSchema):
    """The fields of the MongoDbOnSanSecondaryIgroups object"""

    name = fields.Str(data_key="name")
    r""" The name of the initiator group for each secondary. """

    @property
    def resource(self):
        return MongoDbOnSanSecondaryIgroups

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


class MongoDbOnSanSecondaryIgroups(Resource):  # pylint: disable=missing-docstring

    _schema = MongoDbOnSanSecondaryIgroupsSchema
