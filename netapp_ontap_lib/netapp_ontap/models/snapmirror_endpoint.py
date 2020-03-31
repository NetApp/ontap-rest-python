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


__all__ = ["SnapmirrorEndpoint", "SnapmirrorEndpointSchema"]
__pdoc__ = {
    "SnapmirrorEndpointSchema.resource": False,
    "SnapmirrorEndpoint": False,
}


class SnapmirrorEndpointSchema(ResourceSchema):
    """The fields of the SnapmirrorEndpoint object"""

    cluster = fields.Nested("netapp_ontap.resources.cluster.ClusterSchema", unknown=EXCLUDE, data_key="cluster")
    r""" The cluster field of the snapmirror_endpoint. """

    ipspace = fields.Str(data_key="ipspace")
    r""" Optional property to specify the IPSpace of the SVM.

Example: Default """

    path = fields.Str(data_key="path")
    r""" ONTAP FlexVol/FlexGroup - svm1:volume1
ONTAP SVM               - svm1:


Example: svm1:volume1 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", unknown=EXCLUDE, data_key="svm")
    r""" The svm field of the snapmirror_endpoint. """

    @property
    def resource(self):
        return SnapmirrorEndpoint

    @property
    def patchable_fields(self):
        return [
            "cluster.name",
            "cluster.uuid",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "cluster.name",
            "cluster.uuid",
            "ipspace",
            "path",
            "svm.name",
            "svm.uuid",
        ]


class SnapmirrorEndpoint(Resource):  # pylint: disable=missing-docstring

    _schema = SnapmirrorEndpointSchema
