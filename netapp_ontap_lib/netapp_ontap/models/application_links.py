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


__all__ = ["ApplicationLinks", "ApplicationLinksSchema"]
__pdoc__ = {
    "ApplicationLinksSchema.resource": False,
    "ApplicationLinks": False,
}


class ApplicationLinksSchema(ResourceSchema):
    """The fields of the ApplicationLinks object"""

    self_ = fields.Nested("netapp_ontap.models.href.HrefSchema", unknown=EXCLUDE, data_key="self")
    r""" The self_ field of the application_links. """

    snapshots = fields.Nested("netapp_ontap.models.href.HrefSchema", unknown=EXCLUDE, data_key="snapshots")
    r""" The snapshots field of the application_links. """

    @property
    def resource(self):
        return ApplicationLinks

    @property
    def patchable_fields(self):
        return [
            "self_",
            "snapshots",
        ]

    @property
    def postable_fields(self):
        return [
            "self_",
            "snapshots",
        ]


class ApplicationLinks(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationLinksSchema
