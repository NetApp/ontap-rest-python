# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
ONTAP supports SSH server that can be accessed from any standard SSH client. A user account needs to be associated with SSH as the application (refer the documentation for <i>api/security/accounts</i> [`DOC /security/accounts`](#docs-security-security_accounts)). Upon connecting from a client, the user is authenticated and a command line shell is presented.<br/>
This endpoint is used to retrieve or modify the SSH configuration at the cluster level. The configuration consists of SSH security parameters (security algorithms and maximum authentication retry attempts allowed before closing the connection) and SSH connection limits.<br/>
The security algorithms include SSH key exchange algorithms, ciphers for payload encryption, and MAC algorithms. This configuration is the default for all newly created SVMs; existing SVM configurations are not impacted.
The SSH connection limits include maximum connections per second, maximum simultaneous sessions from the same client host, and overall maximum SSH connections at any given point in time. The connection limits are per node and will be the same for all nodes in the cluster.
## Examples
### Updating the SSH security parameters
Specify the algorithms in the body of the PATCH request.
```
# The API:
PATCH "/api/security/ssh"
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/ssh" -d '{ "ciphers": [ "aes256_ctr", "aes192_ctr" ], "key_exchange_algorithms": [ "diffie_hellman_group_exchange_sha256", "diffie_hellman_group14_sha1" ], "mac_algorithms": [ "hmac_sha2_512_etm", "umac_128_etm" ], "max_authentication_retry_count": 3 }'
```
### Updating the SSH connection limits
Specify the connection limits in the body of the PATCH request.
```
# The API:
PATCH "/api/security/ssh"
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/ssh" -d '{ "connections_per_second": 8, "max_instances": 10, "per_source_limit": 5 }'
```
### Retrieving the cluster SSH server configuration
```
# The API:
GET "/api/security/ssh"
# The call:
curl -X GET "https://<mgmt-ip>/api/security/ssh"
# The response:
{
  "ciphers": [
    "aes256_ctr",
    "aes192_ctr"
  ],
  "key_exchange_algorithms": [
    "diffie_hellman_group_exchange_sha256",
    "diffie_hellman_group14_sha1"
  ],
  "mac_algorithms": [
    "hmac_sha2_512_etm",
    "umac_128_etm"
  ],
  "max_authentication_retry_count": 3,
  "connections_per_second": 8,
  "max_instances": 10,
  "per_source_limit": 5,
  "_links": {
    "self": {
      "href": "/api/security/ssh"
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


__all__ = ["ClusterSshServer", "ClusterSshServerSchema"]
__pdoc__ = {
    "ClusterSshServerSchema.resource": False,
    "ClusterSshServerSchema.patchable_fields": False,
    "ClusterSshServerSchema.postable_fields": False,
}


class ClusterSshServerSchema(ResourceSchema):
    """The fields of the ClusterSshServer object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cluster_ssh_server. """

    ciphers = fields.List(fields.Str, data_key="ciphers")
    r""" Ciphers for encrypting the data.

Example: ["aes256_ctr","aes192_ctr","aes128_ctr"] """

    connections_per_second = fields.Integer(
        data_key="connections_per_second",
        validate=integer_validation(minimum=1, maximum=70),
    )
    r""" Maximum connections allowed per second. """

    key_exchange_algorithms = fields.List(fields.Str, data_key="key_exchange_algorithms")
    r""" Key exchange algorithms.

Example: ["diffie_hellman_group_exchange_sha256","diffie_hellman_group14_sha1"] """

    mac_algorithms = fields.List(fields.Str, data_key="mac_algorithms")
    r""" MAC algorithms.

Example: ["hmac_sha1","hmac_sha2_512_etm"] """

    max_authentication_retry_count = fields.Integer(
        data_key="max_authentication_retry_count",
        validate=integer_validation(minimum=2, maximum=6),
    )
    r""" Maximum authentication retries allowed before closing the connection. """

    max_instances = fields.Integer(
        data_key="max_instances",
        validate=integer_validation(minimum=1, maximum=128),
    )
    r""" Maximum possible simultaneous connections. """

    per_source_limit = fields.Integer(
        data_key="per_source_limit",
        validate=integer_validation(minimum=1, maximum=64),
    )
    r""" Maximum connections from the same client host. """

    @property
    def resource(self):
        return ClusterSshServer

    @property
    def patchable_fields(self):
        return [
            "ciphers",
            "connections_per_second",
            "key_exchange_algorithms",
            "mac_algorithms",
            "max_authentication_retry_count",
            "max_instances",
            "per_source_limit",
        ]

    @property
    def postable_fields(self):
        return [
            "ciphers",
            "connections_per_second",
            "key_exchange_algorithms",
            "mac_algorithms",
            "max_authentication_retry_count",
            "max_instances",
            "per_source_limit",
        ]

class ClusterSshServer(Resource):
    """Allows interaction with ClusterSshServer objects on the host"""

    _schema = ClusterSshServerSchema
    _path = "/api/security/ssh"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the cluster SSH server ciphers, MAC algorithms, key exchange algorithms, and connection limits.
### Related ONTAP commands
* `security ssh`
* `security protocol ssh`

### Learn more
* [`DOC /security/ssh`](#docs-security-security_ssh)"""
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
        r"""Updates the SSH server setting for a cluster.
### Optional parameters
* `ciphers` - Encryption algorithms for the payload
* `key_exchange_algorithms` - SSH key exchange algorithms
* `mac_algorithms` - MAC algorithms
* `max_authentication_retry_count` - Maximum authentication retries allowed before closing the connection
* `connections_per_second` - Maximum allowed connections per second
* `max_instances` - Maximum allowed connections per node
* `per_source_limit` - Maximum allowed connections from the same client host
### Related ONTAP commands
* `security ssh`
* `security protocol ssh`

### Learn more
* [`DOC /security/ssh`](#docs-security-security_ssh)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



