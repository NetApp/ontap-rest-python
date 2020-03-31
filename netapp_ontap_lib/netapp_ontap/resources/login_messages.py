# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
You can use this API to display and manage the login messages configuration. The GET request retrieves all of the login messages in the cluster. GET operations on /security/login/messages/{uuid} retrieve the login messages configuration by UUID. PATCH operations on /security/login/messages/{uuid} update the login messages configuration by UUID.
<br />
---
## Examples
### Retrieving all of the login messages in the cluster
---
```
# The API:
/api/security/login/messages
# The call:
curl -X GET "https://<mgmt-ip>/api/security/login/messages?fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "2581e5aa-9fe3-11e8-b309-005056bbef18",
      "scope": "cluster",
      "banner": "*** WARNING: DO NOT PROCEED IF YOU ARE NOT AUTHORIZED! ****\n",
      "message": "#### Welcome to Cluster X ####\n",
      "show_cluster_message": true,
      "_links": {
        "self": {
          "href": "/api/security/login/messages/2581e5aa-9fe3-11e8-b309-005056bbef18"
        }
      }
    },
    {
      "uuid": "7b1b3715-9ffa-11e8-a5dd-005056bbef18",
      "scope": "svm",
      "svm": {
        "uuid": "7b1b3715-9ffa-11e8-a5dd-005056bbef18",
        "name": "svm1"
      },
      "message": "#### Welcome to SVM1 ####\n",
      "show_cluster_message": true,
      "_links": {
        "self": {
          "href": "/api/security/login/messages/7b1b3715-9ffa-11e8-a5dd-005056bbef18"
        }
      }
    },
    {
      "uuid": "8ddee11e-a58c-11e8-85e0-005056bbef18",
      "scope": "svm",
      "svm": {
        "uuid": "8ddee11e-a58c-11e8-85e0-005056bbef18",
        "name": "svm3"
      },
      "banner": "*** WARNING: This system is for the use of authorized users only. ****\n",
      "_links": {
        "self": {
          "href": "/api/security/login/messages/8ddee11e-a58c-11e8-85e0-005056bbef18"
        }
      }
    },
    {
      "uuid": "f7e41c99-9ffa-11e8-a5dd-005056bbef18",
      "scope": "svm",
      "svm": {
        "uuid": "f7e41c99-9ffa-11e8-a5dd-005056bbef18",
        "name": "svm2"
      },
      "_links": {
        "self": {
          "href": "/api/security/login/messages/f7e41c99-9ffa-11e8-a5dd-005056bbef18"
        }
      }
    }
  ],
  "num_records": 4,
  "_links": {
    "self": {
      "href": "/api/security/login/messages?fields=*"
    }
  }
}
```
---
### Retrieving the login messages configuration at the cluster scope
---
```
# The API:
/api/security/login/messages
# The call:
curl -X GET "https://<mgmt-ip>/api/security/login/messages?scope=cluster&fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "2581e5aa-9fe3-11e8-b309-005056bbef18",
      "scope": "cluster",
      "banner": "*** WARNING: DO NOT PROCEED IF YOU ARE NOT AUTHORIZED! ****\n",
      "message": "#### Welcome to Cluster X ####\n",
      "show_cluster_message": true,
      "_links": {
        "self": {
          "href": "/api/security/login/messages/2581e5aa-9fe3-11e8-b309-005056bbef18"
        }
      }
    ],
  "num_records": 1,
    "_links": {
      "self": {
        "href": "/api/security/login/messages?scope=cluster&fields=*"
    }
  }
}
```
---
### Retrieving the login banner configured at the cluster scope
---
```
# The API:
/api/security/login/messages
# The call:
curl -X GET "https://<mgmt-ip>/api/security/login/messages?scope=cluster&fields=banner" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "2581e5aa-9fe3-11e8-b309-005056bbef18",
      "scope": "cluster",
      "banner": "*** WARNING: DO NOT PROCEED IF YOU ARE NOT AUTHORIZED! ****\n",
      "_links": {
        "self": {
          "href": "/api/security/login/messages/2581e5aa-9fe3-11e8-b309-005056bbef18"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/security/login/messages?scope=cluster&fields=banner"
    }
  }
}
```
---
### Retrieving the login messages configuration of a specific SVM
---
```
# The API:
/api/security/login/messages
# The call:
curl -X GET "https://<mgmt-ip>/api/security/login/messages?svm.name=svm1&fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "7b1b3715-9ffa-11e8-a5dd-005056bbef18",
      "scope": "svm",
      "svm": {
        "uuid": "7b1b3715-9ffa-11e8-a5dd-005056bbef18",
        "name": "svm1"
      },
      "message": "#### Welcome to SVM1 ####\n",
      "show_cluster_message": true,
      "_links": {
        "self": {
          "href": "/api/security/login/messages/7b1b3715-9ffa-11e8-a5dd-005056bbef18"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/security/login/messages?svm.name=svm1&fields=*"
    }
  }
}
```
---
### Retrieving the login messages configuration by UUID, including all fields
---
```
# The API:
/api/security/login/messages/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/security/login/messages/7b1b3715-9ffa-11e8-a5dd-005056bbef18?fields=*" -H "accept: application/hal+json"
# The response:
{
  "uuid": "7b1b3715-9ffa-11e8-a5dd-005056bbef18",
  "scope": "svm",
  "svm": {
    "uuid": "7b1b3715-9ffa-11e8-a5dd-005056bbef18",
    "name": "svm1"
  },
  "message": "#### Welcome to SVM1 ####\n",
  "show_cluster_message": true,
  "_links": {
  "self": {
    "href": "/api/security/login/messages/7b1b3715-9ffa-11e8-a5dd-005056bbef18"
  }
}
```
---
### Configuring the login banner in a cluster
---
```
# The API:
/api/security/login/messages
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/login/messages?scope=cluster" -H "accept: application/hal+json" -H "Content-Type: appplication/json" -d "{ \"banner\": \"You are entering secure area.\" }"
# The response:
{
  "num_records": 1,
  "_links": {
  "self": {
    "href": "/api/security/login/messages?scope=cluster"
  }
}
```
---
### Configuring the message of the day (MOTD) in a cluster
---
```
# The API:
/api/security/login/messages
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/login/messages?scope=cluster" -H "accept: application/hal+json" -H "Content-Type: appplication/json" -d "{ \"message\": \"Welcome to Cluster X\",  \"show_cluster_message\": true }"
# The response:
{
  "num_records": 1,
  "_links": {
  "self": {
    "href": "/api/security/login/messages?scope=cluster"
  }
}
```
---
### Clearing the login banner and message of the day (MOTD) in a cluster
---
```
# The API:
/api/security/login/messages
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/login/messages?scope=cluster" -H "accept: application/hal+json" -H "Content-Type: appplication/json" -d "{ \"banner\": \"\", \"message\": \"\" }"
# The response:
{
  "num_records": 1,
  "_links": {
  "self": {
    "href": "/api/security/login/messages?scope=cluster"
  }
}
```
---
### Configuring the login messages for a specific SVM
---
```
# The API:
/api/security/login/messages
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/login/messages?svm.name=svm1" -H  "accept: application/hal+json" -H  "Content-Type: application/json" -d "{ \"banner\" : \"AUTHORIZED ACCESS ONLY\" }, \"message\": \"WELCOME!\" }"
# The response:
{
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/security/login/messages?svm.name=svm1"
    }
  }
}
```
---
### Configuring the login messages by UUID
---
```
# The API:
/api/security/login/messages/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/login/messages/7b1b3715-9ffa-11e8-a5dd-005056bbef18" -H  "accept: application/hal+json" -H  "Content-Type: application/json" -d "{ \"banner\" : \"AUTHORIZED ACCESS ONLY\" }, \"message\": \"WELCOME!\" }"
```
---
### Clearing the login messages configuration by UUID
---
```
# The API:
/api/security/login/messages/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/login/messages/7b1b3715-9ffa-11e8-a5dd-005056bbef18" -H "accept: application/hal+json" -H "Content-Type: appplication/json" -d "{ \"banner\": \"\", \"message\": \"\" }"
```
---
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["LoginMessages", "LoginMessagesSchema"]
__pdoc__ = {
    "LoginMessagesSchema.resource": False,
    "LoginMessagesSchema.patchable_fields": False,
    "LoginMessagesSchema.postable_fields": False,
}


