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


__all__ = ["SoftwareMcc", "SoftwareMccSchema"]
__pdoc__ = {
    "SoftwareMccSchema.resource": False,
    "SoftwareMcc": False,
}


class SoftwareMccSchema(ResourceSchema):
    """The fields of the SoftwareMcc object"""

    elapsed_duration = fields.Integer(data_key="elapsed_duration")
    r""" Elapsed duration of update time (in seconds) of MetroCluster.

Example: 2140 """

    estimated_duration = fields.Integer(data_key="estimated_duration")
    r""" Estimated duration of update time (in seconds) of MetroCluster.

Example: 3480 """

    name = fields.Str(data_key="name")
    r""" Name of the site in MetroCluster.

Example: cluster_A """

    state = fields.Str(data_key="state")
    r""" Upgrade state of MetroCluster.

Valid choices:

* in_progress
* waiting
* paused_by_user
* paused_on_error
* completed
* canceled
* failed
* pause_pending
* cancel_pending """

    @property
    def resource(self):
        return SoftwareMcc

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class SoftwareMcc(Resource):  # pylint: disable=missing-docstring

    _schema = SoftwareMccSchema
