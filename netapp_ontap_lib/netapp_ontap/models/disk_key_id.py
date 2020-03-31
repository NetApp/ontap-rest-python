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


__all__ = ["DiskKeyId", "DiskKeyIdSchema"]
__pdoc__ = {
    "DiskKeyIdSchema.resource": False,
    "DiskKeyId": False,
}


class DiskKeyIdSchema(ResourceSchema):
    """The fields of the DiskKeyId object"""

    data = fields.Str(data_key="data")
    r""" Key ID of the data authentication key """

    fips = fields.Str(data_key="fips")
    r""" Key ID of the FIPS authentication key """

    @property
    def resource(self):
        return DiskKeyId

    @property
    def patchable_fields(self):
        return [
            "data",
            "fips",
        ]

    @property
    def postable_fields(self):
        return [
            "data",
            "fips",
        ]


class DiskKeyId(Resource):  # pylint: disable=missing-docstring

    _schema = DiskKeyIdSchema
