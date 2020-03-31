# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An iSCSI service defines the properties of the iSCSI target for an SVM. There can be at most one iSCSI service for an SVM. An SVM's iSCSI service must be created before iSCSI initiators can log in to the SVM.<br/>
The iSCSI service REST API allows you to create, update, delete, and discover iSCSI services for SVMs.
## Performance monitoring
Performance of the SVM can be monitored by the `metric.*` and `statistics.*` properties. These show the performance of the SVM in terms of IOPS, latency and throughput. The `metric.*` properties denote an average whereas `statistics.*` properties denote a real-time monotonically increasing value aggregated across all nodes.
## Examples
### Creating an iSCSI service for an SVM
The simplest way to create an iSCSI service is to specify only the SVM, either by name or UUID. By default, the new iSCSI service is enabled and uses the SVM name as its target alias.<br/>
In this example, the `return_records` query parameter is used to retrieve the new iSCSI service object in the REST response.
<br/>
```
# The API:
POST /api/protocols/san/iscsi/services
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/san/iscsi/services?return_records=true' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" } }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "19d04b8e-94d7-11e8-8370-005056b48fd2",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/19d04b8e-94d7-11e8-8370-005056b48fd2"
          }
        }
      },
      "enabled": true,
      "target": {
        "name": "iqn.1992-08.com.netapp:sn.19d04b8e94d711e88370005056b48fd2:vs.4",
        "alias": "svm1"
      },
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/services/19d04b8e-94d7-11e8-8370-005056b48fd2"
        }
      }
    }
  ]
}
```
---
### Retrieving the iSCSI services for all SVMs in the cluster
```
# The API:
GET /api/protocols/san/iscsi/services
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/iscsi/services' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "19d04b8e-94d7-11e8-8370-005056b48fd2",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/19d04b8e-94d7-11e8-8370-005056b48fd2"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/services/19d04b8e-94d7-11e8-8370-005056b48fd2"
        }
      }
    },
    {
      "svm": {
        "uuid": "25f617cf-94d7-11e8-8370-005056b48fd2",
        "name": "svm2",
        "_links": {
          "self": {
            "href": "/api/svm/svms/25f617cf-94d7-11e8-8370-005056b48fd2"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/services/25f617cf-94d7-11e8-8370-005056b48fd2"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/san/iscsi/services"
    }
  }
}
```
---
### Retrieving details for a specific iSCSI service
The iSCSI service is identified by the UUID of its SVM.
<br/>
```
# The API:
GET /api/protocols/san/iscsi/services/{svm.uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/iscsi/services/19d04b8e-94d7-11e8-8370-005056b48fd2' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "19d04b8e-94d7-11e8-8370-005056b48fd2",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/19d04b8e-94d7-11e8-8370-005056b48fd2"
      }
    }
  },
  "enabled": true,
  "target": {
    "name": "iqn.1992-08.com.netapp:sn.19d04b8e94d711e88370005056b48fd2:vs.4",
    "alias": "svm1"
  },
  "_links": {
    "self": {
      "href": "/api/protocols/san/iscsi/services/19d04b8e-94d7-11e8-8370-005056b48fd2"
    }
  }
}
```
---
### Disabling an iSCSI service
Disabling an iSCSI service shuts down all active iSCSI sessions for the SVM and prevents the creation of new iSCSI sessions.<br/>
The iSCSI service to update is identified by the UUID of its SVM.
<br/>
```
# The API:
PATCH /api/protocols/san/iscsi/services/{svm.uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/protocols/san/iscsi/services/19d04b8e-94d7-11e8-8370-005056b48fd2' -H 'accept: application/hal+json' -d '{ "enabled": "false" }'
```
<br/>
You can retrieve the iSCSI service to confirm the change.<br/>
In this example, the `fields` query parameter is used to limit the response to the `enabled` property and iSCSI service identifiers.
<br/>
```
# The API:
GET /api/protocols/san/iscsi/services/{svm.uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/iscsi/services/19d04b8e-94d7-11e8-8370-005056b48fd2?fields=enabled' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "19d04b8e-94d7-11e8-8370-005056b48fd2",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/19d04b8e-94d7-11e8-8370-005056b48fd2"
      }
    }
  },
  "enabled": false,
  "_links": {
    "self": {
      "href": "/api/protocols/san/iscsi/services/19d04b8e-94d7-11e8-8370-005056b48fd2"
    }
  }
}
```
---
### Deleting an iSCSI service
The iSCSI service must be disabled before it can be deleted.<br/>
The iSCSI service to be deleted is identified by the UUID of its SVM.
<br/>
```
# The API:
DELETE /api/protocols/san/iscsi/services/{svm.uuid}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/protocols/san/iscsi/services/19d04b8e-94d7-11e8-8370-005056b48fd2' -H 'accept: application/hal+json'
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["IscsiService", "IscsiServiceSchema"]
__pdoc__ = {
    "IscsiServiceSchema.resource": False,
    "IscsiServiceSchema.patchable_fields": False,
    "IscsiServiceSchema.postable_fields": False,
}


class IscsiServiceSchema(ResourceSchema):
    """The fields of the IscsiService object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the iscsi_service. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The administrative state of the iSCSI service. The iSCSI service can be disabled to block all iSCSI connectivity to the SVM.<br/>
Optional in POST and PATCH. The default setting is _true_ (enabled) in POST. """

    metric = fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the iscsi_service. """

    statistics = fields.Nested("netapp_ontap.models.performance_metric_raw_svm.PerformanceMetricRawSvmSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the iscsi_service. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the iscsi_service. """

    target = fields.Nested("netapp_ontap.models.iscsi_service_target.IscsiServiceTargetSchema", data_key="target", unknown=EXCLUDE)
    r""" The target field of the iscsi_service. """

    @property
    def resource(self):
        return IscsiService

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "metric.iops",
            "metric.latency",
            "metric.throughput",
            "statistics.iops_raw",
            "statistics.latency_raw",
            "statistics.throughput_raw",
            "svm.name",
            "svm.uuid",
            "target",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "metric.iops",
            "metric.latency",
            "metric.throughput",
            "statistics.iops_raw",
            "statistics.latency_raw",
            "statistics.throughput_raw",
            "svm.name",
            "svm.uuid",
            "target",
        ]

class IscsiService(Resource):
    r""" An iSCSI service defines the properties of the iSCSI target for an SVM. There can be at most one iSCSI service for an SVM. An SVM's iSCSI service must be created before iSCSI initiators can log in to the SVM.<br/>
An iSCSI service is identified by the UUID of its SVM. """

    _schema = IscsiServiceSchema
    _path = "/api/protocols/san/iscsi/services"
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
        r"""Retrieves iSCSI services.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `statistics.*`
* `metric.*`
### Related ONTAP commands
* `vserver iscsi show`
### Learn more
* [`DOC /protocols/san/iscsi/services`](#docs-SAN-protocols_san_iscsi_services)
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
        r"""Updates an iSCSI service.
### Related ONTAP commands
* `vserver iscsi modify`
* `vserver iscsi start`
* `vserver iscsi stop`
### Learn more
* [`DOC /protocols/san/iscsi/services`](#docs-SAN-protocols_san_iscsi_services)
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
        r"""Deletes an iSCSI service. An iSCSI service must be disabled before it can be deleted.
### Related ONTAP commands
* `vserver iscsi delete`
### Learn more
* [`DOC /protocols/san/iscsi/services`](#docs-SAN-protocols_san_iscsi_services)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves iSCSI services.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `statistics.*`
* `metric.*`
### Related ONTAP commands
* `vserver iscsi show`
### Learn more
* [`DOC /protocols/san/iscsi/services`](#docs-SAN-protocols_san_iscsi_services)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an iSCSI service.
### Related ONTAP commands
* `vserver iscsi show`
### Learn more
* [`DOC /protocols/san/iscsi/services`](#docs-SAN-protocols_san_iscsi_services)
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
        r"""Creates an iSCSI service.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the iSCSI service.
### Related ONTAP commands
* `vserver iscsi create`
### Learn more
* [`DOC /protocols/san/iscsi/services`](#docs-SAN-protocols_san_iscsi_services)
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
        r"""Updates an iSCSI service.
### Related ONTAP commands
* `vserver iscsi modify`
* `vserver iscsi start`
* `vserver iscsi stop`
### Learn more
* [`DOC /protocols/san/iscsi/services`](#docs-SAN-protocols_san_iscsi_services)
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
        r"""Deletes an iSCSI service. An iSCSI service must be disabled before it can be deleted.
### Related ONTAP commands
* `vserver iscsi delete`
### Learn more
* [`DOC /protocols/san/iscsi/services`](#docs-SAN-protocols_san_iscsi_services)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


