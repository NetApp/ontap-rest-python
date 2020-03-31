# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API changes the password for a local user account.<p/>
Only cluster administrators with the <i>"admin"</i> role can change the password for other cluster or SVM user accounts. If you are not a cluster administrator, you can only change your own password.
## Examples
### Changing the password of another cluster or SVM user account by a cluster administrator
Specify the user account name and the new password in the body of the POST request. The owner.uuid or owner.name are not required to be specified for a cluster-scoped user account.<p/>
For an SVM-scoped account, along with new password and user account name, specify either the SVM name as the owner.name or SVM uuid as the owner.uuid in the body of the POST request. These indicate the SVM for which the user account is created and can be obtained from the response body of a GET request performed on the <i>/api/svm/svms</i> API.
```
# The API:
POST "/api/security/authentication/password"
# The call to change the password of another cluster user:
curl -X POST "https://<mgmt-ip>/api/security/authentication/password" -d '{"name":"cluster_user1","password":"hello@1234"}'
# The call to change the password of another SVM user:
curl -X POST "https://<mgmt-ip>/api/security/authentication/password" -d '{"owner.name":"svm1","name":"svm_user1","password":"hello@1234"}'
```
### Changing the password of an SVM-scoped user
Note: The IP address in the URI must be same as one of the interfaces owned by the SVM.
```
# The API:
POST "/api/security/authentication/password"
# The call:
curl -X POST "https://<SVM-ip>/api/security/authentication/password" -d '{"name":"svm_user1","password":"new1@1234"}'
```
---
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["AccountPassword", "AccountPasswordSchema"]
__pdoc__ = {
    "AccountPasswordSchema.resource": False,
    "AccountPasswordSchema.patchable_fields": False,
    "AccountPasswordSchema.postable_fields": False,
}


class AccountPasswordSchema(ResourceSchema):
    """The fields of the AccountPassword object"""

    name = fields.Str(
        data_key="name",
    )
    r""" The user account name whose password is being modified. """

    owner = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="owner", unknown=EXCLUDE)
    r""" The owner field of the account_password. """

    password = fields.Str(
        data_key="password",
        validate=len_validation(minimum=8, maximum=128),
    )
    r""" The password string """

    @property
    def resource(self):
        return AccountPassword

    @property
    def patchable_fields(self):
        return [
            "name",
            "password",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "owner.name",
            "owner.uuid",
            "password",
        ]

class AccountPassword(Resource):
    r""" The password object """

    _schema = AccountPasswordSchema
    _path = "/api/security/authentication/password"






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
        r"""Updates the password for a user account.
### Required parameters
* `name` - User account name.
* `password` - New password for the user account.
### Optional parameters
* `owner.name` or `owner.uuid` - Name or UUID of the SVM for an SVM-scoped user account.
### Related ONTAP commands
* `security login password`
### Learn more
* [`DOC /security/authentication/password`](#docs-security-security_authentication_password)
* [`DOC /security/accounts`](#docs-security-security_accounts)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member




