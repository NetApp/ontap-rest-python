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


__all__ = ["ApplicationComponentSnapshotSvm", "ApplicationComponentSnapshotSvmSchema"]
__pdoc__ = {
    "ApplicationComponentSnapshotSvmSchema.resource": False,
    "ApplicationComponentSnapshotSvm": False,
}


class ApplicationComponentSnapshotSvmSchema(ResourceSchema):
    """The fields of the ApplicationComponentSnapshotSvm object"""

    name = fields.Str(data_key="name")
    r""" SVM Name """

    uuid = fields.Str(data_key="uuid")
    r""" SVM UUID """

    @property
    def resource(self):
        return ApplicationComponentSnapshotSvm

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationComponentSnapshotSvm(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationComponentSnapshotSvmSchema
