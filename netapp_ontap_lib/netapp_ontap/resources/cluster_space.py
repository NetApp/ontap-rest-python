# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["ClusterSpace", "ClusterSpaceSchema"]
__pdoc__ = {
    "ClusterSpaceSchema.resource": False,
    "ClusterSpaceSchema.patchable_fields": False,
    "ClusterSpaceSchema.postable_fields": False,
}


class ClusterSpaceSchema(ResourceSchema):
    """The fields of the ClusterSpace object"""

    block_storage = fields.Nested("netapp_ontap.models.cluster_space_block_storage.ClusterSpaceBlockStorageSchema", data_key="block_storage", unknown=EXCLUDE)
    r""" The block_storage field of the cluster_space. """

    cloud_storage = fields.Nested("netapp_ontap.models.cluster_space_cloud_storage.ClusterSpaceCloudStorageSchema", data_key="cloud_storage", unknown=EXCLUDE)
    r""" The cloud_storage field of the cluster_space. """

    efficiency = fields.Nested("netapp_ontap.models.space_efficiency.SpaceEfficiencySchema", data_key="efficiency", unknown=EXCLUDE)
    r""" The efficiency field of the cluster_space. """

    efficiency_without_snapshots = fields.Nested("netapp_ontap.models.space_efficiency.SpaceEfficiencySchema", data_key="efficiency_without_snapshots", unknown=EXCLUDE)
    r""" The efficiency_without_snapshots field of the cluster_space. """

    @property
    def resource(self):
        return ClusterSpace

    @property
    def patchable_fields(self):
        return [
            "block_storage",
            "cloud_storage",
            "efficiency",
            "efficiency_without_snapshots",
        ]

    @property
    def postable_fields(self):
        return [
            "block_storage",
            "cloud_storage",
            "efficiency",
            "efficiency_without_snapshots",
        ]

class ClusterSpace(Resource):
    """Allows interaction with ClusterSpace objects on the host"""

    _schema = ClusterSpaceSchema
    _path = "/api/storage/cluster"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Reports cluster wide storage details across different tiers. By default, this endpoint returns all fields.
Supports the following roles: admin, and readonly.
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





