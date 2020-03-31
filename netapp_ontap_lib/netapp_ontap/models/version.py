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


__all__ = ["Version", "VersionSchema"]
__pdoc__ = {
    "VersionSchema.resource": False,
    "Version": False,
}


class VersionSchema(ResourceSchema):
    """The fields of the Version object"""

    full = fields.Str(data_key="full")
    r""" The full cluster version string.

Example: NetApp Release 9.4.0: Sun Nov 05 18:20:57 UTC 2017 """

    generation = fields.Integer(data_key="generation")
    r""" The generation portion of the version.

Example: 9 """

    major = fields.Integer(data_key="major")
    r""" The major portion of the version.

Example: 4 """

    minor = fields.Integer(data_key="minor")
    r""" The minor portion of the version.

Example: 0 """

    @property
    def resource(self):
        return Version

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class Version(Resource):  # pylint: disable=missing-docstring

    _schema = VersionSchema
