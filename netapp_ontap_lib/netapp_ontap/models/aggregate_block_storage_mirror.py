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


__all__ = ["AggregateBlockStorageMirror", "AggregateBlockStorageMirrorSchema"]
__pdoc__ = {
    "AggregateBlockStorageMirrorSchema.resource": False,
    "AggregateBlockStorageMirror": False,
}


class AggregateBlockStorageMirrorSchema(ResourceSchema):
    """The fields of the AggregateBlockStorageMirror object"""

    enabled = fields.Boolean(data_key="enabled")
    r""" Aggregate is SyncMirror protected

Example: false """

    state = fields.Str(data_key="state")
    r""" The state field of the aggregate_block_storage_mirror.

Valid choices:

* unmirrored
* normal
* degraded
* resynchronizing
* failed """

    @property
    def resource(self):
        return AggregateBlockStorageMirror

    @property
    def patchable_fields(self):
        return [
            "enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
        ]


class AggregateBlockStorageMirror(Resource):  # pylint: disable=missing-docstring

    _schema = AggregateBlockStorageMirrorSchema
