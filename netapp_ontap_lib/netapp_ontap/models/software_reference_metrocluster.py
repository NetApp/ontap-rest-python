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


__all__ = ["SoftwareReferenceMetrocluster", "SoftwareReferenceMetroclusterSchema"]
__pdoc__ = {
    "SoftwareReferenceMetroclusterSchema.resource": False,
    "SoftwareReferenceMetrocluster": False,
}


class SoftwareReferenceMetroclusterSchema(ResourceSchema):
    """The fields of the SoftwareReferenceMetrocluster object"""

    clusters = fields.List(fields.Nested("netapp_ontap.models.software_mcc.SoftwareMccSchema", unknown=EXCLUDE), data_key="clusters")
    r""" List of MetroCluster sites, statuses, and active ONTAP versions. """

    progress_details = fields.Nested("netapp_ontap.models.software_reference_metrocluster_progress_details.SoftwareReferenceMetroclusterProgressDetailsSchema", unknown=EXCLUDE, data_key="progress_details")
    r""" The progress_details field of the software_reference_metrocluster. """

    progress_summary = fields.Nested("netapp_ontap.models.software_reference_metrocluster_progress_summary.SoftwareReferenceMetroclusterProgressSummarySchema", unknown=EXCLUDE, data_key="progress_summary")
    r""" The progress_summary field of the software_reference_metrocluster. """

    @property
    def resource(self):
        return SoftwareReferenceMetrocluster

    @property
    def patchable_fields(self):
        return [
            "progress_details",
            "progress_summary",
        ]

    @property
    def postable_fields(self):
        return [
            "progress_details",
            "progress_summary",
        ]


class SoftwareReferenceMetrocluster(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareReferenceMetroclusterSchema
