# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
FPolicy is an infrastructure component of ONTAP that enables partner applications to connect to ONTAP in order to monitor and set file access permissions. Every time a client accesses a file from a storage system, based on the configuration of FPolicy, the partner application is notified about file access. This enables partners to set restrictions on files that are created or accessed on the storage system. FPolicy also allows you to create file policies that specify file operation permissions according to file type. For example, you can restrict certain file types, such as .jpeg and .mp3 files, from being stored on the storage system. FPolicy can monitor file access from CIFS and NFS clients.</br>
As part of FPolicy configuration, you can specify an FPolicy engine which defines the external FPolicy server, FPolicy events, which defines the protocol and file operations to monitor and the FPolicy policy that acts as a container for the FPolicy engine and FPolicy events. It provides a way for policy management functions, such as policy enabling and disabling.
## Examples
### Creating an FPolicy configuration
To create an FPolicy for an SVM use the following API. Note that the <i>return_records=true</i> query parameter is used to obtain the newly created entry in the response.
```
# The API:
POST /protocols/fpolicy/
#The call:
curl -X POST "https://<mgmt-ip>/api/protocols/fpolicy?return_records=tre" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"engines\": [ { \"name\": \"engine1\", \"port\": 9876, \"primary_servers\": [ \"10.132.145.22\", \"10.140.101.109\" ], \"secondary_servers\": [ \"10.132.145.20\", \"10.132.145.21\" ], \"type\": \"synchronous\" } ], \"events\": [ { \"file_operations\": { \"read\": true, \"write\": true }, \"filters\": { \"monitor_ads\": true }, \"name\": \"event_cifs\", \"protocol\": \"cifs\", \"volume_monitoring\": true } ], \"policies\": [ { \"engine\": { \"name\": \"engine1\" }, \"events\": [ \"event_cifs\" ], \"mandatory\": true, \"name\": \"pol0\", \"priority\": 1, \"scope\": { \"include_volumes\": [ \"vol1\" ] } } ], \"svm\": { \"name\": \"vs1\", \"uuid\": \"b34f5e3d-01d0-11e9-8f63-0050568ea311\" }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311",
        "name": "vs1"
      },
      "engines": [
        {
          "name": "engine1",
          "primary_servers": [
            "10.132.145.22",
            "10.140.101.109"
          ],
          "secondary_servers": [
            "10.132.145.20",
            "10.132.145.21"
          ],
          "type": "synchronous",
          "port": 9876
        }
      ],
        "events": [
        {
          "name": "event_cifs",
          "protocol": "cifs",
          "volume_monitoring": true,
          "file_operations": {
            "read": true,
            "write": true
          },
          "filters": {
            "monitor_ads": true
          }
        }
      ],
      "policies": [
        {
          "name": "pol0",
          "priority": 1,
          "events": [
            {
              "name": "event_cifs"
            }
          ],
          "engine": {
            "name": "engine1"
          },
          "scope": {
            "include_volumes": [
              "vol1"
            ]
          },
          "mandatory": true
        }
      ]
    }
  ]
}
```
---
### Retrieving the FPolicy configuration for all the SVMs in the cluster
---
```
# The API:
GET /protocols/fpolicy
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311",
        "name": "vs1"
      },
      "engines": [
        {
          "name": "engine1",
          "primary_servers": [
            "10.132.145.22",
            "10.140.101.109"
          ],
          "secondary_servers": [
            "10.132.145.20",
            "10.132.145.21"
          ],
          "type": "synchronous",
          "port": 9876
        }
      ],
      "events": [
        {
          "name": "event_cifs",
          "protocol": "cifs",
          "volume_monitoring": true,
          "file_operations": {
            "close": false,
            "create": false,
            "create_dir": false,
            "delete": false,
            "delete_dir": false,
            "getattr": false,
            "link": false,
            "lookup": false,
            "open": false,
            "read": true,
            "write": true,
            "rename": false,
            "rename_dir": false,
            "setattr": false,
            "symlink": false
          },
          "filters": {
            "monitor_ads": true,
            "close_with_modification": false,
            "close_without_modification": false,
            "close_with_read": false,
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
        }
      ],
      "policies": [
        {
          "name": "pol0",
          "enabled": true,
          "priority": 1,
          "events": [
            {
              "name": "event_cifs"
            }
          ],
          "engine": {
            "name": "engine1"
          },
          "scope": {
            "include_volumes": [
              "vol1"
            ]
          },
          "mandatory": true
        }
      ]
    }
  ],
  "num_records": 1
}
```
---
### Retrieving an FPolicy configuration for a particular SVM
---
```
# The API:
GET /protocols/fpolicy/{svm.uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy/b34f5e3d-01d0-11e9-8f63-0050568ea311?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311",
    "name": "vs1"
  },
  "engines": [
    {
      "name": "engine1",
      "primary_servers": [
        "10.132.145.22",
        "10.140.101.109"
      ],
      "secondary_servers": [
        "10.132.145.20",
        "10.132.145.21"
      ],
      "type": "synchronous",
      "port": 9876
    }
  ],
  "events": [
    {
      "name": "event_cifs",
      "protocol": "cifs",
      "volume_monitoring": true,
      "file_operations": {
        "close": false,
        "create": false,
        "create_dir": false,
        "delete": false,
        "delete_dir": false,
        "getattr": false,
        "link": false,
        "lookup": false,
        "open": false,
        "read": true,
        "write": true,
        "rename": false,
        "rename_dir": false,
        "setattr": false,
        "symlink": false
      },
      "filters": {
        "monitor_ads": true,
        "close_with_modification": false,
        "close_without_modification": false,
        "close_with_read": false,
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
    }
  ],
  "policies": [
    {
      "name": "pol0",
      "enabled": true,
      "priority": 1,
      "events": [
        {
          "name": "event_cifs"
        }
      ],
      "engine": {
        "name": "engine1"
      },
      "scope": {
        "include_volumes": [
          "vol1"
        ]
      },
      "mandatory": true
    }
  ]
}
```
---
### Deleting an FPolicy configuration for a particular SVM
---
```
# The API:
DELETE /protocols/fpolicy/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/fpolicy/b34f5e3d-01d0-11e9-8f63-0050568ea311" -H "accept: application/json"
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


__all__ = ["Fpolicy", "FpolicySchema"]
__pdoc__ = {
    "FpolicySchema.resource": False,
    "FpolicySchema.patchable_fields": False,
    "FpolicySchema.postable_fields": False,
}


class FpolicySchema(ResourceSchema):
    """The fields of the Fpolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the fpolicy. """

    engines = fields.List(fields.Nested("netapp_ontap.resources.fpolicy_engine.FpolicyEngineSchema", unknown=EXCLUDE), data_key="engines")
    r""" The engines field of the fpolicy. """

    events = fields.List(fields.Nested("netapp_ontap.resources.fpolicy_event.FpolicyEventSchema", unknown=EXCLUDE), data_key="events")
    r""" The events field of the fpolicy. """

    policies = fields.List(fields.Nested("netapp_ontap.resources.fpolicy_policy.FpolicyPolicySchema", unknown=EXCLUDE), data_key="policies")
    r""" The policies field of the fpolicy. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the fpolicy. """

    @property
    def resource(self):
        return Fpolicy

    @property
    def patchable_fields(self):
        return [
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "engines",
            "events",
            "policies",
            "svm.name",
            "svm.uuid",
        ]

class Fpolicy(Resource):
    r""" FPolicy is an infrastructure component of ONTAP that enables partner applications connected to your storage systems to monitor and set file access permissions. Every time a client accesses a file from a storage system, based on the configuration of FPolicy, the partner application is notified about file access. """

    _schema = FpolicySchema
    _path = "/api/protocols/fpolicy"
    @property
    def _keys(self):
        return ["svm.uuid"]

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
        r"""Retrieves an FPolicy configuration.
### Related ONTAP commands
* `fpolicy show`
* `fpolicy policy show`
* `fpolicy policy scope show`
* `fpolicy policy event show`
* `fpolicy policy external-engine show`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
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
        r"""Deletes the FPolicy configuration for the specified SVM. Before deleting the FPolicy configuration, ensure that all policies belonging to the SVM are disabled.
### Related ONTAP commands
* `fpolicy delete`
* `fpolicy policy scope delete`
* `fpolicy policy delete`
* `fpolicy policy event delete`
* `fpolicy policy external-engine delete`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves an FPolicy configuration.
### Related ONTAP commands
* `fpolicy show`
* `fpolicy policy show`
* `fpolicy policy scope show`
* `fpolicy policy event show`
* `fpolicy policy external-engine show`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an FPolicy configuration of an SVM.
### Related ONTAP commands
* `fpolicy show`
* `fpolicy policy show`
* `fpolicy policy scope show`
* `fpolicy policy event show`
* `fpolicy policy external-engine show`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
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
        r"""Creates an FPolicy configuration.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the FPolicy configuration.
### Recommended optional properties
* `engines` -  External server to which the notifications will be sent.
* `events` - File operations to monitor.
* `policies` - Policy configuration which acts as a container for FPolicy event and FPolicy engine.
* `scope` - Scope of the policy. Can be limited to exports, volumes, shares or file extensions.
### Default property values
If not specified in POST, the following default property values are assigned:
* `engines.type` - _synchronous_
* `policies.engine` - _native_
* `policies.mandatory` -  _true_
* `events.volume_monitoring` - _false_
* `events.file_operations.*` - _false_
* `events.filters.*` - _false_
### Related ONTAP commands
* `fpolicy policy event create`
* `fpolicy policy external-engine create`
* `fpolicy policy create`
* `fpolicy policy scope create`
* `fpolicy enable`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
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
        r"""Deletes the FPolicy configuration for the specified SVM. Before deleting the FPolicy configuration, ensure that all policies belonging to the SVM are disabled.
### Related ONTAP commands
* `fpolicy delete`
* `fpolicy policy scope delete`
* `fpolicy policy delete`
* `fpolicy policy event delete`
* `fpolicy policy external-engine delete`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


