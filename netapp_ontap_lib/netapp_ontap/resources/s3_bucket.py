# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An S3 bucket is a container of objects. Each bucket defines an object namespace. S3 server requests specify objects using a bucket-name and object-name pair. An object consists of data, along with optional metadata and access controls, that is accessible using a name. An object resides within a bucket. There can be more than one bucket in an S3 server. Buckets that are created for the server are associated with an S3 user that is created on the S3 server.
## Examples
### Retrieving all fields for all S3 buckets of a cluster
```
# The API:
/api/protocols/s3/buckets
# The call:
curl -X GET "https://10.140.117.223/api/protocols/s3/buckets?fields=*&return_records=true" -H "accept: application/json"
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
    },
    {
      "svm": {
        "uuid": "ee30eb2d-7ae1-11e9-8abe-0050568ea123",
        "name": "vs2"
      },
      "uuid": "19283b75-7ae2-11e9-8abe-0050568ea123",
      "name": "bucket-3",
      "volume": {
        "name": "fg_oss_1558690257",
        "uuid": "a46a1ea7-7e06-11e9-97e8-0050568ea123"
      },
      "size": 1677721600,
      "logical_used_size": 1075838976,
      "encryption": {
        "enabled": false
      },
      "comment": "bucket3"
    }
  ],
  "num_records": 3
}
```
### Retrieving all S3 buckets of a cluster ordered by size
```
# The API:
/api/protocols/s3/buckets
# The call:
curl -X GET "https://10.140.117.223/api/protocols/s3/buckets?return_records=true&order_by=size" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "12f3ba4c-7ae0-11e9-8c06-0050568ea123",
        "name": "vs1"
      },
      "uuid": "754389d0-7e13-11e9-bfdc-0050568ea123",
      "name": "bb1",
      "size": 83886080
    },
    {
      "svm": {
        "uuid": "ee30eb2d-7ae1-11e9-8abe-0050568ea123",
        "name": "vs2"
      },
      "uuid": "19283b75-7ae2-11e9-8abe-0050568ea123",
      "name": "bb2",
      "size": 838860800
    },
    {
      "svm": {
        "uuid": "12f3ba4c-7ae0-11e9-8c06-0050568ea123",
        "name": "vs1"
      },
      "uuid": "a8234aec-7e06-11e9-97e8-0050568ea123",
      "name": "bucket-1",
      "size": 1677721600
    }
  ],
  "num_records": 3
}
```
### Retrieving all S3 buckets of a cluster with name  "bb2"
```
# The API:
/api/protocols/s3/buckets
# The call:
curl -X GET "https://10.140.117.223/api/protocols/s3/buckets?name=bb2&return_records=true" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "12f3ba4c-7ae0-11e9-8c06-0050568ea123",
        "name": "vs1"
      },
      "uuid": "087d940e-7e15-11e9-bfdc-0050568ea123",
      "name": "bb2"
    },
    {
      "svm": {
        "uuid": "ee30eb2d-7ae1-11e9-8abe-0050568ea123",
        "name": "vs2"
      },
      "uuid": "19283b75-7ae2-11e9-8abe-0050568ea123",
      "name": "bb2"
    }
  ],
  "num_records": 2
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


__all__ = ["S3Bucket", "S3BucketSchema"]
__pdoc__ = {
    "S3BucketSchema.resource": False,
    "S3BucketSchema.patchable_fields": False,
    "S3BucketSchema.postable_fields": False,
}


class S3BucketSchema(ResourceSchema):
    """The fields of the S3Bucket object"""

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
    r""" The encryption field of the s3_bucket. """

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
    r""" The svm field of the s3_bucket. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Specifies the unique identifier of the bucket.

Example: 414b29a1-3b26-11e9-bd58-0050568ea055 """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the s3_bucket. """

    @property
    def resource(self):
        return S3Bucket

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

class S3Bucket(Resource):
    r""" A bucket is a container of objects. Each bucket defines an object namespace. S3 requests specify objects using a bucket-name and object-name pair. An object resides within a bucket. """

    _schema = S3BucketSchema
    _path = "/api/protocols/s3/buckets"

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
        r"""Retrieves all S3 buckets for all SVMs.
### Related ONTAP commands
* `vserver object-store-server bucket show`
### Learn more
* [`DOC /protocols/s3/buckets`](#docs-object-store-protocols_s3_buckets)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves all S3 buckets for all SVMs.
### Related ONTAP commands
* `vserver object-store-server bucket show`
### Learn more
* [`DOC /protocols/s3/buckets`](#docs-object-store-protocols_s3_buckets)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






