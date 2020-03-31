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


__all__ = ["ZappNvmeRpo", "ZappNvmeRpoSchema"]
__pdoc__ = {
    "ZappNvmeRpoSchema.resource": False,
    "ZappNvmeRpo": False,
}


class ZappNvmeRpoSchema(ResourceSchema):
    """The fields of the ZappNvmeRpo object"""

    local = fields.Nested("netapp_ontap.models.zapp_nvme_rpo_local.ZappNvmeRpoLocalSchema", unknown=EXCLUDE, data_key="local")
    r""" The local field of the zapp_nvme_rpo. """

    @property
    def resource(self):
        return ZappNvmeRpo

    @property
    def patchable_fields(self):
        return [
            "local",
        ]

    @property
    def postable_fields(self):
        return [
            "local",
        ]


class ZappNvmeRpo(Resource):  # pylint: disable=missing-docstring

    _schema = ZappNvmeRpoSchema
