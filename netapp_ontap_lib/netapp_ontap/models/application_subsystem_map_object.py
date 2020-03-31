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


__all__ = ["ApplicationSubsystemMapObject", "ApplicationSubsystemMapObjectSchema"]
__pdoc__ = {
    "ApplicationSubsystemMapObjectSchema.resource": False,
    "ApplicationSubsystemMapObject": False,
}


class ApplicationSubsystemMapObjectSchema(ResourceSchema):
    """The fields of the ApplicationSubsystemMapObject object"""

    anagrpid = fields.Str(data_key="anagrpid")
    r""" Subsystem ANA group ID """

    nsid = fields.Str(data_key="nsid")
    r""" Subsystem namespace ID """

    subsystem = fields.Nested("netapp_ontap.models.application_subsystem_map_object_subsystem.ApplicationSubsystemMapObjectSubsystemSchema", unknown=EXCLUDE, data_key="subsystem")
    r""" The subsystem field of the application_subsystem_map_object. """

    @property
    def resource(self):
        return ApplicationSubsystemMapObject

    @property
    def patchable_fields(self):
        return [
            "subsystem",
        ]

    @property
    def postable_fields(self):
        return [
            "subsystem",
        ]


class ApplicationSubsystemMapObject(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSubsystemMapObjectSchema
