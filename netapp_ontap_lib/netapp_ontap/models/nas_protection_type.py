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


__all__ = ["NasProtectionType", "NasProtectionTypeSchema"]
__pdoc__ = {
    "NasProtectionTypeSchema.resource": False,
    "NasProtectionType": False,
}


class NasProtectionTypeSchema(ResourceSchema):
    """The fields of the NasProtectionType object"""

    local_policy = fields.Str(data_key="local_policy")
    r""" The snapshot policy to apply to each volume in the smart container. This property is only supported for smart containers. Usage: &lt;snapshot policy&gt; """

    local_rpo = fields.Str(data_key="local_rpo")
    r""" The local rpo of the application.

Valid choices:

* hourly
* none """

    remote_rpo = fields.Str(data_key="remote_rpo")
    r""" The remote rpo of the application.

Valid choices:

* none
* zero """

    @property
    def resource(self):
        return NasProtectionType

    @property
    def patchable_fields(self):
        return [
            "local_rpo",
        ]

    @property
    def postable_fields(self):
        return [
            "local_policy",
            "local_rpo",
            "remote_rpo",
        ]


class NasProtectionType(Resource):  # pylint: disable=missing-docstring

    _schema = NasProtectionTypeSchema
