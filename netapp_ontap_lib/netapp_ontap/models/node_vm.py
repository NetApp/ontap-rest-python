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


__all__ = ["NodeVm", "NodeVmSchema"]
__pdoc__ = {
    "NodeVmSchema.resource": False,
    "NodeVm": False,
}


class NodeVmSchema(ResourceSchema):
    """The fields of the NodeVm object"""

    provider_type = fields.Str(data_key="provider_type")
    r""" Cloud provider where the VM is hosted.

Valid choices:

* GoogleCloud
* AWS_S3
* Azure_Cloud """

    @property
    def resource(self):
        return NodeVm

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class NodeVm(Resource):  # pylint: disable=missing-docstring

    _schema = NodeVmSchema
