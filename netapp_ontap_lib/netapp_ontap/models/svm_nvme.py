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


__all__ = ["SvmNvme", "SvmNvmeSchema"]
__pdoc__ = {
    "SvmNvmeSchema.resource": False,
    "SvmNvme": False,
}


class SvmNvmeSchema(ResourceSchema):
    """The fields of the SvmNvme object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the svm_nvme. """

    enabled = fields.Boolean(data_key="enabled")
    r""" Enable NVMe? Setting to true creates a service if not already created. """

    @property
    def resource(self):
        return SvmNvme

    @property
    def patchable_fields(self):
        return [
            "enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
        ]


class SvmNvme(Resource):  # pylint: disable=missing-docstring

    _schema = SvmNvmeSchema
