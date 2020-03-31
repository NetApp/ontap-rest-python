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


__all__ = ["FlexcacheGuarantee", "FlexcacheGuaranteeSchema"]
__pdoc__ = {
    "FlexcacheGuaranteeSchema.resource": False,
    "FlexcacheGuarantee": False,
}


class FlexcacheGuaranteeSchema(ResourceSchema):
    """The fields of the FlexcacheGuarantee object"""

    type = fields.Str(data_key="type")
    r""" The type of space guarantee of this volume in the aggregate.

Valid choices:

* volume
* none """

    @property
    def resource(self):
        return FlexcacheGuarantee

    @property
    def patchable_fields(self):
        return [
            "type",
        ]

    @property
    def postable_fields(self):
        return [
            "type",
        ]


class FlexcacheGuarantee(Resource):  # pylint: disable=missing-docstring

    _schema = FlexcacheGuaranteeSchema
