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


__all__ = ["ApplicationTemplate1", "ApplicationTemplate1Schema"]
__pdoc__ = {
    "ApplicationTemplate1Schema.resource": False,
    "ApplicationTemplate1": False,
}


class ApplicationTemplate1Schema(ResourceSchema):
    """The fields of the ApplicationTemplate1 object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the application_template1. """

    name = fields.Str(data_key="name")
    r""" The name of the template that was used to provision this application. """

    protocol = fields.Str(data_key="protocol")
    r""" The protocol access of the template that was used to provision this application.

Valid choices:

* nas
* nvme
* san """

    version = fields.Integer(data_key="version")
    r""" The version of the template that was used to provision this application. The template version changes only if the layout of the application changes over time. For example, redo logs in Oracle RAC templates were updated and provisioned differently in DATA ONTAP 9.3.0 compared to prior releases, so the version number was increased. If layouts change in the future, the changes will be documented along with the corresponding version numbers. """

    @property
    def resource(self):
        return ApplicationTemplate1

    @property
    def patchable_fields(self):
        return [
            "links",
        ]

    @property
    def postable_fields(self):
        return [
            "links",
            "name",
        ]


class ApplicationTemplate1(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationTemplate1Schema
