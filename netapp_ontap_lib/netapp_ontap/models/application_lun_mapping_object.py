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


__all__ = ["ApplicationLunMappingObject", "ApplicationLunMappingObjectSchema"]
__pdoc__ = {
    "ApplicationLunMappingObjectSchema.resource": False,
    "ApplicationLunMappingObject": False,
}


class ApplicationLunMappingObjectSchema(ResourceSchema):
    """The fields of the ApplicationLunMappingObject object"""

    fcp = fields.List(fields.Nested("netapp_ontap.models.application_san_access_fcp_endpoint.ApplicationSanAccessFcpEndpointSchema", unknown=EXCLUDE), data_key="fcp")
    r""" All possible Fibre Channel Protocol (FCP) access endpoints for the LUN. """

    igroup = fields.Nested("netapp_ontap.models.application_lun_mapping_object_igroup.ApplicationLunMappingObjectIgroupSchema", unknown=EXCLUDE, data_key="igroup")
    r""" The igroup field of the application_lun_mapping_object. """

    iscsi = fields.List(fields.Nested("netapp_ontap.models.application_san_access_iscsi_endpoint.ApplicationSanAccessIscsiEndpointSchema", unknown=EXCLUDE), data_key="iscsi")
    r""" All possible iSCSI access endpoints for the LUN. """

    lun_id = fields.Integer(data_key="lun_id")
    r""" LUN ID """

    @property
    def resource(self):
        return ApplicationLunMappingObject

    @property
    def patchable_fields(self):
        return [
            "igroup",
        ]

    @property
    def postable_fields(self):
        return [
            "igroup",
        ]


class ApplicationLunMappingObject(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationLunMappingObjectSchema
