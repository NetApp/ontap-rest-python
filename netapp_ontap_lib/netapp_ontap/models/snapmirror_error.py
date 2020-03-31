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


__all__ = ["SnapmirrorError", "SnapmirrorErrorSchema"]
__pdoc__ = {
    "SnapmirrorErrorSchema.resource": False,
    "SnapmirrorError": False,
}


class SnapmirrorErrorSchema(ResourceSchema):
    """The fields of the SnapmirrorError object"""

    code = fields.Integer(data_key="code")
    r""" Error code """

    message = fields.Str(data_key="message")
    r""" Error message """

    parameters = fields.List(fields.Str, data_key="parameters")
    r""" Parameters for the error message """

    @property
    def resource(self):
        return SnapmirrorError

    @property
    def patchable_fields(self):
        return [
            "code",
            "message",
            "parameters",
        ]

    @property
    def postable_fields(self):
        return [
            "code",
            "message",
            "parameters",
        ]


class SnapmirrorError(Resource):  # pylint: disable=missing-docstring

    _schema = SnapmirrorErrorSchema
