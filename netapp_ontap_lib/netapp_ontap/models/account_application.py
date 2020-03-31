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


__all__ = ["AccountApplication", "AccountApplicationSchema"]
__pdoc__ = {
    "AccountApplicationSchema.resource": False,
    "AccountApplication": False,
}


class AccountApplicationSchema(ResourceSchema):
    """The fields of the AccountApplication object"""

    application = fields.Str(data_key="application")
    r""" Applications

Valid choices:

* console
* http
* ontapi
* service_processor
* ssh """

    authentication_methods = fields.List(fields.Str, data_key="authentication_methods")
    r""" The authentication_methods field of the account_application. """

    second_authentication_method = fields.Str(data_key="second_authentication_method")
    r""" An optional additional authentication method for MFA. This only works with SSH as the application. It is ignored for all other applications.

Valid choices:

* none
* password
* publickey
* nsswitch """

    @property
    def resource(self):
        return AccountApplication

    @property
    def patchable_fields(self):
        return [
            "application",
            "authentication_methods",
            "second_authentication_method",
        ]

    @property
    def postable_fields(self):
        return [
            "application",
            "authentication_methods",
            "second_authentication_method",
        ]


class AccountApplication(Resource):  # pylint: disable=missing-docstring

    _schema = AccountApplicationSchema
