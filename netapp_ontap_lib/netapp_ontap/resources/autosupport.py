# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
AutoSupport is the NetApp *call home* mechanism. AutoSupport sends configuration details, status details, and error reporting details to NetApp.<p/>
This endpoint supports both GET and PATCH calls. GET is used to retrieve AutoSupport configuration details for the cluster and PATCH is used to modify the AutoSupport configuration of the cluster. You can also use GET calls to check AutoSupport connectivity.
---
## Examples
### Configuring 'to' addresses
The following example configures AutoSupport to send emails to 'to' addresses.
```JSON
# The API:
PATCH /support/autosupport
# The call:
curl -X PATCH "https://<mgmt-ip>/api/support/autosupport" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"to\": [ \"abc@netapp.com\", \"xyz@netapp.com\" ]}"
# The response:
200 OK
{}
```
---
### Configuring 'SMTP' transport
The following example configures AutoSupport to use 'SMTP' transport. The default transport is 'HTTPS'.
```JSON
# The API:
PATCH /support/autosupport
# The call:
curl -X PATCH "https://<mgmt-ip>/api/support/autosupport" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"transport\": \"smtp\"}"
# The response:
200 OK
{}
```
---
### Retrieving the AutoSupport configuration
The following example retrieves AutoSupport configuration for the cluster.
```JSON
# The API:
GET /support/autosupport
# The call:
curl -X GET "https://<mgmt-ip>/api/support/autosupport" -H "accept: application/hal+json" OR
curl -X GET "https://<mgmt-ip>/api/support/autosupport?fields=*" -H "accept: application/hal+json"
# The response:
200 OK
{
  "enabled": true,
  "mail_hosts": [
    "mailhost"
  ],
  "from": "Postmaster",
  "to": [
    "abc@netapp.com",
    "xyz@netapp.com"
  ],
  "contact_support": true,
  "transport": "smtp",
  "proxy_url": "",
  "is_minimal": false,
  "_links": {
    "self": {
      "href": "/api/support/autosupport"
    }
  }
}
```
---
### Retrieving AutoSupport connectivity issues
The following example retrieves AutoSupport connectivity issues for the cluster. The `fields=issues` parameter must be specified, for the response to return connectivity issues. The `corrective_action` section might contain commands which needs to be executed on the ONTAP CLI.<p/>
Note that the connectivity check can take up to 10 seconds to complete.
```JSON
# The API:
GET /support/autosupport
# The call:
curl -X GET "https://<mgmt-ip>/api/support/autosupport?fields=issues" -H "accept: application/hal+json"
# The response:
200 OK
{
  "issues": [
    {
      "node": {
        "name": "node3",
        "uuid": "0ecfd0a6-f1b3-11e8-9d9f-005056bbaadc",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0ecfd0a6-f1b3-11e8-9d9f-005056bbaadc"
          }
        }
      },
      "issue": {
        "message": "SMTP connectivity check failed for destination: mailhost. Error: Could not resolve host - 'mailhost'",
        "code": "53149746"
      },
      "corrective_action": {
        "message": "Check the hostname of the SMTP server",
        "code": "53149746"
      }
    },
    {
      "node": {
        "name": "node3",
        "uuid": "0ecfd0a6-f1b3-11e8-9d9f-005056bbaadc",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0ecfd0a6-f1b3-11e8-9d9f-005056bbaadc"
          }
        }
      },
      "issue": {
        "message": "AutoSupport OnDemand is disabled when \"-transport\" is not set to \"https\".",
        "code": "53149740"
      },
      "corrective_action": {
        "message": "Run \"system node autosupport modify -transport https -node <node name>\" to set \"-transport\" to \"https\".",
        "code": "53149740"
      }
    }
  ],
  "_links": {
    "self": {
      "href": "/api/support/autosupport"
    }
  }
}
```
---
### Retrieving AutoSupport configuration and connectivity issues
The following example retrieves AutoSupport configuration and connectivity issues on the cluster. Use `fields=*,issues` parameter to return both configuration and connectivity issues.
```JSON
# The API:
GET /support/autosupport
# The call:
curl -X GET "https://<mgmt-ip>/api/support/autosupport?fields=*%2Cissues" -H "accept: application/hal+json"
# The response:
200 OK
{
  "enabled": true,
  "mail_hosts": [
    "mailhost"
  ],
  "from": "Postmaster",
  "to": [
    "abc@netapp.com",
    "xyz@netapp.com"
  ],
  "contact_support": true,
  "transport": "smtp",
  "proxy_url": "",
  "is_minimal": false,
  "issues": [
    {
      "node": {
        "name": "node3",
        "uuid": "0ecfd0a6-f1b3-11e8-9d9f-005056bbaadc",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0ecfd0a6-f1b3-11e8-9d9f-005056bbaadc"
          }
        }
      },
      "issue": {
        "message": "SMTP connectivity check failed for destination: mailhost. Error: Could not resolve host - 'mailhost'",
        "code": "53149746"
      },
      "corrective_action": {
        "message": "Check the hostname of the SMTP server",
        "code": "53149746"
      }
    },
    {
      "node": {
        "name": "node3",
        "uuid": "0ecfd0a6-f1b3-11e8-9d9f-005056bbaadc",
        "_links": {
          "self": {
            "href": "/api/cluster/nodes/0ecfd0a6-f1b3-11e8-9d9f-005056bbaadc"
          }
        }
      },
      "issue": {
        "message": "AutoSupport OnDemand is disabled when \"-transport\" is not set to \"https\".",
        "code": "53149740"
      },
      "corrective_action": {
        "message": "Run \"system node autosupport modify -transport https -node <node name>\" to set \"-transport\" to \"https\".",
        "code": "53149740"
      }
    }
  ],
  "_links": {
    "self": {
      "href": "/api/support/autosupport"
    }
  }
}
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


__all__ = ["Autosupport", "AutosupportSchema"]
__pdoc__ = {
    "AutosupportSchema.resource": False,
    "AutosupportSchema.patchable_fields": False,
    "AutosupportSchema.postable_fields": False,
}


class AutosupportSchema(ResourceSchema):
    """The fields of the Autosupport object"""

    contact_support = fields.Boolean(
        data_key="contact_support",
    )
    r""" Specifies whether to send the AutoSupport messages to vendor support.

Example: true """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies whether the AutoSupport daemon is enabled.  When this setting is disabled, delivery of all AutoSupport messages is turned off.

Example: true """

    from_ = fields.Str(
        data_key="from",
    )
    r""" The e-mail address from which the AutoSupport messages are sent. To generate node-specific 'from' addresses, enable '-node-specific-from' parameter via ONTAP CLI.

Example: postmaster@example.com """

    is_minimal = fields.Boolean(
        data_key="is_minimal",
    )
    r""" Specifies whether the system information is collected in compliant form, to remove private data or in complete form, to enhance diagnostics.

Example: true """

    issues = fields.List(fields.Nested("netapp_ontap.models.autosupport_issues.AutosupportIssuesSchema", unknown=EXCLUDE), data_key="issues")
    r""" A list of nodes in the cluster with connectivity issues to HTTP/SMTP/AOD AutoSupport destinations along with the corresponding error descriptions and corrective actions. """

    mail_hosts = fields.List(fields.Str, data_key="mail_hosts")
    r""" The names of the mail servers used to deliver AutoSupport messages via SMTP.

Example: ["mailhost1.example.com","mailhost2.example.com"] """

    partner_addresses = fields.List(fields.Str, data_key="partner_addresses")
    r""" The list of partner addresses.

Example: ["user1@partner.com","user2@partner.com"] """

    proxy_url = fields.Str(
        data_key="proxy_url",
    )
    r""" Proxy server for AutoSupport message delivery via HTTP/S. Optionally specify a username/password for authentication with the proxy server.

Example: https://proxy.company.com """

    to = fields.List(fields.Str, data_key="to")
    r""" The e-mail addresses to which the AutoSupport messages are sent.

Example: ["user1@example.com","user2@example.com"] """

    transport = fields.Str(
        data_key="transport",
        validate=enum_validation(['smtp', 'http', 'https']),
    )
    r""" The name of the transport protocol used to deliver AutoSupport messages.

Valid choices:

* smtp
* http
* https """

    @property
    def resource(self):
        return Autosupport

    @property
    def patchable_fields(self):
        return [
            "contact_support",
            "enabled",
            "from_",
            "is_minimal",
            "mail_hosts",
            "partner_addresses",
            "proxy_url",
            "to",
            "transport",
        ]

    @property
    def postable_fields(self):
        return [
            "contact_support",
            "enabled",
            "from_",
            "is_minimal",
            "mail_hosts",
            "partner_addresses",
            "proxy_url",
            "to",
            "transport",
        ]

class Autosupport(Resource):
    """Allows interaction with Autosupport objects on the host"""

    _schema = AutosupportSchema
    _path = "/api/support/autosupport"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the AutoSupport configuration of the cluster and if requested, returns connectivity issues with the AutoSupport configuration.<p/>
</br>Important note:
* The **issues** field consists of a list of objects containing details of the node that has a connectivity issue, the issue description, and corrective action you can take to address the issue. When not empty, this indicates a connection issue to the **HTTP/S**, **SMTP**, or **AutoSupport On Demand** server.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `issues`
### Related ONTAP commands
* `system node autosupport show -instance`
* `system node autosupport check show-details`
### Learn more
* [`DOC /support/autosupport`](#docs-support-support_autosupport)
"""
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
        r"""Updates the AutoSupport configuration for the entire cluster.
### Related ONTAP commands
* `system node autosupport modify`
### Learn more
* [`DOC /support/autosupport`](#docs-support-support_autosupport)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



