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


__all__ = ["SoftwareStatusDetailsReferenceAction", "SoftwareStatusDetailsReferenceActionSchema"]
__pdoc__ = {
    "SoftwareStatusDetailsReferenceActionSchema.resource": False,
    "SoftwareStatusDetailsReferenceAction": False,
}


class SoftwareStatusDetailsReferenceActionSchema(ResourceSchema):
    """The fields of the SoftwareStatusDetailsReferenceAction object"""

    message = fields.Str(data_key="message")
    r""" The message field of the software_status_details_reference_action. """

    @property
    def resource(self):
        return SoftwareStatusDetailsReferenceAction

    @property
    def patchable_fields(self):
        return [
            "message",
        ]

    @property
    def postable_fields(self):
        return [
            "message",
        ]


class SoftwareStatusDetailsReferenceAction(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareStatusDetailsReferenceActionSchema
