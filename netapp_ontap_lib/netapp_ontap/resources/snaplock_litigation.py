# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

Use this API to retain Compliance-mode WORM files for the duration of a litigation. A file under a legal-hold behaves as a WORM file with an indefinite retention period. Litigation ID is a combination of volume UUID and litigation name in the format `<volume UUID>:<litigation name>`. Only a user with the security login role vsadmin-snaplock can perform the operation.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnaplockLitigation", "SnaplockLitigationSchema"]
__pdoc__ = {
    "SnaplockLitigationSchema.resource": False,
    "SnaplockLitigationSchema.patchable_fields": False,
    "SnaplockLitigationSchema.postable_fields": False,
}


class SnaplockLitigationSchema(ResourceSchema):
    """The fields of the SnaplockLitigation object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snaplock_litigation. """

    id = fields.Str(
        data_key="id",
    )
    r""" Specifies the litigation ID. """

    name = fields.Str(
        data_key="name",
    )
    r""" Specifies the legal-hold litigation name.

Example: lit1 """

    operation = fields.List(fields.Nested("netapp_ontap.resources.snaplock_legal_hold_operation.SnaplockLegalHoldOperationSchema", unknown=EXCLUDE), data_key="operation")
    r""" The operation field of the snaplock_litigation. """

    path = fields.Str(
        data_key="path",
    )
    r""" Specifies the path on which legal-hold operation has to be applied.

Example: /dir1 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the snaplock_litigation. """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the snaplock_litigation. """

    @property
    def resource(self):
        return SnaplockLitigation

    @property
    def patchable_fields(self):
        return [
            "name",
            "operation",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "operation",
            "path",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

class SnaplockLitigation(Resource):
    """Allows interaction with SnaplockLitigation objects on the host"""

    _schema = SnaplockLitigationSchema
    _path = "/api/storage/snaplock/litigations"
    @property
    def _keys(self):
        return ["id"]

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
        r"""Retrieves the list of litigations under an SVM.
### Related ONTAP commands
* `snaplock legal-hold show`
### Learn more
* [`DOC /storage/snaplock/litigations`](#docs-snaplock-storage_snaplock_litigations)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def delete_collection(
        cls,
        *args,
        body: Union[Resource, dict] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a legal-hold end on all of the files for the specified litigation ID. This is only allowed when an operation is no longer in progress.
### Related ONTAP commands
* `snaplock legal-hold end`
### Example
<br/>
```
DELETE "/api/storage/snaplock/litigations/fd72e138-4bc3-11e9-a85f-0050568eb48f%3Al3"
```
<br/>
### Learn more
* [`DOC /storage/snaplock/litigations`](#docs-snaplock-storage_snaplock_litigations)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the list of litigations under an SVM.
### Related ONTAP commands
* `snaplock legal-hold show`
### Learn more
* [`DOC /storage/snaplock/litigations`](#docs-snaplock-storage_snaplock_litigations)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the list of ongoing operations for the specified litigation ID.
### Related ONTAP commands
* `snaplock legal-hold show`
### Learn more
* [`DOC /storage/snaplock/litigations`](#docs-snaplock-storage_snaplock_litigations)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Starts a  Legal-Hold.
### Required properties
* `path` - Path of the file.
* `name` - Litigation name.
* `volume.name` or `volume.uuid` - Name or UUID  of the volume.
### Related ONTAP commands
* `snaplock legal-hold begin`
### Example
<br/>
```
POST "/api/storage/snaplock/litigations" '{"volume.name":"SLC1","name":"l3","path":"/b.txt"}'
```
<br/>
### Learn more
* [`DOC /storage/snaplock/litigations`](#docs-snaplock-storage_snaplock_litigations)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a legal-hold end on all of the files for the specified litigation ID. This is only allowed when an operation is no longer in progress.
### Related ONTAP commands
* `snaplock legal-hold end`
### Example
<br/>
```
DELETE "/api/storage/snaplock/litigations/fd72e138-4bc3-11e9-a85f-0050568eb48f%3Al3"
```
<br/>
### Learn more
* [`DOC /storage/snaplock/litigations`](#docs-snaplock-storage_snaplock_litigations)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