class LoginMessagesSchema(ResourceSchema):
    """The fields of the LoginMessages object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the login_messages. """

    banner = fields.Str(
        data_key="banner",
        validate=len_validation(minimum=0, maximum=2048),
    )
    r""" The login banner text. This message is displayed during SSH and console device
login just before the password prompt displays. When configured, a cluster-level
login banner is used for every incoming connection. Each data SVM can override
the cluster-level banner to instead display when you log into the SVM. To restore
the default setting for a data SVM, set the banner to an empty string.
New lines are supplied as either LF or CRLF but are always returned as LF.
Optional in the PATCH body. """

    message = fields.Str(
        data_key="message",
        validate=len_validation(minimum=0, maximum=2048),
    )
    r""" The message of the day (MOTD). This message appears just before the clustershell
prompt after a successful login. When configured, the cluster message
displays first. If you log in as a data SVM administrator, the
SVM message is then printed. The cluster-level MOTD can be disabled
for a given data SVM using the "show_cluster_message" property.
New lines are supplied as either LF or CRLF but are always returned as LF.
Optional in the PATCH body. """

    scope = fields.Str(
        data_key="scope",
    )
    r""" The scope field of the login_messages. """

    show_cluster_message = fields.Boolean(
        data_key="show_cluster_message",
    )
    r""" Specifies whether to show a cluster-level message before the SVM message
when logging in as an SVM administrator.
This setting can only be modified by the cluster administrator.
Optional in the PATCH body. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the login_messages. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier (ID) of the login messages configuration. """

    @property
    def resource(self):
        return LoginMessages

    @property
    def patchable_fields(self):
        return [
            "banner",
            "message",
            "scope",
            "show_cluster_message",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "banner",
            "message",
            "scope",
            "show_cluster_message",
            "svm.name",
            "svm.uuid",
        ]

class LoginMessages(Resource):
    r""" The login banner and message of the day (MOTD) configuration. """

    _schema = LoginMessagesSchema
    _path = "/api/security/login/messages"
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
        r"""Retrieves the login banner and messages of the day (MOTD) configured in the cluster
and in specific SVMs.

### Learn more
* [`DOC /security/login/messages`](#docs-security-security_login_messages)"""
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
        r"""Updates the login messages configuration.
There are no required fields. An empty body makes no modifications.

### Learn more
* [`DOC /security/login/messages`](#docs-security-security_login_messages)"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the login banner and messages of the day (MOTD) configured in the cluster
and in specific SVMs.

### Learn more
* [`DOC /security/login/messages`](#docs-security-security_login_messages)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the login messages configuration by UUID.
### Learn more
* [`DOC /security/login/messages`](#docs-security-security_login_messages)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member


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
        r"""Updates the login messages configuration.
There are no required fields. An empty body makes no modifications.

### Learn more
* [`DOC /security/login/messages`](#docs-security-security_login_messages)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



