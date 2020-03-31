# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
A Snapshot copy is the view of the filesystem as it exists at the time when the Snapshot copy is created. <br/>
In ONTAP, different types of Snapshot copies are supported, such as scheduled Snapshot copies, user requested Snapshot copies, SnapMirror Snapshot copies, and so on. <br/>
ONTAP Snapshot copy APIs allow you to create, modify, delete and retrieve Snapshot copies. <br/>
## Snapshot copy APIs
The following APIs are used to perform operations related to Snapshot copies.

* POST      /api/storage/volumes/{volume.uuid}/snapshots
* GET       /api/storage/volumes/{volume.uuid}/snapshots
* GET       /api/storage/volumes/{volume.uuid}/snapshots/{uuid}
* PATCH     /api/storage/volumes/{volume.uuid}/snapshots/{uuid}
* DELETE    /api/storage/volumes/{volume.uuid}/snapshots/{uuid}
## Examples
### Creating a Snapshot copy
The POST operation is used to create a Snapshot copy with the specified attributes.
```
# The API:
/api/storage/volumes/{volume.uuid}/snapshots
# The call:
curl -X POST "https://<mgmt-ip>/api/storage/volumes/{volume.uuid}/snapshots" -H "accept: application/hal+json" -d '{"name": "snapshot_copy", "comment": "Store this copy." }'
# The response:
HTTP/1.1 202 Accepted
Date: Wed, 13 Mar 2019 22:43:34 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/?name=snapshot_copy
Content-Length: 189
Content-Type: application/json
{
  "num_records": 1,
  "records": [
    {
      "volume": {
        "name": "v2"
      },
      "svm": {
        "uuid": "8139f958-3c6e-11e9-a45f-005056bbc848",
        "name": "vs0"
      }
      "name": "snapshot_copy",
      "comment": "Store this copy."
    }
  ],
  "job": {
    "uuid": "6f68c85b-45e1-11e9-8fc7-005056bbc848",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/6f68c85b-45e1-11e9-8fc7-005056bbc848"
      }
    }
  }
}
# The Job:
HTTP/1.1 200 OK
Date: Wed, 13 Mar 2019 22:43:57 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 224
Content-Type: application/json
{
  "uuid": "6f68c85b-45e1-11e9-8fc7-005056bbc848",
  "description": "POST /api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/?name=snapshot_copy",
  "state": "success",
  "message": "success",
  "code": 0
}
```
### Retrieving Snapshot copy attributes
The GET operation is used to retrieve Snapshot copy attributes.
```
# The API:
/api/storage/volumes/{volume.uuid}/snapshots
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/volumes/{volume.uuid}/snapshots" -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Wed, 13 Mar 2019 21:14:06 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Type: application/json
Transfer-Encoding: chunked
{
  "records": [
    {
      "uuid": "402b6c73-73a0-4e89-a58a-75ee0ab3e8c0",
      "name": "hourly.2019-03-13_1305",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/402b6c73-73a0-4e89-a58a-75ee0ab3e8c0"
        }
      }
    },
    {
      "uuid": "f0dd497f-efe8-44b7-a4f4-bdd3890bc0c8",
      "name": "hourly.2019-03-13_1405",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/f0dd497f-efe8-44b7-a4f4-bdd3890bc0c8"
        }
      }
    },
    {
      "uuid": "02701900-51bd-46b8-9c77-47d9a9e2ce1d",
      "name": "hourly.2019-03-13_1522",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/02701900-51bd-46b8-9c77-47d9a9e2ce1d"
        }
      }
    }
  ],
  "num_records": 3,
  "_links": {
    "self": {
      "href": "/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots"
    }
  }
}
```
### Retrieving the attributes of a specific Snapshot copy
The GET operation is used to retrieve the attributes of a specific Snapshot copy.
```
# The API:
/api/storage/volumes/{volume.uuid}/snapshots/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/402b6c73-73a0-4e89-a58a-75ee0ab3e8c0" -H "accept: application/hal+json"
# The response:
HTTP/1.1 200 OK
Date: Wed, 13 Mar 2019 22:39:26 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 308
Content-Type: application/json
{
  "volume": {
    "uuid": "0353dc05-405f-11e9-acb6-005056bbc848",
    "name": "v2",
    "_links": {
      "self": {
        "href": "/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848"
      }
    }
  },
  "uuid": "402b6c73-73a0-4e89-a58a-75ee0ab3e8c0",
  "svm": {
    "uuid": "8139f958-3c6e-11e9-a45f-005056bbc848",
    "name": "vs0",
    "_links": {
      "self": {
        "href": "/api/svm/svms/8139f958-3c6e-11e9-a45f-005056bbc848"
      }
    }
  },
  "name": "hourly.2019-03-13_1305",
  "create_time": "2019-03-13T13:05:00-04:00",
  "_links": {
    "self": {
      "href": "/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/402b6c73-73a0-4e89-a58a-75ee0ab3e8c0"
    }
  }
}
```
### Updating a Snapshot copy
The PATCH operation is used to update the specific attributes of a Snapshot copy.
```
# The API:
/api/storage/volumes/{volume.uuid}/snapshots/{uuid}
# The call:
curl -X PATCH  "https://<mgmt-ip>/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/16f7008c-18fd-4a7d-8485-a0e290d9db7f" -d '{"name": "snapshot_copy_new" }' -H "accept: application/hal+json"
# The response:
HTTP/1.1 202 Accepted
Date: Wed, 13 Mar 2019 22:50:44 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 189
Content-Type: application/json
{
  "job": {
    "uuid": "6f7c3a82-45e2-11e9-8fc7-005056bbc848",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/6f7c3a82-45e2-11e9-8fc7-005056bbc848"
      }
    }
  }
}
# The Job:
HTTP/1.1 200 OK
Date: Wed, 13 Mar 2019 22:54:16 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 242
Content-Type: application/json
{
  "uuid": "6f7c3a82-45e2-11e9-8fc7-005056bbc848",
  "description": "PATCH /api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/16f7008c-18fd-4a7d-8485-a0e290d9db7f",
  "state": "success",
  "message": "success",
  "code": 0
}
```
### Deleting a Snapshot copy
The DELETE operation is used to delete a Snapshot copy.
```
# The API:
/api/storage/volumes/{volume.uuid}/snapshots/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/16f7008c-18fd-4a7d-8485-a0e290d9db7f" -H "accept: application/hal+json"
# The response:
HTTP/1.1 202 Accepted
Date: Wed, 13 Mar 2019 22:57:51 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 189
Content-Type: application/json
{
  "job": {
    "uuid": "6da1dfdd-45e3-11e9-8fc7-005056bbc848",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/6da1dfdd-45e3-11e9-8fc7-005056bbc848"
      }
    }
  }
}
# The Job:
HTTP/1.1 200 OK
Date: Wed, 13 Mar 2019 23:02:46 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 243
Content-Type: application/json
{
  "uuid": "6da1dfdd-45e3-11e9-8fc7-005056bbc848",
  "description": "DELETE /api/storage/volumes/0353dc05-405f-11e9-acb6-005056bbc848/snapshots/16f7008c-18fd-4a7d-8485-a0e290d9db7f",
  "state": "success",
  "message": "success",
  "code": 0
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


__all__ = ["Snapshot", "SnapshotSchema"]
__pdoc__ = {
    "SnapshotSchema.resource": False,
    "SnapshotSchema.patchable_fields": False,
    "SnapshotSchema.postable_fields": False,
}


class SnapshotSchema(ResourceSchema):
    """The fields of the Snapshot object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snapshot. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" A comment associated with the Snapshot copy. This is an optional attribute for POST or PATCH. """

    create_time = fields.DateTime(
        data_key="create_time",
    )
    r""" Creation time of the Snapshot copy. It is the volume access time when the Snapshot copy was created.

Example: 2019-02-04T19:00:00.000+0000 """

    expiry_time = fields.DateTime(
        data_key="expiry_time",
    )
    r""" The expiry time for the Snapshot copy. This is an optional attribute for POST or PATCH. Snapshot copies with an expiry time set are not allowed to be deleted until the retention time is reached.

Example: 2019-02-04T19:00:00.000+0000 """

    name = fields.Str(
        data_key="name",
    )
    r""" Snapshot copy. Valid in POST or PATCH.

Example: this_snapshot """

    owners = fields.List(fields.Str, data_key="owners")
    r""" The owners field of the snapshot. """

    snaplock_expiry_time = fields.DateTime(
        data_key="snaplock_expiry_time",
    )
    r""" SnapLock expiry time for the Snapshot copy, if the Snapshot copy is taken on a SnapLock volume. A Snapshot copy is not allowed to be deleted or renamed until the SnapLock ComplianceClock time goes beyond this retention time.

Example: 2019-02-04T19:00:00.000+0000 """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['valid', 'invalid', 'partial']),
    )
    r""" State of the Snapshot copy. There are cases where some Snapshot copies are not complete. In the "partial" state, the Snapshot copy is consistent but exists only on the subset of the constituents that existed prior to the FlexGroup's expansion. Partial Snapshot copies cannot be used for a Snapshot copy restore operation. A Snapshot copy is in an "invalid" state when it is present in some FlexGroup constituents but not in others. At all other times, a Snapshot copy is valid.

Valid choices:

* valid
* invalid
* partial """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the snapshot. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The UUID of the Snapshot copy in the volume that uniquely identifies the Snapshot copy in that volume.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the snapshot. """

    @property
    def resource(self):
        return Snapshot

    @property
    def patchable_fields(self):
        return [
            "comment",
            "expiry_time",
            "name",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "comment",
            "expiry_time",
            "name",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

class Snapshot(Resource):
    r""" The Snapshot copy object represents a point in time Snapshot copy of a volume. """

    _schema = SnapshotSchema
    _path = "/api/storage/volumes/{volume[uuid]}/snapshots"
    @property
    def _keys(self):
        return ["volume.uuid", "uuid"]

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
        r"""Retrieves a collection of volume Snapshot copies.
### Related ONTAP commands
* `snapshot show`
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapshots`](#docs-storage-storage_volumes_{volume.uuid}_snapshots)
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
        r"""Updates a Volume Snapshot copy.
### Related ONTAP commands
* `snapshot modify`
* `snapshot rename`
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapshots`](#docs-storage-storage_volumes_{volume.uuid}_snapshots)
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
        r"""Deletes a Volume Snapshot copy.
### Related ONTAP commands
* `snapshot delete`
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapshots`](#docs-storage-storage_volumes_{volume.uuid}_snapshots)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of volume Snapshot copies.
### Related ONTAP commands
* `snapshot show`
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapshots`](#docs-storage-storage_volumes_{volume.uuid}_snapshots)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves details of a specific volume Snapshot copy.
### Related ONTAP commands
* `snapshot show`
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapshots`](#docs-storage-storage_volumes_{volume.uuid}_snapshots)
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
        r"""Creates a volume Snapshot copy.
### Required properties
* `name` - Name of the Snapshot copy to be created.
### Recommended optional properties
* `comment` - Comment associated with the Snapshot copy.
* `expiry_time` - Snapshot copies with an expiry time set are not allowed to be deleted until the retention time is reached.
### Related ONTAP commands
* `snapshot create`
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapshots`](#docs-storage-storage_volumes_{volume.uuid}_snapshots)
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
        r"""Updates a Volume Snapshot copy.
### Related ONTAP commands
* `snapshot modify`
* `snapshot rename`
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapshots`](#docs-storage-storage_volumes_{volume.uuid}_snapshots)
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
        r"""Deletes a Volume Snapshot copy.
### Related ONTAP commands
* `snapshot delete`
### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapshots`](#docs-storage-storage_volumes_{volume.uuid}_snapshots)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


