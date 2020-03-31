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


__all__ = ["MaxdataOnSanApplicationComponentsProtectionType", "MaxdataOnSanApplicationComponentsProtectionTypeSchema"]
__pdoc__ = {
    "MaxdataOnSanApplicationComponentsProtectionTypeSchema.resource": False,
    "MaxdataOnSanApplicationComponentsProtectionType": False,
}


class MaxdataOnSanApplicationComponentsProtectionTypeSchema(ResourceSchema):
    """The fields of the MaxdataOnSanApplicationComponentsProtectionType object"""

    local_rpo = fields.Str(data_key="local_rpo")
    r""" The local rpo of the application component.

Valid choices:

* 6_hourly
* 15_minutely
* hourly
* none """

    remote_rpo = fields.Str(data_key="remote_rpo")
    r""" The remote rpo of the application component.

Valid choices:

* 6_hourly
* 15_minutely
* hourly
* none """

    @property
    def resource(self):
        return MaxdataOnSanApplicationComponentsProtectionType

    @property
    def patchable_fields(self):
        return [
            "local_rpo",
            "remote_rpo",
        ]

    @property
    def postable_fields(self):
        return [
            "local_rpo",
            "remote_rpo",
        ]


class MaxdataOnSanApplicationComponentsProtectionType(Resource):  # pylint: disable=missing-docstring

    _schema = MaxdataOnSanApplicationComponentsProtectionTypeSchema
