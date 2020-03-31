# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Use Vscan On-Access scanning to actively scan file objects for viruses when clients access files over SMB. To control which file operations trigger a vscan, use Vscan File-Operations Profile (vscan-fileop-profile) option in the CIFS share. The Vscan On-Access policy configuration defines the scope and status of On-Access scanning on file objects. Use this API to retrieve and manage Vscan On-Access policy configurations and Vscan On-Access policy statuses for the SVM.
## Examples
### Retrieving all fields for all policies of an SVM
---
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_access_policies/
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/{svm.uuid}/on_access_policies?fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "179d3c85-7053-11e8-b9b8-005056b41bd1",
        "name": "vs1"
        "_links": {
          "self": {
            "href": "/api/svm/svms/179d3c85-7053-11e8-b9b8-005056b41bd1"
          }
        }
      },
      "name": "default_CIFS",
      "enabled": true,
      "mandatory": true,
      "scope": {
        "max_file_size": 2147483648,
        "include_extensions": [
          "*"
        ],
        "scan_without_extension": true,
        "scan_readonly_volumes": false,
        "only_execute_access": false
      },
      "_links": {
        "self": {
          "href": "/api/protocols/vscan/179d3c85-7053-11e8-b9b8-005056b41bd1/on_access_policies/default_CIFS"
        }
      }
    },
    {
      "svm": {
        "uuid": "179d3c85-7053-11e8-b9b8-005056b41bd1",
        "name": "vs1"
        "_links": {
          "self": {
            "href": "/api/svm/svms/179d3c85-7053-11e8-b9b8-005056b41bd1"
          }
        }
      },
      "name": "on-access-policy",
      "enabled": false,
      "mandatory": true,
      "scope": {
        "max_file_size": 3221225472,
        "exclude_paths": [
          "\\vol\\a b\\",
          "\\vol\\a,b\\"
        ],
        "include_extensions": [
          "mp*",
          "tx*"
        ],
        "exclude_extensions": [
          "mp3",
          "txt"
        ],
        "scan_without_extension": true,
        "scan_readonly_volumes": false,
        "only_execute_access": true
      }
      "_links": {
        "self": {
          "href": "/api/protocols/vscan/179d3c85-7053-11e8-b9b8-005056b41bd1/on_access_policies/on-access-policy"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/vscan/179d3c85-7053-11e8-b9b8-005056b41bd1/on_access_policies?fields=*"
    }
  }
}
```
---
### Retrieving the specific On-Access policy associated with the specified SVM
---
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_access_policies/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/179d3c85-7053-11e8-b9b8-005056b41bd1/on_access_policies/on-access-policy" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "179d3c85-7053-11e8-b9b8-005056b41bd1",
    "name": "vs1"
    "_links": {
      "self": {
        "href": "/api/svm/svms/179d3c85-7053-11e8-b9b8-005056b41bd1"
      }
    }
  },
  "name": "on-access-policy",
  "enabled": true,
  "mandatory": true,
  "scope": {
    "max_file_size": 3221225472,
    "exclude_paths": [
      "\\vol\\a b\\",
      "\\vol\\a,b\\"
    ],
    "include_extensions": [
      "mp*",
      "tx*"
    ],
    "exclude_extensions": [
      "mp3",
      "txt"
    ],
    "scan_without_extension": true,
    "scan_readonly_volumes": false,
    "only_execute_access": true
  }
  "_links": {
    "self": {
      "href": "/api/protocols/vscan/179d3c85-7053-11e8-b9b8-005056b41bd1/on_access_policies/task1"
    }
  }
}
```
---
### Creating a Vscan On-Access policy
The Vscan On-Access policy POST endpoint creates an On-Access policy for the specified SVM. Set enabled to "true" to enable scanning on the created policy.
<br/>
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_access_policies
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_access_policies?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": false, \"mandatory\": true, \"name\": \"on-access-policy\", \"scope\": { \"exclude_extensions\": [ \"txt\", \"mp3\" ], \"exclude_paths\": [ \"\\\\dir1\\\\dir2\\\\ame\", \"\\\\vol\\\\a b\" ], \"include_extensions\": [  \"mp*\", \"txt\" ], \"max_file_size\": 3221225472, \"only_execute_access\": true, \"scan_readonly_volumes\": false, \"scan_without_extension\": true }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "name": "vs1"
      },
      "name": "on-access-policy",
      "enabled": false,
      "mandatory": true,
      "scope": {
        "max_file_size": 3221225472,
        "exclude_paths": [
          "\\dir1\\dir2\\ame",
          "\\vol\\a b"
        ],
        "include_extensions": [
          "mp*",
          "txt"
        ],
        "exclude_extensions": [
          "txt",
          "mp3"
        ],
        "scan_without_extension": true,
        "scan_readonly_volumes": false,
        "only_execute_access": true
      }
    }
  ]
}
```
---
### Creating a Vscan On-Access policy where a number of optional fields are not specified
---
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_access_policies
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_access_policies?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": false, \"mandatory\": true, \"name\": \"on-access-policy\", \"scope\": { \"exclude_paths\": [ \"\\\\vol\\\\a b\", \"\\\\vol\\\\a,b\\\\\" ], \"max_file_size\": 1073741824, \"scan_without_extension\": true }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "name": "vs1"
      },
      "name": "on-access-policy",
      "enabled": false,
      "mandatory": true,
      "scope": {
        "max_file_size": 1073741824,
        "exclude_paths": [
          "\\vol\\a b",
          "\\vol\\a,b\\"
        ],
        "scan_without_extension": true
      }
    }
  ]
}
```
---
### Updating a Vscan On-Access policy
The policy being modified is identified by the UUID of the SVM and the policy name.
<br/>
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_access_policies/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_access_policies/on-access-policy" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"scope\": { \"include_extensions\": [ \"txt\" ], \"only_execute_access\": true, \"scan_readonly_volumes\": false, \"scan_without_extension\": true }}"
```
---
### Deleting a Vscan On-Access policy
The policy to be deleted is identified by the UUID of the SVM and the policy name.
<br/>
```
# The API:
/api/protocols/vscan/{svm.uuid}/on_access_policies/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/vscan/86fbc414-f140-11e8-8e22-0050568e0945/on_access_policies/on-access-policy" -H "accept: application/hal+json"
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


__all__ = ["VscanOnAccess", "VscanOnAccessSchema"]
__pdoc__ = {
    "VscanOnAccessSchema.resource": False,
    "VscanOnAccessSchema.patchable_fields": False,
    "VscanOnAccessSchema.postable_fields": False,
}


class VscanOnAccessSchema(ResourceSchema):
    """The fields of the VscanOnAccess object"""

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Status of the On-Access Vscan policy """

    mandatory = fields.Boolean(
        data_key="mandatory",
    )
    r""" Specifies if scanning is mandatory. File access is denied if there are no external virus-scanning servers available for virus scanning. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=256),
    )
    r""" On-Access policy ame

Example: on-access-test """

    scope = fields.Nested("netapp_ontap.models.vscan_on_access_scope.VscanOnAccessScopeSchema", data_key="scope", unknown=EXCLUDE)
    r""" The scope field of the vscan_on_access. """

    @property
    def resource(self):
        return VscanOnAccess

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "mandatory",
            "scope",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "mandatory",
            "name",
            "scope",
        ]

class VscanOnAccess(Resource):
    r""" An On-Access policy that defines the scope of an On-Access scan. Use On-Access scanning to check for viruses when clients open, read, rename, or close files over CIFS. By default, ONTAP creates an On-Access policy named "default_CIFS" and enables it for all the SVMs in a cluster. """

    _schema = VscanOnAccessSchema
    _path = "/api/protocols/vscan/{svm[uuid]}/on-access-policies"
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
        r"""Retrieves the Vscan On-Access policy.
### Related ONTAP commands
* `vserver vscan on-access-policy show`
* `vserver vscan on-access-policy file-ext-to-include show`
* `vserver vscan on-access-policy file-ext-to-exclude show`
* `vserver vscan on-access-policy paths-to-exclude show`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-access-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-access-policies)
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
        r"""Updates the Vscan On-Access policy configuration and/or enables/disables the Vscan On-Access policy of an SVM. You cannot modify the configurations for an On-Access policy associated with an administrative SVM, although you can encable and disable the policy associated with an administrative SVM.
