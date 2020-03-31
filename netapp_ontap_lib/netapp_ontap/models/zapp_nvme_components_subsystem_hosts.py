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


__all__ = ["ZappNvmeComponentsSubsystemHosts", "ZappNvmeComponentsSubsystemHostsSchema"]
__pdoc__ = {
    "ZappNvmeComponentsSubsystemHostsSchema.resource": False,
    "ZappNvmeComponentsSubsystemHosts": False,
}


class ZappNvmeComponentsSubsystemHostsSchema(ResourceSchema):
    """The fields of the ZappNvmeComponentsSubsystemHosts object"""

    nqn = fields.Str(data_key="nqn")
    r""" The host NQN. """

    @property
    def resource(self):
        return ZappNvmeComponentsSubsystemHosts

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "nqn",
        ]


class ZappNvmeComponentsSubsystemHosts(Resource):  # pylint: disable=missing-docstring

    _schema = ZappNvmeComponentsSubsystemHostsSchema
