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


__all__ = ["ApplicationComponentSvm", "ApplicationComponentSvmSchema"]
__pdoc__ = {
    "ApplicationComponentSvmSchema.resource": False,
    "ApplicationComponentSvm": False,
}


class ApplicationComponentSvmSchema(ResourceSchema):
    """The fields of the ApplicationComponentSvm object"""

    name = fields.Str(data_key="name")
    r""" SVM name """

    uuid = fields.Str(data_key="uuid")
    r""" SVM UUID """

    @property
    def resource(self):
        return ApplicationComponentSvm

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationComponentSvm(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationComponentSvmSchema
