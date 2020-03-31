# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An S3 server is an object store server that is compatible with the Amazon S3 protocol. In the initial version, only a subset of the protocol features necessary to support Fabric Pool capacity tier usecases are implemented. S3 server allows you to store objects in ONTAP using Amazon S3 protocol. This feature can be used as a target object store server for ONTAP FabricPools.
## Examples
### Retrieving all of the S3 configurations
```
# The API:
/api/protocols/s3/services
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/s3/services?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "cf90b8f2-8071-11e9-8190-0050568eae21",
        "name": "vs2"
      },
      "name": "s1",
      "comment": "S3 server",
      "enabled": false,
    },
    {
      "svm": {
        "uuid": "d7f1219c-7f8e-11e9-9124-0050568eae21",
        "name": "vs1"
      },
      "name": "Server-1",
      "comment": "S3 server",
      "enabled": true,
      "buckets": [
        {
          "uuid": "e08665af-8114-11e9-8190-0050568eae21",
          "name": "bucket-1",
          "volume": {
            "name": "fg_oss_1559026220",
            "uuid": "de146bff-8114-11e9-8190-0050568eae21"
          },
          "size": 209715200,
          "logical_used_size": 157286400,
          "encryption": {
            "enabled": false
          },
          "comment": "s3 bucket"
        },
        {
          "uuid": "fb1912ef-8114-11e9-8190-0050568eae21",
          "name": "bucket-2",
          "volume": {
            "name": "fg_oss_1559026269",
            "uuid": "f9b1cdd0-8114-11e9-8190-0050568eae21"
          },
          "size": 104857600,
          "logical_used_size": 78643200,
          "encryption": {
            "enabled": false
          },
          "comment": "s3 bucket"
        }
      ],
      "users": [
        {
          "name": "user-1",
          "comment": "S3 user",
          "access_key": "3333_w162ypaTi7_aAQuJo76Z16zc9Gz_W3IN83bDQWkcCN3jYU_z_xn20XATMKKa90509KCH__r4lh1IPU58vf1QlWAJt8k2F1BPjPtM6CsDRX_dOP_QZkF5N9fBuz3"
        },
        {
          "name": "user-2",
          "comment": "",
          "access_key": "g6T24qhH92dOA6gc1WTcDO_2oNZhQ6Drl2zu5_s5Id_QK1wLgghgxsD2xP1xqG7oX1T_9AI0D39q65CY3FAg0CbAtVU_903bSnCnht3xqjbrF5_3Cs9RnY8nE_az1Ltc"
        }
      ]
    }
  ],
  "num_records": 2
}
```
### Retrieving all S3 configurations for a particular SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/s3/services/24c2567a-f269-11e8-8852-0050568e5298?fields=*" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "d7f1219c-7f8e-11e9-9124-0050568eae21",
    "name": "vs1"
  },
  "name": "Server-1",
  "comment": "S3 server",
  "enabled": true,
  "buckets": [
    {
      "uuid": "e08665af-8114-11e9-8190-0050568eae21",
      "name": "bucket-1",
      "volume": {
        "name": "fg_oss_1559026220",
        "uuid": "de146bff-8114-11e9-8190-0050568eae21"
      },
      "size": 209715200,
      "logical_used_size": 157286400,
      "encryption": {
        "enabled": false
      },
      "comment": "s3 bucket"
    },
    {
      "uuid": "fb1912ef-8114-11e9-8190-0050568eae21",
      "name": "bucket-2",
      "volume": {
        "name": "fg_oss_1559026269",
        "uuid": "f9b1cdd0-8114-11e9-8190-0050568eae21"
      },
      "size": 1677721600,
      "logical_used_size": 1075838976,
      "encryption": {
        "enabled": false
      },
      "comment": "s3 bucket"
    }
  ],
  "users": [
    {
      "name": "user-1",
      "comment": "s3 user",
      "access_key": "3333_w162ypaTi7_aAQuJo76Z16zc9Gz_W3IN83bDQWkcCN3jYU_z_xn20XATMKKa90509KCH__r4lh1IPU58vf1QlWAJt8k2F1BPjPtM6CsDRX_dOP_QZkF5N9fBuz3"
    },
    {
      "name": "user-2",
      "comment": "",
      "access_key": "g6T24qhH92dOA6gc1WTcDO_2oNZhQ6Drl2zu5_s5Id_QK1wLgghgxsD2xP1xqG7oX1T_9AI0D39q65CY3FAg0CbAtVU_903bSnCnht3xqjbrF5_3Cs9RnY8nE_az1Ltc"
    }
  ]
}
```
### Creating an S3 server, users, and buckets configurations with required fields specified
```
# The API:
/api/protocols/s3/services
# The call:
curl -X POST "https://10.140.103.139/api/protocols/s3/services" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"buckets\": [ { \"name\": \"bucket-1\" }, { \"name\": \"bucket-2\" } ], \"enabled\": true, \"name\": \"Server-1\", \"svm\": { \"uuid\": \"d49ef663-7f8e-11e9-9b2c-0050568e4594\" }, \"users\": [ { \"name\": \"user-1\" }, { \"name\": \"user-2\" } ]}"
# The response:
HTTP/1.1 201 Created
Date: Fri, 31 May 2019 08:44:16 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/protocols/s3/services/
Content-Length: 623
Content-Type: application/hal+json
{
  "num_records": 1,
  "records": [
    {
      "users": [
        {
          "name": "user-1",
          "access_key": "x129aL0q9bu3J_4_2S0OcU34AA5DJXXB_j9R34_60tqiqAS5_c8PAgN6Lg1zkv_76P4IxNWir9st9uhhgldb31u364Cczq_c39C1fUP7HDheUmYY6u4xt61_N7Sw6c33",
          "secret_key": "gh0pYc__43Csnx_Ks4_C0tb_5AfT4HZTfQl8xN8Dl5TjqB90oNt5ZaPO6Hs4h6Q4Fq4B4uq5Cqht82X6vcE32c3uLZB8pXAAx819LWPgpOSwD5xga2RE3czr1qhCd9V6"
        },
        {
          "name": "user-2",
          "access_key": "nntYZrNN65mKn57yS04o1sDp_D0AY58jdwCW573_5x2OPW09AbyFl86DB7r30N2373_bA12n08aovQp8ySItRss9AjsYoSj7TsIiHOW_Y21DaqYPl5I2a849b11y8X4c",
          "secret_key": "bjtsPXV2D8BM6pZNQ9pzmKoXU3qIv2yQ3957dhjK4X7M2dB6Rjtrq1As_8cS_4bSP0jt_P31R5eLdZ_zcBO9Z_ZRMldTc1Bw_5c7LugBnzG2D3xXB91jqLaP2xnKn_Zg"
        }
      ],
      "job": {
        "uuid": "f51675dd-820a-11e9-a762-0050568e4594",
        "_links": {
          "self": {
            "href": "/api/cluster/jobs/f51675dd-820a-11e9-a762-0050568e4594"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/protocols/s3/services/"
        }
      }
    }
  ]
}
```
### Creating an S3 server, users, and buckets configurations
```
# The API:
/api/protocols/s3/services
# The call:
curl -X POST "https://10.140.103.139/api/protocols/s3/services" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"buckets\": [ { \"aggregates\": [ { \"name\": \"aggr1\", \"uuid\": \"1cd8a442-86d1-11e0-ae1c-123478563412\" } ], \"constituents_per_aggregate\": 2, \"name\": \"bucket-1\", \"size\": \"209715200\" }, { \"aggregates\": [ { \"name\": \"aggr1\", \"uuid\": \"1cd8a442-86d1-11e0-ae1c-123478563412\" }, { \"name\": \"aggr2\", \"uuid\": \"982fc4d0-d1a2-4da4-9c47-5b433f24757d\"} ], \"constituents_per_aggregate\": 4, \"name\": \"bucket-2\" } ], \"enabled\": true, \"name\": \"Server-1\", \"svm\": { \"name\": \"vs1\", \"uuid\": \"d49ef663-7f8e-11e9-9b2c-0050568e4594\" }, \"users\": [ { \"name\": \"user-1\" }, { \"name\": \"user-2\" } ]}"
# The response:
HTTP/1.1 201 Created
Date: Fri, 31 May 2019 08:44:16 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/protocols/s3/services/
Content-Length: 623
Content-Type: application/hal+json
{
  "num_records": 1,
  "records": [
    {
      "users": [
        {
          "name": "user-1",
          "access_key": "x129aL0q9bu3J_4_2S0OcU34AA5DJXXB_j9R34_60tqiqAS5_c8PAgN6Lg1zkv_76P4IxNWir9st9uhhgldb31u364Cczq_c39C1fUP7HDheUmYY6u4xt61_N7Sw6c33",
          "secret_key": "gh0pYc__43Csnx_Ks4_C0tb_5AfT4HZTfQl8xN8Dl5TjqB90oNt5ZaPO6Hs4h6Q4Fq4B4uq5Cqht82X6vcE32c3uLZB8pXAAx819LWPgpOSwD5xga2RE3czr1qhCd9V6"
        },
        {
          "name": "user-2",
          "access_key": "nntYZrNN65mKn57yS04o1sDp_D0AY58jdwCW573_5x2OPW09AbyFl86DB7r30N2373_bA12n08aovQp8ySItRss9AjsYoSj7TsIiHOW_Y21DaqYPl5I2a849b11y8X4c",
          "secret_key": "bjtsPXV2D8BM6pZNQ9pzmKoXU3qIv2yQ3957dhjK4X7M2dB6Rjtrq1As_8cS_4bSP0jt_P31R5eLdZ_zcBO9Z_ZRMldTc1Bw_5c7LugBnzG2D3xXB91jqLaP2xnKn_Zg"
        }
      ],
      "job": {
        "uuid": "f51675dd-820a-11e9-a762-0050568e4594",
        "_links": {
          "self": {
            "href": "/api/cluster/jobs/f51675dd-820a-11e9-a762-0050568e4594"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/protocols/s3/services/"
        }
      }
    }
  ]
}
```
### Creating an S3 server configuration
```
# The API:
/api/protocols/s3/services
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/s3/services" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"comment\": \"S3 server\", \"enabled\": true, \"name\": \"Server-1\", \"svm\": { \"name\": \"vs1\", \"uuid\": \"db2ec036-8375-11e9-99e1-0050568e3ed9\" } }"
```
### Disable s3 server for the specified SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/s3/services/03ce5c36-f269-11e8-8852-0050568e5298" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": false }"
```
### Deleting the S3 server for a specified SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/s3/services/a425f10b-ad3b-11e9-b559-0050568e8222?delete_all=false" -H  "accept: application/json"
HTTP/1.1 200 OK
Date: Wed, 14 Aug 2019 07:04:24 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 132
Content-Type: application/json
{
  "num_records": 1,
  "records": [
    {
      "job": {
        "uuid": "bf74ba50-be61-11e9-bea8-0050568e8222"
      }
    }
  ]
}
```
### Deleting all of the S3 server configuration for a specified SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/s3/services/03ce5c36-f269-11e8-8852-0050568e5298?delete_all=true" -H "accept: application/json"
# The response:
HTTP/1.1 200 OK
Date: Sat, 01 Jun 2019 15:46:39 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 132
Content-Type: application/hal+json
{
  "num_records": 1,
  "records": [
    {
      "job": {
        "uuid": "71eaaf02-8484-11e9-91f7-0050568ebc5f"
      }
    }
  ]
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


__all__ = ["S3Service", "S3ServiceSchema"]
__pdoc__ = {
    "S3ServiceSchema.resource": False,
    "S3ServiceSchema.patchable_fields": False,
    "S3ServiceSchema.postable_fields": False,
}


class S3ServiceSchema(ResourceSchema):
    """The fields of the S3Service object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the s3_service. """

    buckets = fields.List(fields.Nested("netapp_ontap.resources.s3_bucket.S3BucketSchema", unknown=EXCLUDE), data_key="buckets")
    r""" The buckets field of the s3_service. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=256),
    )
    r""" Can contain any additional information about the server being created or modified.

Example: S3 server """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies whether the S3 server being created or modified should be up or down. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=0, maximum=15),
    )
    r""" Specifies the name of the S3 server. A server name can contain 0 to 15 characters using only the following combination of characters':' 0-9, A-Z, a-z, ".", and "-".

Example: Server-1 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the s3_service. """

    users = fields.List(fields.Nested("netapp_ontap.resources.s3_user.S3UserSchema", unknown=EXCLUDE), data_key="users")
    r""" The users field of the s3_service. """

    @property
    def resource(self):
        return S3Service

    @property
    def patchable_fields(self):
        return [
            "links",
            "comment",
            "enabled",
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "links",
            "buckets",
            "comment",
            "enabled",
            "name",
            "svm.name",
            "svm.uuid",
            "users",
        ]

class S3Service(Resource):
    r""" Specifies the S3 server configuration. """

    _schema = S3ServiceSchema
    _path = "/api/protocols/s3/services"
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
        r"""Retrieves the S3 server configuration for all SVMs.
### Related ONTAP commands
* `vserver object-store-server show`
### Learn more
* [`DOC /protocols/s3/services`](#docs-object-store-protocols_s3_services)
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
        r"""Updates the S3 Server configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server modify`
### Learn more
* [`DOC /protocols/s3/services`](#docs-object-store-protocols_s3_services)
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
        r"""Deletes the S3 server configuration of an SVM. If the 'delete_all' parameter is set to false, only the S3 server is deleted. Otherwise S3 users and buckets present on the SVM are also deleted. Note that only empty buckets can be deleted. This endpoint returns the S3 server delete job-uuid in response. To monitor the job status follow /api/cluster/jobs/<job-uuid>.
### Related ONTAP commands
* `vserver object-store-server delete`
### Learn more
* [`DOC /protocols/s3/services`](#docs-object-store-protocols_s3_services)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the S3 server configuration for all SVMs.
### Related ONTAP commands
* `vserver object-store-server show`
### Learn more
* [`DOC /protocols/s3/services`](#docs-object-store-protocols_s3_services)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the S3 Server configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server show`
### Learn more
* [`DOC /protocols/s3/services`](#docs-object-store-protocols_s3_services)
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
        r"""Creates an S3 server, users, and buckets configurations.
### Important notes
- Each SVM can have one S3 server configuration.
- One or more buckets and users can also be created using this end-point.
- If creating a user configuration fails, buckets are not created either and already created users are not saved.
- If creating a bucket configuration fails, all buckets already created are saved with no new buckets created.
### Required properties
* `svm.uuid` - Existing SVM in which to create an S3 server configuration.
### Recommended optional properties
* `enabled` - Specifies the state of the server created.
* `comment` - Any information related to the server created.
### Default property values
* `comment` - ""
* `enabled` - _true_
### Related ONTAP commands
* `vserver object-store-server create`
* `vserver object-store-server bucket create`
* `vserver object-store-server user create`
### Learn more
* [`DOC /protocols/s3/services`](#docs-object-store-protocols_s3_services)
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
        r"""Updates the S3 Server configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server modify`
### Learn more
* [`DOC /protocols/s3/services`](#docs-object-store-protocols_s3_services)
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
        r"""Deletes the S3 server configuration of an SVM. If the 'delete_all' parameter is set to false, only the S3 server is deleted. Otherwise S3 users and buckets present on the SVM are also deleted. Note that only empty buckets can be deleted. This endpoint returns the S3 server delete job-uuid in response. To monitor the job status follow /api/cluster/jobs/<job-uuid>.
### Related ONTAP commands
* `vserver object-store-server delete`
### Learn more
* [`DOC /protocols/s3/services`](#docs-object-store-protocols_s3_services)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