### Related ONTAP commands
* `vserver vscan on-access-policy modify`
* `vserver vscan on-access-policy enable`
* `vserver vscan on-access-policy disable`
* `vserver vscan on-access-policy file-ext-to-include add`
* `vserver vscan on-access-policy file-ext-to-exclude add`
* `vserver vscan on-access-policy paths-to-exclude add`
* `vserver vscan on-access-policy file-ext-to-include remove`
* `vserver vscan on-access-policy file-ext-to-exclude remove`
* `vserver vscan on-access-policy paths-to-exclude remove`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-access-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-access-policies)
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
        r"""Deletes the anti-virus On-Access policy configuration.
### Related ONTAP commands
* `vserver vscan on-access-policy delete`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-access-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-access-policies)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the Vscan On-Access policy.
### Related ONTAP commands
* `vserver vscan on-access-policy show`
* `vserver vscan on-access-policy file-ext-to-include show`
* `vserver vscan on-access-policy file-ext-to-exclude show`
* `vserver vscan on-access-policy paths-to-exclude show`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-access-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-access-policies)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the Vscan On-Access policy configuration of an SVM.
### Related ONTAP commands
* `vserver vscan on-access-policy show`
* `vserver vscan on-access-policy file-ext-to-include show`
* `vserver vscan on-access-policy file-ext-to-exclude show`
* `vserver vscan on-access-policy paths-to-exclude show`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-access-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-access-policies)
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
        r"""Creates a Vscan On-Access policy. Created only on a data SVM.
</b>Important notes:
* You must enable the policy on an SVM before its files can be scanned.
* You can enable only one On-Access policy at a time on an SVM. By default, the policy is enabled on creation. * If the Vscan On-Access policy has been created successfully on an SVM but cannot be enabled due to an error, the Vscan On-Access policy configurations are saved. The Vscan On-Access policy is then enabled using the PATCH operation.
### Required properties
* `svm.uuid` - Existing SVM in which to create the Vscan On-Access policy.
* `name` - Name of the Vscan On-Access policy. Maximum length is 256 characters.
### Default property values
If not specified in POST, the following default property values are assigned:
* `enabled` - _true_
* `mandatory` - _true_
* `include_extensions` - _*_
* `max_file_size` - _2147483648_
* `only_execute_access` - _false_
* `scan_readonly_volumes` - _false_
* `scan_without_extension` - _true_
### Related ONTAP commands
* `vserver vscan on-access-policy create`
* `vserver vscan on-access-policy enable`
* `vserver vscan on-access-policy disable`
* `vserver vscan on-access-policy file-ext-to-include add`
* `vserver vscan on-access-policy file-ext-to-exclude add`
* `vserver vscan on-access-policy paths-to-exclude add`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-access-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-access-policies)
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
        r"""Updates the Vscan On-Access policy configuration and/or enables/disables the Vscan On-Access policy of an SVM. You cannot modify the configurations for an On-Access policy associated with an administrative SVM, although you can encable and disable the policy associated with an administrative SVM.
### Related ONTAP commands
* `vserver vscan on-access-policy modify`
* `vserver vscan on-access-policy enable`
* `vserver vscan on-access-policy disable`
* `vserver vscan on-access-policy file-ext-to-include add`
* `vserver vscan on-access-policy file-ext-to-exclude add`
* `vserver vscan on-access-policy paths-to-exclude add`
* `vserver vscan on-access-policy file-ext-to-include remove`
* `vserver vscan on-access-policy file-ext-to-exclude remove`
* `vserver vscan on-access-policy paths-to-exclude remove`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-access-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-access-policies)
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
        r"""Deletes the anti-virus On-Access policy configuration.
### Related ONTAP commands
* `vserver vscan on-access-policy delete`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/on-access-policies`](#docs-NAS-protocols_vscan_{svm.uuid}_on-access-policies)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


