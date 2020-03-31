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


__all__ = ["LunMovementProgressFailure", "LunMovementProgressFailureSchema"]
__pdoc__ = {
    "LunMovementProgressFailureSchema.resource": False,
    "LunMovementProgressFailure": False,
}


class LunMovementProgressFailureSchema(ResourceSchema):
    """The fields of the LunMovementProgressFailure object"""

    code = fields.Str(data_key="code")
    r""" The error code.


Example: 4 """

    message = fields.Str(data_key="message")
    r""" The error message.


Example: Destination volume is offline. """

    @property
    def resource(self):
        return LunMovementProgressFailure

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class LunMovementProgressFailure(Resource):  # pylint: disable=missing-docstring

    _schema = LunMovementProgressFailureSchema
