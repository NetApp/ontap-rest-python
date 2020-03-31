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


__all__ = ["SnapmirrorTransferRelationship", "SnapmirrorTransferRelationshipSchema"]
__pdoc__ = {
    "SnapmirrorTransferRelationshipSchema.resource": False,
    "SnapmirrorTransferRelationship": False,
}


class SnapmirrorTransferRelationshipSchema(ResourceSchema):
    """The fields of the SnapmirrorTransferRelationship object"""

    destination = fields.Nested("netapp_ontap.models.snapmirror_endpoint.SnapmirrorEndpointSchema", unknown=EXCLUDE, data_key="destination")
    r""" The destination field of the snapmirror_transfer_relationship. """

    restore = fields.Boolean(data_key="restore")
    r""" Is the relationship for restore? """

    uuid = fields.Str(data_key="uuid")
    r""" The uuid field of the snapmirror_transfer_relationship.

Example: d2d7ceea-ab52-11e8-855e-00505682a4c7 """

    @property
    def resource(self):
        return SnapmirrorTransferRelationship

    @property
    def patchable_fields(self):
        return [
            "destination",
            "restore",
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "destination",
            "restore",
            "uuid",
        ]


class SnapmirrorTransferRelationship(Resource):  # pylint: disable=missing-docstring

    _schema = SnapmirrorTransferRelationshipSchema
