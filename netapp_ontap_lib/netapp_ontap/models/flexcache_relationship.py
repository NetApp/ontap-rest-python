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


__all__ = ["FlexcacheRelationship", "FlexcacheRelationshipSchema"]
__pdoc__ = {
    "FlexcacheRelationshipSchema.resource": False,
    "FlexcacheRelationship": False,
}


class FlexcacheRelationshipSchema(ResourceSchema):
    """The fields of the FlexcacheRelationship object"""

    cluster = fields.Nested("netapp_ontap.resources.cluster.ClusterSchema", unknown=EXCLUDE, data_key="cluster")
    r""" The cluster field of the flexcache_relationship. """

    create_time = fields.DateTime(data_key="create_time")
    r""" Creation time of the relationship.

Example: 2018-06-04T19:00:00.000+0000 """

    ip_address = fields.Str(data_key="ip_address")
    r""" Cluster managerment IP of the remote cluster.

Example: 10.10.10.7 """

    size = fields.Integer(data_key="size")
    r""" Size of the remote volume. """

    state = fields.Str(data_key="state")
    r""" Volume state

Valid choices:

* error
* mixed
* offline
* online """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", unknown=EXCLUDE, data_key="svm")
    r""" The svm field of the flexcache_relationship. """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", unknown=EXCLUDE, data_key="volume")
    r""" The volume field of the flexcache_relationship. """

    @property
    def resource(self):
        return FlexcacheRelationship

    @property
    def patchable_fields(self):
        return [
            "cluster.name",
            "cluster.uuid",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "cluster.name",
            "cluster.uuid",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]


class FlexcacheRelationship(Resource):  # pylint: disable=missing-docstring

    _schema = FlexcacheRelationshipSchema
