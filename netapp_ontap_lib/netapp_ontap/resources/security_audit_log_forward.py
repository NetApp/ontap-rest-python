# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API controls the forwarding of audit log information to remote syslog/splunk servers. Multiple destinations can be configured and all audit records are forwarded to all destinations.</br>
A GET operation retrieves information about remote syslog/splunk server destinations.
A POST operation creates a remote syslog/splunk server destination.
A GET operation on /security/audit/destinations/{address}/{port} retrieves information about the syslog/splunk server destination given its address and port number.
A PATCH operation on /security/audit/destinations/{address}/{port} updates information about the syslog/splunk server destination given its address and port number.
A DELETE operation on /security/audit/destinations/{address}/{port} deletes a syslog/splunk server destination given its address and port number.
### Overview of fields used for creating a remote syslog/splunk destination
The fields used for creating a remote syslog/splunk destination fall into the following categories
#### Required properties
All of the following fields are required for creating a remote syslog/splunk destination

* `address`
#### Optional properties
All of the following fields are optional for creating a remote syslog/splunk destination

* `port`
* `protocol`
* `facility`
* `verify_server`
<br />
---
## Examples
### Retrieving remote syslog/splunk server destinations
The following example shows remote syslog/splunk server destinations
<br />
---
```
# The API:
/api/security/audit/destinations
# The call:
curl -X GET "https://<cluster-ip>/api/security/audit/destinations"
# The response:
{
  "records": [
    {
      "address": "1.1.1.1",
      "port": 514,
      "_links": {
        "self": {
          "href": "/api/security/audit/destinations/1.1.1.1/514"
        }
    }
  }
 ],
 "num_records": 1,
   "_links": {
     "self": {
       "href": "/api/security/audit/destinations"
     }
   }
}
```
---
### Creating remote syslog/splunk server destinations
The following example creates remote syslog/splunk server destinations.
<br />
---
```
# The API:
/api/security/audit/destinations
# The call:
curl -X POST "https://<cluster-ip>/api/security/audit/destinations?force=true -d '{ "address": "<destination-address>", "port": <destination-port>, "protocol": "udp_unencrypted", "facility": "kern"}'"
```
---
### Retrieving a remote syslog/splunk server destination given its destination address and port number
The following example retrieves a remote syslog/splunk server destination given its destination address and port number.
<br />
---
```
# The API:
/api/security/audit/destinations/{address}/{port}
# The call:
curl -X GET "https://<cluster-ip>/api/security/audit/destinations/<destination-address>/<destination-port>"
# The response:
{
  "address": "1.1.1.1",
  "port": 514,
  "protocol": "udp_unencrypted",
  "facility": "kern",
  "verify_server": false,
  "_links": {
    "self": {
      "href": "/api/security/audit/destinations/1.1.1.1/514"
    }
  }
}
```
---
### Updating a remote syslog/splunk server destination given its destination address and port number
The following example updates a remote syslog/splunk server destination configuration given its destination address and port number.
<br />
---
```
# The API:
/api/security/audit/destinations/{address}/{port}
# The call:
curl -X PATCH "https://<cluster-ip>/api/security/audit/destinations/<destination-address>/<destination-port> -d '{"facility":  "kern"}'"
```
---
### Deleting a remote syslog/splunk server destination given its destination address and port number
The following example deletes a remote syslog/splunk server destination configuration given its destination address and port number.
<br />
---
```
# The API:
/api/security/audit/destinations/{address}/{port}
# The call:
curl -X DELETE "https://<cluster-ip>/api/security/audit/destinations/<destination-address>/<destination-port>"
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


__all__ = ["SecurityAuditLogForward", "SecurityAuditLogForwardSchema"]
__pdoc__ = {
    "SecurityAuditLogForwardSchema.resource": False,
    "SecurityAuditLogForwardSchema.patchable_fields": False,
    "SecurityAuditLogForwardSchema.postable_fields": False,
}


class SecurityAuditLogForwardSchema(ResourceSchema):
    """The fields of the SecurityAuditLogForward object"""

    address = fields.Str(
        data_key="address",
    )
    r""" Destination syslog|splunk host to forward audit records to. This can be an IP address (IPv4|IPv6) or a hostname. """

    facility = fields.Str(
        data_key="facility",
        validate=enum_validation(['kern', 'user', 'local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7']),
    )
    r""" This is the standard Syslog Facility value that is used when sending audit records to a remote server.

Valid choices:

* kern
* user
* local0
* local1
* local2
* local3
* local4
* local5
* local6
* local7 """

    port = fields.Integer(
        data_key="port",
    )
    r""" Destination Port. The default port depends on the protocol chosen:
For un-encrypted destinations the default port is 514.
For encrypted destinations the default port is 6514. """

    protocol = fields.Str(
        data_key="protocol",
        validate=enum_validation(['udp_unencrypted', 'tcp_unencrypted', 'tcp_encrypted']),
    )
    r""" Log forwarding protocol

Valid choices:

* udp_unencrypted
* tcp_unencrypted
* tcp_encrypted """

    verify_server = fields.Boolean(
        data_key="verify_server",
    )
    r""" This is only applicable when the protocol is tcp_encrypted. This controls whether the remote server's certificate is validated. Setting "verify_server" to "true" will enforce validation of remote server's certificate. Setting "verify_server" to "false" will not enforce validation of remote server's certificate. """

    @property
    def resource(self):
        return SecurityAuditLogForward

    @property
    def patchable_fields(self):
        return [
            "facility",
            "verify_server",
        ]

    @property
    def postable_fields(self):
        return [
            "address",
            "facility",
            "port",
            "protocol",
            "verify_server",
        ]

class SecurityAuditLogForward(Resource):
    """Allows interaction with SecurityAuditLogForward objects on the host"""

    _schema = SecurityAuditLogForwardSchema
    _path = "/api/security/audit/destinations"
    @property
    def _keys(self):
        return ["address", "port"]

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
        r"""Defines a remote syslog/splunk server for sending audit information to.
### Learn more
* [`DOC /security/audit/destinations`](#docs-security-security_audit_destinations)"""
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
        r"""Updates remote syslog/splunk server information.
### Learn more
* [`DOC /security/audit/destinations`](#docs-security-security_audit_destinations)"""
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
        r"""Deletes remote syslog/splunk server information.
### Learn more
* [`DOC /security/audit/destinations`](#docs-security-security_audit_destinations)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Defines a remote syslog/splunk server for sending audit information to.
### Learn more
* [`DOC /security/audit/destinations`](#docs-security-security_audit_destinations)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Defines a remote syslog/splunk server for sending audit information to.
### Learn more
* [`DOC /security/audit/destinations`](#docs-security-security_audit_destinations)"""
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
        r"""Configures remote syslog/splunk server information.
### Required properties
All of the following fields are required for creating a remote syslog/splunk destination
* `address`
### Optional properties
All of the following fields are optional for creating a remote syslog/splunk destination
* `port`
* `protocol`
* `facility`
* `verify_server` (Can only be "true" when protocol is "tcp_encrypted")

### Learn more
* [`DOC /security/audit/destinations`](#docs-security-security_audit_destinations)"""
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
        r"""Updates remote syslog/splunk server information.
### Learn more
* [`DOC /security/audit/destinations`](#docs-security-security_audit_destinations)"""
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
        r"""Deletes remote syslog/splunk server information.
### Learn more
* [`DOC /security/audit/destinations`](#docs-security-security_audit_destinations)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


