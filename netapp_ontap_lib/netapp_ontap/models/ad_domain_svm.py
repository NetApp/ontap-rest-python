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


__all__ = ["AdDomainSvm", "AdDomainSvmSchema"]
__pdoc__ = {
    "AdDomainSvmSchema.resource": False,
    "AdDomainSvm": False,
}


class AdDomainSvmSchema(ResourceSchema):
    """The fields of the AdDomainSvm object"""

    fqdn = fields.Str(data_key="fqdn")
    r""" The fully qualified domain name of the Windows Active Directory to which this CIFS server belongs. A CIFS server appears as a member of Windows server object in the Active Directory store.


Example: example.com """

    organizational_unit = fields.Str(data_key="organizational_unit")
    r""" Specifies the organizational unit within the Active Directory domain to associate with the CIFS server. """

    password = fields.Str(data_key="password")
    r""" The account password used to add this CIFS server to the Active Directory. This is not audited. Valid in POST only. """

    user = fields.Str(data_key="user")
    r""" The user account used to add this CIFS server to the Active Directory. Valid in POST only. """

    @property
    def resource(self):
        return AdDomainSvm

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "fqdn",
            "organizational_unit",
            "password",
            "user",
        ]


class AdDomainSvm(Resource):  # pylint: disable=missing-docstring

    _schema = AdDomainSvmSchema
