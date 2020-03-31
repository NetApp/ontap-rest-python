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


__all__ = ["SnapmirrorDestinationCreationStorageService", "SnapmirrorDestinationCreationStorageServiceSchema"]
__pdoc__ = {
    "SnapmirrorDestinationCreationStorageServiceSchema.resource": False,
    "SnapmirrorDestinationCreationStorageService": False,
}


class SnapmirrorDestinationCreationStorageServiceSchema(ResourceSchema):
    """The fields of the SnapmirrorDestinationCreationStorageService object"""

    enabled = fields.Boolean(data_key="enabled")
    r""" This property indicates whether to create the destination endpoint using storage service. """

    enforce_performance = fields.Boolean(data_key="enforce_performance")
    r""" Optional property to enforce storage service performance on the destination endpoint when the destination endpoint is used for read-write operations. This property is applicable to FlexVol volume and FlexGroup volume endpoints. """

    name = fields.Str(data_key="name")
    r""" Optional property to specify the storage service name for the destination endpoint. This property is considered when the property "create_destination.storage_service.enabled" is set to "true". When the property "create_destination.storage_service.enabled" is set to "true" and the "create_destination.storage_service.name" for the endpoint is not specified, then ONTAP selects the highest storage service available on the cluster to provision the destination endpoint. This property is applicable to FlexVol volume and FlexGroup volume endpoints.

Valid choices:

* extreme
* performance
* value """

    @property
    def resource(self):
        return SnapmirrorDestinationCreationStorageService

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "enforce_performance",
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "enforce_performance",
            "name",
        ]


class SnapmirrorDestinationCreationStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = SnapmirrorDestinationCreationStorageServiceSchema
