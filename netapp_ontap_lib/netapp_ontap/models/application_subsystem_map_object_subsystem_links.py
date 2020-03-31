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


__all__ = ["ApplicationSubsystemMapObjectSubsystemLinks", "ApplicationSubsystemMapObjectSubsystemLinksSchema"]
__pdoc__ = {
    "ApplicationSubsystemMapObjectSubsystemLinksSchema.resource": False,
    "ApplicationSubsystemMapObjectSubsystemLinks": False,
}


class ApplicationSubsystemMapObjectSubsystemLinksSchema(ResourceSchema):
    """The fields of the ApplicationSubsystemMapObjectSubsystemLinks object"""

    self_ = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="self")
    r""" The self_ field of the application_subsystem_map_object_subsystem_links. """

    @property
    def resource(self):
        return ApplicationSubsystemMapObjectSubsystemLinks

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationSubsystemMapObjectSubsystemLinks(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSubsystemMapObjectSubsystemLinksSchema
