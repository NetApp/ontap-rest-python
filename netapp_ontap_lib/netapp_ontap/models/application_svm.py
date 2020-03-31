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


__all__ = ["ApplicationSvm", "ApplicationSvmSchema"]
__pdoc__ = {
    "ApplicationSvmSchema.resource": False,
    "ApplicationSvm": False,
}


class ApplicationSvmSchema(ResourceSchema):
    """The fields of the ApplicationSvm object"""

    name = fields.Str(data_key="name")
    r""" SVM Name. Either the SVM name or UUID must be provided to create an application. """

    uuid = fields.Str(data_key="uuid")
    r""" SVM UUID. Either the SVM name or UUID must be provided to create an application. """

    @property
    def resource(self):
        return ApplicationSvm

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "uuid",
        ]


class ApplicationSvm(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationSvmSchema
