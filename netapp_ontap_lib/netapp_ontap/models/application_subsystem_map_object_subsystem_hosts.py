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


__all__ = ["ApplicationSubsystemMapObjectSubsystemHosts", "ApplicationSubsystemMapObjectSubsystemHostsSchema"]
__pdoc__ = {
    "ApplicationSubsystemMapObjectSubsystemHostsSchema.resource": False,
    "ApplicationSubsystemMapObjectSubsystemHosts": False,
}


class ApplicationSubsystemMapObjectSubsystemHostsSchema(ResourceSchema):
    """The fields of the ApplicationSubsystemMapObjectSubsystemHosts object"""

    links = fields.Nested("netapp_ontap.models.application_subsystem_map_object_subsystem_links.ApplicationSubsystemMapObjectSubsystemLinksSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_subsystem_map_object_subsystem_hosts. """

    nqn = fields.Str(data_key="nqn")
    r""" Host """

    @property
    def resource(self):
        return ApplicationSubsystemMapObjectSubsystemHosts

    @property
    def patchable_fields(self):
        return [
            "links",
        ]

    @property
    def postable_fields(self):
        return [
            "links",
        ]


class ApplicationSubsystemMapObjectSubsystemHosts(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSubsystemMapObjectSubsystemHostsSchema
