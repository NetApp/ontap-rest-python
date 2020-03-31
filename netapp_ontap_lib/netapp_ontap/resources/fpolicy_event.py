# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
FPolicy events configurations allow you to specify which file access is monitored. As part of an FPolicy event, you can configure the SVM for which the events are generated, the name of the event configuration, the protocol (cifs, nfsv3/nfsv4) for which the events are generated, the file operations which are monitored, and filters that can be used to filter the unwanted notification generation for a specified protocol and file operation.</br>
Each protocol has a set of supported file operations and filters. An SVM can have multiple events. A single FPolicy policy can have multiple FPolicy events.
## Examples
### Creating an FPolicy event for a CIFS protocol with all the supported file operations and filters
---
```
# The API:
POST /protocols/fpolicy/{svm.uuid}/events
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/eventsreturn_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"file_operations\": { \"close\": true, \"create\": true, \"create_dir\": true, \"delete\": true, \"delete_dir\": true, \"getattr\": true, \"open\": true, \"read\": true, \"rename\": true, \"rename_dir\": true, \"setattr\": true, \"write\": true }, \"filters\": { \"close_with_modification\": true, \"close_with_read\": true, \"close_without_modification\": true, \"first_read\": true, \"first_write\": true, \"monitor_ads\": true, \"offline_bit\": true, \"open_with_delete_intent\": true, \"open_with_write_intent\": true, \"write_with_size_change\": true }, \"name\": \"event_cifs\", \"protocol\": \"cifs\", \"volume_monitoring\": true}"
# The response:
{
  "num_records": 1,
    "records": [
      {
        "name": "event_cifs",
        "protocol": "cifs",
        "volume_monitoring": true,
        "file_operations": {
          "close": true,
          "create": true,
          "create_dir": true,
          "delete": true,
          "delete_dir": true,
          "getattr": true,
          "open": true,
          "read": true,
          "write": true,
          "rename": true,
          "rename_dir": true,
          "setattr": true
        },
        "filters": {
          "monitor_ads": true,
          "close_with_modification": true,
          "close_without_modification": true,
          "close_with_read": true,
          "first_read": true,
          "first_write": true,
          "offline_bit": true,
          "open_with_delete_intent": true,
          "open_with_write_intent": true,
          "write_with_size_change": true
        }
      }
    ]
}
```
---
### Creating an FPolicy event for an NFS protocol with all the supported file operations and filters
---
```
# The API:
post /protocols/fpolicy/{svm.uuid}/events
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/eventsreturn_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"file_operations\": { \"create\": true, \"create_dir\": true, \"delete\": true, \"delete_dir\": true, \"link\": true, \"lookup\": true, \"read\": true, \"rename\": true, \"rename_dir\": true, \"setattr\": true, \"symlink\": true, \"write\": true }, \"filters\": { \"offline_bit\": true, \"write_with_size_change\": ture }, \"name\": \"event_nfsv3\", \"protocol\": \"nfsv3\", \"volume_monitoring\": false}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "name": "event_nfsv3",
      "protocol": "nfsv3",
      "volume_monitoring": false,
      "file_operations": {
        "create": true,
        "create_dir": true,
        "delete": true,
        "delete_dir": true,
        "link": true,
        "lookup": true,
        "read": true,
        "write": true,
        "rename": true,
        "rename_dir": true,
        "setattr": true,
        "symlink": true
      },
      "filters": {
      "offline_bit": true,
      "write_with_size_change": true
      }
    }
  ]
}
```
---
### Retrieving all of the FPolicy event configurations for a specified SVM
---
```
# The API:
GET /protocols/fpolicy/{svm.uuid}/events
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/events/?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "4f643fb4-fd21-11e8-ae49-0050568e2c1e"
      },
      "name": "cluster",
      "protocol": "cifs",
      "volume_monitoring": false,
      "file_operations": {
        "close": true,
        "create": false,
        "create_dir": false,
        "delete": false,
        "delete_dir": false,
        "getattr": false,
        "link": false,
        "lookup": false,
        "open": false,
        "read": false,
        "write": false,
        "rename": false,
        "rename_dir": false,
        "setattr": false,
        "symlink": false
      },
      "filters": {
        "monitor_ads": false,
        "close_with_modification": false,
        "close_without_modification": false,
        "close_with_read": true,
        "first_read": false,
        "first_write": false,
        "offline_bit": false,
        "open_with_delete_intent": false,
        "open_with_write_intent": false,
        "write_with_size_change": false,
        "setattr_with_owner_change": false,
        "setattr_with_group_change": false,
        "setattr_with_sacl_change": false,
        "setattr_with_dacl_change": false,
        "setattr_with_modify_time_change": false,
        "setattr_with_access_time_change": false,
        "setattr_with_creation_time_change": false,
        "setattr_with_mode_change": false,
        "setattr_with_size_change": false,
        "setattr_with_allocation_size_change": false,
        "exclude_directory": false
      }
    },
    {
      "svm": {
        "uuid": "4f643fb4-fd21-11e8-ae49-0050568e2c1e"
      },
      "name": "event_cifs",
      "protocol": "cifs",
      "volume_monitoring": true,
      "file_operations": {
        "close": true,
        "create": true,
        "create_dir": true,
        "delete": true,
        "delete_dir": true,
        "getattr": true,
        "link": false,
        "lookup": false,
        "open": true,
        "read": true,
        "write": true,
        "rename": true,
        "rename_dir": true,
        "setattr": true,
        "symlink": false
      },
      "filters": {
        "monitor_ads": true,
        "close_with_modification": true,
        "close_without_modification": true,
        "close_with_read": true,
        "first_read": true,
        "first_write": true,
        "offline_bit": true,
        "open_with_delete_intent": true,
        "open_with_write_intent": true,
        "write_with_size_change": true,
        "setattr_with_owner_change": false,
        "setattr_with_group_change": false,
        "setattr_with_sacl_change": false,
        "setattr_with_dacl_change": false,
        "setattr_with_modify_time_change": false,
        "setattr_with_access_time_change": false,
        "setattr_with_creation_time_change": false,
        "setattr_with_mode_change": false,
        "setattr_with_size_change": false,
        "setattr_with_allocation_size_change": false,
        "exclude_directory": false
      }
    }
  ],
  "num_records": 2
}
```
---
### Retrieving a specific FPolicy event configuration for an SVM
---
```
# The API:
GET /protocols/fpolicy/{svm.uuid}/events/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/events/event_cifs?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "4f643fb4-fd21-11e8-ae49-0050568e2c1e"
  },
  "name": "event_cifs",
  "protocol": "cifs",
  "volume_monitoring": true,
  "file_operations": {
    "close": true,
    "create": true,
    "create_dir": true,
    "delete": true,
    "delete_dir": true,
    "getattr": true,
    "link": false,
    "lookup": false,
    "open": true,
    "read": true,
    "write": true,
    "rename": true,
    "rename_dir": true,
    "setattr": true,
    "symlink": false
  },
  "filters": {
    "monitor_ads": true,
    "close_with_modification": true,
    "close_without_modification": true,
    "close_with_read": true,
    "first_read": true,
    "first_write": true,
    "offline_bit": true,
    "open_with_delete_intent": true,
    "open_with_write_intent": true,
    "write_with_size_change": true,
    "setattr_with_owner_change": false,
    "setattr_with_group_change": false,
    "setattr_with_sacl_change": false,
    "setattr_with_dacl_change": false,
    "setattr_with_modify_time_change": false,
    "setattr_with_access_time_change": false,
    "setattr_with_creation_time_change": false,
    "setattr_with_mode_change": false,
    "setattr_with_size_change": false,
    "setattr_with_allocation_size_change": false,
    "exclude_directory": false
   }
  }
 ],
 "num_records": 2
}
```
---
### Updating a specific FPolicy event configuration for a specified SVM
---
```
# The API:
PATCH /protocols/fpolicy/{svm.uuid}/events/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/events/event_cifs" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"file_operations\": { \"close\": false, \"create\": false, \"read\": true }, \"filters\": { \"close_with_modification\": false, \"close_with_read\": false, \"close_without_modification\": false }, \"protocol\": \"cifs\", \"volume_monitoring\": false}"
```
---
### Deleting a specific FPolicy event configuration for a specific SVM
---
```
# The API:
DELETE /protocols/fpolicy/{svm.uuid}/events/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/events/event_cifs" -H "accept: application/json"
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


__all__ = ["FpolicyEvent", "FpolicyEventSchema"]
__pdoc__ = {
    "FpolicyEventSchema.resource": False,
    "FpolicyEventSchema.patchable_fields": False,
    "FpolicyEventSchema.postable_fields": False,
}


class FpolicyEventSchema(ResourceSchema):
    """The fields of the FpolicyEvent object"""

    file_operations = fields.Nested("netapp_ontap.models.fpolicy_event_file_operations.FpolicyEventFileOperationsSchema", data_key="file_operations", unknown=EXCLUDE)
    r""" The file_operations field of the fpolicy_event. """

    filters = fields.Nested("netapp_ontap.models.fpolicy_event_filters.FpolicyEventFiltersSchema", data_key="filters", unknown=EXCLUDE)
    r""" The filters field of the fpolicy_event. """

    name = fields.Str(
        data_key="name",
    )
    r""" Specifies the name of the FPolicy event.

Example: event_nfs_close """

    protocol = fields.Str(
        data_key="protocol",
        validate=enum_validation(['cifs', 'nfsv3', 'nfsv4']),
    )
    r""" Protocol for which event is created. If you specify protocol, then you
must also specify a valid value for the file operation parameters.
  The value of this parameter must be one of the following:

    * cifs  - for the CIFS protocol.
    * nfsv3 - for the NFSv3 protocol.
    * nfsv4 - for the NFSv4 protocol.


Valid choices:

* cifs
* nfsv3
* nfsv4 """

    volume_monitoring = fields.Boolean(
        data_key="volume_monitoring",
    )
    r""" Specifies whether volume operation monitoring is required. """

    @property
    def resource(self):
        return FpolicyEvent

    @property
    def patchable_fields(self):
        return [
            "file_operations",
            "filters",
            "protocol",
            "volume_monitoring",
        ]

    @property
    def postable_fields(self):
        return [
            "file_operations",
            "filters",
            "name",
            "protocol",
            "volume_monitoring",
        ]

class FpolicyEvent(Resource):
    r""" The information that a FPolicy process needs to determine what file access operations to monitor and for which of the monitored events notifications should be sent to the external FPolicy server. """

    _schema = FpolicyEventSchema
    _path = "/api/protocols/fpolicy/{svm[uuid]}/events"
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
        r"""Retrieves FPolicy event configurations for all events for a specified SVM. ONTAP allows the creation of cluster-level FPolicy events that act as a template for all the data SVMs belonging to the cluster. These cluster-level FPolicy events are also retrieved for the specified SVM.
### Related ONTAP commands
* `fpolicy policy event show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/events`](#docs-NAS-protocols_fpolicy_{svm.uuid}_events)
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
        r"""Updates a specific FPolicy event configuration for an SVM. A cluster-level FPolicy event configuration cannot be modified for a data SVM through REST. When the file operations and filters fields are modified, the previous values are retained and new values are added to the list of previous values. To remove a particular file operation or filter, set its value to false in the request.
### Related ONTAP commands
* `fpolicy policy event modify`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/events`](#docs-NAS-protocols_fpolicy_{svm.uuid}_events)
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
        r"""Deletes a specific FPolicy event configuration for an SVM. A cluster-level FPolicy event configuration cannot be modified for a data SVM through REST. An FPolicy event that is attached to an FPolicy policy cannot be deleted.
### Related ONTAP commands
* `fpolicy policy event delete`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/events`](#docs-NAS-protocols_fpolicy_{svm.uuid}_events)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves FPolicy event configurations for all events for a specified SVM. ONTAP allows the creation of cluster-level FPolicy events that act as a template for all the data SVMs belonging to the cluster. These cluster-level FPolicy events are also retrieved for the specified SVM.
### Related ONTAP commands
* `fpolicy policy event show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/events`](#docs-NAS-protocols_fpolicy_{svm.uuid}_events)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific FPolicy event configuration for an SVM. A cluster-level FPolicy event configuration cannot be retrieved for a data SVM through a REST API.
### Related ONTAP commands
* `fpolicy policy event show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/events`](#docs-NAS-protocols_fpolicy_{svm.uuid}_events)
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
        r"""Creates an FPolicy event configuration for a specified SVM. FPolicy event creation is allowed only on data SVMs. When a protocol is specified, you must specify a file operation or a file operation and filters.
### Required properties
* `svm.uuid` - Existing SVM in which to create the FPolicy event.
* `name` - Name of the FPolicy event.
### Recommended optional properties
* `file-operations` - List of file operations to monitor.
* `protocol` - Protocol for which the file operations should be monitored.
* `filters` - List of filters for the specified file operations.
### Default property values
If not specified in POST, the following default property values are assigned:
* `file_operations.*` - _false_
* `filters.*` - _false_
* `volume-monitoring` - _false_
### Related ONTAP commands
* `fpolicy policy event create`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/events`](#docs-NAS-protocols_fpolicy_{svm.uuid}_events)
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
        r"""Updates a specific FPolicy event configuration for an SVM. A cluster-level FPolicy event configuration cannot be modified for a data SVM through REST. When the file operations and filters fields are modified, the previous values are retained and new values are added to the list of previous values. To remove a particular file operation or filter, set its value to false in the request.
### Related ONTAP commands
* `fpolicy policy event modify`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/events`](#docs-NAS-protocols_fpolicy_{svm.uuid}_events)
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
        r"""Deletes a specific FPolicy event configuration for an SVM. A cluster-level FPolicy event configuration cannot be modified for a data SVM through REST. An FPolicy event that is attached to an FPolicy policy cannot be deleted.
### Related ONTAP commands
* `fpolicy policy event delete`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/events`](#docs-NAS-protocols_fpolicy_{svm.uuid}_events)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


