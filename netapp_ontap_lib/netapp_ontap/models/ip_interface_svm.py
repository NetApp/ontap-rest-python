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


__all__ = ["IpInterfaceSvm", "IpInterfaceSvmSchema"]
__pdoc__ = {
    "IpInterfaceSvmSchema.resource": False,
    "IpInterfaceSvm": False,
}


class IpInterfaceSvmSchema(ResourceSchema):
    """The fields of the IpInterfaceSvm object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the ip_interface_svm. """

    ip = fields.Nested("netapp_ontap.models.ip_interface_svm_ip.IpInterfaceSvmIpSchema", unknown=EXCLUDE, data_key="ip")
    r""" The ip field of the ip_interface_svm. """

    location = fields.Nested("netapp_ontap.models.ip_interface_svm_location.IpInterfaceSvmLocationSchema", unknown=EXCLUDE, data_key="location")
    r""" The location field of the ip_interface_svm. """

    name = fields.Str(data_key="name")
    r""" The name of the interface (optional).

Example: lif1 """

    service_policy = fields.Str(data_key="service_policy")
    r""" The service_policy field of the ip_interface_svm. """

    services = fields.List(fields.Str, data_key="services")
    r""" The services associated with the interface. """

    uuid = fields.Str(data_key="uuid")
    r""" The UUID that uniquely identifies the interface.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return IpInterfaceSvm

    @property
    def patchable_fields(self):
        return [
            "ip",
            "service_policy",
        ]

    @property
    def postable_fields(self):
        return [
            "ip",
            "location",
            "name",
            "service_policy",
        ]


class IpInterfaceSvm(Resource):  # pylint: disable=missing-docstring

    _schema = IpInterfaceSvmSchema
