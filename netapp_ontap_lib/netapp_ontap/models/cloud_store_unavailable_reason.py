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


__all__ = ["CloudStoreUnavailableReason", "CloudStoreUnavailableReasonSchema"]
__pdoc__ = {
    "CloudStoreUnavailableReasonSchema.resource": False,
    "CloudStoreUnavailableReason": False,
}


class CloudStoreUnavailableReasonSchema(ResourceSchema):
    """The fields of the CloudStoreUnavailableReason object"""

    message = fields.Str(data_key="message")
    r""" Indicates why the object store is unavailable. """

    @property
    def resource(self):
        return CloudStoreUnavailableReason

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class CloudStoreUnavailableReason(Resource):  # pylint: disable=missing-docstring

    _schema = CloudStoreUnavailableReasonSchema
