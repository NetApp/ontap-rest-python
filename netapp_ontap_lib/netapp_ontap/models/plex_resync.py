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


__all__ = ["PlexResync", "PlexResyncSchema"]
__pdoc__ = {
    "PlexResyncSchema.resource": False,
    "PlexResync": False,
}


class PlexResyncSchema(ResourceSchema):
    """The fields of the PlexResync object"""

    active = fields.Boolean(data_key="active")
    r""" Plex is being resynchronized to its mirrored plex """

    level = fields.Str(data_key="level")
    r""" Plex resyncing level

Valid choices:

* full
* incremental """

    percent = fields.Integer(data_key="percent")
    r""" Plex resyncing percentage

Example: 10 """

    @property
    def resource(self):
        return PlexResync

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class PlexResync(Resource):  # pylint: disable=missing-docstring

    _schema = PlexResyncSchema
