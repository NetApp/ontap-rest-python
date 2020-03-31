# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An S3 user account is created on the S3 server. Buckets that are created for the server are associated with that user (as the owner of the buckets).
The creation of the user account involves generating a pair of keys "access" and "secret".
These keys are shared with clients (by the administrator out of band) who want to access the S3 server. The access_key is sent in the request and it identifies the user performing the operation. The client or server never send the secret_key over the wire.
Only the access_key can be retrieved from a GET operation. The secret_key along with the access_key is returned from a POST operation and from a PATCH operation if the administrator needs to regenerate the keys.
## Examples
### Retrieving S3 user configurations for a particular SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}/users
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users?fields=*&return_records=true" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "db2ec036-8375-11e9-99e1-0050568e3ed9",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/db2ec036-8375-11e9-99e1-0050568e3ed9"
          }
        }
      },
      "name": "user-1",
      "comment": "S3 user",
      "access_key": "8OPlYd5gm53sTNkTNgrsJ0_4iHvw_Ir_9xtDhzGa3m2_a_Yhtv6Bm3Dq_Xv79Stq90BWa5NrTL7UQ2u_0xN0IW_x39cm1h3sn69fN6cf6STA48W05PAxuGED3NcR7rsn",
      "_links": {
        "self": {
          "href": "/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users/user-1"
        }
      }
    },
    {
      "svm": {
        "uuid": "db2ec036-8375-11e9-99e1-0050568e3ed9",
        "name": "vs1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/db2ec036-8375-11e9-99e1-0050568e3ed9"
          }
        }
      },
      "name": "user-2",
      "comment": "s3-user",
      "access_key": "uYo34d4eR8a3is7JDSCY1xrNwL7gFMA338ZEX2mNrgJ34Kb4u98QNhBGT3ghs9GA2bzNdYBSn5_rBfjIY4mt36CMFE4d3g0L3Pa_2nXD6g6CAq_D0422LK__pbH6wvy8",
      "_links": {
        "self": {
          "href": "/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users/user-2"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users?fields=*&return_records=true"
    }
  }
}
```
### Retrieving the user configuration of a specific S3 user
```
# The API:
/api/protocols/s3/services/{svm.uuid}/users/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users/user-1" -H "accept: application/hal+json"
# The response:
{
  "svm": {
    "uuid": "db2ec036-8375-11e9-99e1-0050568e3ed9",
    "name": "vs1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/db2ec036-8375-11e9-99e1-0050568e3ed9"
      }
    }
  },
  "name": "user-1",
  "comment": "s3-user",
  "access_key": "uYo34d4eR8a3is7JDSCY1xrNwL7gFMA338ZEX2mNrgJ34Kb4u98QNhBGT3ghs9GA2bzNdYBSn5_rBfjIY4mt36CMFE4d3g0L3Pa_2nXD6g6CAq_D0422LK__pbH6wvy8",
  "_links": {
    "self": {
      "href": "/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users/user-1"
    }
  }
}
```
### Creating an S3 user configuration
```
# The API:
/api/protocols/s3/services/{svm.uuid}/users
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"name\": \"user-1\"}"
# The response:
HTTP/1.1 201 Created
Date: Fri, 31 May 2019 09:34:25 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users/user-1
Content-Length: 244
Content-Type: application/json
{
  "num_records": 1,
  "records": [
    {
      "name": "user-1",
      "access_key": "8OPlYd5gm53sTNkTNgrsJ0_4iHvw_Ir_9xtDhzGa3m2_a_Yhtv6Bm3Dq_Xv79Stq90BWa5NrTL7UQ2u_0xN0IW_x39cm1h3sn69fN6cf6STA48W05PAxuGED3NcR7rsn",
      "secret_key": "SSS4oNA7_43yfu_zs938T5nY9xYZccFq_60_Q925h4t535km313qb0bDvdQ2MIK_8ebVf0gnD06K8qcNBg3t_KcpjHTXA2elshTEjrdMhsM9b47uOdQGw4Mex6yrbPgr"
    }
  ]
}
```
### Regenerating keys for a specific S3 user for the specified SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}/users/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users/user-2?regenerate_keys=true" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ }"
# The response:
HTTP/1.1 200 OK
Date: Fri, 31 May 2019 09:55:45 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Content-Length: 391
Content-Type: application/hal+json
{
  "num_records": 1,
  "records": [
    {
      "name": "user-2",
      "access_key": "hUod3l_sg632PjPlTgdQNKWXI3E_yTra0h96xrpsAPly3Qa_KmYYXq3kIuAJ3CyD4gVOakjj_PwVIVjATP1C2t1IQ3KB_9ctS1Ph921b1C17N6Y0PtWfv6AZD__j_C4j",
      "secret_key": "3w03fT_7Pv328_dYB8FN4YsD101Hn0i1u_gmqOenYydaNc22c7AIDN46c__T_5y0A3Y69w412F13A1bzJSpXH4C0nNAP4N_Ce1_Z_9_d7bA08bs28ccw50ab_4osA3bq",
      "_links": {
        "self": {
          "href": "/api/protocols/s3/services/db2ec036-8375-11e9-99e1-0050568e3ed9/users/user-2"
        }
      }
    }
  ]
}
```
### Deleting the specified S3 user configuration for a specified SVM
```
# The API:
/api/protocols/s3/services/{svm.uuid}/users/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/s3/services/03ce5c36-f269-11e8-8852-0050568e5298/users/user-2" -H "accept: application/json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["S3User", "S3UserSchema"]
__pdoc__ = {
    "S3UserSchema.resource": False,
    "S3UserSchema.patchable_fields": False,
    "S3UserSchema.postable_fields": False,
}


class S3UserSchema(ResourceSchema):
    """The fields of the S3User object"""

    access_key = fields.Str(
        data_key="access_key",
    )
    r""" Specifies the access key for the user.

Example: Pz3SB54G2B_6dsXQPrA5HrTPcf478qoAW6_Xx6qyqZ948AgZ_7YfCf_9nO87YoZmskxx3cq41U2JAH2M3_fs321B4rkzS3a_oC5_8u7D8j_45N8OsBCBPWGD_1d_ccfq """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=256),
    )
    r""" Can contain any additional information about the user being created or modified.

Example: S3 user """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=64),
    )
    r""" Specifies the name of the user. A user name length can range from 1 to 64 characters and can only contain the following combination of characters 0-9, A-Z, a-z, "_", "+", "=", ",", ".","@", and "-".

Example: user-1 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the s3_user. """

    @property
    def resource(self):
        return S3User

    @property
    def patchable_fields(self):
        return [
            "comment",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "comment",
            "name",
            "svm.name",
            "svm.uuid",
        ]

class S3User(Resource):
    r""" This is a container of S3 users. """

    _schema = S3UserSchema
    _path = "/api/protocols/s3/services/{svm[uuid]}/users"
    @property
    def _keys(self):
        return ["svm.uuid", "name"]

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
        r"""Retrieves the S3 user's SVM configuration.
### Related ONTAP commands
* `vserver object-store-server user show`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/users`](#docs-object-store-protocols_s3_services_{svm.uuid}_users)
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
        r"""Updates the S3 user configuration of an SVM.
### Important notes
- User access_key and secret_key pair can be regenerated using the PATCH operation.
- User access_key and secret_key is returned in a PATCH operation if the "regenerate_keys" field is specified as true.
### Recommended optional properties
* `regenerate_keys` - Specifies if secret_key and access_key need to be regenerated.
* `comment` - Any information related to the S3 user.
### Related ONTAP commands
* `vserver object-store-server user show`
* `vserver object-store-server user regenerate-keys`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/users`](#docs-object-store-protocols_s3_services_{svm.uuid}_users)
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
        r"""Deletes the S3 user configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server user delete`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/users`](#docs-object-store-protocols_s3_services_{svm.uuid}_users)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the S3 user's SVM configuration.
### Related ONTAP commands
* `vserver object-store-server user show`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/users`](#docs-object-store-protocols_s3_services_{svm.uuid}_users)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the S3 user configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server user show`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/users`](#docs-object-store-protocols_s3_services_{svm.uuid}_users)
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
        r"""Creates the S3 user configuration.
### Important notes
- Each SVM can have one or more user configurations.
- If user creation is successful, a user access_key and secret_key is returned as part of the response.
### Required properties
* `svm.uuid` - Existing SVM in which to create the user configuration.
* `name` - User name that is to be created.
### Default property values
* `comment` - ""
### Related ONTAP commands
* `vserver object-store-server user create`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/users`](#docs-object-store-protocols_s3_services_{svm.uuid}_users)
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
        r"""Updates the S3 user configuration of an SVM.
### Important notes
- User access_key and secret_key pair can be regenerated using the PATCH operation.
- User access_key and secret_key is returned in a PATCH operation if the "regenerate_keys" field is specified as true.
### Recommended optional properties
* `regenerate_keys` - Specifies if secret_key and access_key need to be regenerated.
* `comment` - Any information related to the S3 user.
### Related ONTAP commands
* `vserver object-store-server user show`
* `vserver object-store-server user regenerate-keys`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/users`](#docs-object-store-protocols_s3_services_{svm.uuid}_users)
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
        r"""Deletes the S3 user configuration of an SVM.
### Related ONTAP commands
* `vserver object-store-server user delete`
### Learn more
* [`DOC /protocols/s3/services/{svm.uuid}/users`](#docs-object-store-protocols_s3_services_{svm.uuid}_users)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


