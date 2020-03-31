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


__all__ = ["ApplicationRpo", "ApplicationRpoSchema"]
__pdoc__ = {
    "ApplicationRpoSchema.resource": False,
    "ApplicationRpo": False,
}


class ApplicationRpoSchema(ResourceSchema):
    """The fields of the ApplicationRpo object"""

    components = fields.List(fields.Nested("netapp_ontap.models.application_rpo_components.ApplicationRpoComponentsSchema", unknown=EXCLUDE), data_key="components")
    r""" The components field of the application_rpo. """

    is_supported = fields.Boolean(data_key="is_supported")
    r""" Is RPO supported for this application? Generation 1 applications did not support Snapshot copies or MetroCluster. """

    local = fields.Nested("netapp_ontap.models.application_rpo_local.ApplicationRpoLocalSchema", unknown=EXCLUDE, data_key="local")
    r""" The local field of the application_rpo. """

    remote = fields.Nested("netapp_ontap.models.application_rpo_remote.ApplicationRpoRemoteSchema", unknown=EXCLUDE, data_key="remote")
    r""" The remote field of the application_rpo. """

    @property
    def resource(self):
        return ApplicationRpo

    @property
    def patchable_fields(self):
        return [
            "local",
            "remote",
        ]

    @property
    def postable_fields(self):
        return [
            "local",
            "remote",
        ]


class ApplicationRpo(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationRpoSchema
