# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
An iSCSI credentials object defines authentication credentials to be used between an initiator and ONTAP. It identifies an authentication type, user names, and passwords that must be used to authenticate a specific initiator.<br/>
The iSCSI credentials REST API allows you to create, update, delete, and discover iSCSI credentials.<br/>
## How iSCSI authentication works
An iSCSI credentials object defines the authentication credentials to be used between an initiator and ONTAP. While establishing an iSCSI connection, the initiator sends a login request to ONTAP to begin an iSCSI session. ONTAP then either permits or denies the login request, or determines that a login is not required.<p/>
For an initiator, you can specify an authentication type, user names and passwords, and a whitelist of optional network addresses from which the initiator is allowed to connect.
## iSCSI authentication methods
  - Challenge-Handshake Authentication Protocol (CHAP) - The initiator logs in using a CHAP user name and password. There are two types of CHAP user names and passwords:
    - Inbound - ONTAP authenticates the initiator. Inbound settings are required if you are using CHAP authentication.
    - Outbound - These are optional credentials to enable the initiator to authenticate ONTAP. You can use credentials only if inbound credentials are also being used.
  - deny - The initiator is denied access to ONTAP.
  - none - ONTAP does not require authentication for the initiator.
The CHAP inbound/outbound password can be any valid string or an even number of valid hexidecimal digits preceded by '0X' or '0x'.
## Initiator address list
The initiator address list is a way to specify valid IP addresses from which the initiator is allowed to connect. If the list is specified and the source address of an iSCSI connection is not in the list, the connection is rejected. Initiator addresses can be specified in either IPv4 or IPv6 format and in one of two forms:
- Range
  ```
  {
    "start": "192.168.0.0",
    "end": "192.168.0.255"
  }
  ```
- Mask
  ```
  {
    "address": "192.168.0.0",
    "netmask": "24"
  }
  ```
## Initiator "default"
The default iSCSI authentication definition is created when the iSCSI service is created. An iSCSI credentials object with _default_ as the initiator name identifies the default authentication for an SVM. The default credentials are used for any initiator that does not have specific iSCSI credentials. The default iSCSI authentication method is _none_, but can be changed to _deny_ or _CHAP_. The default credentials object does not support an initiator address list.
## Examples
### Creating iSCSI credentials requiring no authentication
```
# The API:
POST /api/protocols/san/iscsi/credentials
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/san/iscsi/credentials' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "initiator": "iqn.1992-08.com.netapp:initiator1", "authentication_type": "none" }'
```
---
### Creating iSCSI credentials using CHAP inbound authentication
```
# The API:
POST /api/protocols/san/iscsi/credentials
# The call:
curl -X POST 'https://<mgmt-ip>/api/protocols/san/iscsi/credentials' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "initiator": "iqn.1992-08.com.netapp:initiator2", "authentication_type": "CHAP", "chap": { "inbound": { "user": "user1", "password": "password1" } } }'
```
---
### Retrieving all properties of all iSCSI credentials
The `fields` query parameter is used to request all iSCSI credentials properties.<br/>
Passwords are not included in the GET output.
<br/>
```
# The API:
GET /api/protocols/san/iscsi/credentials
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/iscsi/credentials?fields=*' -H 'accept: application/hal+json'
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
      "initiator": "default",
      "authentication_type": "none",
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/credentials/19d04b8e-94d7-11e8-8370-005056b48fd2/default"
        }
      }
    },
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
      "initiator": "iqn.1992-08.com.netapp:initiator1",
      "authentication_type": "none",
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/credentials/19d04b8e-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator1"
        }
      }
    },
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
      "initiator": "iqn.1992-08.com.netapp:initiator2",
      "authentication_type": "chap",
      "chap": {
        "inbound": {
          "user": "user1"
        }
      },
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/credentials/19d04b8e-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator2"
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
      "initiator": "default",
      "authentication_type": "none",
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/credentials/25f617cf-94d7-11e8-8370-005056b48fd2/default"
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
      "initiator": "iqn.1992-08.com.netapp:initiator2",
      "authentication_type": "none",
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/credentials/25f617cf-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator2"
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
      "initiator": "iqn.1992-08.com.netapp:initiator3",
      "authentication_type": "deny",
      "_links": {
        "self": {
          "href": "/api/protocols/san/iscsi/credentials/25f617cf-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator3"
        }
      }
    }
  ],
  "num_records": 6,
  "_links": {
    "self": {
      "href": "/api/protocols/san/iscsi/credentials?fields=*"
    }
  }
}
```
---
### Retrieving specific iSCSI credentials
```
# The API:
GET /api/protocols/san/iscsi/credentials/{svm.uuid}/{initiator}
# The call:
curl -X GET 'https://<mgmt-ip>/api/protocols/san/iscsi/credentials/25f617cf-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator2' -H 'accept: application/hal+json'
# The response:
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
  "initiator": "iqn.1992-08.com.netapp:initiator2",
  "authentication_type": "chap",
  "chap": {
    "inbound": {
      "user": "user1"
    }
  },
  "_links": {
    "self": {
      "href": "/api/protocols/san/iscsi/credentials/25f617cf-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator2"
    }
  }
}
```
---
### Updating the authentication type of iSCSI credentials
```
# The API:
PATCH /api/protocols/san/iscsi/credentials/{svm.uuid}/{initiator}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/protocols/san/iscsi/credentials/25f617cf-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator2' -H 'accept: application/hal+json' -d '{ "authentication_type": "chap", "chap": { "inbound": { "user": "user1", "password": "password1" } } }'
```
---
### Updating the initiator address list of iSCSI credentials
```
# The API:
PATCH /api/protocols/san/iscsi/credentials/{svm.uuid}/{initiator}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/protocols/san/iscsi/credentials/25f617cf-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator2' -H 'accept: application/hal+json' -d '{ "initiator_address": { "ranges": [ { "start": "192.168.0.0", "end": "192.168.255.255" } ] } }'
```
---
### Deleting iSCSI credentials
```
# The API:
DELETE /api/protocols/san/iscsi/credentials/{svm.uuid}/{initiator}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/protocols/san/iscsi/credentials/25f617cf-94d7-11e8-8370-005056b48fd2/iqn.1992-08.com.netapp:initiator2' -H 'accept: application/hal+json'
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["IscsiCredentials", "IscsiCredentialsSchema"]
__pdoc__ = {
    "IscsiCredentialsSchema.resource": False,
    "IscsiCredentialsSchema.patchable_fields": False,
    "IscsiCredentialsSchema.postable_fields": False,
}


class IscsiCredentialsSchema(ResourceSchema):
    """The fields of the IscsiCredentials object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the iscsi_credentials. """

    authentication_type = fields.Str(
        data_key="authentication_type",
        validate=enum_validation(['chap', 'none', 'deny']),
    )
    r""" The iSCSI authentication type. Required in POST and optional in PATCH.

Valid choices:

* chap
* none
* deny """

    chap = fields.Nested("netapp_ontap.models.iscsi_credentials_chap.IscsiCredentialsChapSchema", data_key="chap", unknown=EXCLUDE)
    r""" The chap field of the iscsi_credentials. """

    initiator = fields.Str(
        data_key="initiator",
    )
    r""" The iSCSI initiator to which the credentials apply. Required in POST.


Example: iqn.1998-01.com.corp.iscsi:name1 """

    initiator_address = fields.Nested("netapp_ontap.models.iscsi_credentials_initiator_address.IscsiCredentialsInitiatorAddressSchema", data_key="initiator_address", unknown=EXCLUDE)
    r""" The initiator_address field of the iscsi_credentials. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the iscsi_credentials. """

    @property
    def resource(self):
        return IscsiCredentials

    @property
    def patchable_fields(self):
        return [
            "authentication_type",
            "chap",
            "initiator_address",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "authentication_type",
            "chap",
            "initiator",
            "initiator_address",
            "svm.name",
            "svm.uuid",
        ]

class IscsiCredentials(Resource):
    """Allows interaction with IscsiCredentials objects on the host"""

    _schema = IscsiCredentialsSchema
    _path = "/api/protocols/san/iscsi/credentials"
    @property
    def _keys(self):
        return ["svm.uuid", "initiator"]

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
        r"""Retrieves iSCSI credentials.
### Related ONTAP commands
* `vserver iscsi security show`
### Learn more
* [`DOC /protocols/san/iscsi/credentials`](#docs-SAN-protocols_san_iscsi_credentials)
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
        r"""Updates specified iSCSI credentials.
### Related ONTAP commands
* `vserver iscsi security add-initiator-address-ranges`
* `vserver iscsi security default`
* `vserver iscsi security modify`
* `vserver iscsi security remove-initiator-address-ranges`
### Learn more
* [`DOC /protocols/san/iscsi/credentials`](#docs-SAN-protocols_san_iscsi_credentials)
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
        r"""Deletes specified iSCSI credentials.
### Related ONTAP commands
* `vserver iscsi security delete`
### Learn more
* [`DOC /protocols/san/iscsi/credentials`](#docs-SAN-protocols_san_iscsi_credentials)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves iSCSI credentials.
### Related ONTAP commands
* `vserver iscsi security show`
### Learn more
* [`DOC /protocols/san/iscsi/credentials`](#docs-SAN-protocols_san_iscsi_credentials)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves specified iSCSI credentials.
### Related ONTAP commands
* `vserver iscsi security show`
### Learn more
* [`DOC /protocols/san/iscsi/credentials`](#docs-SAN-protocols_san_iscsi_credentials)
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
        r"""Creates iSCSI credentials.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the iSCSI credentials.
* `initiator` - Initiator for which the iSCSI credentials are to be created.
* `authentication_type` - Type of authentication to use for the credentials.
### Recommended optional properties
* `chap.inbound.user` - In-bound CHAP authentication user name.
* `chap.inbound.password` - In-bound CHAP authentication password.
* `chap.outbound.user` - Out-bound CHAP authentication user name.
* `chap.outbound.password` - Out-bound CHAP authentication password.
### Related ONTAP commands
* `vserver iscsi security create`
### Learn more
* [`DOC /protocols/san/iscsi/credentials`](#docs-SAN-protocols_san_iscsi_credentials)
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
        r"""Updates specified iSCSI credentials.
### Related ONTAP commands
* `vserver iscsi security add-initiator-address-ranges`
* `vserver iscsi security default`
* `vserver iscsi security modify`
* `vserver iscsi security remove-initiator-address-ranges`
### Learn more
* [`DOC /protocols/san/iscsi/credentials`](#docs-SAN-protocols_san_iscsi_credentials)
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
        r"""Deletes specified iSCSI credentials.
### Related ONTAP commands
* `vserver iscsi security delete`
### Learn more
* [`DOC /protocols/san/iscsi/credentials`](#docs-SAN-protocols_san_iscsi_credentials)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


