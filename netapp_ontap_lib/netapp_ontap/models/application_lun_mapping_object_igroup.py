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


__all__ = ["ApplicationLunMappingObjectIgroup", "ApplicationLunMappingObjectIgroupSchema"]
__pdoc__ = {
    "ApplicationLunMappingObjectIgroupSchema.resource": False,
    "ApplicationLunMappingObjectIgroup": False,
}


class ApplicationLunMappingObjectIgroupSchema(ResourceSchema):
    """The fields of the ApplicationLunMappingObjectIgroup object"""

    initiators = fields.List(fields.Str, data_key="initiators")
    r""" The initiators field of the application_lun_mapping_object_igroup. """

    name = fields.Str(data_key="name")
    r""" Igroup name """

    uuid = fields.Str(data_key="uuid")
    r""" Igroup UUID """

    @property
    def resource(self):
        return ApplicationLunMappingObjectIgroup

    @property
    def patchable_fields(self):
        return [
            "initiators",
        ]

    @property
    def postable_fields(self):
        return [
            "initiators",
        ]


class ApplicationLunMappingObjectIgroup(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationLunMappingObjectIgroupSchema
