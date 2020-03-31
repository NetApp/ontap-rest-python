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


__all__ = ["SvmNis", "SvmNisSchema"]
__pdoc__ = {
    "SvmNisSchema.resource": False,
    "SvmNis": False,
}


class SvmNisSchema(ResourceSchema):
    """The fields of the SvmNis object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the svm_nis. """

    domain = fields.Str(data_key="domain")
    r""" The domain field of the svm_nis. """

    enabled = fields.Boolean(data_key="enabled")
    r""" Enable NIS? Setting to true creates a configuration if not already created. """

    servers = fields.List(fields.Str, data_key="servers")
    r""" The servers field of the svm_nis. """

    @property
    def resource(self):
        return SvmNis

    @property
    def patchable_fields(self):
        return [
            "domain",
            "enabled",
            "servers",
        ]

    @property
    def postable_fields(self):
        return [
            "domain",
            "enabled",
            "servers",
        ]


class SvmNis(Resource):  # pylint: disable=missing-docstring

    _schema = SvmNisSchema
