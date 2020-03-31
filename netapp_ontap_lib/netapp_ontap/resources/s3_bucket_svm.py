# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An S3 bucket is a container of objects. Each bucket defines an object namespace. S3 server requests specify objects using a bucket-name and object-name pair. An object consists of data, along with optional metadata and access controls, accessible via a name. An object resides within a bucket. There can be more than one bucket in an S3 server. Buckets which are created for the server are associated with an S3 user that is created on the S3 server.
## Examples
### Retrieving all fields for all S3 buckets of an SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}/buckets
# The call:
curl -X GET "https://10.140.117.223/api/protocols/s3/services/12f3ba4c-7ae0-11e9-8c06-0050568ea123/buckets?fields=*&return_records=true" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "12f3ba4c-7ae0-11e9-8c06-0050568ea123",
        "name": "vs1"
      },
      "uuid": "527812ab-7c6d-11e9-97e8-0050568ea123",
      "name": "bucket-2",
      "volume": {
        "name": "fg_oss_1558514455",
        "uuid": "51276f5f-7c6d-11e9-97e8-0050568ea123"
      },
      "size": 209715200,
      "logical_used_size": 157286400,
      "encryption": {
        "enabled": false
      },
      "comment": "S3 bucket."
    },
    {
      "svm": {
        "uuid": "12f3ba4c-7ae0-11e9-8c06-0050568ea123",
        "name": "vs1"
      },
      "uuid": "a8234aec-7e06-11e9-97e8-0050568ea123",
      "name": "bucket-1",
      "volume": {
        "name": "fg_oss_1558690256",
        "uuid": "a36a1ea7-7e06-11e9-97e8-0050568ea123"
      },
      "size": 1677721600,
      "logical_used_size": 0,
      "encryption": {
        "enabled": false
      },
      "comment": "bucket1"
    }
  ],
  "num_records": 2
}
```
### Retrieving the specified bucket associated with an SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}/buckets/{uuid}
# The call:
curl -X GET "https://10.140.117.223/api/protocols/s3/services/12f3ba4c-7ae0-11e9-8c06-0050568ea123/buckets/527812ab-7c6d-11e9-97e8-0050568ea123" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "12f3ba4c-7ae0-11e9-8c06-0050568ea123",
    "name": "vs1"
  },
  "uuid": "527812ab-7c6d-11e9-97e8-0050568ea123",
  "name": "bucket-2",
  "volume": {
    "name": "fg_oss_1558514455",
    "uuid": "51276f5f-7c6d-11e9-97e8-0050568ea123"
  },
  "size": 209715200,
  "logical_used_size": 157286400,
  "encryption": {
    "enabled": false
  },
  "comment": "S3 bucket."
}
```
### Creating an S3 bucket for an SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}/buckets
# The call:
curl -iku admin:netapp1! -X POST "https://10.140.117.223/api/protocols/s3/services/12f3ba4c-7ae0-11e9-8c06-0050568ea123/buckets?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"aggregates\": [ { \"name\": \"aggr5\", \"uuid\": \"12f3ba4c-7ae0-11e9-8c06-0050568ea123\" } ], \"comment\": \"S3 bucket.\", \"constituents_per_aggregate\": 1, \"name\": \"bucket-3\"}"
# The response:
HTTP/1.1 202 Accepted
Date: Fri, 24 May 2019 11:22:14 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/protocols/s3/services/12f3ba4c-7ae0-11e9-8c06-0050568ea123/buckets/?name=bucket-3
Content-Length: 353
Content-Type: application/json
{
  "num_records": 1,
  "records": [
    {
      "name": "bucket-3",
      "comment": "S3 bucket."
    }
  ],
  "job": {
    "uuid": "2e880171-7e16-11e9-bfdc-0050568ea123",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/2e880171-7e16-11e9-bfdc-0050568ea123"
      }
    }
  }
}
```
### Updating an S3 bucket for an SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}/buckets/{uuid}
# The call:
curl -X PATCH "https://10.140.117.223/api/protocols/s3/services/12f3ba4c-7ae0-11e9-8c06-0050568ea123/buckets/754389d0-7e13-11e9-bfdc-0050568ea122" -H "accept: application/json?return_records=true" -H "Content-Type: application/json" -d "{ \"comment\": \"Bucket modified.\", \"size\": 111111111111}"
# The response:
HTTP/1.1 202 Accepted
Date: Fri, 24 May 2019 11:32:27 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 189
Content-Type: application/json
{
  "job": {
    "uuid": "9beafabb-7e17-11e9-bfdc-0050568ea123",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/9beafabb-7e17-11e9-bfdc-0050568ea123"
      }
    }
  }
}
```
### Deleting an S3 bucket for a specified SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}/buckets/{uuid}
# The call:
curl -iku admin:netapp1! -X DELETE "https://10.140.117.223/api/protocols/s3/services/12f3ba4c-7ae0-11e9-8c06-0050568ea123/buckets/754389d0-7e13-11e9-bfdc-0050568ea123?return_records=true" -H "accept: application/json"
# The response:
HTTP/1.1 202 Accepted
Date: Fri, 24 May 2019 11:40:17 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 189
Content-Type: application/json
{
  "job": {
    "uuid": "b3af4a54-7e18-11e9-bfdc-0050568ea123",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/b3af4a54-7e18-11e9-bfdc-0050568ea123"
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


__all__ = ["S3BucketSvm", "S3BucketSvmSchema"]
__pdoc__ = {
    "S3BucketSvmSchema.resource": False,
    "S3BucketSvmSchema.patchable_fields": False,
    "S3BucketSvmSchema.postable_fields": False,
}


class S3BucketSvmSchema(ResourceSchema):
    """The fields of the S3BucketSvm object"""

    aggregates = fields.List(fields.Nested("netapp_ontap.resources.aggregate.AggregateSchema", unknown=EXCLUDE), data_key="aggregates")
    r""" A list of aggregates for FlexGroup volume constituents where the bucket is hosted. If this option is not specified, the bucket is auto-provisioned as a FlexGroup volume. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=256),
    )
    r""" Can contain any additional information about the bucket being created or modified.

Example: S3 bucket. """

    constituents_per_aggregate = fields.Integer(
        data_key="constituents_per_aggregate",
        validate=integer_validation(minimum=1, maximum=1000),
    )
    r""" Specifies the number of constituents or FlexVol volumes per aggregate. A FlexGroup volume consisting of all such constituents across all specified aggregates is created. This option is used along with the aggregates option and cannot be used independently.

Example: 4 """

    encryption = fields.Nested("netapp_ontap.models.s3_bucket_encryption.S3BucketEncryptionSchema", data_key="encryption", unknown=EXCLUDE)
    r""" The encryption field of the s3_bucket_svm. """

    logical_used_size = fields.Integer(
        data_key="logical_used_size",
    )
    r""" Specifies the bucket logical used size up to this point. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=3, maximum=63),
    )
    r""" Specifies the name of the bucket. Bucket name is a string that can only contain the following combination of ASCII-range alphanumeric characters 0-9, a-z, ".", and "-".

Example: bucket-1 """

    size = fields.Integer(
        data_key="size",
        validate=integer_validation(minimum=83886080, maximum=70368744177664),
    )
    r""" Specifies the bucket size in bytes; ranges from 80MB to 64TB.

Example: 1677721600 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the s3_bucket_svm. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Specifies the unique identifier of the bucket.

Example: 414b29a1-3b26-11e9-bd58-0050568ea055 """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the s3_bucket_svm. """

    @property
    def resource(self):
        return S3BucketSvm

    @property
    def patchable_fields(self):
        return [
            "comment",
            "encryption",
            "size",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "aggregates.name",
            "aggregates.uuid",
            "comment",
            "constituents_per_aggregate",
            "encryption",
            "name",
            "size",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

class S3BucketSvm(Resource):
    r""" A bucket is a container of objects. Each bucket defines an object namespace. S3 requests specify objects using a bucket-name and object-name pair. An object resides within a bucket. """

    _schema = S3BucketSvmSchema
    _path = "/api/protocols/s3/services/{svm[uuid]}/buckets"
    @property
    def _keys(self):
        return ["svm.uuid", "uuid"]

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
        r"""Retrieves the S3 bucket's configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server bucket show`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/buckets`](#docs-object-store-protocols_s3_services_{svm.uuid}_buckets)
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
        r"""Updates the S3 bucket configuration of an SVM.
### Important notes
- The following fields can be modified for a bucket:
  * `comment` - Any information related to the bucket.
  * `size` - Bucket size.
### Related ONTAP commands
* `vserver object-store-server bucket modify`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/buckets`](#docs-object-store-protocols_s3_services_{svm.uuid}_buckets)
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
        r"""Deletes the S3 bucket configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server bucket delete`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/buckets`](#docs-object-store-protocols_s3_services_{svm.uuid}_buckets)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the S3 bucket's configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server bucket show`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/buckets`](#docs-object-store-protocols_s3_services_{svm.uuid}_buckets)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the S3 bucket configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server bucket show`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/buckets`](#docs-object-store-protocols_s3_services_{svm.uuid}_buckets)
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
        r"""Creates the S3 bucket configuration of an SVM.
### Important notes
- Each SVM can have one or more bucket configurations.
- Aggregate lists should be specified explicitly. If not specified, then the bucket is auto-provisioned as a FlexGroup.
- Constituents per aggregate specifies the number of components (or FlexVols) per aggregate. Is specified only when an aggregate list is explicitly defined.
### Required properties
* `svm.uuid` - Existing SVM in which to create the bucket configuration.
* `name` - Bucket name that is to be created.
### Recommended optional properties
* `aggregates` - List of aggregates for the FlexGroup on which the bucket is hosted on.
* `constituents_per_aggregate` - Number of constituents per aggregate.
* `size` - Specifying the bucket size is recommended.
### Default property values
* `size` - 800MB
* `comment` - ""
* `aggregates` - No default value.
* `constituents_per_aggregate` - _4_ , if an aggregates list is specified. Otherwise, no default value.
### Related ONTAP commands
* `vserver object-store-server bucket create`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/buckets`](#docs-object-store-protocols_s3_services_{svm.uuid}_buckets)
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
        r"""Updates the S3 bucket configuration of an SVM.
### Important notes
- The following fields can be modified for a bucket:
  * `comment` - Any information related to the bucket.
  * `size` - Bucket size.
### Related ONTAP commands
* `vserver object-store-server bucket modify`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/buckets`](#docs-object-store-protocols_s3_services_{svm.uuid}_buckets)
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
        r"""Deletes the S3 bucket configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server bucket delete`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/buckets`](#docs-object-store-protocols_s3_services_{svm.uuid}_buckets)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


