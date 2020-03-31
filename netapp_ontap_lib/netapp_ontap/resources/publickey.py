# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API configures the public keys for end-user (non-cluster admin) accounts.
Specify the owner UUID, the user account name, and the index in the URI path. The owner UUID corresponds to the UUID of the SVM containing the user account associated with the public key and can be obtained from the response body of the GET request performed on the API “/api/svm/svms".<br/> The index value corresponds to the public key that needs to be modified or deleted (it is possible to create more than one public key for the same user account).
## Examples
### Retrieving the specific configured public key for user accounts
```
# The API:
GET "/api/security/authentication/publickeys/{owner.uuid}/{account.name}/{index}"
# The call:
curl -k https://<mgmt-ip>/api/security/authentication/publickeys/513a78c7-8c13-11e9-8f78-005056bbf6ac/pubuser4/0
```
### Updating the public key and comment for user accounts
```
# The API:
PATCH "/api/security/authentication/publickeys/{owner.uuid}/{account.name}/{index}"
# The call:
curl -k https://<mgmt-ip>/api/security/authentication/publickeys/d49de271-8c11-11e9-8f78-005056bbf6ac/pubuser1/0 --request PATCH --data '{ "comment": "Cserver-modification","public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCmSLP/FeiT1J4Fb4GNVO4ioa1NIUHWeG08+anDbFke3JcFT5JqBn0QZiG0uF0bqepken/moVKZg8iQng1arjP4ULhhje/LwDuUbaB7kvtPL2gyzAX1qFYnBJ5R1LXja25Z4xeeaXUBJjhUmvpfque0TxbvpaG5V9rFTzVg9ccjBnkBchg3EkhF4VtHmrZNpTDAUOBAz69FRYXYz2ExoCHWqElHBJep9D0DLN0XtzQA0IF9hJck6xja5RcAQ6f9pLMCol9vJiqpcBAjkUmg1qH5ZNHsgDQ7dtGNGJw45zqXHPAy9z8yKJuIsdK2/4iVYLDL8mlHFElgeADn6OSxuij1" }'
```
### Deleting the public key for user accounts
```
# The API:
DELETE "/api/security/authentication/publickeys/{owner.uuid}/{account.name}/{index}"
# The call:
curl -k https://<mgmt-ip>/api/security/authentication/publickeys/d49de271-8c11-11e9-8f78-005056bbf6ac/pubuser1/0 --request DELETE
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Publickey", "PublickeySchema"]
__pdoc__ = {
    "PublickeySchema.resource": False,
    "PublickeySchema.patchable_fields": False,
    "PublickeySchema.postable_fields": False,
}


class PublickeySchema(ResourceSchema):
    """The fields of the Publickey object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the publickey. """

    account = fields.Nested("netapp_ontap.resources.account.AccountSchema", data_key="account", unknown=EXCLUDE)
    r""" The account field of the publickey. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" Optional comment for the public key. """

    index = fields.Integer(
        data_key="index",
        validate=integer_validation(minimum=0, maximum=99),
    )
    r""" Index number for the public key (where there are multiple keys for the same account). """

    obfuscated_fingerprint = fields.Str(
        data_key="obfuscated_fingerprint",
    )
    r""" The obfuscated fingerprint for the public key (READONLY). """

    owner = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="owner", unknown=EXCLUDE)
    r""" The owner field of the publickey. """

    public_key = fields.Str(
        data_key="public_key",
    )
    r""" The public key """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['cluster', 'svm']),
    )
    r""" Scope of the entity. Set to "cluster" for cluster owned objects and to "svm" for SVM owned objects.

Valid choices:

* cluster
* svm """

    sha_fingerprint = fields.Str(
        data_key="sha_fingerprint",
    )
    r""" The SHA fingerprint for the public key (READONLY). """

    @property
    def resource(self):
        return Publickey

    @property
    def patchable_fields(self):
        return [
            "account.name",
            "comment",
            "public_key",
        ]

    @property
    def postable_fields(self):
        return [
            "account.name",
            "comment",
            "index",
            "owner.name",
            "owner.uuid",
            "public_key",
        ]

class Publickey(Resource):
    r""" The public key for the user account (to access SSH). """

    _schema = PublickeySchema
    _path = "/api/security/authentication/publickeys"
    @property
    def _keys(self):
        return ["owner.uuid", "account.name", "index"]

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
        r"""Retrieves the public keys configured for user accounts.
### Learn more
* [`DOC /security/authentication/publickeys`](#docs-security-security_authentication_publickeys)"""
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
        r"""Updates the public key for a user account.
### Learn more
* [`DOC /security/authentication/publickeys/{owner.uuid}/{account.name}/{index}`](#docs-security-security_authentication_publickeys_{owner.uuid}_{account.name}_{index})"""
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
        r"""Deletes the public key for a user account.
### Learn more
* [`DOC /security/authentication/publickeys/{owner.uuid}/{account.name}/{index}`](#docs-security-security_authentication_publickeys_{owner.uuid}_{account.name}_{index})"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the public keys configured for user accounts.
### Learn more
* [`DOC /security/authentication/publickeys`](#docs-security-security_authentication_publickeys)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the public keys configured for a user account.
### Learn more
* [`DOC /security/authentication/publickeys/{owner.uuid}/{account.name}/{index}`](#docs-security-security_authentication_publickeys_{owner.uuid}_{account.name}_{index})"""
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
        r"""Creates a public key for a user account.
### Learn more
* [`DOC /security/authentication/publickeys`](#docs-security-security_authentication_publickeys)"""
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
        r"""Updates the public key for a user account.
### Learn more
* [`DOC /security/authentication/publickeys/{owner.uuid}/{account.name}/{index}`](#docs-security-security_authentication_publickeys_{owner.uuid}_{account.name}_{index})"""
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
        r"""Deletes the public key for a user account.
### Learn more
* [`DOC /security/authentication/publickeys/{owner.uuid}/{account.name}/{index}`](#docs-security-security_authentication_publickeys_{owner.uuid}_{account.name}_{index})"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


