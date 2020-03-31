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


__all__ = ["LunMovementPaths", "LunMovementPathsSchema"]
__pdoc__ = {
    "LunMovementPathsSchema.resource": False,
    "LunMovementPaths": False,
}


class LunMovementPathsSchema(ResourceSchema):
    """The fields of the LunMovementPaths object"""

    destination = fields.Str(data_key="destination")
    r""" The fully qualified path of the LUN movement destination composed of a "/vol" prefix, the volume name, the (optional) qtree name, and base name of the LUN.

Example: /vol/vol1/lun1 """

    source = fields.Str(data_key="source")
    r""" The fully qualified path of the LUN movement source composed of a "/vol" prefix, the volume name, the (optional) qtree name, and base name of the LUN.


Example: /vol/vol2/lun2 """

    @property
    def resource(self):
        return LunMovementPaths

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class LunMovementPaths(Resource):  # pylint: disable=missing-docstring

    _schema = LunMovementPathsSchema
