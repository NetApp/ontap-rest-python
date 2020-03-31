# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API displays and manages the configuration of scoped user accounts.<p/>
Newly created user accounts might need to be updated for many reasons. For example, a user account might need to use a different application or its role might need to be modified. According to a policy, the password or authentication source of a user account might need to be changed, or a user account might need to be locked or deleted from the system. This API allows you to make these changes to user accounts.<p/>
Specify the owner UUID and the user account name in the URI path. The owner UUID corresponds to the UUID of the SVM for which the user account has been created and can be obtained from the response body of the GET request performed on one of the following APIs:
<i>/api/security/accounts</i> for all user accounts
<i>/api/security/accounts/?scope=cluster</i> for cluster-scoped user accounts
<i>/api/security/accounts/?scope=svm</i> for SVM-scoped accounts
<i>/api/security/accounts/?owner.name=<svm-name></i> for a specific SVM
This API response contains the complete URI for each user account that can be used.
## Examples
### Retrieving the user account details
```
# The API:
GET "/api/security/accounts/{owner.uuid}/{name}"
# The call:
curl -X GET "https://<mgmt-ip>/api/security/accounts/aef7c38-4bd3-11e9-b238-0050568e2e25/svm_user1"
# The response:
{
  "owner": {
    "uuid": "aaef7c38-4bd3-11e9-b238-0050568e2e25",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/aaef7c38-4bd3-11e9-b238-0050568e2e25"
      }
          }
  },
  "name": "svm_user1",
  "applications": [
    {
      "application": "ssh",
      "authentication_methods": [
        "password"
      ],
      "second_authentication_method": "none"
    }
  ],
  "role": {
    "name": "vsadmin",
    "_links": {
      "self": {
        "href": "/api/svms/aaef7c38-4bd3-11e9-b238-0050568e2e25/admin/roles/vsadmin"
      }
    }
  },
  "locked": false,
  "scope": "svm",
  "_links": {
    "self": {
      "href": "/api/security/accounts/aaef7c38-4bd3-11e9-b238-0050568e2e25/svm_user1"
    }
  }
}
```
### Updating the applications and role in a user account
Specify the desired configuration in the form of tuples (of applications and authentication methods) and the role. All other previously configured applications that are not specified in the "applications" parameter of the PATCH request will be de-provisioned for the user account.<p/>
```
# The API:
PATCH "/api/security/accounts/{owner.uuid}/{name}"
# The call to update the applications and role:
curl -X PATCH "https://<mgmt-ip>/api/security/accounts/aaef7c38-4bd3-11e9-b238-0050568e2e25/svm_user1" -d '{"applications":[{"application":"http","authentication_methods":["domain"]},{"application":"ontapi","authentication_methods":["password"]}],"role":"vsadmin-backup"}'
# The call to update only the role:
curl -X PATCH "https://<mgmt-ip>/api/security/accounts/aaef7c38-4bd3-11e9-b238-0050568e2e25/svm_user1" -d '{"role":"vsadmin-protocol"}'
```
### Updating the password for a user account
```
# The API:
PATCH "/api/security/accounts/{owner.uuid}/{name}"
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/accounts/aaef7c38-4bd3-11e9-b238-0050568e2e25/svm_user1" -d '{"password":"newp@ssw@rd2"}'
```
### Locking a user account
```
The API:
PATCH "/api/security/accounts/{owner.uuid}/{name}"
The call:
curl -X PATCH "https://<mgmt-ip>/api/security/accounts/aaef7c38-4bd3-11e9-b238-0050568e2e25/svm_user1" -d '{"locked":"true"}'
```
### Deleting a user account
```
# The API:
DELETE "/api/security/accounts/{owner.uuid}/{name}"
# The call:
curl -X DELETE "https://<mgmt-ip>/api/security/accounts/aaef7c38-4bd3-11e9-b238-0050568e2e25/svm_user1"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Account", "AccountSchema"]
__pdoc__ = {
    "AccountSchema.resource": False,
    "AccountSchema.patchable_fields": False,
    "AccountSchema.postable_fields": False,
}


class AccountSchema(ResourceSchema):
    """The fields of the Account object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the account. """

    applications = fields.List(fields.Nested("netapp_ontap.models.account_application.AccountApplicationSchema", unknown=EXCLUDE), data_key="applications")
    r""" The applications field of the account. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" Optional comment for the user account. """

    locked = fields.Boolean(
        data_key="locked",
    )
    r""" Locked status of the account. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=3, maximum=64),
    )
    r""" User or group account name

Example: joe.smith """

    owner = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="owner", unknown=EXCLUDE)
    r""" The owner field of the account. """

    password = fields.Str(
        data_key="password",
        validate=len_validation(minimum=8, maximum=128),
    )
    r""" Password for the account. The password can contain a mix of lower and upper case alphabetic characters, digits, and special characters. """

    role = fields.Nested("netapp_ontap.resources.role.RoleSchema", data_key="role", unknown=EXCLUDE)
    r""" The role field of the account. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['cluster', 'svm']),
    )
    r""" Scope of the entity. Set to "cluster" for cluster owned objects and to "svm" for SVM owned objects.

Valid choices:

* cluster
* svm """

    @property
    def resource(self):
        return Account

    @property
    def patchable_fields(self):
        return [
            "applications",
            "comment",
            "locked",
            "password",
            "role.name",
        ]

    @property
    def postable_fields(self):
        return [
            "applications",
            "comment",
            "locked",
            "name",
            "owner.name",
            "owner.uuid",
            "password",
            "role.name",
        ]

class Account(Resource):
    """Allows interaction with Account objects on the host"""

    _schema = AccountSchema
    _path = "/api/security/accounts"
    @property
    def _keys(self):
        return ["owner.uuid", "name"]

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
        r"""Retrieves a list of user accounts in the cluster.
### Related ONTAP commands
* `security login show`
### Learn more
* [`DOC /security/accounts`](#docs-security-security_accounts)
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
        r"""Updates a user account. Locks or unlocks a user account and/or updates the role, applications, and/or password for the user account.
### Required parameters
* `name` - Account name to be updated.
* `owner.uuid`  - UUID of the SVM housing the user account to be updated.
### Optional parameters
* `applications` - Array of one or more tuples (of application and authentication methods).
* `role` - RBAC role for the user account.
* `password` - Password for the user account (if the authentication method is opted as password for one or more of applications).
* `second_authentication_method` - Needed for MFA and only supported for ssh application. Defaults to `none` if not supplied.
* `comment` - Comment for the user account (e.g purpose of this account).
* `locked` - Set to true/false to lock/unlock the account.
### Related ONTAP commands
* `security login create`
* `security login modify`
* `security login password`
* `security login lock`
* `security login unlock`
### Learn more
* [`DOC /security/accounts/{owner.uuid}/{name}`](#docs-security-security_accounts_{owner.uuid}_{name})
* [`DOC /security/accounts`](#docs-security-security_accounts)
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
        r"""Deletes a user account.
### Required parameters
* `name` - Account name to be deleted.
* `owner.uuid`  - UUID of the SVM housing the user account to be deleted.
### Related ONTAP commands
* `security login delete`
### Learn more
* [`DOC /security/accounts/{owner.uuid}/{name}`](#docs-security-security_accounts_{owner.uuid}_{name})
* [`DOC /security/accounts`](#docs-security-security_accounts)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of user accounts in the cluster.
### Related ONTAP commands
* `security login show`
### Learn more
* [`DOC /security/accounts`](#docs-security-security_accounts)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific user account.
### Related ONTAP commands
* `security login show`
### Learn more
* [`DOC /security/accounts/{owner.uuid}/{name}`](#docs-security-security_accounts_{owner.uuid}_{name})
* [`DOC /security/accounts`](#docs-security-security_accounts)
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
        r"""Creates a new user account.
### Required parameters
* `name` - Account name to be created.
* `applications` - Array of one or more application tuples (of application and authentication methods).
### Optional parameters
* `owner.name` or `owner.uuid`  - Name or UUID of the SVM for an SVM-scoped user account. If not supplied, a cluster-scoped user account is created.
* `role` - RBAC role for the user account. Defaulted to `admin` for cluster user account and to `vsadmin` for SVM-scoped account.
* `password` - Password for the user account (if the authentication method is opted as password for one or more of applications).
* `second_authentication_method` - Needed for MFA and only supported for ssh application. Defaults to `none` if not supplied.
* `comment` - Comment for the user account (e.g purpose of this account).
* `locked` - Locks the account after creation. Defaults to `false` if not supplied.
### Related ONTAP commands
* `security login create`
### Learn more
* [`DOC /security/accounts`](#docs-security-security_accounts)
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
        r"""Updates a user account. Locks or unlocks a user account and/or updates the role, applications, and/or password for the user account.
### Required parameters
* `name` - Account name to be updated.
* `owner.uuid`  - UUID of the SVM housing the user account to be updated.
### Optional parameters
* `applications` - Array of one or more tuples (of application and authentication methods).
* `role` - RBAC role for the user account.
* `password` - Password for the user account (if the authentication method is opted as password for one or more of applications).
* `second_authentication_method` - Needed for MFA and only supported for ssh application. Defaults to `none` if not supplied.
* `comment` - Comment for the user account (e.g purpose of this account).
* `locked` - Set to true/false to lock/unlock the account.
### Related ONTAP commands
* `security login create`
* `security login modify`
* `security login password`
* `security login lock`
* `security login unlock`
### Learn more
* [`DOC /security/accounts/{owner.uuid}/{name}`](#docs-security-security_accounts_{owner.uuid}_{name})
* [`DOC /security/accounts`](#docs-security-security_accounts)
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
        r"""Deletes a user account.
### Required parameters
* `name` - Account name to be deleted.
* `owner.uuid`  - UUID of the SVM housing the user account to be deleted.
### Related ONTAP commands
* `security login delete`
### Learn more
* [`DOC /security/accounts/{owner.uuid}/{name}`](#docs-security-security_accounts_{owner.uuid}_{name})
* [`DOC /security/accounts`](#docs-security-security_accounts)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


