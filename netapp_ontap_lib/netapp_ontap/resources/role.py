# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This APi is used to retrieve or delete a role. The role can be SVM-scoped or cluster-scoped.<p/>
Specify the owner UUID and the role name in the URI path. The owner UUID corresponds to the UUID of the SVM for which the role has been created and can be obtained from the response body of a GET call performed on one of the following APIs:
<i>/api/security/roles</i> for all roles
<i>/api/security/roles/?scope=svm</i> for SVM-scoped roles
<i>/api/security/roles/?owner.name=<svm-name></i> for roles in a specific SVM
This API response contains the complete URI for each role that can be used for retrieving or deleting a role.<p/>
Note: The pre-defined roles can be retrieved but cannot be deleted.
## Examples
### Retrieving a role configuration
```
# The API:
GET "/api/security/roles/{owner.uuid}/{name}"
# The call:
curl -X GET "https://<mgmt-ip>/api/security/roles/aaef7c38-4bd3-11e9-b238-0050568e2e25/secure_role"
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
  "name": "secure_role",
  "privileges": [
    {
      "path": "/api/security",
      "access": "all",
      "_links": {
        "self": {
          "href": "/api/security/roles/aaef7c38-4bd3-11e9-b238-0050568e2e25/secure_role/privileges/%2Fapi%2Fsecurity"
        }
      }
    }
  ],
  "builtin": false,
  "scope": "svm",
  "_links": {
    "self": {
      "href": "/api/security/roles/aaef7c38-4bd3-11e9-b238-0050568e2e25/secure_role"
    }
  }
}
```
### Deleting a custom role
```
# The API:
DELETE "/api/security/roles/{owner.uuid}/{name}"
# The call:
curl -X DELETE "https://<mgmt-ip>/api/security/roles/aaef7c38-4bd3-11e9-b238-0050568e2e25/svm_role1"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Role", "RoleSchema"]
__pdoc__ = {
    "RoleSchema.resource": False,
    "RoleSchema.patchable_fields": False,
    "RoleSchema.postable_fields": False,
}


class RoleSchema(ResourceSchema):
    """The fields of the Role object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the role. """

    builtin = fields.Boolean(
        data_key="builtin",
    )
    r""" Indicates if this is a built-in (pre-defined) role which cannot be modified or deleted. """

    name = fields.Str(
        data_key="name",
    )
    r""" Role name

Example: admin """

    owner = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="owner", unknown=EXCLUDE)
    r""" The owner field of the role. """

    privileges = fields.List(fields.Nested("netapp_ontap.resources.role_privilege.RolePrivilegeSchema", unknown=EXCLUDE), data_key="privileges")
    r""" The list of privileges that this role has been granted. """

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
        return Role

    @property
    def patchable_fields(self):
        return [
            "privileges",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "owner.name",
            "owner.uuid",
            "privileges",
        ]

class Role(Resource):
    r""" A named set of privileges that defines the rights an account has when it is assigned the role. """

    _schema = RoleSchema
    _path = "/api/security/roles"
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
        r"""Retrieves a list of roles configured in the cluster.
### Related ONTAP commands
* `security login rest-role show`
### Learn more
* [`DOC /security/roles`](#docs-security-security_roles)
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
        r"""Deletes the specified role.
### Required parameters
* `name` - Name of the role to be deleted.
* `owner.uuid` - UUID of the SVM housing the role.
### Related ONTAP commands
* `security login rest-role delete`
### Learn more
* [`DOC /security/roles/{owner.uuid}/{name}`](#docs-security-security_roles_{owner.uuid}_{name})
* [`DOC /security/roles`](#docs-security-security_roles)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of roles configured in the cluster.
### Related ONTAP commands
* `security login rest-role show`
### Learn more
* [`DOC /security/roles`](#docs-security-security_roles)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the details of the specified role.
### Related ONTAP commands
* `security login rest-role show`
### Learn more
* [`DOC /security/roles/{owner.uuid}/{name}`](#docs-security-security_roles_{owner.uuid}_{name})
* [`DOC /security/roles`](#docs-security-security_roles)
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
        r"""Creates a new cluster-scoped role or an SVM-scoped role. For an SVM-scoped role, specify either the SVM name as the owner.name or SVM UUID as the owner.uuid in the request body along with other parameters for the role. The owner.uuid or owner.name are not required to be specified for a cluster-scoped role.
### Required parameters
* `name` - Name of the role to be created.
* `privileges` - Array of privilege tuples. Each tuple consists of a REST API path and its desired access level.
### Optional parameters
* `owner.name` or `owner.uuid`  - Name or UUID of the SVM for an SVM-scoped role.
### Related ONTAP commands
* `security login rest-role create`
### Learn more
* [`DOC /security/roles`](#docs-security-security_roles)
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
        r"""Deletes the specified role.
### Required parameters
* `name` - Name of the role to be deleted.
* `owner.uuid` - UUID of the SVM housing the role.
### Related ONTAP commands
* `security login rest-role delete`
### Learn more
* [`DOC /security/roles/{owner.uuid}/{name}`](#docs-security-security_roles_{owner.uuid}_{name})
* [`DOC /security/roles`](#docs-security-security_roles)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


