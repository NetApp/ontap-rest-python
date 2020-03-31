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


__all__ = ["AppNfsAccess", "AppNfsAccessSchema"]
__pdoc__ = {
    "AppNfsAccessSchema.resource": False,
    "AppNfsAccess": False,
}


class AppNfsAccessSchema(ResourceSchema):
    """The fields of the AppNfsAccess object"""

    access = fields.Str(data_key="access")
    r""" The NFS access granted.

Valid choices:

* none
* ro
* rw """

    host = fields.Str(data_key="host")
    r""" The name of the NFS entity granted access. """

    @property
    def resource(self):
        return AppNfsAccess

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "access",
            "host",
        ]


class AppNfsAccess(Resource):  # pylint: disable=missing-docstring

    _schema = AppNfsAccessSchema
