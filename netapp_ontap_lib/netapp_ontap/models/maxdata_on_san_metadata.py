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


__all__ = ["MaxdataOnSanMetadata", "MaxdataOnSanMetadataSchema"]
__pdoc__ = {
    "MaxdataOnSanMetadataSchema.resource": False,
    "MaxdataOnSanMetadata": False,
}


class MaxdataOnSanMetadataSchema(ResourceSchema):
    """The fields of the MaxdataOnSanMetadata object"""

    key = fields.Str(data_key="key")
    r""" Key to look up metadata associated with an application. """

    value = fields.Str(data_key="value")
    r""" Value associated with the key. """

    @property
    def resource(self):
        return MaxdataOnSanMetadata

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "key",
            "value",
        ]


class MaxdataOnSanMetadata(Resource):  # pylint: disable=missing-docstring

    _schema = MaxdataOnSanMetadataSchema
