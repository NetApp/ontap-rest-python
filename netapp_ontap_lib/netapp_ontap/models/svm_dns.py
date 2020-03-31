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


__all__ = ["SvmDns", "SvmDnsSchema"]
__pdoc__ = {
    "SvmDnsSchema.resource": False,
    "SvmDns": False,
}


class SvmDnsSchema(ResourceSchema):
    """The fields of the SvmDns object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the svm_dns. """

    domains = fields.List(fields.Str, data_key="domains")
    r""" The domains field of the svm_dns. """

    servers = fields.List(fields.Str, data_key="servers")
    r""" The servers field of the svm_dns. """

    @property
    def resource(self):
        return SvmDns

    @property
    def patchable_fields(self):
        return [
            "domains",
            "servers",
        ]

    @property
    def postable_fields(self):
        return [
            "domains",
            "servers",
        ]


class SvmDns(Resource):  # pylint: disable=missing-docstring

    _schema = SvmDnsSchema
