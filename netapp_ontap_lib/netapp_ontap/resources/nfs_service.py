# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

### Retrieving an NFS configuration
```
# The API:
GET /api/protocols/nfs/services
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/nfs/services"
```
### Creating an NFS configuration for an SVM
```
# The API:
POST /api/protocols/nfs/services
# The call:
curl  -d "@test_nfs_post.txt" -X POST "https://<mgmt-ip>/api/protocols/nfs/services"
test_nfs_post.txt(body):
{
  "svm": {
    "uuid": "1cd8a442-86d1-11e0-ae1c-123478563412"
  },
  "protocol": {
    "v4_id_domain": "nfs-nsr-w01.rtp.netapp.com"
  },
  "vstorage_enabled": "true"
}
```
### Updating an  NFS configuration for an SVM
```
# The API:
PATCH /api/protocols/nfs/services/{svm.uuid}
# The call:
curl -d "@test_nfs_patch.txt" -X PATCH "https://<mgmt-ip>/api/protocols/nfs/services/4a415601-548c-11e8-a21d-0050568bcbc9"
test_nfs_patch.txt(body):
{
  "protocol": {
    "v4_id_domain": "nfs-nsr-w01.rtp.netapp.com"
  },
  "vstorage_enabled": "false"
}
```
### Deleting an NFS configuration for an SVM
```
# The API:
DELETE /api/protocols/nfs/services/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/nfs/services/4a415601-548c-11e8-a21d-0050568bcbc9"
```
## Performance monitoring
Performance of the SVM can be monitored by the `metric.*` and `statistics.*` properties. These show the performance of the SVM in terms of IOPS, latency and throughput. The `metric.*` properties denote an average whereas `statistics.*` properties denote a real-time monotonically increasing value aggregated across all nodes.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["NfsService", "NfsServiceSchema"]
__pdoc__ = {
    "NfsServiceSchema.resource": False,
    "NfsServiceSchema.patchable_fields": False,
    "NfsServiceSchema.postable_fields": False,
}


class NfsServiceSchema(ResourceSchema):
    """The fields of the NfsService object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the nfs_service. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies if the NFS service is administratively enabled. """

    metric = fields.Nested("netapp_ontap.models.performance_svm_nfs_metric.PerformanceSvmNfsMetricSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the nfs_service. """

    protocol = fields.Nested("netapp_ontap.models.nfs_service_protocol.NfsServiceProtocolSchema", data_key="protocol", unknown=EXCLUDE)
    r""" The protocol field of the nfs_service. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['online', 'offline']),
    )
    r""" Specifies the state of the NFS service on the SVM. The following values are supported:

          * online - NFS server is ready to accept client requests.
          * offline - NFS server is not ready to accept client requests.


Valid choices:

* online
* offline """

    statistics = fields.Nested("netapp_ontap.models.performance_svm_nfs_statistics.PerformanceSvmNfsStatisticsSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the nfs_service. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the nfs_service. """

    transport = fields.Nested("netapp_ontap.models.nfs_service_transport.NfsServiceTransportSchema", data_key="transport", unknown=EXCLUDE)
    r""" The transport field of the nfs_service. """

    vstorage_enabled = fields.Boolean(
        data_key="vstorage_enabled",
    )
    r""" Specifies whether VMware vstorage feature is enabled. """

    @property
    def resource(self):
        return NfsService

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "protocol",
            "svm.name",
            "svm.uuid",
            "transport",
            "vstorage_enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "protocol",
            "svm.name",
            "svm.uuid",
            "transport",
            "vstorage_enabled",
        ]

class NfsService(Resource):
    """Allows interaction with NfsService objects on the host"""

    _schema = NfsServiceSchema
    _path = "/api/protocols/nfs/services"
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
        r"""Retrieves the NFS configuration of SVMs.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `statistics.*`
* `metric.*`
### Related ONTAP commands
* `vserver nfs show`
* `vserver nfs status`
### Learn more
* [`DOC /protocols/nfs/services`](#docs-NAS-protocols_nfs_services)
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
        r"""Updates the NFS configuration of an SVM.
### Related ONTAP commands
* `vserver nfs modify`
* `vserver nfs on`
* `vserver nfs off`
* `vserver nfs start`
* `vserver nfs stop`
### Learn more
* [`DOC /protocols/nfs/services`](#docs-NAS-protocols_nfs_services)
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
        r"""Deletes the NFS configuration of an SVM.
### Related ONTAP commands
* `vserver nfs delete`
### Learn more
* [`DOC /protocols/nfs/services`](#docs-NAS-protocols_nfs_services)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the NFS configuration of SVMs.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `statistics.*`
* `metric.*`
### Related ONTAP commands
* `vserver nfs show`
* `vserver nfs status`
### Learn more
* [`DOC /protocols/nfs/services`](#docs-NAS-protocols_nfs_services)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the NFS configuration of an SVM.
### Related ONTAP commands
* `vserver nfs show`
* `vserver nfs status`
### Learn more
* [`DOC /protocols/nfs/services`](#docs-NAS-protocols_nfs_services)
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
        r"""Creates an NFS configuration for an SVM.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM for which to create the NFS configuration.
### Default property values
If not specified in POST, the following default property values are assigned:
* `enabled` - _true_
* `state` - online
* `transport.udp_enabled` - _true_
* `transport.tcp_enabled` - _true_
* `protocol.v3_enabled` - _true_
* `protocol.v4_id_domain` - defaultv4iddomain.com
* `protocol.v4_enabled` - _false_
* `protocol.v41_enabled` - _false_
* `protocol.v40_features.acl_enabled` - _false_
* `protocol.v40_features.read_delegation_enabled` - _false_
* `protocol.v40_features.write_delegation_enabled` - _false_
* `protocol.v41_features.acl_enabled` - _false_
* `protocol.v41_features.read_delegation_enabled` - _false_
* `protocol.v41_features.write_delegation_enabled` - _false_
* `protocol.v41_features.pnfs_enabled` - _false_
* `vstorage_enabled` - _false_
### Related ONTAP commands
* `vserver nfs create`
### Learn more
* [`DOC /protocols/nfs/services`](#docs-NAS-protocols_nfs_services)
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
        r"""Updates the NFS configuration of an SVM.
### Related ONTAP commands
* `vserver nfs modify`
* `vserver nfs on`
* `vserver nfs off`
* `vserver nfs start`
* `vserver nfs stop`
### Learn more
* [`DOC /protocols/nfs/services`](#docs-NAS-protocols_nfs_services)
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
        r"""Deletes the NFS configuration of an SVM.
### Related ONTAP commands
* `vserver nfs delete`
### Learn more
* [`DOC /protocols/nfs/services`](#docs-NAS-protocols_nfs_services)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


