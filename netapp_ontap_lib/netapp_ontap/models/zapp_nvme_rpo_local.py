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


__all__ = ["ZappNvmeRpoLocal", "ZappNvmeRpoLocalSchema"]
__pdoc__ = {
    "ZappNvmeRpoLocalSchema.resource": False,
    "ZappNvmeRpoLocal": False,
}


class ZappNvmeRpoLocalSchema(ResourceSchema):
    """The fields of the ZappNvmeRpoLocal object"""

    name = fields.Str(data_key="name")
    r""" The local rpo of the application.

Valid choices:

* hourly
* none """

    policy = fields.Str(data_key="policy")
    r""" The snapshot policy to apply to each volume in the smart container. This property is only supported for smart containers. Usage: &lt;snapshot policy&gt; """

    @property
    def resource(self):
        return ZappNvmeRpoLocal

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "policy",
        ]


class ZappNvmeRpoLocal(Resource):  # pylint: disable=missing-docstring

    _schema = ZappNvmeRpoLocalSchema
