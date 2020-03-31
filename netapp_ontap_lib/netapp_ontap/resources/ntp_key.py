# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
You can configure NTP to use shared private keys between ONTAP and trusted external NTP time servers.</br>
You acquire the keys from the external NTP time servers and individual entries created for each
unique key. You can use the /cluster/ntp/servers API to associate a key with an external NTP time server
used by ONTAP and enable authentication.
### Fields used for adding an NTP shared key
The required fields are:

* `id`
* `digest_type`
* `secret_key`
## Example
```
# Body
body =
{
  "id": 10,
  "digest_type": "sha1",
  "value": "da39a3ee5e6b4b0d3255bfef95601890afd80709"
}
# Request
curl -X POST "https://<mgmt-ip>/api/cluster/ntp/keys" -d body
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["NtpKey", "NtpKeySchema"]
__pdoc__ = {
    "NtpKeySchema.resource": False,
    "NtpKeySchema.patchable_fields": False,
    "NtpKeySchema.postable_fields": False,
}


class NtpKeySchema(ResourceSchema):
    """The fields of the NtpKey object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ntp_key. """

    digest_type = fields.Str(
        data_key="digest_type",
        validate=enum_validation(['sha1']),
    )
    r""" The type of cryptographic hash used to create and verify the NTP's message authentication code appended to each NTP packet header.


Valid choices:

* sha1 """

    id = fields.Integer(
        data_key="id",
        validate=integer_validation(minimum=1, maximum=65535),
    )
    r""" NTP symmetric authentication key identifier or index number (ID). This ID is included
in the NTP cryptographic hash encoded header.


Example: 10 """

    value = fields.Str(
        data_key="value",
    )
    r""" A hexadecimal digit string that represents the cryptographic key that is shared with the remote NTP server.
The current expected length is 40 characters.
</br>
Use the cryptographic key and key ID to create a unique hash value used to authenticate the rest of the NTP data.


Example: da39a3ee5e6b4b0d3255bfef95601890afd80709 """

    @property
    def resource(self):
        return NtpKey

    @property
    def patchable_fields(self):
        return [
            "digest_type",
            "value",
        ]

    @property
    def postable_fields(self):
        return [
            "digest_type",
            "id",
            "value",
        ]

class NtpKey(Resource):
    """Allows interaction with NtpKey objects on the host"""

    _schema = NtpKeySchema
    _path = "/api/cluster/ntp/keys"
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
        r"""Retrieves the collection of NTP symmetric authentication keys known by ONTAP that
are uniquely indexed by an identifier.
### Related ONTAP commands
* `cluster time-service ntp key show`
### Learn more
* [`DOC /cluster/ntp/keys`](#docs-cluster-cluster_ntp_keys)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the details of a specific NTP symmetric authentication key by numeric
identifier or index (ID).
### Required properties
* `digest_type` - Shared private key cryptographic hash type.
* `value` - Value of shared private key.
### Related ONTAP commands
* `cluster time-service ntp key modify`
### Learn more
* [`DOC /cluster/ntp/keys`](#docs-cluster-cluster_ntp_keys)
"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member

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
        r"""Deletes an NTP key.
### Related ONTAP commands
* `cluster time-service ntp key delete`
### Learn more
* [`DOC /cluster/ntp/keys`](#docs-cluster-cluster_ntp_keys)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the collection of NTP symmetric authentication keys known by ONTAP that
are uniquely indexed by an identifier.
### Related ONTAP commands
* `cluster time-service ntp key show`
### Learn more
* [`DOC /cluster/ntp/keys`](#docs-cluster-cluster_ntp_keys)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the details of a specific NTP symmetric authentication key by numeric identifier or index (ID).
### Related ONTAP commands
* `cluster time-service ntp key show`
### Learn more
* [`DOC /cluster/ntp/keys`](#docs-cluster-cluster_ntp_keys)
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
        r"""Creates an NTP symmetric authentication key entry including the type of key
using an unused identifier or index number (ID).
### Required properties
* `id` - Shared symmetric key number (ID).
* `digest_type` - Shared private key cryptographic hash type.
* `value` - Value of shared private key.
### Related ONTAP commands
* `cluster time-service ntp key create`
### Learn more
* [`DOC /cluster/ntp/keys`](#docs-cluster-cluster_ntp_keys)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the details of a specific NTP symmetric authentication key by numeric
identifier or index (ID).
### Required properties
* `digest_type` - Shared private key cryptographic hash type.
* `value` - Value of shared private key.
### Related ONTAP commands
* `cluster time-service ntp key modify`
### Learn more
* [`DOC /cluster/ntp/keys`](#docs-cluster-cluster_ntp_keys)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member

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
        r"""Deletes an NTP key.
### Related ONTAP commands
* `cluster time-service ntp key delete`
### Learn more
* [`DOC /cluster/ntp/keys`](#docs-cluster-cluster_ntp_keys)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


