# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Managing SVM peer permissions
A cluster administrator can provide permissions for use during intercluster SVM peer relationship creation. Once this permission exists for a local SVM and peer cluster combination on a local cluster, no explicit SVM peer accept (or REST PATCH) API is required for any incoming SVM peer relationship creation requests from a remote cluster for that local SVM. Peer relationship directly changes the state to peered on both clusters. Use an SVM name as "*" to create permissions that apply to all local SVMs.
### SVM peer permission APIs
The following APIs are used to manage SVM peer permissions:
- GET /api/svm/peer-permissions
- POST /api/svm/peer-permissions
- GET /api/svm/peer-permissions/{cluster_peer.uuid}/{svm.uuid}
- PATCH /api/svm/peer-permissions/{cluster_peer.uuid}/{svm.uuid}
- DELETE /api/svm/peer-permissions/{cluster_peer.uuid}/{svm.uuid}
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SvmPeerPermission", "SvmPeerPermissionSchema"]
__pdoc__ = {
    "SvmPeerPermissionSchema.resource": False,
    "SvmPeerPermissionSchema.patchable_fields": False,
    "SvmPeerPermissionSchema.postable_fields": False,
}


class SvmPeerPermissionSchema(ResourceSchema):
    """The fields of the SvmPeerPermission object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the svm_peer_permission. """

    applications = fields.List(fields.Str, data_key="applications")
    r""" A list of applications for an SVM peer relation.

Example: ["snapmirror","flexcache"] """

    cluster_peer = fields.Nested("netapp_ontap.resources.cluster_peer.ClusterPeerSchema", data_key="cluster_peer", unknown=EXCLUDE)
    r""" The cluster_peer field of the svm_peer_permission. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the svm_peer_permission. """

    @property
    def resource(self):
        return SvmPeerPermission

    @property
    def patchable_fields(self):
        return [
            "applications",
        ]

    @property
    def postable_fields(self):
        return [
            "applications",
            "cluster_peer.name",
            "cluster_peer.uuid",
            "svm.name",
            "svm.uuid",
        ]

class SvmPeerPermission(Resource):
    r""" Manage SVM peer permissions. """

    _schema = SvmPeerPermissionSchema
    _path = "/api/svm/peer-permissions"
    @property
    def _keys(self):
        return ["cluster_peer.uuid", "svm.uuid"]

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
        r"""Retrieves the list of SVM peer permissions.
### Related ONTAP commands
* `vserver peer permission show`
### Examples
The following examples show how to retrieve a collection of SVM peer permissions based on a query.
<br/>
1. Retrieves a list of SVM peer permissions of a specific local SVM
   <br/>
   ```
   GET "/api/svm/peer-permissions/?svm.name=VS1"
   ```
   <br/>
2. Retrieves a list of SVM peer permissions of a specific cluster peer
   <br/>
   ```
   GET "/api/svm/peer-permissions/?cluster_peer.name=cluster2"
   ```
   <br/>
### Learn more
* [`DOC /svm/peer-permissions`](#docs-svm-svm_peer-permissions)
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
        r"""Updates the SVM peer permissions.
### Related ONTAP commands
* `vserver peer permission modify`
### Example
Updates an SVM peer permission.
<br/>
```
PATCH "/api/svm/peer-permissions/d3268a74-ee76-11e8-a9bb-005056ac6dc9/8f467b93-f2f1-11e8-9027-005056ac81fc" '{"applications":["flexcache"]}'
```
<br/>
### Learn more
* [`DOC /svm/peer-permissions`](#docs-svm-svm_peer-permissions)
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
        r"""Deletes the SVM peer permissions.
### Related ONTAP commands
* `verver peer permission delete`
### Example
Deletes an SVM peer permission.
<br/>
```
DELETE "/api/svm/peer-permissions/d3268a74-ee76-11e8-a9bb-005056ac6dc9/8f467b93-f2f1-11e8-9027-005056ac81fc"
```
<br/>
### Learn more
* [`DOC /svm/peer-permissions`](#docs-svm-svm_peer-permissions)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the list of SVM peer permissions.
### Related ONTAP commands
* `vserver peer permission show`
### Examples
The following examples show how to retrieve a collection of SVM peer permissions based on a query.
<br/>
1. Retrieves a list of SVM peer permissions of a specific local SVM
   <br/>
   ```
   GET "/api/svm/peer-permissions/?svm.name=VS1"
   ```
   <br/>
2. Retrieves a list of SVM peer permissions of a specific cluster peer
   <br/>
   ```
   GET "/api/svm/peer-permissions/?cluster_peer.name=cluster2"
   ```
   <br/>
### Learn more
* [`DOC /svm/peer-permissions`](#docs-svm-svm_peer-permissions)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the SVM peer permission instance.
### Related ONTAP commands
* `vserver peer permission show`
### Example
The following example shows how to retrieve the parameters for an SVM peer permission.
<br/>
```
GET "/api/svm/peer-permissions/d3268a74-ee76-11e8-a9bb-005056ac6dc9/8f467b93-f2f1-11e8-9027-005056ac81fc"
```
<br/>
### Learn more
* [`DOC /svm/peer-permissions`](#docs-svm-svm_peer-permissions)
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
        r"""Creates an SVM peer permission.
### Required properties
* `svm.name` or `svm.uuid` - SVM name
* `cluster_peer.uuid` or `cluster_peer.name` - Peer cluster name or peer cluster UUID
* `applications` - Peering applications
### Related ONTAP commands
* `vserver peer permission create`
### Examples
The following examples show how to create SVM peer permissions.
<br/>
1. Creates an SVM peer permission entry with the local SVM and cluster peer names
   <br/>
   ```
   POST "/api/svm/peer-permissions" '{"cluster_peer":{"name":"cluster2"}, "svm":{"name":"VS1"}, "applications":["snapmirror"]}'
   ```
   <br/>
2. Creates an SVM peer permission entry with the local SVM and cluster peer UUID
   <br/>
   ```
   POST "/api/svm/peer-permissions" '{"cluster_peer":{"uuid":"d3268a74-ee76-11e8-a9bb-005056ac6dc9"}, "svm":{"uuid":"8f467b93-f2f1-11e8-9027-005056ac81fc"}, "applications":["snapmirror"]}'
   ```
   <br/>
3. Creates an SVM peer permission entry with all SVMs and the cluster peer name
   <br/>
   ```
   POST "/api/svm/peer-permissions" '{"cluster_peer":{"name":"cluster2"}, "svm":{"name":"*"}, "applications":["snapmirror"]}'
   ```
   <br/>
### Learn more
* [`DOC /svm/peer-permissions`](#docs-svm-svm_peer-permissions)
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
        r"""Updates the SVM peer permissions.
### Related ONTAP commands
* `vserver peer permission modify`
### Example
Updates an SVM peer permission.
<br/>
```
PATCH "/api/svm/peer-permissions/d3268a74-ee76-11e8-a9bb-005056ac6dc9/8f467b93-f2f1-11e8-9027-005056ac81fc" '{"applications":["flexcache"]}'
```
<br/>
### Learn more
* [`DOC /svm/peer-permissions`](#docs-svm-svm_peer-permissions)
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
        r"""Deletes the SVM peer permissions.
### Related ONTAP commands
* `verver peer permission delete`
### Example
Deletes an SVM peer permission.
<br/>
```
DELETE "/api/svm/peer-permissions/d3268a74-ee76-11e8-a9bb-005056ac6dc9/8f467b93-f2f1-11e8-9027-005056ac81fc"
```
<br/>
### Learn more
* [`DOC /svm/peer-permissions`](#docs-svm-svm_peer-permissions)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


