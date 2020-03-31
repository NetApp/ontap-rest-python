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


__all__ = ["SoftwareReferenceMetroclusterProgressSummary", "SoftwareReferenceMetroclusterProgressSummarySchema"]
__pdoc__ = {
    "SoftwareReferenceMetroclusterProgressSummarySchema.resource": False,
    "SoftwareReferenceMetroclusterProgressSummary": False,
}


class SoftwareReferenceMetroclusterProgressSummarySchema(ResourceSchema):
    """The fields of the SoftwareReferenceMetroclusterProgressSummary object"""

    message = fields.Str(data_key="message")
    r""" MetroCluster update progress summary.

Example: MetroCluster updated successfully. """

    @property
    def resource(self):
        return SoftwareReferenceMetroclusterProgressSummary

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


class SoftwareReferenceMetroclusterProgressSummary(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareReferenceMetroclusterProgressSummarySchema
