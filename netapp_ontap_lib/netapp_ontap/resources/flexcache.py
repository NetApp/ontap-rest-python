# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
FlexCache is a persistent cache of an origin volume. An origin volume can only be a FlexVol while a FlexCache is always a FlexGroup.</br>
The following relationship configurations are supported:</br>

* Intra-Vserver where FlexCache and the corresponding origin volume reside in the same Vserver.
* Cross-Vserver but intra-cluster where FlexCache and the origin volume reside in the same cluster but belong to different Vservers.
* Cross-cluster where FlexCache and the origin volume reside in different clusters.</br>
FlexCache supports fan-out and more than one FlexCache can be created from one origin volume.
This API retrieves and manages FlexCache configurations in the cache cluster.
## FlexCache APIs
The following APIs can be used to perform operations related with FlexCache:

* GET       /api/storage/flexcache/flexcaches
* GET       /api/storage/flexcache/flexcaches/{uuid}
* POST      /api/storage/flexcache/flexcaches
* DELETE    /api/storage/flexcache/flexcaches/{uuid}
## Examples
### Creating a FlexCache
The POST request is used to create a FlexCache.
```
# The API:
/api/storage/flexcache/flexcaches
# The call:
curl -X POST "https://<mgmt-ip>/api/storage/flexcache/flexcaches" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{ \"aggregates\": [ { \"name\": \"aggr_1\" } ], \"name\": \"fc_333\", \"origins\": [ {  \"svm\": { \"name\": \"vs_3\"  }, \"volume\": { \"name\": \"vol_o1\" } } ], \"svm\": { \"name\": \"vs_1\" } }"
# The response:
{
  "job": {
    "uuid": "e751dd5d-0f3c-11e9-8b2b-0050568e0b79",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/e751dd5d-0f3c-11e9-8b2b-0050568e0b79"
      }
    }
  }
}
```
### Retrieving FlexCache attributes
The GET request is used to retrieve FlexCache attributes. The object includes a large set of fields which can be expensive to retrieve. Most notably, the fields size, guarantee.type, aggregates, path, origins.ip_address, origins.size, and origins.state are expensive to retrieve. The recommended method to use this API is to filter and retrieve only the required fields.
```
# The API:
/api/storage/flexcache/flexcaches
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/flexcache/flexcaches?" -H  "accept: application/json"
# The response:
  {
    "records": [
      {
        "uuid": "04d5e07b-0ebe-11e9-8180-0050568e0b79",
        "name": "fc_322",
        "_links": {
          "self": {
            "href": "/api/storage/flexcache/flexcaches/04d5e07b-0ebe-11e9-8180-0050568e0b79"
          }
        }
      },
      {
        "uuid": "47902654-0ea4-11e9-8180-0050568e0b79",
        "name": "fc_321",
        "_links": {
          "self": {
            "href": "/api/storage/flexcache/flexcaches/47902654-0ea4-11e9-8180-0050568e0b79"
          }
        }
      },
      {
        "uuid": "77e911ff-0ebe-11e9-8180-0050568e0b79",
        "name": "fc_323",
        "_links": {
          "self": {
            "href": "/api/storage/flexcache/flexcaches/77e911ff-0ebe-11e9-8180-0050568e0b79"
          }
        }
      },
      {
        "uuid": "ddb42bbc-0e95-11e9-8180-0050568e0b79",
        "name": "fc_32",
        "_links": {
          "self": {
            "href": "/api/storage/flexcache/flexcaches/ddb42bbc-0e95-11e9-8180-0050568e0b79"
          }
        }
      },
      {
        "uuid": "ec774932-0f3c-11e9-8b2b-0050568e0b79",
        "name": "fc_333",
        "_links": {
          "self": {
            "href": "/api/storage/flexcache/flexcaches/ec774932-0f3c-11e9-8b2b-0050568e0b79"
          }
        }
      }
    ],
    "num_records": 5,
    "_links": {
      "self": {
        "href": "/api/storage/flexcache/flexcaches?"
      }
    }
  }
```
### Retrieving the attributes of a FlexCache
The GET request is used to retrieve the attributes of a FlexCache. The object includes a large set of fields which can be expensive to retrieve. Most notably, the fields size, guarantee.type, aggregates, path, origins.ip_address, origins.size, and origins.state are expensive to retrieve. The recommended method to use this API is to filter and retrieve only the required fields.
```
# The API:
/api/storage/flexcache/flexcaches/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/flexcache/flexcaches/ec774932-0f3c-11e9-8b2b-0050568e0b79" -H  "accept: application/json"
# The response:
  {
    "uuid": "ec774932-0f3c-11e9-8b2b-0050568e0b79",
    "name": "fc_333",
    "svm": {
      "name": "vs_1",
      "uuid": "e708fbe2-0e92-11e9-8180-0050568e0b79"
    },
    "size": 4294967296,
    "guarantee": {
        "type": "volume"
    },
    "aggregates": [
      {
        "name": "aggr_1",
        "uuid": "26f34b76-88f8-4a47-b5e0-d8e901fb1114"
      }
    ],
    "origins": [
      {
        "ip_address": "10.140.103.175",
        "size": 20971520,
        "create_time": "2019-01-03T15:19:55+05:30",
        "state": "online",
        "volume": {
          "name": "vol_o1",
          "uuid": "2bc957dd-2617-4afb-8d2f-66ac6070d313"
        },
        "svm": {
          "name": "vs_3",
          "uuid": "8aa2cd28-0e92-11e9-b391-0050568e4115"
        },
        "cluster": {
          "name": "node2",
          "uuid": "50733f81-0e90-11e9-b391-0050568e4115"
        }
      }
    ],
    "_links": {
      "self": {
        "href": "/api/storage/flexcache/flexcaches/ec774932-0f3c-11e9-8b2b-0050568e0b79"
      }
    }
  }
```
### Deleting a FlexCache
The DELETE request is used to delete a FlexCache.
```
# The API:
/api/storage/flexcache/flexcaches
# The call:
curl -X DELETE "https://<mgmt-ip>/api/storage/flexcache/flexcaches/ec774932-0f3c-11e9-8b2b-0050568e0b79" -H  "accept: application/json"
# The response:
  {
    "job": {
      "uuid": "e17994f2-0f3e-11e9-8b2b-0050568e0b79",
      "_links": {
        "self": {
          "href": "/api/cluster/jobs/e17994f2-0f3e-11e9-8b2b-0050568e0b79"
        }
      }
    }
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


__all__ = ["Flexcache", "FlexcacheSchema"]
__pdoc__ = {
    "FlexcacheSchema.resource": False,
    "FlexcacheSchema.patchable_fields": False,
    "FlexcacheSchema.postable_fields": False,
}


class FlexcacheSchema(ResourceSchema):
    """The fields of the Flexcache object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the flexcache. """

    aggregates = fields.List(fields.Nested("netapp_ontap.resources.aggregate.AggregateSchema", unknown=EXCLUDE), data_key="aggregates")
    r""" The aggregates field of the flexcache. """

    constituents_per_aggregate = fields.Integer(
        data_key="constituents_per_aggregate",
    )
    r""" Number of FlexCache constituents per aggregate when the 'aggregates' field is mentioned. """

    guarantee = fields.Nested("netapp_ontap.models.flexcache_guarantee.FlexcacheGuaranteeSchema", data_key="guarantee", unknown=EXCLUDE)
    r""" The guarantee field of the flexcache. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=203),
    )
    r""" FlexCache name

Example: vol1 """

    origins = fields.List(fields.Nested("netapp_ontap.models.flexcache_relationship.FlexcacheRelationshipSchema", unknown=EXCLUDE), data_key="origins")
    r""" The origins field of the flexcache. """

    path = fields.Str(
        data_key="path",
    )
    r""" The fully-qualified path in the owning SVM's namespace at which the FlexCache is mounted. The path is case insensitive and must be unique within a SVM's namespace. Path must begin with '/' and must not end with '/'. Only one FlexCache be mounted at any given junction path.

Example: /user/my_fc """

    size = fields.Integer(
        data_key="size",
    )
    r""" Physical size of the FlexCache. The recommended size for a FlexCache is 10% of the origin volume. The minimum FlexCache constituent size is 1GB. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the flexcache. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" FlexCache UUID. Unique identifier for the FlexCache.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return Flexcache

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "aggregates.name",
            "aggregates.uuid",
            "constituents_per_aggregate",
            "guarantee",
            "name",
            "origins",
            "path",
            "size",
            "svm.name",
            "svm.uuid",
        ]

class Flexcache(Resource):
    r""" Defines the cache endpoint of FlexCache. """

    _schema = FlexcacheSchema
    _path = "/api/storage/flexcache/flexcaches"
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
        r"""Retrieves FlexCache in the cluster.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `origins.ip_address` - IP address of origin.
* `origins.size` - Physical size of origin.
* `origins.state` - State of origin.
* `size` - Physical size of FlexCache.
* `guarantee.type` - Space guarantee style of FlexCache.
* `aggregates.name` or `aggregates.uuid` - Name or UUID of aggregrate of FlexCache volume.
* `path` - Fully-qualified path of the owning SVM's namespace where the FlexCache is mounted.
### Related ONTAP commands
* `volume flexcache show`
### Learn more
* [`DOC /storage/flexcache/flexcaches`](#docs-storage-storage_flexcache_flexcaches)
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
        r"""Deletes a FlexCache. If a FlexCache volume is online, it is offlined before deletion.
### Related ONTAP commands
* `volume flexcache delete`
### Learn more
* [`DOC /storage/flexcache/flexcaches`](#docs-storage-storage_flexcache_flexcaches)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves FlexCache in the cluster.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `origins.ip_address` - IP address of origin.
* `origins.size` - Physical size of origin.
* `origins.state` - State of origin.
* `size` - Physical size of FlexCache.
* `guarantee.type` - Space guarantee style of FlexCache.
* `aggregates.name` or `aggregates.uuid` - Name or UUID of aggregrate of FlexCache volume.
* `path` - Fully-qualified path of the owning SVM's namespace where the FlexCache is mounted.
### Related ONTAP commands
* `volume flexcache show`
### Learn more
* [`DOC /storage/flexcache/flexcaches`](#docs-storage-storage_flexcache_flexcaches)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves attributes of the FlexCache in the cluster.
### Expensive properties
There is an added cost to retrieving values for these properties. They are included by default in GET. The recommended method to use this API is to filter and retrieve only the required fields. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `origins.ip_address` - IP address of origin.
* `origins.size` - Physical size of origin.
* `origins.state` - State of origin.
* `size` - Physical size of FlexCache.
* `guarantee.type` - Space guarantee style of FlexCache.
* `aggregates.name` or `aggregates.uuid` - Name or UUID of aggregrate of FlexCache volume.
* `path` - Fully-qualified path of the owning SVM's namespace where the FlexCache is mounted.
### Related ONTAP commands
* `volume flexcache show`
### Learn more
* [`DOC /storage/flexcache/flexcaches`](#docs-storage-storage_flexcache_flexcaches)
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
        r"""Creates a FlexCache in the cluster.
### Required properties
* `name` - Name of FlexCache volume.
* `origins.volume.name` or `origins.volume.uuid` - Name or UUID of origin volume.
* `origins.svm.name` - Name of origin Vserver.
* `svm.name` or `svm.uuid` - Name or UUID of Vserver where FlexCache will be created.
### Recommended optional properties
* `path` - Path to mount the FlexCache volume
### Default property values
If not specified in POST, the following default property values are assigned:
* `size` - 10% of origin volume size or 1GB per constituent, whichever is greater.
* `guarantee.type` - Same as for a non-FlexCache FlexGroup volume.
* `constituents_per_aggregate` - 4 if aggregates.name or aggregates.uuid is used.
### Related ONTAP commands
* `volume flexcache create`
### Learn more
* [`DOC /storage/flexcache/flexcaches`](#docs-storage-storage_flexcache_flexcaches)
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
        r"""Deletes a FlexCache. If a FlexCache volume is online, it is offlined before deletion.
### Related ONTAP commands
* `volume flexcache delete`
### Learn more
* [`DOC /storage/flexcache/flexcaches`](#docs-storage-storage_flexcache_flexcaches)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


