# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Before any users or applications can access data on the CIFS server over SMB, a CIFS share must be created with sufficient share permissions. CIFS share is a named access point in a volume which is tied to the CIFS server on the SVM. Before creating a CIFS share make sure that the path is valid within the scope of the SVM and that it is reachable.</br>
Permissions can be assigned to this newly created share by specifying the 'acls' field. When a CIFS share is created, ONTAP creates a default ACL for this share with 'Full-Control' permissions for an 'Everyone' user.
## Examples
### Creating a CIFS share
To create a CIFS share for a CIFS server, use the following API. Note the <i>return_records=true</i> query parameter used to obtain the newly created entry in the response.
<br/>
---
```
# The API:
POST /api/protocols/cifs/shares
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/cifs/shares?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"access_based_enumeration\": false, \"acls\": [ { \"permission\": \"no_access\", \"type\": \"unix_user\", \"user_or_group\": \"root\" } ], \"change_notify\": true, \"comment\": \"HR Department Share\", \"encryption\": false, \"home_directory\": false, \"name\": \"TEST\", \"oplocks\": true, \"path\": \"/\", \"svm\": { \"name\": \"vs1\", \"uuid\": \"000c5cd2-ebdf-11e8-a96e-0050568ea3cb\" }, \"unix_symlink\": \"local\"}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1"
      },
      "name": "TEST",
      "path": "/",
      "comment": "HR Department Share",
      "home_directory": false,
      "oplocks": true,
      "access_based_enumeration": false,
      "change_notify": true,
      "encryption": false,
      "unix_symlink": "local",
      "acls": [
        {
          "user_or_group": "root",
          "type": "unix_user",
          "permission": "no_access",
          "winsid_unixId": "0"
        }
      ]
    }
  ]
}
```
---
### Retrieving CIFS Shares for all SVMs in the cluster
---
```
# The API:
GET /api/protocols/cifs/shares
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/shares?fields=*&return_records=true&return_timeout=15" -H "accept application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/000c5cd2-ebdf-11e8-a96e-0050568ea3cb"
          }
        }
      },
      "name": "admin$",
      "path": "/",
      "home_directory": false,
      "oplocks": false,
      "access_based_enumeration": false,
      "change_notify": false,
      "encryption": false,
      "volume": {
        "name": "vol1",
        "uuid": "4e06f1bc-1ddc-42e2-abb2-f221c6a2ab2a"
      },
      "_links": {
        "self": {
          "href": "/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/admin%24"
        }
      }
    },
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/000c5cd2-ebdf-11e8-a96e-0050568ea3cb"
          }
        }
      },
      "name": "c$",
      "path": "/",
      "home_directory": false,
      "oplocks": true,
      "access_based_enumeration": false,
      "change_notify": true,
      "encryption": false,
      "unix_symlink": "local",
      "acls": [
        {
          "user_or_group": "BUILTIN\\Administrators",
          "type": "windows",
          "permission": "full_control"
        }
      ],
      "volume": {
        "name": "vol1",
        "uuid": "4e06f1bc-1ddc-42e2-abb2-f221c6a2ab2a"
      },
      "_links": {
        "self": {
          "href": "/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/c%24"
        }
      }
    },
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/000c5cd2-ebdf-11e8-a96e-0050568ea3cb"
          }
        }
      },
      "name": "ipc$",
      "path": "/",
      "home_directory": false,
      "oplocks": false,
      "access_based_enumeration": false,
      "change_notify": false,
      "encryption": false,
      "volume": {
        "name": "vol1",
        "uuid": "4e06f1bc-1ddc-42e2-abb2-f221c6a2ab2a"
      },
      "_links": {
        "self": {
          "href": "/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/ipc%24"
        }
      }
    },
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/000c5cd2-ebdf-11e8-a96e-0050568ea3cb"
          }
        }
      },
      "name": "TEST",
      "path": "/",
      "comment": "HR Department Share",
      "home_directory": false,
      "oplocks": true,
      "access_based_enumeration": false,
      "change_notify": true,
      "encryption": false,
      "unix_symlink": "local",
      "acls": [
        {
          "user_or_group": "Everyone",
          "type": "windows",
          "permission": "full_control"
        },
        {
          "user_or_group": "root",
          "type": "unix_user",
          "permission": "no_access"
        }
      ],
      "volume": {
        "name": "vol1",
        "uuid": "4e06f1bc-1ddc-42e2-abb2-f221c6a2ab2a"
      },
      "_links": {
        "self": {
          "href": "/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/TEST"
        }
      }
    }
  ],
  "num_records": 4,
  "_links": {
    "self": {
      "href": "/api/protocols/cifs/shares?fields=*&return_records=true&return_timeout=15"
    }
  }
}
```
---
### Retrieving all CIFS Shares for all SVMs in the cluster for which the acls are configured for a "root" user
---
```
# The API:
GET /api/protocols/cifs/shares
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/shares?acls.user_or_group=root&fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1"
      },
      "name": "TEST",
      "path": "/",
      "comment": "HR Department Share",
      "home_directory": false,
      "oplocks": true,
      "access_based_enumeration": false,
      "change_notify": true,
      "encryption": false,
      "unix_symlink": "local",
      "acls": [
        {
          "user_or_group": "Everyone",
          "type": "windows",
          "permission": "full_control"
        },
        {
          "user_or_group": "root",
          "type": "unix_user",
          "permission": "no_access"
        }
      ],
      "volume": {
        "name": "vol1",
        "uuid": "4e06f1bc-1ddc-42e2-abb2-f221c6a2ab2a"
      }
    }
  ],
  "num_records": 1
}
```
### Retrieving a specific CIFS share configuration for an SVM
The configuration being returned is identified by the UUID of its SVM and the name of the share.
```
# The API:
GET /api/protocols/cifs/shares/{svm.uuid}/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/TEST" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
    "name": "vs1"
  },
  "name": "TEST",
  "path": "/",
  "comment": "HR Department Share",
  "home_directory": false,
  "oplocks": true,
  "access_based_enumeration": false,
  "change_notify": true,
  "encryption": false,
  "unix_symlink": "local",
  "acls": [
    {
      "user_or_group": "Everyone",
      "type": "windows",
      "permission": "full_control"
    },
    {
      "user_or_group": "root",
      "type": "unix_user",
      "permission": "no_access"
    }
  ],
  "volume": {
    "name": "vol1",
    "uuid": "4e06f1bc-1ddc-42e2-abb2-f221c6a2ab2a"
  }
}
```
### Updating a specific CIFS share for an SVM
The CIFS share being modified is identified by the UUID of its SVM and the CIFS share name. The CIFS share ACLs cannot be modified with this API.
```
# The API:
PATCH /api/protocols/cifs/shares/{svm.uuid}/{name}
# The call:
 curl -X PATCH "https://<mgmt-ip>/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/TEST" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"access_based_enumeration\": true, \"change_notify\": true, \"comment\": \"HR Department Share\", \"encryption\": false, \"oplocks\": true, \"path\": \"/\", \"unix_symlink\": \"widelink\"}"
 ```
