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


__all__ = ["ApplicationNfsPropertiesExportPolicy", "ApplicationNfsPropertiesExportPolicySchema"]
__pdoc__ = {
    "ApplicationNfsPropertiesExportPolicySchema.resource": False,
    "ApplicationNfsPropertiesExportPolicy": False,
}


class ApplicationNfsPropertiesExportPolicySchema(ResourceSchema):
    """The fields of the ApplicationNfsPropertiesExportPolicy object"""

    name = fields.Str(data_key="name")
    r""" Export policy name """

    @property
    def resource(self):
        return ApplicationNfsPropertiesExportPolicy

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationNfsPropertiesExportPolicy(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationNfsPropertiesExportPolicySchema
