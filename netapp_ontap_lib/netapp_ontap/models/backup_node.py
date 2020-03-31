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


__all__ = ["BackupNode", "BackupNodeSchema"]
__pdoc__ = {
    "BackupNodeSchema.resource": False,
    "BackupNode": False,
}


class BackupNodeSchema(ResourceSchema):
    """The fields of the BackupNode object"""

    name = fields.Str(data_key="name")
    r""" The name field of the backup_node. """

    @property
    def resource(self):
        return BackupNode

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


class BackupNode(Resource):  # pylint: disable=missing-docstring

    _schema = BackupNodeSchema
