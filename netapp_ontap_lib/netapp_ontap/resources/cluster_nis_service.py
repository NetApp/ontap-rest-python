# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
NIS servers are used to authenticate user and client computers. NIS domain name and NIS server information is required to configure NIS. This API retrieves and manages NIS server configurations.
## Examples
### Retrieving cluster NIS information
The cluster NIS GET request retrieves the NIS configuration of the cluster.<br>
The following example shows how a GET request is used to retrieve the cluster NIS configuration:
```
# The API:
/security/authentication/cluster/nis
# The call:
curl -X GET "https://<mgmt-ip>/api/security/authentication/cluster/nis" -H "accept: application/hal+json"
# The response:
{
  "domain": "domainA.example.com",
  "servers": [
    "10.10.10.10",
    "example.com"
  ]
  "bound_servers": [
    "10.10.10.10"
  ]
}
```
### Creating the cluster NIS configuration
The cluster NIS POST request creates a NIS configuration for the cluster.<br>
The following example shows how a POST request is used to create a cluster NIS configuration:
```
# The API:
/security/authentication/cluster/nis
# The call:
curl -X POST "https://<mgmt-ip>/api/security/authentication/cluster/nis" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"domain\": \"domainA.example.com\", \"servers\": [ \"10.10.10.10\",\"example.com\" ]}"
```
### Updating the cluster NIS configuration
The cluster NIS PATCH request updates the NIS configuration of the cluster.<br>
The following example shows how to update the domain:
```
# The API:
/security/authentication/cluster/nis
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/authentication/cluster/nis" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"domain\": \"domainC.example.com\", \"servers\": [ \"13.13.13.13\" ]}"
```
The following example shows how to update the server:
```
# The API:
/security/authentication/cluster/nis
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/authentication/cluster/nis" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"servers\": [ \"14.14.14.14\" ]}"
```
## Deleting the cluster NIS configuration
The cluster NIS DELETE request deletes the NIS configuration of the cluster.<br>
The following example shows how a DELETE request is used to delete the cluster NIS configuration:
```
# The API:
/security/authentication/cluster/nis
# The call:
curl -X DELETE "https://<mgmt-ip>/api/security/authentication/cluster/nis" -H "accept: application/hal+json"
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


__all__ = ["ClusterNisService", "ClusterNisServiceSchema"]
__pdoc__ = {
    "ClusterNisServiceSchema.resource": False,
    "ClusterNisServiceSchema.patchable_fields": False,
    "ClusterNisServiceSchema.postable_fields": False,
}


class ClusterNisServiceSchema(ResourceSchema):
    """The fields of the ClusterNisService object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cluster_nis_service. """

    bound_servers = fields.List(fields.Str, data_key="bound_servers")
    r""" The bound_servers field of the cluster_nis_service. """

    domain = fields.Str(
        data_key="domain",
        validate=len_validation(minimum=1, maximum=64),
    )
    r""" The NIS domain to which this configuration belongs. """

    servers = fields.List(fields.Str, data_key="servers")
    r""" A list of hostnames or IP addresses of NIS servers used
by the NIS domain configuration. """

    @property
    def resource(self):
        return ClusterNisService

    @property
    def patchable_fields(self):
        return [
            "domain",
            "servers",
        ]

    @property
    def postable_fields(self):
        return [
            "domain",
            "servers",
        ]

class ClusterNisService(Resource):
    """Allows interaction with ClusterNisService objects on the host"""

    _schema = ClusterNisServiceSchema
    _path = "/api/security/authentication/cluster/nis"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the NIS configuration of the cluster. Both NIS domain and servers are displayed by default.
The `bound_servers` property indicates the successfully bound NIS servers.

### Learn more
* [`DOC /security/authentication/cluster/nis`](#docs-security-security_authentication_cluster_nis)"""
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
        r"""The cluster can have one NIS server configuration. Specify the NIS domain and NIS servers as input. Domain name and servers fields cannot be empty.
Both FQDNs and IP addresses are supported for the `server` property. IPv6 must be enabled if IPv6 family addresses are specified in the `server` property. A maximum of ten NIS servers are supported.
### Required properties
* `domain` - NIS domain to which this configuration belongs.
* `servers` - List of hostnames or IP addresses of NIS servers used by the NIS domain configuration.

### Learn more
* [`DOC /security/authentication/cluster/nis`](#docs-security-security_authentication_cluster_nis)"""
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
        r"""Both NIS domain and servers can be updated. Domains and servers cannot be empty. Both FQDNs and IP addresses are supported for the 'servers' field. If the domain is updated, NIS servers must also be specified. IPv6 must be enabled if IPv6 family addresses are specified for the `servers` property.<br/>

### Learn more
* [`DOC /security/authentication/cluster/nis`](#docs-security-security_authentication_cluster_nis)"""
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
        r"""Deletes the NIS configuration of the cluster. NIS can be removed as a source from ns-switch if NIS is not used for lookups.

### Learn more
* [`DOC /security/authentication/cluster/nis`](#docs-security-security_authentication_cluster_nis)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


