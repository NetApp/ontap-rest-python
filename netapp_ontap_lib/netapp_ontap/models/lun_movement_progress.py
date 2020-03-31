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


__all__ = ["LunMovementProgress", "LunMovementProgressSchema"]
__pdoc__ = {
    "LunMovementProgressSchema.resource": False,
    "LunMovementProgress": False,
}


class LunMovementProgressSchema(ResourceSchema):
    """The fields of the LunMovementProgress object"""

    elapsed = fields.Integer(data_key="elapsed")
    r""" The amount of time, in seconds, that has elapsed since the start of the LUN movement. """

    failure = fields.Nested("netapp_ontap.models.lun_movement_progress_failure.LunMovementProgressFailureSchema", unknown=EXCLUDE, data_key="failure")
    r""" The failure field of the lun_movement_progress. """

    percent_complete = fields.Integer(data_key="percent_complete")
    r""" The percentage complete of the LUN movement. """

    state = fields.Str(data_key="state")
    r""" The state of the LUN movement.<br/>
Valid in PATCH when an LUN movement is active. Set to _paused_ to pause a LUN movement. Set to _replicating_ to resume a paused LUN movement.


Valid choices:

* preparing
* replicating
* paused
* paused_error
* complete
* reverting
* failed """

    volume_snapshot_blocked = fields.Boolean(data_key="volume_snapshot_blocked")
    r""" This property reports if volume Snapshot copies are blocked by the LUN movement. This property can be polled to identify when volume Snapshot copies can be resumed after beginning a LUN movement. """

    @property
    def resource(self):
        return LunMovementProgress

    @property
    def patchable_fields(self):
        return [
            "failure",
            "state",
        ]

    @property
    def postable_fields(self):
        return [
            "failure",
        ]


class LunMovementProgress(Resource):  # pylint: disable=missing-docstring

    _schema = LunMovementProgressSchema
