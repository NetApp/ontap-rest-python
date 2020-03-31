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


__all__ = ["VscanOnAccessScope", "VscanOnAccessScopeSchema"]
__pdoc__ = {
    "VscanOnAccessScopeSchema.resource": False,
    "VscanOnAccessScope": False,
}


class VscanOnAccessScopeSchema(ResourceSchema):
    """The fields of the VscanOnAccessScope object"""

    exclude_extensions = fields.List(fields.Str, data_key="exclude_extensions")
    r""" List of file extensions for which scanning is not performed.

Example: ["mp*","txt"] """

    exclude_paths = fields.List(fields.Str, data_key="exclude_paths")
    r""" List of file paths for which scanning must not be performed.

Example: ["\\dir1\\dir2\\name","\\vol\\a b","\\vol\\a,b\\"] """

    include_extensions = fields.List(fields.Str, data_key="include_extensions")
    r""" List of file extensions to be scanned.

Example: ["mp*","txt"] """

    max_file_size = fields.Integer(data_key="max_file_size")
    r""" Maximum file size, in bytes, allowed for scanning.

Example: 2147483648 """

    only_execute_access = fields.Boolean(data_key="only_execute_access")
    r""" Scan only files opened with execute-access. """

    scan_readonly_volumes = fields.Boolean(data_key="scan_readonly_volumes")
    r""" Specifies whether or not read-only volume can be scanned. """

    scan_without_extension = fields.Boolean(data_key="scan_without_extension")
    r""" Specifies whether or not files without any extension can be scanned. """

    @property
    def resource(self):
        return VscanOnAccessScope

    @property
    def patchable_fields(self):
        return [
            "exclude_extensions",
            "exclude_paths",
            "include_extensions",
            "max_file_size",
            "only_execute_access",
            "scan_readonly_volumes",
            "scan_without_extension",
        ]

    @property
    def postable_fields(self):
        return [
            "exclude_extensions",
            "exclude_paths",
            "include_extensions",
            "max_file_size",
            "only_execute_access",
            "scan_readonly_volumes",
            "scan_without_extension",
        ]


class VscanOnAccessScope(Resource):  # pylint: disable=missing-docstring

    _schema = VscanOnAccessScopeSchema
