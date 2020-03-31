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


__all__ = ["ApplicationRpoComponents", "ApplicationRpoComponentsSchema"]
__pdoc__ = {
    "ApplicationRpoComponentsSchema.resource": False,
    "ApplicationRpoComponents": False,
}


class ApplicationRpoComponentsSchema(ResourceSchema):
    """The fields of the ApplicationRpoComponents object"""

    name = fields.Str(data_key="name")
    r""" Component Name. """

    rpo = fields.Nested("netapp_ontap.models.application_rpo_rpo.ApplicationRpoRpoSchema", unknown=EXCLUDE, data_key="rpo")
    r""" The rpo field of the application_rpo_components. """

    uuid = fields.Str(data_key="uuid")
    r""" Component UUID. """

    @property
    def resource(self):
        return ApplicationRpoComponents

    @property
    def patchable_fields(self):
        return [
            "rpo",
        ]

    @property
    def postable_fields(self):
        return [
            "rpo",
        ]


class ApplicationRpoComponents(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationRpoComponentsSchema
