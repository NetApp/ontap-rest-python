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


__all__ = ["SoftwarePackageDownloadGet", "SoftwarePackageDownloadGetSchema"]
__pdoc__ = {
    "SoftwarePackageDownloadGetSchema.resource": False,
    "SoftwarePackageDownloadGet": False,
}


class SoftwarePackageDownloadGetSchema(ResourceSchema):
    """The fields of the SoftwarePackageDownloadGet object"""

    code = fields.Integer(data_key="code")
    r""" Code corresponds to download message

Example: 10551496 """

    message = fields.Str(data_key="message")
    r""" Download progress details

Example: Package download in progress """

    state = fields.Str(data_key="state")
    r""" Download status of the package

Valid choices:

* not_started
* running
* success
* failure """

    @property
    def resource(self):
        return SoftwarePackageDownloadGet

    @property
    def patchable_fields(self):
        return [
            "code",
            "message",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "code",
            "message",
            "state",
        ]


class SoftwarePackageDownloadGet(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwarePackageDownloadGetSchema
