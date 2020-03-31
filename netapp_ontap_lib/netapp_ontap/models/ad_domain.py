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


__all__ = ["AdDomain", "AdDomainSchema"]
__pdoc__ = {
    "AdDomainSchema.resource": False,
    "AdDomain": False,
}


class AdDomainSchema(ResourceSchema):
    """The fields of the AdDomain object"""

    fqdn = fields.Str(data_key="fqdn")
    r""" The fully qualified domain name of the Windows Active Directory to which this CIFS server belongs. A CIFS server appears as a member of Windows server object in the Active Directory store. POST and PATCH only.

Example: example.com """

    organizational_unit = fields.Str(data_key="organizational_unit")
    r""" Specifies the organizational unit within the Active Directory domain to associate with the CIFS server. POST and PATCH only. """

    password = fields.Str(data_key="password")
    r""" The account password used to add this CIFS server to the Active Directory. This is not audited. """

    user = fields.Str(data_key="user")
    r""" The user account used to add this CIFS server to the Active Directory. POST and DELETE only. """

    @property
    def resource(self):
        return AdDomain

    @property
    def patchable_fields(self):
        return [
            "fqdn",
            "organizational_unit",
            "password",
        ]

    @property
    def postable_fields(self):
        return [
            "fqdn",
            "organizational_unit",
            "password",
            "user",
        ]


class AdDomain(Resource):  # pylint: disable=missing-docstring

    _schema = AdDomainSchema
