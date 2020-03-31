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


__all__ = ["KerberosRealmAdServer", "KerberosRealmAdServerSchema"]
__pdoc__ = {
    "KerberosRealmAdServerSchema.resource": False,
    "KerberosRealmAdServer": False,
}


class KerberosRealmAdServerSchema(ResourceSchema):
    """The fields of the KerberosRealmAdServer object"""

    address = fields.Str(data_key="address")
    r""" Active Directory server IP address

Example: 1.2.3.4 """

    name = fields.Str(data_key="name")
    r""" Active Directory server name """

    @property
    def resource(self):
        return KerberosRealmAdServer

    @property
    def patchable_fields(self):
        return [
            "address",
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "address",
            "name",
        ]


class KerberosRealmAdServer(Resource):  # pylint: disable=missing-docstring

    _schema = KerberosRealmAdServerSchema
