# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
In ONTAP, scheduled Snapshot copy creation works based on Snapshot copy policies.
ONTAP provides three cluster-wide Snapshot copy policies: "default", "default-1weekly" and "none".
A Snapshot copy policy can have more than one schedule associated with it.
A Snapshot copy policy can be linked to a storage object and based on the schedule in the policy, Snapshot copies will be created on the object at that interval.
Each schedule in a Snapshot copy policy has a Snapshot copy name prefix attached to it. Every Snapshot copy created using this policy will have this prefix in its name.
There is also a retention count associated with every schedule. This count indicates the maximum number of Snapshot copies that can exist for a given schedule. Once the Snapshot copy count reaches the retention count, on the next create operation, the oldest Snapshot copy is deleted.<br/>
## Snapshot copy policy APIs
The following APIs are used to perform operations related to Snapshot copy policy information:

* POST      /api/storage/snapshot_policies
* GET       /api/storage/snapshot_policies
* GET       /api/storage/snapshot_policies/{uuid}
* PATCH     /api/storage/snapshot_policies/{uuid}
* DELETE    /api/storage/snapshot_policies/{uuid}
## Examples
### Creating a Snapshot copy policy
The POST operation is used to create a Snapshot copy policy with the specified attributes.
```
# The API:
/api/storage/snapshot_policies
# The call:
curl -X POST  "https://<mgmt-ip>/api/storage/snapshot_policies" -H "accept: application/hal+json" -d '{"name": "new_policy", "enabled": "true", "comment": "policy comment", "copies": [{ "schedule": { "name": "5min" }, "count": "5", "prefix": "xyz" }], "svm": { "name": "vs0"}}'
# The response:
HTTP/1.1 201 Created
Date: Tue, 12 Mar 2019 21:20:24 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/storage/snapshot_policies/a69d8173-450c-11e9-aa44-005056bbc848
Content-Length: 369
Content-Type: application/json
{
  "num_records": 1,
  "records": [
    {
      "uuid": "a69d8173-450c-11e9-aa44-005056bbc848",
      "svm": {
        "name": "vs0"
      },
      "name": "new_policy",
      "comment": "This is a 5min schedule policy",
      "enabled": true,
      "copies": [
        {
          "count": 5,
          "schedule": {
            "name": "5min"
          }
        }
      ]
    }
  ]
}
```
### Retrieving Snapshot copy policy attributes
The GET operation is used to retrieve Snapshot copy policy attributes.
```
# The API:
/api/storage/snapshot_policies
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/snapshot_policies/" -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Tue, 12 Mar 2019 21:17:17 GMT
Server: libzapid-http
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 686
Content-Type: application/json
{
  "records": [
    {
      "uuid": "0fa7a554-348d-11e9-b55e-005056bbf1c8",
      "name": "spsv0",
      "_links": {
        "self": {
          "href": "/api/storage/snapshot_policies/0fa7a554-348d-11e9-b55e-005056bbf1c8"
        }
      }
    },
    {
      "uuid": "3c112527-2fe8-11e9-b55e-005056bbf1c8",
      "name": "default",
      "_links": {
        "self": {
          "href": "/api/storage/snapshot_policies/3c112527-2fe8-11e9-b55e-005056bbf1c8"
        }
      }
    },
    {
      "uuid": "3c1c1656-2fe8-11e9-b55e-005056bbf1c8",
      "name": "default-1weekly",
      "_links": {
        "self": {
          "href": "/api/storage/snapshot_policies/3c1c1656-2fe8-11e9-b55e-005056bbf1c8"
        }
      }
    },
    {
      "uuid": "3c228b82-2fe8-11e9-b55e-005056bbf1c8",
      "name": "none",
      "_links": {
        "self": {
          "href": "/api/storage/snapshot_policies/3c228b82-2fe8-11e9-b55e-005056bbf1c8"
        }
      }
    }
  ],
  "num_records": 4,
  "_links": {
    "self": {
      "href": "/api/storage/snapshot_policies/"
    }
  }
}
```
### Retrieving the attributes of a specific Snapshot copy policy
The GET operation is used to retrieve the attributes of a specific Snapshot copy policy.
```
# The API:
/api/storage/snapshot_policies
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/snapshot_policies/3c112527-2fe8-11e9-b55e-005056bbf1c8" -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Tue, 12 Mar 2019 21:24:48 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 381
Content-Type: application/json
{
  "uuid": "3c112527-2fe8-11e9-b55e-005056bbf1c8",
  "name": "default",
  "comment": "Default policy with hourly, daily & weekly schedules.",
  "enabled": true,
  "scope": "cluster",
  "copies": [
    {
      "count": 6,
      "prefix": "hourly",
      "schedule": {
        "name": "hourly"
      }
    },
    {
      "count": 2,
      "prefix": "daily",
      "schedule": {
        "name": "daily"
      }
    },
    {
      "count": 2,
      "prefix": "weekly",
      "schedule": {
        "name": "weekly"
      }
    }
  ],
  "_links": {
    "self": {
      "href": "/api/storage/snapshot_policies/3c112527-2fe8-11e9-b55e-005056bbf1c8"
    }
  }
}
```
### Updating a Snapshot copy policy
The PATCH operation is used to update the specific attributes of a Snapshot copy policy.
```
# The API:
/api/storage/snapshot_policies/{uuid}
# The call:
curl -X PATCH  "https://<mgmt-ip>/api/storage/snapshot_policies/ae9e65c4-4506-11e9-aa44-005056bbc848" -d '{"enabled": "false" }' -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Tue, 12 Mar 2019 21:27:04 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 3
Content-Type: application/json
```
### Deleting a Snapshot copy policy
The DELETE operation is used to delete a Snapshot copy policy.
```
# The API:
/api/storage/snapshot_policies/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/storage/snapshot_policies/  ae9e65c4-4506-11e9-aa44-005056bbc848" -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Tue, 12 Mar 2019 21:19:04 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 3
Content-Type: application/json
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnapshotPolicy", "SnapshotPolicySchema"]
__pdoc__ = {
    "SnapshotPolicySchema.resource": False,
    "SnapshotPolicySchema.patchable_fields": False,
    "SnapshotPolicySchema.postable_fields": False,
}


class SnapshotPolicySchema(ResourceSchema):
    """The fields of the SnapshotPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snapshot_policy. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" A comment associated with the Snapshot copy policy. """

    copies = fields.List(fields.Nested("netapp_ontap.models.snapshot_policy_copies.SnapshotPolicyCopiesSchema", unknown=EXCLUDE), data_key="copies")
    r""" The copies field of the snapshot_policy. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Is the Snapshot copy policy enabled?

Example: true """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the Snapshot copy policy.

Example: default """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" when the request is on a data SVM, otherwise set to "cluster".

Valid choices:

* svm
* cluster """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the snapshot_policy. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the snapshot_policy.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return SnapshotPolicy

    @property
    def patchable_fields(self):
        return [
            "comment",
            "enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "comment",
            "copies",
            "enabled",
            "name",
            "svm.name",
            "svm.uuid",
        ]

class SnapshotPolicy(Resource):
    r""" The Snapshot copy policy object is associated with a read-write volume used to create and delete Snapshot copies at regular intervals. """

    _schema = SnapshotPolicySchema
    _path = "/api/storage/snapshot-policies"
    @property
    def _keys(self):
        return ["uuid"]

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
        r"""Retrieves a collection of Snapshot copy policies.
### Related ONTAP commands
* `snapshot policy show`
### Learn more
* [`DOC /storage/snapshot-policies`](#docs-storage-storage_snapshot-policies)
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
        r"""Updates a Snapshot copy policy
### Related ONTAP commands
* `snapshot policy modify`
* `snapshot policy modify-schedule`
* `snapshot policy add-schedule`
### Learn more
* [`DOC /storage/snapshot-policies`](#docs-storage-storage_snapshot-policies)
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
        r"""Deletes a Snapshot copy policy
### Related ONTAP commands
* `snapshot policy delete`
### Learn more
* [`DOC /storage/snapshot-policies`](#docs-storage-storage_snapshot-policies)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of Snapshot copy policies.
### Related ONTAP commands
* `snapshot policy show`
### Learn more
* [`DOC /storage/snapshot-policies`](#docs-storage-storage_snapshot-policies)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves details of a specific Snapshot copy policy.
### Related ONTAP commands
* `snapshot policy show`
### Learn more
* [`DOC /storage/snapshot-policies`](#docs-storage-storage_snapshot-policies)
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
        r"""Creates a Snapshot copy policy.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the Snapshot copy policy.
* `name` - Name for the Snapshot copy policy.
* `copies.schedule` - Schedule at which Snapshot copies are captured on the volume.
* `copies.count` - Number of Snapshot copies to maintain for this schedule.
### Recommended optional properties
* `copies.prefix` - Prefix to use when creating Snapshot copies at regular intervals.
### Default property values
If not specified in POST, the following default property values are assigned:
* `enabled` - _true_
* `copies.prefix` - Value of `schedule.name`
### Related ONTAP commands
* `snapshot policy create`
### Learn more
* [`DOC /storage/snapshot-policies`](#docs-storage-storage_snapshot-policies)
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
        r"""Updates a Snapshot copy policy
### Related ONTAP commands
* `snapshot policy modify`
* `snapshot policy modify-schedule`
* `snapshot policy add-schedule`
### Learn more
* [`DOC /storage/snapshot-policies`](#docs-storage-storage_snapshot-policies)
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
        r"""Deletes a Snapshot copy policy
### Related ONTAP commands
* `snapshot policy delete`
### Learn more
* [`DOC /storage/snapshot-policies`](#docs-storage-storage_snapshot-policies)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


