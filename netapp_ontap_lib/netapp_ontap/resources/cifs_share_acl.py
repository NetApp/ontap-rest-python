# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Access to files and folders can be secured over a network by configuring share access control lists (ACLs) on CIFS shares. Share-level ACLs can be configured by using either Windows users and groups or UNIX users and groups. A share-level ACL consists of a list of access control entries (ACEs). Each ACE contains a user or group name and a set of permissions that determines user or group access to the share, regardless of the security style of the volume or qtree containing the share. </br>
When an SMB user tries to access a share, ONTAP checks the share-level ACL to determine whether access should be granted. A share-level ACL only restricts access to files in the share; it never grants more access than the file level ACLs.
## Examples
### Creating a CIFS share ACL
To create a share ACL for a CIFS share, use the following API. Note the <i>return_records=true</i> query parameter used to obtain the newly created entry in the response.
<br/>
---
```
# The API:
POST /api/protocols/cifs/shares{svm.uuid}/{share}/acls
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/sh1/acls?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"permission\": \"no_access\", \"type\": \"windows\", \"user_or_group\": \"root\"}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "name": "vs1"
      },
      "user_or_group": "root",
      "type": "windows",
      "permission": "no_access"
    }
  ]
}
```
---
### Retrieving all CIFS shares ACLs for a specific CIFS share for a specific SVM in the cluster
---
```
# The API:
GET /api/protocols/cifs/shares/{svm.uuid}/{share}/acls
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/sh1/acls?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1"
      },
      "share": "sh1",
      "user_or_group": "Everyone",
      "type": "windows",
      "permission": "full_control"
    },
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1"
      },
      "share": "sh1",
      "user_or_group": "root",
      "type": "windows",
      "permission": "no_access"
    }
  ],
  "num_records": 2
}
```
---
### Retrieving a CIFS share ACLs for a user or a group of type Windows or type UNIX on a CIFS share for a specific SVM
---
```
# The API:
GET /api/protocols/cifs/shares/{svm.uuid}/{share}/acls/{user_or_group}/{type}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/sh1/acls/everyone/windows" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
    "name": "vs1"
  },
  "share": "sh1",
  "user_or_group": "everyone",
  "type": "windows",
  "permission": "full_control"
}
```
### Updating a CIFS share ACLs of a user or group on a CIFS share for a specific SVM
The CIFS share ACL being modified is identified by the UUID of its SVM, the CIFS share name, user or group name and the type of the user or group.
```
# The API:
PATCH /api/protocols/cifs/shares/{svm.uuid}/{share}/acls/{user_or_group}/{type}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/sh1/acls/everyone/windows" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"permission\": \"no_access\"}"
```
### Removing a CIFS share ACLs of a user or group on a CIFS Share for a specific SVM
The CIFS share ACL being removed is identified by the UUID of its SVM, the CIFS share name, user or group name and the type of the user or group.
```
# The API:
DELETE /api/protocols/cifs/shares/{svm.uuid}/{share}/acls/{user_or_group}/{type}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/sh1/acls/everyone/windows" -H "accept: application/json"
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


__all__ = ["CifsShareAcl", "CifsShareAclSchema"]
__pdoc__ = {
    "CifsShareAclSchema.resource": False,
    "CifsShareAclSchema.patchable_fields": False,
    "CifsShareAclSchema.postable_fields": False,
}


class CifsShareAclSchema(ResourceSchema):
    """The fields of the CifsShareAcl object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cifs_share_acl. """

    permission = fields.Str(
        data_key="permission",
        validate=enum_validation(['no_access', 'read', 'change', 'full_control']),
    )
    r""" Specifies the access rights that a user or group has on the defined CIFS Share.
The following values are allowed:

* no_access    - User does not have CIFS share access
* read         - User has only read access
* change       - User has change access
* full_control - User has full_control access


Valid choices:

* no_access
* read
* change
* full_control """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['windows', 'unix_user', 'unix_group']),
    )
    r""" Specifies the type of the user or group to add to the access control
list of a CIFS share. The following values are allowed:

* windows    - Windows user or group
* unix_user  - UNIX user
* unix_group - UNIX group


Valid choices:

* windows
* unix_user
* unix_group """

    user_or_group = fields.Str(
        data_key="user_or_group",
    )
    r""" Specifies the user or group name to add to the access control list of a CIFS share.

Example: ENGDOMAIN\ad_user """

    @property
    def resource(self):
        return CifsShareAcl

    @property
    def patchable_fields(self):
        return [
            "permission",
        ]

    @property
    def postable_fields(self):
        return [
            "permission",
            "type",
            "user_or_group",
        ]

class CifsShareAcl(Resource):
    r""" The permissions that users and groups have on a CIFS share. """

    _schema = CifsShareAclSchema
    _path = "/api/protocols/cifs/shares/{svm[uuid]}/{cifs_share[share]}/acls"
    @property
    def _keys(self):
        return ["svm.uuid", "cifs_share.share", "user_or_group", "type"]

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
        r"""Retrieves the share-level ACL on a CIFS share.
### Related ONTAP commands
* `vserver cifs share access-control show`
### Learn more
* [`DOC /protocols/cifs/shares/{svm.uuid}/{share}/acls`](#docs-NAS-protocols_cifs_shares_{svm.uuid}_{share}_acls)
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
        r"""Updates a share-level ACL on a CIFS share.
### Related ONTAP commands
* `vserver cifs share access-control modify`
### Learn more
* [`DOC /protocols/cifs/shares/{svm.uuid}/{share}/acls`](#docs-NAS-protocols_cifs_shares_{svm.uuid}_{share}_acls)
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
        r"""Deletes a share-level ACL on a CIFS share.
### Related ONTAP commands
* `vserver cifs share access-control delete`
### Learn more
* [`DOC /protocols/cifs/shares/{svm.uuid}/{share}/acls`](#docs-NAS-protocols_cifs_shares_{svm.uuid}_{share}_acls)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the share-level ACL on a CIFS share.
### Related ONTAP commands
* `vserver cifs share access-control show`
### Learn more
* [`DOC /protocols/cifs/shares/{svm.uuid}/{share}/acls`](#docs-NAS-protocols_cifs_shares_{svm.uuid}_{share}_acls)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the share-level ACL on CIFS share for a specified user or group.
### Related ONTAP commands
* `vserver cifs share access-control show`
### Learn more
* [`DOC /protocols/cifs/shares/{svm.uuid}/{share}/acls`](#docs-NAS-protocols_cifs_shares_{svm.uuid}_{share}_acls)
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
        r"""Creates a share-level ACL on a CIFS share.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the share acl.
* `share` - Existing CIFS share in which to create the share acl.
* `user_or_group` - Existing user or group name for which the acl is added on the CIFS share.
* `permission` - Access rights that a user or group has on the defined CIFS share.
### Default property values
* `type` - _windows_
### Related ONTAP commands
* `vserver cifs share access-control create`
### Learn more
* [`DOC /protocols/cifs/shares/{svm.uuid}/{share}/acls`](#docs-NAS-protocols_cifs_shares_{svm.uuid}_{share}_acls)
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
        r"""Updates a share-level ACL on a CIFS share.
### Related ONTAP commands
* `vserver cifs share access-control modify`
### Learn more
* [`DOC /protocols/cifs/shares/{svm.uuid}/{share}/acls`](#docs-NAS-protocols_cifs_shares_{svm.uuid}_{share}_acls)
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
        r"""Deletes a share-level ACL on a CIFS share.
### Related ONTAP commands
* `vserver cifs share access-control delete`
### Learn more
* [`DOC /protocols/cifs/shares/{svm.uuid}/{share}/acls`](#docs-NAS-protocols_cifs_shares_{svm.uuid}_{share}_acls)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


