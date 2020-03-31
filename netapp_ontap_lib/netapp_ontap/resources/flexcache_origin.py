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
The following relationship configurations are supported:

* Intra-Vserver where FlexCache and the corresponding origin volume reside in the same Vserver.
* Cross-Vserver but intra-cluster where FlexCache and the origin volume reside in the same cluster but belong to different Vservers.
* Cross-cluster where FlexCache and the origin volume reside in different clusters.</br>
FlexCache supports fan-out and more than one FlexCache can be created from one origin volume.
This API retrieves the origin of FlexCache onfigurations in the origin cluster.
## FlexCache APIs
The following APIs can be used to perform operations related to the origin of a FlexCache:

* GET       /api/storage/flexcache/origins
* GET       /api/storage/flexcache/origins/{uuid}
## Examples
### Retrieving origins of FlexCache attributes
The GET request is used to retrieve the origins of FlexCache attributes.
```
# The API:
/api/storage/flexcache/origins
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/flexcache/origins?" -H  "accept: application/json"
# The response:
  {
    "records": [
      {
        "uuid": "2bc957dd-2617-4afb-8d2f-66ac6070d313",
        "name": "vol_o1",
        "_links": {
          "self": {
            "href": "/api/storage/flexcache/origins/2bc957dd-2617-4afb-8d2f-66ac6070d313"
          }
        }
      },
      {
        "uuid": "80fcaee4-0dc2-488b-afb8-86d28a34cda8",
        "name": "vol_1",
        "_links": {
          "self": {
            "href": "/api/storage/flexcache/origins/80fcaee4-0dc2-488b-afb8-86d28a34cda8"
          }
        }
      }
    ],
    "num_records": 2,
    "_links": {
      "self": {
        "href": "/api/storage/flexcache/origins?"
      }
    }
  }
```
### Retrieving the attributes of an origin volume
The GET request is used to retrieve the attributes of an origin volume.
```
# The API:
/api/storage/flexcache/origins/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/flexcache/origins/80fcaee4-0dc2-488b-afb8-86d28a34cda8" -H  "accept: application/json"
# The response:
  {
    "uuid": "80fcaee4-0dc2-488b-afb8-86d28a34cda8",
    "name": "vol_1",
    "svm": {
      "name": "vs_3",
      "uuid": "8aa2cd28-0e92-11e9-b391-0050568e4115"
    },
    "flexcaches": [
      {
        "ip_address": "10.140.103.183",
        "create_time": "2019-01-02T19:27:22+05:30",
        "volume": {
          "name": "fc_42",
          "uuid": "4e7f9d49-0e96-11e9-aed0-0050568eddbe"
        },
        "svm": {
          "name": "vs_1_4",
          "uuid": "36f68322-0e93-11e9-aed0-0050568eddbe"
        },
        "cluster": {
          "name": "node4",
          "uuid": "c32f16b8-0e90-11e9-aed0-0050568eddbe"
        }
      },
      {
        "ip_address": "10.140.103.183",
        "create_time": "2019-01-02T21:08:34+05:30",
        "volume": {
          "name": "fc_421",
          "uuid": "71ee8f36-0ea4-11e9-aed0-0050568eddbe"
        },
        "svm": {
          "name": "vs_1_4",
          "uuid": "36f68322-0e93-11e9-aed0-0050568eddbe"
        },
        "cluster": {
          "name": "node4",
          "uuid": "c32f16b8-0e90-11e9-aed0-0050568eddbe"
        }
      },
      {
        "ip_address": "10.140.103.183",
        "create_time": "2019-01-03T11:14:38+05:30",
        "volume": {
          "name": "fc_422"
        },
        "svm": {
          "name": "vs_1_4",
          "uuid": "36f68322-0e93-11e9-aed0-0050568eddbe"
        },
        "cluster": {
          "name": "node4",
          "uuid": "c32f16b8-0e90-11e9-aed0-0050568eddbe"
        }
      },
      {
        "ip_address": "10.140.103.179",
        "size": 4294967296,
        "create_time": "2019-01-02T19:24:14+05:30",
        "state": "online",
        "volume": {
          "name": "fc_32",
          "uuid": "ddb42bbc-0e95-11e9-8180-0050568e0b79"
        },
        "svm": {
          "name": "vs_1",
          "uuid": "e708fbe2-0e92-11e9-8180-0050568e0b79"
        },
        "cluster": {
          "name": "node3",
          "uuid": "8eb21b3b-0e90-11e9-8180-0050568e0b79"
        }
      },
      {
        "ip_address": "10.140.103.179",
        "size": 4294967296,
        "create_time": "2019-01-02T21:07:23+05:30",
        "state": "online",
        "volume": {
          "name": "fc_321",
          "uuid": "47902654-0ea4-11e9-8180-0050568e0b79"
        },
        "svm": {
          "name": "vs_1",
          "uuid": "e708fbe2-0e92-11e9-8180-0050568e0b79"
        },
        "cluster": {
          "name": "node3",
          "uuid": "8eb21b3b-0e90-11e9-8180-0050568e0b79"
        }
      },
      {
        "ip_address": "10.140.103.179",
        "size": 4294967296,
        "create_time": "2019-01-03T00:11:38+05:30",
        "state": "online",
        "volume": {
          "name": "fc_322",
          "uuid": "04d5e07b-0ebe-11e9-8180-0050568e0b79"
        },
        "svm": {
          "name": "vs_1",
          "uuid": "e708fbe2-0e92-11e9-8180-0050568e0b79"
        },
        "cluster": {
          "name": "node3",
          "uuid": "8eb21b3b-0e90-11e9-8180-0050568e0b79"
        }
      },
      {
        "ip_address": "10.140.103.179",
        "size": 4294967296,
        "create_time": "2019-01-03T00:14:52+05:30",
        "state": "online",
        "volume": {
          "name": "fc_323",
          "uuid": "77e911ff-0ebe-11e9-8180-0050568e0b79"
        },
        "svm": {
          "name": "vs_1",
          "uuid": "e708fbe2-0e92-11e9-8180-0050568e0b79"
        },
        "cluster": {
          "name": "node3",
          "uuid": "8eb21b3b-0e90-11e9-8180-0050568e0b79"
        }
      }
    ],
    "_links": {
      "self": {
        "href": "/api/storage/flexcache/origins/80fcaee4-0dc2-488b-afb8-86d28a34cda8"
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


__all__ = ["FlexcacheOrigin", "FlexcacheOriginSchema"]
__pdoc__ = {
    "FlexcacheOriginSchema.resource": False,
    "FlexcacheOriginSchema.patchable_fields": False,
    "FlexcacheOriginSchema.postable_fields": False,
}


class FlexcacheOriginSchema(ResourceSchema):
    """The fields of the FlexcacheOrigin object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the flexcache_origin. """

    flexcaches = fields.List(fields.Nested("netapp_ontap.models.flexcache_relationship.FlexcacheRelationshipSchema", unknown=EXCLUDE), data_key="flexcaches")
    r""" The flexcaches field of the flexcache_origin. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=203),
    )
    r""" Origin volume name

Example: vol1, vol_2 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the flexcache_origin. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Origin volume UUID. Unique identifier for origin of FlexCache.

Example: 1cd8a442-86d1-11e0-ae1c-123478563512 """

    @property
    def resource(self):
        return FlexcacheOrigin

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "flexcaches",
            "name",
            "svm.name",
            "svm.uuid",
        ]

class FlexcacheOrigin(Resource):
    r""" Defines the origin endpoint of FlexCache. """

    _schema = FlexcacheOriginSchema
    _path = "/api/storage/flexcache/origins"
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
        r"""Retrieves origin of FlexCache in the cluster.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `flexcaches.ip_address` - IP address of FlexCache.
* `flexcaches.size` - Physical size of FlexCache.
* `flexcaches.guarantee.type` - Space guarantee style of FlexCache.
* `flexcaches.state` - State of FlexCache.
### Related ONTAP commands
* `volume flexcache origin show-caches`
### Learn more
* [`DOC /storage/flexcache/origins`](#docs-storage-storage_flexcache_origins)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves origin of FlexCache in the cluster.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `flexcaches.ip_address` - IP address of FlexCache.
* `flexcaches.size` - Physical size of FlexCache.
* `flexcaches.guarantee.type` - Space guarantee style of FlexCache.
* `flexcaches.state` - State of FlexCache.
### Related ONTAP commands
* `volume flexcache origin show-caches`
### Learn more
* [`DOC /storage/flexcache/origins`](#docs-storage-storage_flexcache_origins)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves attributes of the origin of a FlexCache in the cluster.
### Expensive properties
There is an added cost to retrieving values for these properties. They are included by default in GET results. The recommended method to use this API is to filter and retrieve only the required fields. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `flexcaches.ip_address` - IP address of FlexCache.
* `flexcaches.size` - Physical size of FlexCache.
* `flexcaches.guarantee.type` - Space guarantee style of FlexCache.
* `flexcaches.state` - State of FlexCache.
### Related ONTAP commands
* `volume flexcache origin show-caches`
### Learn more
* [`DOC /storage/flexcache/origins`](#docs-storage-storage_flexcache_origins)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





