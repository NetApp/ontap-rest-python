# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
ONTAP allows both CIFS and NFS to access the same datastore. This datastore can contain symbolic links which are files, created by UNIX clients. It contains a reference to another file or directory. If an SMB client accesses a symbolic link, it is redirected to the target file or directory that the symbolic link refers to. The symbolic links can point to files within the volume that contain the share, or to files that are contained in other volumes on the Storage Virtual Machine (SVM), or even to volumes contained on other SVMs.<p/>
There are two types of symbolic links:

  * <b>Relative</b>  A relative symbolic link contains a reference to the file or directory relative to its parent directory. Therefore, the path of the file it is referring to should not begin with a backslash (/). If you enable symbolic links on a share, relative symbolic links work without UNIX symlink mapping.
  * <b>Absolute</b> An absolute symbolic link contains a reference to a file or directory in the form of an absolute path. Therefore, the path of the file it is referring to should begin with a backslash (/). An absolute symbolic link can refer to a file or directory within or outside of the file system of the symbolic link. If the target is not in the same local file system, the symbolic link is called a "widelink". If the symbolic link is enabled on a share and absolute symbolic links do not work right away, the mapping between the UNIX path of the symbolic link to the destination CIFS path must be created. When creating absolute symbolic link mappings, locality could be either "local" or "widelink" and it must be specified. If UNIX symlink mapping is created for a file or directory which is outside of the local share but the locality is set to "local", ONTAP does not allow access to the target.
