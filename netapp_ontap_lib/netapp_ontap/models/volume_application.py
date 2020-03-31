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


__all__ = ["VolumeApplication", "VolumeApplicationSchema"]
__pdoc__ = {
    "VolumeApplicationSchema.resource": False,
    "VolumeApplication": False,
}


class VolumeApplicationSchema(ResourceSchema):
    """The fields of the VolumeApplication object"""

    name = fields.Str(data_key="name")
    r""" Name of the application to which the volume belongs. Available only when the volume is part of an application. """

    uuid = fields.Str(data_key="uuid")
    r""" UUID of the application to which the volume belongs. Available only when the volume is part of an application.

Example: 1cd8a442-86d1-11e0-ae1d-123478563412 """

    @property
    def resource(self):
        return VolumeApplication

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class VolumeApplication(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeApplicationSchema
