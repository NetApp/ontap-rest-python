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


__all__ = ["CloudTargetCluster", "CloudTargetClusterSchema"]
__pdoc__ = {
    "CloudTargetClusterSchema.resource": False,
    "CloudTargetCluster": False,
}


class CloudTargetClusterSchema(ResourceSchema):
    """The fields of the CloudTargetCluster object"""

    name = fields.Str(data_key="name")
    r""" The name of the cluster that owns the cloud target. For POST, this accepts the name of the peer cluster only if the cluster is in switchover state. """

    uuid = fields.Str(data_key="uuid")
    r""" The UUID of the cluster that owns the cloud target. For POST, this accepts the UUID of the peer cluster only if the cluster is in switchover state. """

    @property
    def resource(self):
        return CloudTargetCluster

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "uuid",
        ]


class CloudTargetCluster(Resource):  # pylint: disable=missing-docstring

    _schema = CloudTargetClusterSchema
