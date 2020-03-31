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


__all__ = ["MaxdataOnSanApplicationComponentsMetadata", "MaxdataOnSanApplicationComponentsMetadataSchema"]
__pdoc__ = {
    "MaxdataOnSanApplicationComponentsMetadataSchema.resource": False,
    "MaxdataOnSanApplicationComponentsMetadata": False,
}


class MaxdataOnSanApplicationComponentsMetadataSchema(ResourceSchema):
    """The fields of the MaxdataOnSanApplicationComponentsMetadata object"""

    key = fields.Str(data_key="key")
    r""" Key to look up metadata associated with an application component. """

    value = fields.Str(data_key="value")
    r""" Value associated with the key. """

    @property
    def resource(self):
        return MaxdataOnSanApplicationComponentsMetadata

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


class MaxdataOnSanApplicationComponentsMetadata(Resource):  # pylint: disable=missing-docstring

    _schema = MaxdataOnSanApplicationComponentsMetadataSchema
