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


__all__ = ["SqlOnSmbAccess", "SqlOnSmbAccessSchema"]
__pdoc__ = {
    "SqlOnSmbAccessSchema.resource": False,
    "SqlOnSmbAccess": False,
}


class SqlOnSmbAccessSchema(ResourceSchema):
    """The fields of the SqlOnSmbAccess object"""

    installer = fields.Str(data_key="installer")
    r""" SQL installer admin user name. """

    service_account = fields.Str(data_key="service_account")
    r""" SQL service account user name. """

    @property
    def resource(self):
        return SqlOnSmbAccess

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "installer",
            "service_account",
        ]


class SqlOnSmbAccess(Resource):  # pylint: disable=missing-docstring

    _schema = SqlOnSmbAccessSchema
