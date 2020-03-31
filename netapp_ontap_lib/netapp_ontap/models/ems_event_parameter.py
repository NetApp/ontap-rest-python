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


__all__ = ["EmsEventParameter", "EmsEventParameterSchema"]
__pdoc__ = {
    "EmsEventParameterSchema.resource": False,
    "EmsEventParameter": False,
}


class EmsEventParameterSchema(ResourceSchema):
    """The fields of the EmsEventParameter object"""

    name = fields.Str(data_key="name")
    r""" Name of parameter

Example: numOps """

    value = fields.Str(data_key="value")
    r""" Value of parameter

Example: 123 """

    @property
    def resource(self):
        return EmsEventParameter

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class EmsEventParameter(Resource):  # pylint: disable=missing-docstring

    _schema = EmsEventParameterSchema
