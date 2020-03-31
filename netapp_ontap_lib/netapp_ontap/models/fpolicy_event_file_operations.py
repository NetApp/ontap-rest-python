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


__all__ = ["FpolicyEventFileOperations", "FpolicyEventFileOperationsSchema"]
__pdoc__ = {
    "FpolicyEventFileOperationsSchema.resource": False,
    "FpolicyEventFileOperations": False,
}


class FpolicyEventFileOperationsSchema(ResourceSchema):
    """The fields of the FpolicyEventFileOperations object"""

    close = fields.Boolean(data_key="close")
    r""" File close operations """

    create = fields.Boolean(data_key="create")
    r""" File create operations """

    create_dir = fields.Boolean(data_key="create_dir")
    r""" Directory create operations """

    delete = fields.Boolean(data_key="delete")
    r""" File delete operations """

    delete_dir = fields.Boolean(data_key="delete_dir")
    r""" Directory delete operations """

    getattr = fields.Boolean(data_key="getattr")
    r""" Get attribute operations """

    link = fields.Boolean(data_key="link")
    r""" Link operations """

    lookup = fields.Boolean(data_key="lookup")
    r""" Lookup operations """

    open = fields.Boolean(data_key="open")
    r""" File open operations """

    read = fields.Boolean(data_key="read")
    r""" File read operations """

    rename = fields.Boolean(data_key="rename")
    r""" File rename operations """

    rename_dir = fields.Boolean(data_key="rename_dir")
    r""" Directory rename operations """

    setattr = fields.Boolean(data_key="setattr")
    r""" Set attribute operations """

    symlink = fields.Boolean(data_key="symlink")
    r""" Symbolic link operations """

    write = fields.Boolean(data_key="write")
    r""" File write operations """

    @property
    def resource(self):
        return FpolicyEventFileOperations

    @property
    def patchable_fields(self):
        return [
            "close",
            "create",
            "create_dir",
            "delete",
            "delete_dir",
            "getattr",
            "link",
            "lookup",
            "open",
            "read",
            "rename",
            "rename_dir",
            "setattr",
            "symlink",
            "write",
        ]

    @property
    def postable_fields(self):
        return [
            "close",
            "create",
            "create_dir",
            "delete",
            "delete_dir",
            "getattr",
            "link",
            "lookup",
            "open",
            "read",
            "rename",
            "rename_dir",
            "setattr",
            "symlink",
            "write",
        ]


class FpolicyEventFileOperations(Resource):  # pylint: disable=missing-docstring

    _schema = FpolicyEventFileOperationsSchema
