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


__all__ = ["SoftwareReferenceMetroclusterProgressDetails", "SoftwareReferenceMetroclusterProgressDetailsSchema"]
__pdoc__ = {
    "SoftwareReferenceMetroclusterProgressDetailsSchema.resource": False,
    "SoftwareReferenceMetroclusterProgressDetails": False,
}


class SoftwareReferenceMetroclusterProgressDetailsSchema(ResourceSchema):
    """The fields of the SoftwareReferenceMetroclusterProgressDetails object"""

    message = fields.Str(data_key="message")
    r""" MetroCluster update progress details.

Example: Switchover in progress """

    @property
    def resource(self):
        return SoftwareReferenceMetroclusterProgressDetails

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


class SoftwareReferenceMetroclusterProgressDetails(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareReferenceMetroclusterProgressDetailsSchema