</br>A UNIX symbolic link support could be added to SMB shares by specifying the <i>unix_symlink</i> property during the creation of SMB shares or at any time by modifying the existing SMB <i>unix_symlink</i> property. UNIX symbolic link support is enabled by default.<p/>
## Examples
### Creating a UNIX symlink mapping for CIFS shares
To create UNIX symlink mappings for SMB shares, use the following API. Note the <i>return_records=true</i> query parameter used to obtain the newly created entry in the response.
<br/>
```
# The API:
POST /api/protocols/cifs/unix-symlink-mapping
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/cifs/unix-symlink-mapping?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"svm\": { \"name\": \"vs1\", \"uuid\": \"000c5cd2-ebdf-11e8-a96e-0050568ea3cb\" }, \"target\": { \"home_directory\": false, \"locality\": \"local\", \"path\": \"/dir1/dir2/\", \"server\": \"cifs123\", \"share\": \"sh1\" }, \"unix_path\": \"/mnt/eng_volume/\"}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs1"
      },
      "unix_path": "/mnt/eng_volume/",
      "target": {
        "share": "sh1",
        "path": "/dir1/dir2/",
        "server": "cifs123",
        "locality": "local",
        "home_directory": false
      }
    }
  ]
}
```
---
### Retrieving UNIX symlink mappings for all SVMs in the cluster
```
# The API:
GET /api/protocols/cifs/unix-symlink-mapping
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/unix-symlink-mapping?fields=*&return_records=true&return_timeout=15" -H "accept: application/hal+json"
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
      "unix_path": "/mnt/eng_volume/",
      "target": {
        "share": "sh1",
        "path": "/dir1/dir2/",
        "server": "CIFS123",
        "locality": "local",
        "home_directory": false
      },
      "_links": {
        "self": {
          "href": "/api/protocols/cifs/unix-symlink-mapping/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/%2Fmnt%2Feng_volume%2F"
        }
      }
    },
    {
      "svm": {
        "uuid": "1d30d1b1-ebdf-11e8-a96e-0050568ea3cb",
        "name": "vs2",
        "_links": {
          "self": {
            "href": "/api/svm/svms/1d30d1b1-ebdf-11e8-a96e-0050568ea3cb"
          }
        }
      },
      "unix_path": "/mnt/eng_volume/",
      "target": {
        "share": "ENG_SHARE",
        "path": "/dir1/dir2/",
        "server": "ENGCIFS",
        "locality": "widelink",
        "home_directory": false
      },
      "_links": {
        "self": {
          "href": "/api/protocols/cifs/unix-symlink-mapping/1d30d1b1-ebdf-11e8-a96e-0050568ea3cb/%2Fmnt%2Feng_volume%2F"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/cifs/unix-symlink-mapping?fields=*&return_records=true&return_timeout=15"
    }
  }
}
```
### Retrieving a specific UNIX symlink mapping for an SVM
The mapping being returned is identified by the UUID of its SVM and the unix-path.
<br/>
```
# The API:
GET /api/protocols/cifs/unix-symlink-mapping/{svm.uuid}/{unix_path}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/unix-symlink-mapping/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/%2Fmnt%2Feng_volume%2F" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "000c5cd2-ebdf-11e8-a96e-0050568ea3cb",
   "name": "vs1"
  },
  "unix_path": "/mnt/eng_volume/",
  "target": {
    "share": "sh1",
    "path": "/dir1/dir2/",
    "server": "CIFS123",
    "locality": "local",
    "home_directory": false
  }
}
```
### Updating a specific UNIX symlink mapping for an SVM
The mapping being modified is identified by the UUID of its SVM and the unix-path.
<br/>
```
# The API:
PATCH /api/protocols/cifs/unix-symlink-mapping/{svm.uuid}/{unix_path}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/cifs/unix-symlink-mapping/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/%2Fmnt%2Feng_volume%2F" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"target\": { \"home_directory\": true, \"locality\": \"widelink\", \"path\": \"/new_path/\", \"server\": \"HR_SERVER\", \"share\": \"sh2\" }}"
```
### Removing a specific UNIX symlink mapping for an SVM
The mapping being removed is identified by the UUID of its SVM and the unix-path.
<br/>
```
# The API:
DELETE /api/protocols/cifs/unix-symlink-mapping/{svm.uuid}/{unix_path}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/cifs/unix-symlink-mapping/000c5cd2-ebdf-11e8-a96e-0050568ea3cb/%2Fmnt%2Feng_volume%2F" -H "accept: application/json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["CifsSymlinkMapping", "CifsSymlinkMappingSchema"]
__pdoc__ = {
    "CifsSymlinkMappingSchema.resource": False,
    "CifsSymlinkMappingSchema.patchable_fields": False,
    "CifsSymlinkMappingSchema.postable_fields": False,
}


class CifsSymlinkMappingSchema(ResourceSchema):
    """The fields of the CifsSymlinkMapping object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cifs_symlink_mapping. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the cifs_symlink_mapping. """

    target = fields.Nested("netapp_ontap.models.cifs_target.CifsTargetSchema", data_key="target", unknown=EXCLUDE)
    r""" The target field of the cifs_symlink_mapping. """

    unix_path = fields.Str(
        data_key="unix_path",
        validate=len_validation(minimum=0, maximum=256),
    )
    r""" Specifies the UNIX path prefix to be matched for the mapping.

Example: /mnt/eng_volume/ """

    @property
    def resource(self):
        return CifsSymlinkMapping

    @property
    def patchable_fields(self):
        return [
            "svm.name",
            "svm.uuid",
            "target",
        ]

    @property
    def postable_fields(self):
        return [
            "svm.name",
            "svm.uuid",
            "target",
            "unix_path",
        ]

class CifsSymlinkMapping(Resource):
    r""" ONTAP allows for both CIFS and NFS access to the same datastore. This datastore can contain symbolic links created by UNIX clients which can point anywhere from the perspective of the UNIX client. To Access such UNIX symlink from CIFS share, we need to create a CIFS symbolic link path mapping from a UNIX symlink and target it as a CIFS path. """

    _schema = CifsSymlinkMappingSchema
    _path = "/api/protocols/cifs/unix-symlink-mapping"
    @property
    def _keys(self):
        return ["svm.uuid", "unix_path"]

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
        r"""Retrieves UNIX symbolic link mappings for CIFS clients.
### Related ONTAP commands
* `vserver cifs symlink show`
### Learn more
* [`DOC /protocols/cifs/unix-symlink-mapping`](#docs-NAS-protocols_cifs_unix-symlink-mapping)
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
        r"""Updates the UNIX symbolic link mapping for CIFS clients.
### Related ONTAP commands
* `vserver cifs symlink modify`
### Learn more
* [`DOC /protocols/cifs/unix-symlink-mapping`](#docs-NAS-protocols_cifs_unix-symlink-mapping)
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
        r"""Deletes the UNIX symbolic link mapping for CIFS clients.
### Related ONTAP commands
* `vserver cifs symlink delete`
### Learn more
* [`DOC /protocols/cifs/unix-symlink-mapping`](#docs-NAS-protocols_cifs_unix-symlink-mapping)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves UNIX symbolic link mappings for CIFS clients.
### Related ONTAP commands
* `vserver cifs symlink show`
### Learn more
* [`DOC /protocols/cifs/unix-symlink-mapping`](#docs-NAS-protocols_cifs_unix-symlink-mapping)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a UNIX symbolic link mapping for CIFS clients.
### Related ONTAP commands
* `vserver cifs symlink show`
### Learn more
* [`DOC /protocols/cifs/unix-symlink-mapping`](#docs-NAS-protocols_cifs_unix-symlink-mapping)
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
        r"""Creates a UNIX symbolic link mapping for a CIFS client.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the CIFS unix-symlink-mapping.
* `unix_path` - UNIX path to which the CIFS symlink mapping to be created.
* `target.share` - CIFS share name on the destination CIFS server to which the UNIX symbolic link is pointing.
* `target.path` - CIFS path on the destination to which the symbolic link maps.
### Default property values
* `target.server` - _Local_NetBIOS_Server_Name_
* `locality` - _local_
* `home_directory` - _false_
### Related ONTAP commands
* `vserver cifs symlink create`
### Learn more
* [`DOC /protocols/cifs/unix-symlink-mapping`](#docs-NAS-protocols_cifs_unix-symlink-mapping)
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
        r"""Updates the UNIX symbolic link mapping for CIFS clients.
### Related ONTAP commands
* `vserver cifs symlink modify`
### Learn more
* [`DOC /protocols/cifs/unix-symlink-mapping`](#docs-NAS-protocols_cifs_unix-symlink-mapping)
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
        r"""Deletes the UNIX symbolic link mapping for CIFS clients.
### Related ONTAP commands
* `vserver cifs symlink delete`
### Learn more
* [`DOC /protocols/cifs/unix-symlink-mapping`](#docs-NAS-protocols_cifs_unix-symlink-mapping)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


