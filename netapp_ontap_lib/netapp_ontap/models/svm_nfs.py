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


__all__ = ["SvmNfs", "SvmNfsSchema"]
__pdoc__ = {
    "SvmNfsSchema.resource": False,
    "SvmNfs": False,
}


class SvmNfsSchema(ResourceSchema):
    """The fields of the SvmNfs object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the svm_nfs. """

    enabled = fields.Boolean(data_key="enabled")
    r""" Enable NFS? Setting to true creates a service if not already created. """

    @property
    def resource(self):
        return SvmNfs

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


class SvmNfs(Resource):  # pylint: disable=missing-docstring

    _schema = SvmNfsSchema
