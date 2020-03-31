# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

Displays the list of files under the specified litigation ID.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnaplockLitigationFile", "SnaplockLitigationFileSchema"]
__pdoc__ = {
    "SnaplockLitigationFileSchema.resource": False,
    "SnaplockLitigationFileSchema.patchable_fields": False,
    "SnaplockLitigationFileSchema.postable_fields": False,
}


class SnaplockLitigationFileSchema(ResourceSchema):
    """The fields of the SnaplockLitigationFile object"""

    file = fields.List(fields.Str, data_key="file")
    r""" Name of the file including the path from the root. """

    sequence_index = fields.Integer(
        data_key="sequence_index",
    )
    r""" Sequence index of files path list. """

    @property
    def resource(self):
        return SnaplockLitigationFile

    @property
    def patchable_fields(self):
        return [
            "file",
            "sequence_index",
        ]

    @property
    def postable_fields(self):
        return [
            "file",
            "sequence_index",
        ]

class SnaplockLitigationFile(Resource):
    """Allows interaction with SnaplockLitigationFile objects on the host"""

    _schema = SnaplockLitigationFileSchema
    _path = "/api/storage/snaplock/litigations/{litigation[id]}/files"
    @property
    def _keys(self):
        return ["litigation.id"]

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Displays the list of files for the specified litigation ID.
### Learn more
* [`DOC /storage/snaplock/litigations/{litigation.id}/files`](#docs-snaplock-storage_snaplock_litigations_{litigation.id}_files)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Displays the list of files for the specified litigation ID.
### Learn more
* [`DOC /storage/snaplock/litigations/{litigation.id}/files`](#docs-snaplock-storage_snaplock_litigations_{litigation.id}_files)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






