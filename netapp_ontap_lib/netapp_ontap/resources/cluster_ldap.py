# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
LDAP servers are used to centrally maintain user information. LDAP configurations must be set up
to look up information stored in the LDAP directory on the external LDAP servers. This API is used to retrieve and manage
cluster LDAP server configurations.<br>
## Examples
### Retrieving the cluster LDAP information
The cluster LDAP GET request retrieves the LDAP configuration of the cluster.<br>
The following example shows how a GET request is used to retrieve the cluster LDAP information:
```
# The API:
/api/security/authentication/cluster/ldap
# The call:
curl -X GET "https://<mgmt-ip>/api/security/authentication/cluster/ldap" -H "accept: application/hal+json"
# The response:
{
  "servers": [
    "10.10.10.10",
    "domainB.example.com"
  ],
  "schema": "ad_idmu",
  "port": 389,
  "min_bind_level": "anonymous",
  "bind_dn": "cn=Administrators,cn=users,dc=domainA,dc=example,dc=com",
  "base_dn": "dc=domainA,dc=example,dc=com",
  "base_scope": "subtree",
  "use_start_tls": true,
  "session_security": "none",
  "_links": {
    "self": {
      "href": "/api/security/authentication/cluster/ldap"
    }
  }
}
```
### Creating the cluster LDAP configuration
The cluster LDAP POST operation creates an LDAP configuration for the cluster.<br>
The following example shows how to issue a POST request with all of the fields specified:
```
# The API:
/api/security/authentication/cluster/ldap
# The call:
curl -X POST "https://<mgmt-ip>/api/security/authentication/cluster/ldap" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"servers\": [ \"10.10.10.10\"\, \"domainB.example.com\" ], \"schema\": \"ad_idmu\", \"port\": 389, \"min_bind_level\": \"anonymous\", \"bind_dn\": \"cn=Administrators,cn=users,dc=domainA,dc=example,dc=com\", \"bind_password\": \"abc\", \"base_dn\": \"dc=domainA,dc=example,dc=com\", \"base_scope\": \"subtree\", \"use_start_tls\": false, \"session_security\": \"none\"}"
```
The following example shows how to issue a POST request with a number of optional fields not specified:
```
# The API:
/api/security/authentication/cluster/ldap
# The call:
curl -X POST "https://<mgmt-ip>/api/security/authentication/cluster/ldap" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"port\": 389, \"bind_dn\": \"cn=Administrators,cn=users,dc=domainA,dc=example,dc=com\", \"bind_password\": \"abc\", \"base_dn\": \"dc=domainA,dc=example,dc=com\", \"session_security\": \"none\"}"
```
### Updating the cluster LDAP configuration
The cluster LDAP PATCH request updates the LDAP configuration of the cluster.<br>
The following example shows how a PATCH request is used to update the cluster LDAP configuration:
```
# The API:
/api/security/authentication/cluster/ldap
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/authentication/cluster/ldap" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"servers\": [ \"55.55.55.55\" ], \"schema\": \"ad_idmu\", \"port\": 636, \"use_start_tls\": false }"
```
### Deleting the cluster LDAP configuration
The cluster LDAP DELETE request deletes the LDAP configuration of the cluster.<br>
The following example shows how a DELETE request is used to delete the cluster LDAP configuration:
```
# The API:
/api/security/authentication/cluster/ldap
# The call:
curl -X DELETE "https://<mgmt-ip>/api/security/authentication/cluster/ldap" -H "accept: application/hal+json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["ClusterLdap", "ClusterLdapSchema"]
__pdoc__ = {
    "ClusterLdapSchema.resource": False,
    "ClusterLdapSchema.patchable_fields": False,
    "ClusterLdapSchema.postable_fields": False,
}


class ClusterLdapSchema(ResourceSchema):
    """The fields of the ClusterLdap object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cluster_ldap. """

    base_dn = fields.Str(
        data_key="base_dn",
    )
    r""" Specifies the default base DN for all searches. """

    base_scope = fields.Str(
        data_key="base_scope",
        validate=enum_validation(['base', 'onelevel', 'subtree']),
    )
    r""" Specifies the default search scope for LDAP queries:

* base - search the named entry only
* onelevel - search all entries immediately below the DN
* subtree - search the named DN entry and the entire subtree below the DN


Valid choices:

* base
* onelevel
* subtree """

    bind_dn = fields.Str(
        data_key="bind_dn",
    )
    r""" Specifies the user that binds to the LDAP servers. """

    bind_password = fields.Str(
        data_key="bind_password",
    )
    r""" Specifies the bind password for the LDAP servers. """

    min_bind_level = fields.Str(
        data_key="min_bind_level",
        validate=enum_validation(['anonymous', 'simple', 'sasl']),
    )
    r""" The minimum bind authentication level. Possible values are:

* anonymous - anonymous bind
* simple - simple bind
* sasl - Simple Authentication and Security Layer (SASL) bind


Valid choices:

* anonymous
* simple
* sasl """

    port = fields.Integer(
        data_key="port",
        validate=integer_validation(minimum=1, maximum=65535),
    )
    r""" The port used to connect to the LDAP Servers.

Example: 389 """

    schema = fields.Str(
        data_key="schema",
    )
    r""" The name of the schema template used by the SVM.

* AD-IDMU - Active Directory Identity Management for UNIX
* AD-SFU - Active Directory Services for UNIX
* MS-AD-BIS - Active Directory Identity Management for UNIX
* RFC-2307 - Schema based on RFC 2307
* Custom schema """

    servers = fields.List(fields.Str, data_key="servers")
    r""" The servers field of the cluster_ldap. """

    session_security = fields.Str(
        data_key="session_security",
        validate=enum_validation(['none', 'sign', 'seal']),
    )
    r""" Specifies the level of security to be used for LDAP communications:

* none - no signing or sealing
* sign - sign LDAP traffic
* seal - seal and sign LDAP traffic


Valid choices:

* none
* sign
* seal """

    use_start_tls = fields.Boolean(
        data_key="use_start_tls",
    )
    r""" Specifies whether or not to use Start TLS over LDAP connections. """

    @property
    def resource(self):
        return ClusterLdap

    @property
    def patchable_fields(self):
        return [
            "base_dn",
            "base_scope",
            "bind_dn",
            "bind_password",
            "min_bind_level",
            "port",
            "schema",
            "servers",
            "session_security",
            "use_start_tls",
        ]

    @property
    def postable_fields(self):
        return [
            "base_dn",
            "base_scope",
            "bind_dn",
            "bind_password",
            "min_bind_level",
            "port",
            "schema",
            "servers",
            "session_security",
            "use_start_tls",
        ]

class ClusterLdap(Resource):
    """Allows interaction with ClusterLdap objects on the host"""

    _schema = ClusterLdapSchema
    _path = "/api/security/authentication/cluster/ldap"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the cluster LDAP configuration.

### Learn more
* [`DOC /security/authentication/cluster/ldap`](#docs-security-security_authentication_cluster_ldap)"""
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
        r"""A cluster can have only one LDAP configuration. IPv6 must be enabled if IPv6 family addresses are specified.
### Required properties
* `servers` - List of LDAP servers used for this client configuration.
* `bind_dn` - Specifies the user that binds to the LDAP servers.
* `base_dn` - Specifies the default base DN for all searches.
### Recommended optional properties
* `schema` - Schema template name.
* `port` - Port used to connect to the LDAP Servers.
* `min_bind_level` - Minimum bind authentication level.
* `bind_password` - Specifies the bind password for the LDAP servers.
* `base_scope` - Specifies the default search scope for LDAP queries.
* `use_start_tls` - Specifies whether or not to use Start TLS over LDAP connections.
* `session_security` - Specifies the level of security to be used for LDAP communications.
### Default property values
* `schema` - _RFC-2307_
* `port` - _389_
* `min_bind_level` - _simple_
* `base_scope` - _subtree_
* `use_start_tls` - _false_
* `session_security` - _none_
<br/>
Configuring more than one LDAP server is recommended to avoid a single point of failure. Both FQDNs and IP addresses are supported for the `servers` property.
The LDAP servers are validated as part of this operation. LDAP validation fails in the following scenarios:<br/>
1. The server does not have LDAP installed.
2. The server is invalid.
3. The server is unreachable.<br/>

### Learn more
* [`DOC /security/authentication/cluster/ldap`](#docs-security-security_authentication_cluster_ldap)"""
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
        r"""Both mandatory and optional parameters of the LDAP configuration can be updated.
IPv6 must be enabled if IPv6 family addresses are specified. Configuring more than one LDAP server is recommended to avoid a single point of failure. Both FQDNs and IP addresses are supported for the `servers` property.
The LDAP servers are validated as part of this operation. LDAP validation fails in the following scenarios:<br/>
1. The server does not have LDAP installed.
2. The server is invalid.
3. The server is unreachable. <br/>

### Learn more
* [`DOC /security/authentication/cluster/ldap`](#docs-security-security_authentication_cluster_ldap)"""
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
        r"""Deletes the LDAP configuration of the cluster.

### Learn more
* [`DOC /security/authentication/cluster/ldap`](#docs-security-security_authentication_cluster_ldap)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


