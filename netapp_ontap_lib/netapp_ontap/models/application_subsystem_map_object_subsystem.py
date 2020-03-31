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


__all__ = ["ApplicationSubsystemMapObjectSubsystem", "ApplicationSubsystemMapObjectSubsystemSchema"]
__pdoc__ = {
    "ApplicationSubsystemMapObjectSubsystemSchema.resource": False,
    "ApplicationSubsystemMapObjectSubsystem": False,
}


class ApplicationSubsystemMapObjectSubsystemSchema(ResourceSchema):
    """The fields of the ApplicationSubsystemMapObjectSubsystem object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_subsystem_map_object_subsystem. """

    hosts = fields.List(fields.Nested("netapp_ontap.models.application_subsystem_map_object_subsystem_hosts.ApplicationSubsystemMapObjectSubsystemHostsSchema", unknown=EXCLUDE), data_key="hosts")
    r""" The hosts field of the application_subsystem_map_object_subsystem. """

    name = fields.Str(data_key="name")
    r""" Subsystem name """

    uuid = fields.Str(data_key="uuid")
    r""" Subsystem UUID """

    @property
    def resource(self):
        return ApplicationSubsystemMapObjectSubsystem

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationSubsystemMapObjectSubsystem(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSubsystemMapObjectSubsystemSchema
