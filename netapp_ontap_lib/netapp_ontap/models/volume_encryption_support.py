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


__all__ = ["VolumeEncryptionSupport", "VolumeEncryptionSupportSchema"]
__pdoc__ = {
    "VolumeEncryptionSupportSchema.resource": False,
    "VolumeEncryptionSupport": False,
}


class VolumeEncryptionSupportSchema(ResourceSchema):
    """The fields of the VolumeEncryptionSupport object"""

    code = fields.Integer(data_key="code")
    r""" Code corresponding to the status message. Returns a 0 if volume encryption is supported in all nodes of the cluster.

Example: 346758 """

    message = fields.Str(data_key="message")
    r""" Reason for not supporting volume encryption.

Example: No platform support for volume encryption in following nodes - node1, node2. """

    supported = fields.Boolean(data_key="supported")
    r""" Set to true when volume encryption support is available on all nodes of the cluster. """

    @property
    def resource(self):
        return VolumeEncryptionSupport

    @property
    def patchable_fields(self):
        return [
            "code",
            "message",
            "supported",
        ]

    @property
    def postable_fields(self):
        return [
            "code",
            "message",
            "supported",
        ]


class VolumeEncryptionSupport(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeEncryptionSupportSchema
