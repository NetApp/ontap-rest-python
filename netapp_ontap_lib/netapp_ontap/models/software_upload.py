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


__all__ = ["SoftwareUpload", "SoftwareUploadSchema"]
__pdoc__ = {
    "SoftwareUploadSchema.resource": False,
    "SoftwareUpload": False,
}


class SoftwareUploadSchema(ResourceSchema):
    """The fields of the SoftwareUpload object"""

    file = fields.Str(data_key="file")
    r""" Package file on a local file system

Example: base64 encoded package file content """

    @property
    def resource(self):
        return SoftwareUpload

    @property
    def patchable_fields(self):
        return [
            "file",
        ]

    @property
    def postable_fields(self):
        return [
            "file",
        ]


class SoftwareUpload(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareUploadSchema
