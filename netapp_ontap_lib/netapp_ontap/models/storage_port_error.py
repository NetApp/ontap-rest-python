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


__all__ = ["StoragePortError", "StoragePortErrorSchema"]
__pdoc__ = {
    "StoragePortErrorSchema.resource": False,
    "StoragePortError": False,
}


class StoragePortErrorSchema(ResourceSchema):
    """The fields of the StoragePortError object"""

    corrective_action = fields.Str(data_key="corrective_action")
    r""" Error corrective action """

    message = fields.Str(data_key="message")
    r""" Error message """

    @property
    def resource(self):
        return StoragePortError

    @property
    def patchable_fields(self):
        return [
            "corrective_action",
            "message",
        ]

    @property
    def postable_fields(self):
        return [
            "corrective_action",
            "message",
        ]


class StoragePortError(Resource):  # pylint: disable=missing-docstring

    _schema = StoragePortErrorSchema
