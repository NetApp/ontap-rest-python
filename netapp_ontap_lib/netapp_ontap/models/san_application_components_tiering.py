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


__all__ = ["SanApplicationComponentsTiering", "SanApplicationComponentsTieringSchema"]
__pdoc__ = {
    "SanApplicationComponentsTieringSchema.resource": False,
    "SanApplicationComponentsTiering": False,
}


class SanApplicationComponentsTieringSchema(ResourceSchema):
    """The fields of the SanApplicationComponentsTiering object"""

    control = fields.Str(data_key="control")
    r""" Storage tiering placement rules for the container(s)

Valid choices:

* required
* best_effort
* disallowed """

    object_stores = fields.List(fields.Nested("netapp_ontap.models.nas_application_components_tiering_object_stores.NasApplicationComponentsTieringObjectStoresSchema", unknown=EXCLUDE), data_key="object_stores")
    r""" The object_stores field of the san_application_components_tiering. """

    policy = fields.Str(data_key="policy")
    r""" The storage tiering type of the application component.

Valid choices:

* all
* auto
* none
* snapshot_only """

    @property
    def resource(self):
        return SanApplicationComponentsTiering

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "control",
            "object_stores",
            "policy",
        ]


class SanApplicationComponentsTiering(Resource):  # pylint: disable=missing-docstring

    _schema = SanApplicationComponentsTieringSchema