### Removing a specific CIFS share for an SVM
The CIFS share being removed is identified by the UUID of its SVM and the CIFS share name.
```
# The API:
DELETE /api/protocols/cifs/shares/{svm.uuid}/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/cifs/shares/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/test" -H "accept: application/json"
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


__all__ = ["CifsShare", "CifsShareSchema"]
__pdoc__ = {
    "CifsShareSchema.resource": False,
    "CifsShareSchema.patchable_fields": False,
    "CifsShareSchema.postable_fields": False,
}


class CifsShareSchema(ResourceSchema):
    """The fields of the CifsShare object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cifs_share. """

    access_based_enumeration = fields.Boolean(
        data_key="access_based_enumeration",
    )
    r""" If enabled, all folders inside this share are visible to a user based on that individual user access right; prevents
the display of folders or other shared resources that the user does not have access to. """

    acls = fields.List(fields.Nested("netapp_ontap.resources.cifs_share_acl.CifsShareAclSchema", unknown=EXCLUDE), data_key="acls")
    r""" The acls field of the cifs_share. """

    change_notify = fields.Boolean(
        data_key="change_notify",
    )
    r""" Specifies whether CIFS clients can request for change notifications for directories on this share. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=1, maximum=256),
    )
    r""" Specify the CIFS share descriptions.

Example: HR Department Share """

    encryption = fields.Boolean(
        data_key="encryption",
    )
    r""" Specifies that SMB encryption must be used when accessing this share. Clients that do not support encryption are not
able to access this share. """

    home_directory = fields.Boolean(
        data_key="home_directory",
    )
    r""" Specifies whether or not the share is a home directory share, where the share and path names are dynamic.
ONTAP home directory functionality automatically offer each user a dynamic share to their home directory without creating an
individual SMB share for each user.
The ONTAP CIFS home directory feature enable us to configure a share that maps to
different directories based on the user that connects to it. Instead of creating a separate shares for each user,
a single share with a home directory parameters can be created.
In a home directory share, ONTAP dynamically generates the share-name and share-path by substituting
%w, %u, and %d variables with the corresponding Windows user name, UNIX user name, and domain name, respectively. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=80),
    )
    r""" Specifies the name of the CIFS share that you want to create. If this
is a home directory share then the share name includes the pattern as
%w (Windows user name), %u (UNIX user name) and %d (Windows domain name)
variables in any combination with this parameter to generate shares dynamically.


Example: HR_SHARE """

    oplocks = fields.Boolean(
        data_key="oplocks",
    )
    r""" Specify whether opportunistic locks are enabled on this share. "Oplocks" allow clients to lock files and cache content locally,
which can increase performance for file operations. """

    path = fields.Str(
        data_key="path",
        validate=len_validation(minimum=1, maximum=256),
    )
    r""" The fully-qualified pathname in the owning SVM namespace that is shared through this share.
If this is a home directory share then the path should be dynamic by specifying the pattern
%w (Windows user name), %u (UNIX user name), or %d (domain name) variables in any combination.
ONTAP generates the path dynamically for the connected user and this path is appended to each
search path to find the full Home Directory path.


Example: /volume_1/eng_vol/ """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the cifs_share. """

    unix_symlink = fields.Str(
        data_key="unix_symlink",
        validate=enum_validation(['local', 'widelink', 'disable']),
    )
    r""" Controls the access of UNIX symbolic links to CIFS clients.
The supported values are:

    * local - Enables only local symbolic links which is within the same CIFS share.
    * widelink - Enables both local symlinks and widelinks.
    * disable - Disables local symlinks and widelinks.


Valid choices:

* local
* widelink
* disable """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the cifs_share. """

    @property
    def resource(self):
        return CifsShare

    @property
    def patchable_fields(self):
        return [
            "access_based_enumeration",
            "change_notify",
            "comment",
            "encryption",
            "oplocks",
            "path",
            "svm.name",
            "svm.uuid",
            "unix_symlink",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "access_based_enumeration",
            "acls",
            "change_notify",
            "comment",
            "encryption",
            "home_directory",
            "name",
            "oplocks",
            "path",
            "svm.name",
            "svm.uuid",
            "unix_symlink",
            "volume.name",
            "volume.uuid",
        ]

class CifsShare(Resource):
    r""" CIFS share is a named access point in a volume. Before users and applications can access data on the CIFS server over SMB,
a CIFS share must be created with sufficient share permission. CIFS shares are tied to the CIFS server on the SVM.
When a CIFS share is created, ONTAP creates a default ACL for the share with Full Control permissions for Everyone. """

    _schema = CifsShareSchema
    _path = "/api/protocols/cifs/shares"
    @property
    def _keys(self):
        return ["svm.uuid", "name"]

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
        r"""Retrieves CIFS shares.
### Related ONTAP commands
* `vserver cifs share show`
* `vserver cifs share properties show`
### Learn more
* [`DOC /protocols/cifs/shares`](#docs-NAS-protocols_cifs_shares)
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
        r"""Updates a CIFS share.
### Related ONTAP commands
* `vserver cifs share modify`
* `vserver cifs share properties add`
* `vserver cifs share properties remove`
### Learn more
* [`DOC /protocols/cifs/shares`](#docs-NAS-protocols_cifs_shares)
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
        r"""Deletes a CIFS share.
### Related ONTAP commands
* `vserver cifs share delete`
### Learn more
* [`DOC /protocols/cifs/shares`](#docs-NAS-protocols_cifs_shares)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves CIFS shares.
### Related ONTAP commands
* `vserver cifs share show`
* `vserver cifs share properties show`
### Learn more
* [`DOC /protocols/cifs/shares`](#docs-NAS-protocols_cifs_shares)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a CIFS share.
### Related ONTAP commands
* `vserver cifs share show`
* `vserver cifs share properties show`
### Learn more
* [`DOC /protocols/cifs/shares`](#docs-NAS-protocols_cifs_shares)
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
        r"""Creates a CIFS share.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the CIFS share.
* `name` - Name of the CIFS share.
* `path` - Path in the owning SVM namespace that is shared through this share.
### Recommended optional properties
* `comment` - Optionally choose to add a text comment of up to 256 characters about the CIFS share.
* `acls` - Optionally choose to add share permissions that users and groups have on the CIFS share.
### Default property values
If not specified in POST, the following default property values are assigned:
* `home_directory` - _false_
* `oplocks` - _true_
* `access_based_enumeration` - _false_
* `change_notify` - _true_
* `encryption` - _false_
* `unix_symlink` - _local_
### Related ONTAP commands
* `vserver cifs share create`
* `vserver cifs share properties add`
* `vserver cifs share access-control create`
### Learn more
* [`DOC /protocols/cifs/shares`](#docs-NAS-protocols_cifs_shares)
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
        r"""Updates a CIFS share.
### Related ONTAP commands
* `vserver cifs share modify`
* `vserver cifs share properties add`
* `vserver cifs share properties remove`
### Learn more
* [`DOC /protocols/cifs/shares`](#docs-NAS-protocols_cifs_shares)
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
        r"""Deletes a CIFS share.
### Related ONTAP commands
* `vserver cifs share delete`
### Learn more
* [`DOC /protocols/cifs/shares`](#docs-NAS-protocols_cifs_shares)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


