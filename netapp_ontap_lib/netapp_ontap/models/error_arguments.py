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


__all__ = ["ErrorArguments", "ErrorArgumentsSchema"]
__pdoc__ = {
    "ErrorArgumentsSchema.resource": False,
    "ErrorArguments": False,
}


class ErrorArgumentsSchema(ResourceSchema):
    """The fields of the ErrorArguments object"""

    code = fields.Str(data_key="code")
    r""" Argument code """

    message = fields.Str(data_key="message")
    r""" Message argument """

    @property
    def resource(self):
        return ErrorArguments

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ErrorArguments(Resource):  # pylint: disable=missing-docstring

    _schema = ErrorArgumentsSchema
