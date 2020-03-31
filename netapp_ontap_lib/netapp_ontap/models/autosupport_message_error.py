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


__all__ = ["AutosupportMessageError", "AutosupportMessageErrorSchema"]
__pdoc__ = {
    "AutosupportMessageErrorSchema.resource": False,
    "AutosupportMessageError": False,
}


class AutosupportMessageErrorSchema(ResourceSchema):
    """The fields of the AutosupportMessageError object"""

    code = fields.Integer(data_key="code")
    r""" Error code

Example: 53149746 """

    message = fields.Str(data_key="message")
    r""" Error message

Example: Could not resolve host: test.com """

    @property
    def resource(self):
        return AutosupportMessageError

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class AutosupportMessageError(Resource):  # pylint: disable=missing-docstring

    _schema = AutosupportMessageErrorSchema
