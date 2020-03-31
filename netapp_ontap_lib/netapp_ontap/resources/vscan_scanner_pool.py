# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
A scanner-pool defines the Vscan servers and privileged users that can connect to SVMs and a scanner policy or role determines whether a scanner-pool is active. You can configure a scanner-pool to be used on the local cluster or any other cluster in an MCC/DR setup.
## Examples
### Retrieving all fields for all scanner-pools of an SVM
```
# The API:
/api/protocols/vscan/{svm.uuid}/scanner-pools
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/<svm-uuid>/scanner-pools?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "0e2f7c91-f227-11e8-9601-0050568ecc06"
      },
      "name": "scanner-1",
      "servers": [
        "1.1.1.1",
        "10.72.204.27"
      ],
      "privileged_users": [
        "cifs\\u1",
        "cifs\\u2"
      ],
      "role": "primary"
    },
    {
      "svm": {
        "uuid": "0e2f7c91-f227-11e8-9601-0050568ecc06"
      },
      "name": "scanner-2",
      "servers": [
        "1.1.1.1",
        "10.72.204.27"
      ],
      "privileged_users": [
        "cifs\\u1",
        "cifs\\u2"
      ],
      "role": "secondary"
    }
  ],
  "num_records": 2
}
```
### Retrieving all scanner-pools with *role* set as *secondary*
```
# The API:
/api/protocols/vscan/{svm.uuid}/scanner-pools
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/<svm-uuid>/scanner-pools?role=secondary&fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "0e2f7c91-f227-11e8-9601-0050568ecc06",
        "name": "vs1"
      },
      "name": "scanner-2",
      "servers": [
        "1.1.1.1",
        "10.72.204.27"
      ],
      "privileged_users": [
        "cifs\\u1",
        "cifs\\u2"
      ],
      "role": "secondary",
      "cluster": {
        "uuid": "0933f9b5-f226-11e8-9601-0050568ecc06",
        "name": "Cluster3"
      }
    }
  ],
  "num_records": 1
}
```
### Retrieving the specified scanner-pool associated with an SVM
```
# The API:
/api/protocols/vscan/{svm.uuid}/scanner-pools/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/0e2f7c91-f227-11e8-9601-0050568ecc06/scanner-pools/scanner-1?fields=*" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "0e2f7c91-f227-11e8-9601-0050568ecc06",
    "name": "vs1"
  },
  "name": "scanner-1",
  "servers": [
    "1.1.1.1",
    "10.72.204.27"
  ],
  "privileged_users": [
    "cifs\\u1",
    "cifs\\u2"
  ],
  "role": "primary",
  "cluster": {
    "uuid": "0933f9b5-f226-11e8-9601-0050568ecc06",
    "name": "Cluster3"
  }
}
```
### Creating a scanner-pool for an SVM with all fields specified
```
# The API:
/api/protocols/vscan/{svm.uuid}/scanner-pools/
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan/b103be27-17b8-11e9-b451-0050568ecd85/scanner-pools?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"cluster\": { \"name\": \"Cluster1\", \"uuid\": \"ab746d77-17b7-11e9-b450-0050568ecd85\" }, \"name\": \"test-scanner\", \"privileged_users\": [ \"cifs\\\\u1\", \"cifs\\\\u2\" ], \"role\": \"primary\", \"servers\": [ \"1.1.1.1\", \"10.72.204.27\" ]}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "name": "test-scanner",
      "servers": [
        "1.1.1.1",
        "10.72.204.27"
      ],
      "privileged_users": [
        "cifs\\u1",
        "cifs\\u2"
      ],
      "role": "primary",
      "cluster": {
        "uuid": "ab746d77-17b7-11e9-b450-0050568ecd85",
        "name": "Cluster1"
      }
    }
  ]
}
```
### Creating a scanner-pool for an SVM with an unspecified role and cluster
```
# The API:
/api/protocols/vscan/{svm.uuid}/scanner-pools/
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan/b103be27-17b8-11e9-b451-0050568ecd85/scanner-pools" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"name\": \"test-scanner-1\", \"privileged_users\": [ \"cifs\\\\u1\", \"cifs\\\\u2\" ], \"servers\": [ \"1.1.1.1\", \"10.72.204.27\" ]}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "name": "test-scanner-1",
      "servers": [
        "1.1.1.1",
        "10.72.204.27"
      ],
      "privileged_users": [
        "cifs\\u1",
        "cifs\\u2"
      ]
    }
  ]
}
```
### Updating a scanner-pool for an SVM with all of the fields specified
```
# The API:
/api/protocols/vscan/{svm.uuid}/scanner-pools/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/vscan/0e2f7c91-f227-11e8-9601-0050568ecc06/scanner-pools/test-scanner-1" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"cluster\": { \"name\": \"Cluster3\", \"uuid\": \"0933f9b5-f226-11e8-9601-0050568ecc06\" }, \"privileged_users\": [ \"cifs\\\\u1\", \"cifs\\\\u2\" ], \"role\": \"secondary\", \"servers\": [ \"1.1.1.1\", \"10.72.204.27\" ]}"
```
### Updating the "role" of a scanner-pool for an SVM
```
# The API:
/api/protocols/vscan/{svm.uuid}/scanner-pools/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/vscan/0e2f7c91-f227-11e8-9601-0050568ecc06/scanner-pools/test-scanner-1" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"cluster\": { \"name\": \"Cluster3\", \"uuid\": \"0933f9b5-f226-11e8-9601-0050568ecc06\" }, \"role\": \"primary\"}"
```
### Deleting a scanner-pool for a specified SVM
```
# The API:
/api/protocols/vscan/{svm.uuid}/scanner-pools/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/vscan/0e2f7c91-f227-11e8-9601-0050568ecc06/scanner-pools/test-scanner-1" -H "accept: application/json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["VscanScannerPool", "VscanScannerPoolSchema"]
__pdoc__ = {
    "VscanScannerPoolSchema.resource": False,
    "VscanScannerPoolSchema.patchable_fields": False,
    "VscanScannerPoolSchema.postable_fields": False,
}


class VscanScannerPoolSchema(ResourceSchema):
    """The fields of the VscanScannerPool object"""

    cluster = fields.Nested("netapp_ontap.resources.cluster.ClusterSchema", data_key="cluster", unknown=EXCLUDE)
    r""" The cluster field of the vscan_scanner_pool. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=256),
    )
    r""" Specifies the name of the scanner pool. Scanner pool name can be up to 256 characters long and is a string that can only contain any combination of ASCII-range alphanumeric characters a-z, A-Z, 0-9), "_", "-" and ".".

Example: scanner-1 """

    privileged_users = fields.List(fields.Str, data_key="privileged_users")
    r""" Specifies a list of privileged users. A valid form of privileged user-name is "domain-name\user-name". Privileged user-names are stored and treated as case-insensitive strings. Virus scanners must use one of the registered privileged users for connecting to clustered Data ONTAP for exchanging virus-scanning protocol messages and to access file for scanning, remedying and quarantining operations.

Example: ["cifs\\u1","cifs\\u2"] """

    role = fields.Str(
        data_key="role",
        validate=enum_validation(['primary', 'secondary', 'idle']),
    )
    r""" Specifies the role of the scanner pool. The possible values are:

  * primary   - Always active.
  * secondary - Active only when none of the primary external virus-scanning servers are connected.
  * idle      - Always inactive.


Valid choices:

* primary
* secondary
* idle """

    servers = fields.List(fields.Str, data_key="servers")
    r""" Specifies a list of IP addresses or FQDN for each Vscan server host names which are allowed to connect to clustered ONTAP.

Example: ["1.1.1.1","10.72.204.27","vmwin204-27.fsct.nb"] """

    @property
    def resource(self):
        return VscanScannerPool

    @property
    def patchable_fields(self):
        return [
            "cluster.name",
            "cluster.uuid",
            "privileged_users",
            "role",
            "servers",
        ]

    @property
    def postable_fields(self):
        return [
            "cluster.name",
            "cluster.uuid",
            "name",
            "privileged_users",
            "role",
            "servers",
        ]

class VscanScannerPool(Resource):
    r""" Scanner pool is a set of attributes which are used to validate and manage connections between clustered ONTAP and external virus-scanning server, or "Vscan server". """

    _schema = VscanScannerPoolSchema
    _path = "/api/protocols/vscan/{svm[uuid]}/scanner-pools"
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
        r"""Retrieves the Vscan scanner-pool configuration of an SVM.
### Related ONTAP commands
* `vserver vscan scanner-pool show`
* `vserver vscan scanner-pool privileged-users show`
* `vserver vscan scanner-pool servers show`
* `vserver vscan scanner-pool show-active`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Updates the Vscan scanner-pool configuration of an SVM.<br/>
Important notes:
* Along with servers and privileged-users, the role of a scanner-pool can also be updated with the cluster on which a scanner-pool is allowed.
* If role is specified and cluster isn't, then role is applied to the local cluster.
### Related ONTAP commands
* `vserver vscan scanner-pool modify`
* `vserver vscan scanner-pool apply-policy`
* `vserver vscan scanner-pool privileged-users add`
* `vserver vscan scanner-pool privileged-users remove`
* `vserver vscan scanner-pool servers remove`
* `vserver vscan scanner-pool servers add`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Deletes a Vscan scanner-pool configuration.<br/>
Important notes:
* The Vscan scanner-pool DELETE endpoint deletes all of the Vscan scanner-pools for a specified SVM.
* If a Vscan is enabled, it requires at least one scanner-pool to be in the active state. Therefore, disable Vscan on the specified SVM so all the scanner-pools configured on that SVM can be deleted.
### Related ONTAP commands
* `vserver vscan scanner-pool delete`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the Vscan scanner-pool configuration of an SVM.
### Related ONTAP commands
* `vserver vscan scanner-pool show`
* `vserver vscan scanner-pool privileged-users show`
* `vserver vscan scanner-pool servers show`
* `vserver vscan scanner-pool show-active`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the configuration of a specified scanner-pool of an SVM.
### Related ONTAP commands
* `vserver vscan scanner-pool show`
* `vserver vscan scanner-pool privileged-users show`
* `vserver vscan scanner-pool servers show`
* `vserver vscan scanner-pool show-active`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Creates a Vscan scanner-pool configuration for a specified SVM. You can create a scanner-pool with all fields specified or only mandatory fields specified.<br/>
Important notes:
* A scanner-pool must have servers and privileged users specified.
* If the role or cluster is not specified, the scanner-pool is created on the local cluster with the role set as primary.
*`Only one of the fields cluster-uuid or cluster-name is required.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the Vscan configuration.
* `name` - Scanner-pool name.
* `privileged_users` - List of privileged users.
* `servers` - List of server IP addresses or FQDNs.
### Recommended optional properties
* `role` - Setting a role for a scanner-pool is recommended.
* `cluster` - Passing the cluster name or UUID (or both) in a multi-cluster environment is recommended.
### Default property values
If not specified in POST, the following default property values are assigned:
* `role` - _primary_
* `cluster.name` - Local cluster name.
* `cluster.uuid` - Local cluster UUID.
### Related ONTAP commands
* `vserver vscan scanner-pool create`
* `vserver vscan scanner-pool apply-policy`
* `vserver vscan scanner-pool privileged-users add`
* `vserver vscan scanner-pool servers add`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Updates the Vscan scanner-pool configuration of an SVM.<br/>
Important notes:
* Along with servers and privileged-users, the role of a scanner-pool can also be updated with the cluster on which a scanner-pool is allowed.
* If role is specified and cluster isn't, then role is applied to the local cluster.
### Related ONTAP commands
* `vserver vscan scanner-pool modify`
* `vserver vscan scanner-pool apply-policy`
* `vserver vscan scanner-pool privileged-users add`
* `vserver vscan scanner-pool privileged-users remove`
* `vserver vscan scanner-pool servers remove`
* `vserver vscan scanner-pool servers add`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Deletes a Vscan scanner-pool configuration.<br/>
Important notes:
* The Vscan scanner-pool DELETE endpoint deletes all of the Vscan scanner-pools for a specified SVM.
* If a Vscan is enabled, it requires at least one scanner-pool to be in the active state. Therefore, disable Vscan on the specified SVM so all the scanner-pools configured on that SVM can be deleted.
### Related ONTAP commands
* `vserver vscan scanner-pool delete`
### Learn more
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


