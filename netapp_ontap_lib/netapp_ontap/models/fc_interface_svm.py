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


__all__ = ["FcInterfaceSvm", "FcInterfaceSvmSchema"]
__pdoc__ = {
    "FcInterfaceSvmSchema.resource": False,
    "FcInterfaceSvm": False,
}


class FcInterfaceSvmSchema(ResourceSchema):
    """The fields of the FcInterfaceSvm object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the fc_interface_svm. """

    data_protocol = fields.Str(data_key="data_protocol")
    r""" The data protocol for which the Fibre Channel interface is configured.

Valid choices:

* fcp
* fc_nvme """

    location = fields.Nested("netapp_ontap.models.fc_interface_svm_location.FcInterfaceSvmLocationSchema", unknown=EXCLUDE, data_key="location")
    r""" The location field of the fc_interface_svm. """

    name = fields.Str(data_key="name")
    r""" The name of the Fibre Channel interface.

Example: lif1 """

    uuid = fields.Str(data_key="uuid")
    r""" The unique identifier of the Fibre Channel interface.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return FcInterfaceSvm

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "data_protocol",
            "location",
            "name",
        ]


class FcInterfaceSvm(Resource):  # pylint: disable=missing-docstring

    _schema = FcInterfaceSvmSchema
