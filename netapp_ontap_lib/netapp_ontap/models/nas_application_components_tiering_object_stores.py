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


__all__ = ["NasApplicationComponentsTieringObjectStores", "NasApplicationComponentsTieringObjectStoresSchema"]
__pdoc__ = {
    "NasApplicationComponentsTieringObjectStoresSchema.resource": False,
    "NasApplicationComponentsTieringObjectStores": False,
}


class NasApplicationComponentsTieringObjectStoresSchema(ResourceSchema):
    """The fields of the NasApplicationComponentsTieringObjectStores object"""

    name = fields.Str(data_key="name")
    r""" The name of the object-store to use. Usage: &lt;(size 1..512)&gt; """

    @property
    def resource(self):
        return NasApplicationComponentsTieringObjectStores

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class NasApplicationComponentsTieringObjectStores(Resource):  # pylint: disable=missing-docstring

    _schema = NasApplicationComponentsTieringObjectStoresSchema
