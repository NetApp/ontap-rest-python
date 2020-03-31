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


__all__ = ["ApplicationSanAccessFcpEndpoint", "ApplicationSanAccessFcpEndpointSchema"]
__pdoc__ = {
    "ApplicationSanAccessFcpEndpointSchema.resource": False,
    "ApplicationSanAccessFcpEndpoint": False,
}


class ApplicationSanAccessFcpEndpointSchema(ResourceSchema):
    """The fields of the ApplicationSanAccessFcpEndpoint object"""

    interface = fields.Nested("netapp_ontap.resources.fc_interface.FcInterfaceSchema", unknown=EXCLUDE, data_key="interface")
    r""" The interface field of the application_san_access_fcp_endpoint. """

    @property
    def resource(self):
        return ApplicationSanAccessFcpEndpoint

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationSanAccessFcpEndpoint(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSanAccessFcpEndpointSchema
