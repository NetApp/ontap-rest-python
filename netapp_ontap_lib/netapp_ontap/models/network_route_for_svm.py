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


__all__ = ["NetworkRouteForSvm", "NetworkRouteForSvmSchema"]
__pdoc__ = {
    "NetworkRouteForSvmSchema.resource": False,
    "NetworkRouteForSvm": False,
}


class NetworkRouteForSvmSchema(ResourceSchema):
    """The fields of the NetworkRouteForSvm object"""

    destination = fields.Nested("netapp_ontap.models.ip_info.IpInfoSchema", unknown=EXCLUDE, data_key="destination")
    r""" The destination field of the network_route_for_svm. """

    gateway = fields.Str(data_key="gateway")
    r""" The IP address of the gateway router leading to the destination.

Example: 10.1.1.1 """

    @property
    def resource(self):
        return NetworkRouteForSvm

    @property
    def patchable_fields(self):
        return [
            "destination",
            "gateway",
        ]

    @property
    def postable_fields(self):
        return [
            "destination",
            "gateway",
        ]


class NetworkRouteForSvm(Resource):  # pylint: disable=missing-docstring

    _schema = NetworkRouteForSvmSchema
