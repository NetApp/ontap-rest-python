# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Vscan On-Demand scanning is used to check files for viruses on a schedule. For example, it can be used to run scans only in off-peak hours, or to scan very large files that are excluded from an on-access scan. Vscan On-Demand scanning can be used for any path in the SVM namespace.<p/>
Vscan On-Demand policy configurations define the scope of a Vscan On-Demand scan. The schedule parameter in the On-Demand policy configuration decides when to execute the task. Schedule can be created using the /api/clusters/schedule endpoint and can be assigned on policy create or policy modify. This API is used to retrieve and manage Vscan On-Demand policy configurations. It is also used to schedule the Vscan On-Demand scan.
## Examples
### Retrieving all fields for all policies of an SVM
---
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_demand_policies/
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/{svm.uuid}/on_demand_policies?fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "86fbc414-f140-11e8-8e22-0050568e0945",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/86fbc414-f140-11e8-8e22-0050568e0945"
          }
        }
      },
      "name": "on-demand-policy1",
      "scan_paths": [
        "/vol1/",
        "/vol2/cifs/"
      ],
      "log_path": "/vol0/report_dir",
      "schedule": {
        "uuid": "f6d0843e-f159-11e8-8e22-0050568e0945",
        "name": "schedule",
        "_links": {
          "self": {
            "href": "/api/cluster/schedules/f6d0843e-f159-11e8-8e22-0050568e0945"
          }
        }
      },
      "scope": {
        "max_file_size": 10737418240,
        "exclude_paths": [
          "/vol1/cold-files/",
          "/vol1/cifs/names"
        ],
        "include_extensions": [
          "vmdk",
          "mp*"
        ],
        "exclude_extensions": [
          "mp3",
          "mp4"
        ],
        "scan_without_extension": false
      },
      "_links": {
        "self": {
          "href": "/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies/policy1"
        }
      }
    },
    {
      "svm": {
        "uuid": "86fbc414-f140-11e8-8e22-0050568e0945",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/86fbc414-f140-11e8-8e22-0050568e0945"
          }
        }
      },
      "name": "on-demand-policy2",
      "scan_paths": [
        "/vol1/",
        "/vol2/cifs/"
      ],
      "log_path": "/report",
      "scope": {
        "max_file_size": 10737418240,
        "include_extensions": [
          "mp*"
        ],
        "scan_without_extension": true
      },
      "_links": {
        "self": {
          "href": "/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies/policy2"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies?fields=*"
    }
  }
}
```
---
### Retrieving a specific On-Demand policy associated with a specified SVM
---
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_demand_policies/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies/on-demand-task" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "86fbc414-f140-11e8-8e22-0050568e0945",
    "name": "vs1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/86fbc414-f140-11e8-8e22-0050568e0945"
      }
    }
  },
  "name": "on-demand-policy",
  "scan_paths": [
    "/vol1/cifs"
  ],
  "log_path": "/report",
  "scope": {
    "max_file_size": 10737418240,
    "include_extensions": [
      "vmdk",
      "mp*"
    ],
    "scan_without_extension": true
  },
  "_links": {
    "self": {
      "href": "/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies/policy2"
    }
  }
}
```
---
### Creating a Vscan On-Demand policy
The Vscan On-Demand policy POST endpoint creates an On-Demand policy for the specified SVM. Specify the schedule parameter to schedule an On-Demand scan.
<br/>
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_demand_policies
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"log_path\": \"/vol0/report_dir\", \"name\": \"on-demand-policy\", \"scan_paths\": [ \"/vol1/\", \"/vol2/cifs/\" ], \"schedule\": { \"name\": \"weekly\", \"uuid\": \"1cd8a442-86d1-11e0-ae1c-123478563412\" }, \"scope\": { \"exclude_extensions\": [ \"mp3\" ], \"exclude_paths\": [ \"/vol/cold-files/\" ], \"include_extensions\": [ \"vmdk\", \"mp*\" ], \"max_file_size\": 1073741824, \"scan_without_extension\": true }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "name": "vs1"
      },
      "name": "on-demand-policy",
      "scan_paths": [
        "/vol1/",
        "/vol2/cifs/"
      ],
      "log_path": "/vol0/report_dir",
      "schedule": {
        "name": "weekly"
      },
      "scope": {
        "max_file_size": 1073741824,
        "exclude_paths": [
          "/vol/cold-files/"
        ],
        "include_extensions": [
          "vmdk",
          "mp*"
        ],
        "exclude_extensions": [
          "mp3"
        ],
        "scan_without_extension": true
      }
    }
  ]
}
```
---
### Creating a Vscan On-Demand policy where a number of optional fields are not specified
---
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_demand_policies
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"log_path\": \"/report\", \"name\": \"on-demand-policy\", \"scan_paths\": [ \"/vol1/cifs/\" ], \"scope\": { \"include_extensions\": [ \"mp*\" ], \"scan_without_extension\": true }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "name": "vs1"
      },
      "name": "on-demand-policy",
      "scan_paths": [
        "vol1/cifs/"
      ],
      "log_path": "/report",
      "scope": {
        "max_file_size": 10737418240,
        "include_extensions": [
          "vmdk",
          "mp*"
        ],
        "scan_without_extension": true
      }
    }
  ]
}
```
---
### Updating a Vscan On-Demand policy
The policy being modified is identified by the UUID of the SVM and the policy name.
<br/>
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_demand_policies/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies/on-demand-policy" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"schedule\": { \"name\": \"weekly\" }, \"scope\": { \"exclude_extensions\": [ \"mp3\" ], \"exclude_paths\": [ \"/vol/\" ], \"include_extensions\": [ \"vmdk\", \"mp3\" ], \"scan_without_extension\": true }}"
```
---
### Deleting a Vscan On-Demand policy
The policy to be deleted is identified by the UUID of the SVM and the policy name.
<br/>
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_demand_policies/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_demand_policies/on-demand-policy" -H "accept: application/hal+json"
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


__all__ = ["VscanOnDemand", "VscanOnDemandSchema"]
__pdoc__ = {
    "VscanOnDemandSchema.resource": False,
    "VscanOnDemandSchema.patchable_fields": False,
    "VscanOnDemandSchema.postable_fields": False,
}


class VscanOnDemandSchema(ResourceSchema):
    """The fields of the VscanOnDemand object"""

    log_path = fields.Str(
        data_key="log_path",
    )
    r""" The path from the Vserver root where the task report is created.

Example: /vol0/report_dir """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=256),
    )
    r""" On-Demand task name

Example: task-1 """

    scan_paths = fields.List(fields.Str, data_key="scan_paths")
    r""" List of paths that need to be scanned.

Example: ["/vol1/","/vol2/cifs/"] """

    schedule = fields.Nested("netapp_ontap.resources.schedule.ScheduleSchema", data_key="schedule", unknown=EXCLUDE)
    r""" The schedule field of the vscan_on_demand. """

    scope = fields.Nested("netapp_ontap.models.vscan_on_demand_scope.VscanOnDemandScopeSchema", data_key="scope", unknown=EXCLUDE)
    r""" The scope field of the vscan_on_demand. """

    @property
    def resource(self):
        return VscanOnDemand

    @property
    def patchable_fields(self):
        return [
            "log_path",
            "scan_paths",
            "schedule.name",
            "schedule.uuid",
            "scope",
        ]

    @property
    def postable_fields(self):
        return [
            "log_path",
            "name",
            "scan_paths",
            "schedule.name",
            "schedule.uuid",
            "scope",
        ]

class VscanOnDemand(Resource):
    r""" Use On-Demand scanning to check files for viruses on a schedule. An On-Demand policy defines the scope of an On-Demand scan. """

    _schema = VscanOnDemandSchema
    _path = "/api/protocols/vscan/{svm[uuid]}/on-demand-policies"
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
        r"""Retrieves the Vscan On-Demand policy.
### Related ONTAP commands
* `vserver vscan on-demand-task show`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-demand-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-demand-policies)
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
        r"""Updates the Vscan On-Demand policy configuration of an SVM. Use schedule name or schedule UUID to schedule an On-Demand scan.
### Related ONTAP commands
* `vserver vscan on-demand-task modify`
* `vserver vscan on-demand-task schedule`
* `vserver vscan on-demand-task unschedule`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-demand-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-demand-policies)
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
        r"""Deletes the Vscan On-Demand configuration.
### Related ONTAP commands
* `vserver vscan on-demand-task delete`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-demand-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-demand-policies)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the Vscan On-Demand policy.
### Related ONTAP commands
* `vserver vscan on-demand-task show`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-demand-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-demand-policies)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the Vscan On-Demand configuration of an SVM.
### Related ONTAP commands
* `vserver vscan on-demand-task show`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-demand-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-demand-policies)
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
        r"""Creates a Vscan On-Demand policy. Created only on a data SVM.
</br> Important notes:
  * Only one policy can be scheduled at a time on an SVM. Use schedule name or schedule uuid to schedule an On-Demand policy.
  * Scanning must be enabled on the SVM before the policy is scheduled to run.
  * The exclude_extensions setting overrides the include_extensions setting. Set scan_without_extension to true to scan files without extensions.
### Required properties
* `svm.uuid` - Existing SVM in which to create the Vscan On-Demand policy.
* `name` - Name of the Vscan On-Demand policy. Maximum length is 256 characters.
* `log_path` - Path from the Vserver root where the On-Demand policy report is created.
* `scan_paths` - List of paths that need to be scanned.
### Recommended optional properties
* `schedule` - Scan schedule. It is recommended to set the schedule property, as it dictates when to scan for viruses.
### Default property values
If not specified in POST, the following default property values are assigned:
* `include_extensions` - _*_
* `max_file_size` - _10737418240_
* `scan_without_extension` - _true_
### Related ONTAP commands
* `vserver vscan on-demand-task create`
* `vserver vscan on-demand-task schedule`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-demand-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-demand-policies)
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
        r"""Updates the Vscan On-Demand policy configuration of an SVM. Use schedule name or schedule UUID to schedule an On-Demand scan.
### Related ONTAP commands
* `vserver vscan on-demand-task modify`
* `vserver vscan on-demand-task schedule`
* `vserver vscan on-demand-task unschedule`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-demand-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-demand-policies)
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
        r"""Deletes the Vscan On-Demand configuration.
### Related ONTAP commands
* `vserver vscan on-demand-task delete`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-demand-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-demand-policies)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


