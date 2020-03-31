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


__all__ = ["SecurityAuditLogSvm", "SecurityAuditLogSvmSchema"]
__pdoc__ = {
    "SecurityAuditLogSvmSchema.resource": False,
    "SecurityAuditLogSvm": False,
}


class SecurityAuditLogSvmSchema(ResourceSchema):
    """The fields of the SecurityAuditLogSvm object"""

    name = fields.Str(data_key="name")
    r""" The name field of the security_audit_log_svm. """

    @property
    def resource(self):
        return SecurityAuditLogSvm

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class SecurityAuditLogSvm(Resource):  # pylint: disable=missing-docstring

    _schema = SecurityAuditLogSvmSchema
