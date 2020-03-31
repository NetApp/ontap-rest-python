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
to lookup information stored in the LDAP directory on the external LDAP servers. This API is used to retrieve and manage
LDAP server configurations.
## Retrieving LDAP information
The LDAP GET endpoint retrieves all of the LDAP configurations in the cluster.
## Examples
### Retrieving all of the fields for all LDAP configurations
---
```
# The API:
/api/name-services/ldap
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/ldap?fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "179d3c85-7053-11e8-b9b8-005056b41bd1",
        "name": "vs1"
        "_links": {
          "self": {
            "href": "/api/svm/svms/179d3c85-7053-11e8-b9b8-005056b41bd1"
          }
        }
      },
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
          "href": "/api/name-services/ldap/179d3c85-7053-11e8-b9b8-005056b41bd1"
        }
      }
    },
    {
      "svm": {
        "uuid": "6a52023b-7066-11e8-b9b8-005056b41bd1",
        "name": "vs2"
        "_links": {
          "self": {
            "href": "/api/svm/svms/6a52023b-7066-11e8-b9b8-005056b41bd1"
          }
        }
      },
      "servers": [
        "11.11.11.11"
      ],
      "schema": "rfc_2307",
      "port": 389,
      "min_bind_level": "simple",
      "bind_dn": "cn=Administrators,cn=users,dc=domainB,dc=example,dc=com",
      "base_dn": "dc=domainB,dc=example,dc=com",
      "base_scope": "subtree",
      "use_start_tls": true,
      "session_security": "sign",
      "_links": {
        "self": {
          "href": "/api/name-services/ldap/6a52023b-7066-11e8-b9b8-005056b41bd1"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/name-services/ldap?fields=*"
    }
  }
}
```
---
### Retrieving all of the LDAP configurations that have the *use_start_tls* set to *true*
---
```
# The API:
/api/name-services/ldap
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/ldap?use_start_tls=true" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "6a52023b-7066-11e8-b9b8-005056b41bd1",
        "name": "vs2"
        "_links": {
          "self": {
            "href": "/api/svm/svms/6a52023b-7066-11e8-b9b8-005056b41bd1"
          }
        }
      },
      "use_start_tls": true,
      "_links": {
        "self": {
          "href": "/api/name-services/ldap/6a52023b-7066-11e8-b9b8-005056b41bd1"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/name-services/ldap?use_start_tls=true"
    }
  }
}
```
---
### Retrieving the LDAP configuration of a specific SVM
---
```
# The API:
/api/name-services/ldap/{svm.uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/ldap/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "179d3c85-7053-11e8-b9b8-005056b41bd1",
    "name": "vs1"
    "_links": {
      "self": {
        "href": "/api/svm/svms/179d3c85-7053-11e8-b9b8-005056b41bd1"
      }
    }
  },
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
      "href": "/api/name-services/ldap/179d3c85-7053-11e8-b9b8-005056b41bd1"
    }
  }
}
```
---
## Creating an LDAP configuration
The LDAP POST endpoint creates an LDAP configuration for the specified SVM.
## Examples
### Creating an LDAP configuration with all the fields specified
---
```
# The API:
/api/name-services/ldap
# The call:
curl -X POST "https://<mgmt-ip>/api/name-services/ldap" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"svm\": { \"uuid\": \"179d3c85-7053-11e8-b9b8-005056b41bd1\" }, \"servers\": [ \"10.10.10.10\"\, \"domainB.example.com\" ], \"schema\": \"ad_idmu\", \"port\": 389, \"min_bind_level\": \"anonymous\", \"bind_dn\": \"cn=Administrators,cn=users,dc=domainA,dc=example,dc=com\", \"bind_password\": \"abc\", \"base_dn\": \"dc=domainA,dc=example,dc=com\", \"base_scope\": \"subtree\", \"use_start_tls\": false, \"session_security\": \"none\"}"
```
---
### Creating an LDAP configuration with Active Directory domain and preferred Active Directory servers specified
---
```
# The API:
/api/name-services/ldap
# The call:
curl -X POST "https://<mgmt-ip>/api/name-services/ldap" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"svm\": { \"name\": \"vs2\" }, \"ad_domain\": \"domainA.example.com\", \"preferred_ad_servers\": [ \"11.11.11.11\" ], \"port\": 389, \"bind_dn\": \"cn=Administrators,cn=users,dc=domainA,dc=example,dc=com\", \"bind_password\": \"abc\", \"base_dn\": \"dc=domainA,dc=example,dc=com\", \"session_security\": \"none\"}"
```
---
### Creating an LDAP configuration with a number of optional fields not specified
---
```
# The API:
/api/name-services/ldap
# The call:
curl -X POST "https://<mgmt-ip>/api/name-services/ldap" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"svm\": { \"name\": \"vs2\" }, \"servers\": [ \"11.11.11.11\" ], \"port\": 389, \"bind_dn\": \"cn=Administrators,cn=users,dc=domainA,dc=example,dc=com\", \"bind_password\": \"abc\", \"base_dn\": \"dc=domainA,dc=example,dc=com\", \"session_security\": \"none\"}"
```
---
## Updating an LDAP configuration
The LDAP PATCH endpoint updates the LDAP configuration for the specified SVM. The following example shows a PATCH operation:
```
# The API:
/api/name-services/ldap/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/name-services/ldap/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"servers\": [ \"55.55.55.55\" ], \"schema\": \"ad_idmu\", \"port\": 636, \"use_start_tls\": false }"
```
---
## Deleting an LDAP configuration
The LDAP DELETE endpoint deletes the LDAP configuration for the specified SVM. The following example shows a DELETE operation:
```
# The API:
/api/name-services/ldap/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/name-services/ldap/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/hal+json"
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


__all__ = ["LdapService", "LdapServiceSchema"]
__pdoc__ = {
    "LdapServiceSchema.resource": False,
    "LdapServiceSchema.patchable_fields": False,
    "LdapServiceSchema.postable_fields": False,
}


class LdapServiceSchema(ResourceSchema):
    """The fields of the LdapService object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ldap_service. """

    ad_domain = fields.Str(
        data_key="ad_domain",
    )
    r""" This parameter specifies the name of the Active Directory domain
used to discover LDAP servers for use by this client.
This is mutually exclusive with `servers` during POST and PATCH. """

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

    preferred_ad_servers = fields.List(fields.Str, data_key="preferred_ad_servers")
    r""" The preferred_ad_servers field of the ldap_service. """

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
    r""" The servers field of the ldap_service. """

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

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the ldap_service. """

    use_start_tls = fields.Boolean(
        data_key="use_start_tls",
    )
    r""" Specifies whether or not to use Start TLS over LDAP connections. """

    @property
    def resource(self):
        return LdapService

    @property
    def patchable_fields(self):
        return [
            "ad_domain",
            "base_dn",
            "base_scope",
            "bind_dn",
            "bind_password",
            "min_bind_level",
            "port",
            "preferred_ad_servers",
            "schema",
            "servers",
            "session_security",
            "svm.name",
            "svm.uuid",
            "use_start_tls",
        ]

    @property
    def postable_fields(self):
        return [
            "ad_domain",
            "base_dn",
            "base_scope",
            "bind_dn",
            "bind_password",
            "min_bind_level",
            "port",
            "preferred_ad_servers",
            "schema",
            "servers",
            "session_security",
            "svm.name",
            "svm.uuid",
            "use_start_tls",
        ]

class LdapService(Resource):
    """Allows interaction with LdapService objects on the host"""

    _schema = LdapServiceSchema
    _path = "/api/name-services/ldap"
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
        r"""Retrieves the LDAP configurations for all SVMs.

### Learn more
* [`DOC /name-services/ldap`](#docs-name-services-name-services_ldap)"""
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
        r"""Updates an LDAP configuration of an SVM.
### Important notes
* Both mandatory and optional parameters of the LDAP configuration can be updated.
* The LDAP servers and Active Directory domain are mutually exclusive fields. These fields cannot be empty. At any point in time, either the LDAP servers or Active Directory domain must be populated.
* IPv6 must be enabled if IPv6 family addresses are specified.<br/>
</br>Configuring more than one LDAP server is recommended to avoid a sinlge point of failure.
Both FQDNs and IP addresses are supported for the "servers" field.
The Active Directory domain or LDAP servers are validated as part of this operation.<br/>
LDAP validation fails in the following scenarios:<br/>
1. The server does not have LDAP installed.
2. The server or Active Directory domain is invalid.
3. The server or Active Directory domain is unreachable<br/>

### Learn more
* [`DOC /name-services/ldap`](#docs-name-services-name-services_ldap)"""
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
        r"""Deletes the LDAP configuration of the specified SVM. LDAP can be removed as a source from the ns-switch if LDAP is not used as a source for lookups.

### Learn more
* [`DOC /name-services/ldap`](#docs-name-services-name-services_ldap)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the LDAP configurations for all SVMs.

### Learn more
* [`DOC /name-services/ldap`](#docs-name-services-name-services_ldap)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves LDAP configuration for an SVM. All parameters for the LDAP configuration are displayed by default.

### Learn more
* [`DOC /name-services/ldap`](#docs-name-services-name-services_ldap)"""
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
        r"""Creates an LDAP configuration for an SVM.
### Important notes
* Each SVM can have one LDAP configuration.
* The LDAP servers and Active Directory domain are mutually exclusive fields. These fields cannot be empty. At any point in time, either the LDAP servers or Active Directory domain must be populated.
* LDAP configuration with Active Directory domain cannot be created on an admin SVM.
* IPv6 must be enabled if IPv6 family addresses are specified.</br>
#### The following parameters are optional:
- preferred AD servers
- schema
- port
- min_bind_level
- bind_password
- base_scope
- use_start_tls
- session_security</br>
Configuring more than one LDAP server is recommended to avoid a single point of failure.
Both FQDNs and IP addresses are supported for the "servers" field.
The Acitve Directory domain or LDAP servers are validated as part of this operation.</br>
LDAP validation fails in the following scenarios:<br/>
1. The server does not have LDAP installed.
2. The server or Active Directory domain is invalid.
3. The server or Active Directory domain is unreachable.<br/>

### Learn more
* [`DOC /name-services/ldap`](#docs-name-services-name-services_ldap)"""
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
        r"""Updates an LDAP configuration of an SVM.
### Important notes
* Both mandatory and optional parameters of the LDAP configuration can be updated.
* The LDAP servers and Active Directory domain are mutually exclusive fields. These fields cannot be empty. At any point in time, either the LDAP servers or Active Directory domain must be populated.
* IPv6 must be enabled if IPv6 family addresses are specified.<br/>
</br>Configuring more than one LDAP server is recommended to avoid a sinlge point of failure.
Both FQDNs and IP addresses are supported for the "servers" field.
The Active Directory domain or LDAP servers are validated as part of this operation.<br/>
LDAP validation fails in the following scenarios:<br/>
1. The server does not have LDAP installed.
2. The server or Active Directory domain is invalid.
3. The server or Active Directory domain is unreachable<br/>

### Learn more
* [`DOC /name-services/ldap`](#docs-name-services-name-services_ldap)"""
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
        r"""Deletes the LDAP configuration of the specified SVM. LDAP can be removed as a source from the ns-switch if LDAP is not used as a source for lookups.

### Learn more
* [`DOC /name-services/ldap`](#docs-name-services-name-services_ldap)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


