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


__all__ = ["SvmCifsService", "SvmCifsServiceSchema"]
__pdoc__ = {
    "SvmCifsServiceSchema.resource": False,
    "SvmCifsService": False,
}


class SvmCifsServiceSchema(ResourceSchema):
    """The fields of the SvmCifsService object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the svm_cifs_service. """

    ad_domain = fields.Nested("netapp_ontap.models.ad_domain_svm.AdDomainSvmSchema", unknown=EXCLUDE, data_key="ad_domain")
    r""" The ad_domain field of the svm_cifs_service. """

    enabled = fields.Boolean(data_key="enabled")
    r""" Specifies whether or not the CIFS service is administratively enabled. """

    name = fields.Str(data_key="name")
    r""" The NetBIOS name of the CIFS server.

Example: CIFS1 """

    @property
    def resource(self):
        return SvmCifsService

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "name",
        ]


class SvmCifsService(Resource):  # pylint: disable=missing-docstring

    _schema = SvmCifsServiceSchema
