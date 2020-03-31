# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API supports creating, deleting and retrieving configuration backup files.
Configuration backups can be 'cluster' or 'node' type. A 'cluster' backup contains cluster-wide configuration in addition to the configuration of each node in the cluster. A 'node' backup contains only node-specific configuration such as configuration files on the root volume and the boot variables. For creating a cluster backup, a cluster-wide job is queued. For creating a node backup, a private job local to the node is queued.
In addition to the backups created using this API, ONTAP creates configuration backups automatically based on job schedules. This API supports creating configuration backups on demand only. It supports deleting and retrieving configuration backups that are created automatically or on demand.
For information on configuration backup settings for automatically created backups, see [`DOC /support/configuration-backup`](#docs-support-support_configuration-backup)
## Examples
### Retrieving a list of configuration backup files
---
```
# The API:
/api/support/configuration-backup/backups
# The call:
curl -X GET "https://<mgmt-ip>/api/support/configuration-backup/backups" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "node": {
        "uuid": "5cafe0f6-499f-11e9-b644-005056bbcf93",
        "name": "node1",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/5cafe0f6-499f-11e9-b644-005056bbcf93"
          }
        }
      },
      "name": "backup1.7z",
      "_links": {
        "self": {
          "href": "/api/support/configuration_backup/backups/5cafe0f6-499f-11e9-b644-005056bbcf93/backup1.7z"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/support/configuration_backup/backups"
    }
  }
}
```
---
### Retrieving details of the specified configuration backup file
---
```
# The API:
/api/support/configuration-backup/backups/{node.uuid}/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/support/configuration-backup/backups/bc2f15d0-8b93-11e9-90e9-005056bb6a30/backup1.7z" -H "accept: application/hal+json"
# The response:
{
  "node": {
    "uuid": "bc2f15d0-8b93-11e9-90e9-005056bb6a30",
    "name": "node1",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/bc2f15d0-8b93-11e9-90e9-005056bb6a30"
      }
    }
  },
  "name": "backup1.7z",
  "type": "cluster",
  "time": "2019-06-10T13:35:06-04:00",
  "size": 6058408,
  "backup_nodes": [
    {
      "name": "node1"
    },
    {
      "name": "node2"
    }
  ],
  "version": "9.7.0",
  "auto": false,
  "download_link": "https://10.224.66.113/backups/backup1.7z",
  "_links": {
    "self": {
      "href": "/api/support/configuration-backup/backups/bc2f15d0-8b93-11e9-90e9-005056bb6a30/backup1.7z"
    }
  }
}
```
---
### Creating a configuration backup file
---
```
# The API:
/api/support/configuration-backup/backups
# The call:
curl -X POST "https://<mgmt-ip>/api/support/configuration-backup/backups" -H "accept: application/hal+json"
# The body:
{
  "node":
    {
      "uuid": "ac13c636-4fc9-11e9-94c2-005056bb2516",
      "name": "node1"
    },
  "name": "backup3.7z"
}
# The response header:
HTTP/1.1 202 Accepted
Date: Tue, 26 Mar 2019 14:26:24 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/support/configuration_backup/backups/ac13c636-4fc9-11e9-94c2-005056bb2516/backup3.7z
Content-Length: 189
Content-Type: application/hal+json
{
  "job": {
    "uuid": "22acfb68-4fd3-11e9-94c2-005056bb2516",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/22acfb68-4fd3-11e9-94c2-005056bb2516"
      }
    }
  }
}
```
---
### Deleting a configuration backup file
---
```
# The API:
/api/support/configuration-backup/backups/{node.uuid}/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/support/configuration_backup/backups/5cafe0f6-499f-11e9-b644-005056bbcf93/backup1.7z" -H "content-type: application/json"
# The response header:
HTTP/1.1 200 OK
Date: Tue, 26 Mar 2019 14:32:23 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 3
Content-Type: application/hal+json
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


__all__ = ["ConfigurationBackupFile", "ConfigurationBackupFileSchema"]
__pdoc__ = {
    "ConfigurationBackupFileSchema.resource": False,
    "ConfigurationBackupFileSchema.patchable_fields": False,
    "ConfigurationBackupFileSchema.postable_fields": False,
}


class ConfigurationBackupFileSchema(ResourceSchema):
    """The fields of the ConfigurationBackupFile object"""

    auto = fields.Boolean(
        data_key="auto",
    )
    r""" Indicates if the backup was created automatically. """

    backup_nodes = fields.List(fields.Nested("netapp_ontap.models.backup_node.BackupNodeSchema", unknown=EXCLUDE), data_key="backup_nodes")
    r""" The list of nodes included in the backup. """

    download_link = fields.Str(
        data_key="download_link",
    )
    r""" The link to download the backup file.

Example: https://10.224.65.198/backups/backup_file.7z """

    name = fields.Str(
        data_key="name",
    )
    r""" The backup name.

Example: backup_file.7z """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the configuration_backup_file. """

    size = fields.Integer(
        data_key="size",
    )
    r""" The size of the backup in bytes.

Example: 4787563 """

    time = fields.DateTime(
        data_key="time",
    )
    r""" The backup creation time.

Example: 2019-02-04T18:33:48.000+0000 """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['node', 'cluster']),
    )
    r""" The backup type.

Valid choices:

* node
* cluster """

    version = fields.Str(
        data_key="version",
    )
    r""" The software version.

Example: 9.7.0 """

    @property
    def resource(self):
        return ConfigurationBackupFile

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "node.name",
            "node.uuid",
        ]

class ConfigurationBackupFile(Resource):
    r""" The configuration backup file. """

    _schema = ConfigurationBackupFileSchema
    _path = "/api/support/configuration-backup/backups"
    @property
    def _keys(self):
        return ["node.uuid", "name"]

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
        r"""Retrieves a list of configuration backup files.
### Related ONTAP commands
* `system configuration backup show`

### Learn more
* [`DOC /support/configuration-backup/backups`](#docs-support-support_configuration-backup_backups)"""
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
        r"""Deletes a configuration backup.
### Related ONTAP commands
* `system configuration backup delete`

### Learn more
* [`DOC /support/configuration-backup/backups`](#docs-support-support_configuration-backup_backups)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of configuration backup files.
### Related ONTAP commands
* `system configuration backup show`

### Learn more
* [`DOC /support/configuration-backup/backups`](#docs-support-support_configuration-backup_backups)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves details of the specified configuration backup file.
### Related ONTAP commands
* `system configuration backup show`

### Learn more
* [`DOC /support/configuration-backup/backups`](#docs-support-support_configuration-backup_backups)"""
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
        r"""Creates a configuration backup. The required backup file name must end with .7z extension.
### Required properties
* `node.uuid` or `node.name` - The node UUID or node name on which the configuration backup will be created.
* `name` - The backup file name
### Related ONTAP commands
* `system configuration backup create`

### Learn more
* [`DOC /support/configuration-backup/backups`](#docs-support-support_configuration-backup_backups)"""
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
        r"""Deletes a configuration backup.
### Related ONTAP commands
* `system configuration backup delete`

### Learn more
* [`DOC /support/configuration-backup/backups`](#docs-support-support_configuration-backup_backups)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


