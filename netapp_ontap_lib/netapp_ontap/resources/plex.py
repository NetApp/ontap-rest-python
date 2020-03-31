# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
The Storage Aggregate Plex API provides relevant state information for each plex in the aggregate.
For each plex, details are provided for the RAID groups in the plex and the disks that make up each RAID group.<br>
## Examples
### Retrieving the list of plexes in an aggregate
The following example shows the response with the list of plexes in an aggregate:<br>
```
# The API:
/api/storage/aggregates/{uuid}/plexes
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/aggregates/19425837-f2fa-4a9f-8f01-712f626c983c/plexes" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "name": "plex0",
    },
    {
      "name": "plex4",
    }
  ],
  "num_records": 2,
}
```
### Retrieving a specific plex in an aggregate
The following example shows the response when requesting a specific plex of an aggregate:<br>
```
# The API:
/api/storage/aggregates/{uuid}/plexes/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/aggregates/19425837-f2fa-4a9f-8f01-712f626c983c/plexes/plex0" -H "accept: application/json"
# The response:
{
  "aggregate": {
    "uuid": "19425837-f2fa-4a9f-8f01-712f626c983c",
    "name": "test1",
  },
  "name": "plex0",
  "online": true,
  "state": "normal",
  "pool": "pool0",
  "resync": {
    "active": false
  },
  "raid_groups": [
    {
      "name": "rg0",
      "cache_tier": false,
      "degraded": false,
      "recomputing_parity": {
        "active": false
      },
      "reconstruct": {
        "active": false
      },
      "disks": [
        {
          "position": "dparity",
          "state": "normal",
          "type": "ssd",
          "usable_size": 86769664,
          "disk": {
            "name": "1.1.29",
          }
        },
        {
          "position": "parity",
          "state": "normal",
          "type": "ssd",
          "usable_size": 86769664,
          "disk": {
            "name": "1.1.4",
          }
        },
        {
          "position": "data",
          "state": "normal",
          "type": "ssd",
          "usable_size": 86769664,
          "disk": {
            "name": "1.1.30",
          }
        },
        {
          "position": "data",
          "state": "normal",
          "type": "ssd",
          "usable_size": 86769664,
          "disk": {
            "name": "1.1.5",
          }
        },
        {
          "position": "data",
          "state": "normal",
          "type": "ssd",
          "usable_size": 86769664,
          "disk": {
            "name": "1.1.31",
          }
        },
        {
          "position": "data",
          "state": "normal",
          "type": "ssd",
          "usable_size": 86769664,
          "disk": {
            "name": "1.1.6",
          }
        }
      ]
    }
  ],
}
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Plex", "PlexSchema"]
__pdoc__ = {
    "PlexSchema.resource": False,
    "PlexSchema.patchable_fields": False,
    "PlexSchema.postable_fields": False,
}


class PlexSchema(ResourceSchema):
    """The fields of the Plex object"""

    aggregate = fields.Nested("netapp_ontap.resources.aggregate.AggregateSchema", data_key="aggregate", unknown=EXCLUDE)
    r""" The aggregate field of the plex. """

    name = fields.Str(
        data_key="name",
    )
    r""" Plex name

Example: plex0 """

    online = fields.Boolean(
        data_key="online",
    )
    r""" Plex is online """

    pool = fields.Str(
        data_key="pool",
        validate=enum_validation(['pool0', 'pool1']),
    )
    r""" SyncMirror pool assignment

Valid choices:

* pool0
* pool1 """

    raid_groups = fields.List(fields.Nested("netapp_ontap.models.raid_group.RaidGroupSchema", unknown=EXCLUDE), data_key="raid_groups")
    r""" The raid_groups field of the plex. """

    resync = fields.Nested("netapp_ontap.models.plex_resync.PlexResyncSchema", data_key="resync", unknown=EXCLUDE)
    r""" The resync field of the plex. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['normal', 'failed', 'out_of_date']),
    )
    r""" Plex state

Valid choices:

* normal
* failed
* out_of_date """

    @property
    def resource(self):
        return Plex

    @property
    def patchable_fields(self):
        return [
            "aggregate.name",
            "aggregate.uuid",
            "resync",
        ]

    @property
    def postable_fields(self):
        return [
            "aggregate.name",
            "aggregate.uuid",
            "resync",
        ]

class Plex(Resource):
    """Allows interaction with Plex objects on the host"""

    _schema = PlexSchema
    _path = "/api/storage/aggregates/{aggregate[uuid]}/plexes"
    @property
    def _keys(self):
        return ["aggregate.uuid", "name"]

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
        r"""Retrieves the collection of plexes for the specified aggregate.
### Related ONTAP commands
* `storage aggregate plex show`

### Learn more
* [`DOC /storage/aggregates/{aggregate.uuid}/plexes`](#docs-storage-storage_aggregates_{aggregate.uuid}_plexes)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the collection of plexes for the specified aggregate.
### Related ONTAP commands
* `storage aggregate plex show`

### Learn more
* [`DOC /storage/aggregates/{aggregate.uuid}/plexes`](#docs-storage-storage_aggregates_{aggregate.uuid}_plexes)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the plex specified by the aggregate UUID and plex name.
### Related ONTAP commands
* `storage aggregate plex show`

### Learn more
* [`DOC /storage/aggregates/{aggregate.uuid}/plexes`](#docs-storage-storage_aggregates_{aggregate.uuid}_plexes)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





