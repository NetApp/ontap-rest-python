# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
NIS servers are used to authenticate user and client computers. NIS domain name and NIS server information is required to configure NIS.
It is important to note that this API is used to retrieve and manage NIS server configurations for data SVMs only. NIS configuration for the cluster is managed via [`/api/security/authentication/cluster/nis`](#docs-security-security_authentication_cluster_nis).
## Retrieving NIS Information
The NIS GET endpoint retrieves all of the NIS configurations for data SVMs.
## Examples
### Retrieving all fields for all NIS configurations
---
```
# The API:
/api/name-services/nis
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/nis?fields=*" -H "accept: application/hal+json"
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
      "domain": "domainA.example.com",
      "servers": [
        "10.10.10.10",
        "example.com"
      ]
      "bound-servers": [
        "10.10.10.10"
      ]
      "_links": {
        "self": {
          "href": "/api/name-services/nis/179d3c85-7053-11e8-b9b8-005056b41bd1"
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
      "domain": "domainB.example.com",
      "servers": [
        "2.2.2.2",
        "3.3.3.3"
        "4.4.4.4"
      ]
      "bound-servers": [],
      "_links": {
        "self": {
          "href": "/api/name-services/nis/6a52023b-7066-11e8-b9b8-005056b41bd1"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/name-services/nis?fields=*"
    }
  }
}
```
---
### Retrieving all NIS configurations whose bound servers start with *10*
---
```
# The API:
/api/name-services/nis
# The call:
curl -X GET "https://<mgmt-ip/api/name-services/nis?bound_servers=10*" -H "accept: application/hal+json"
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
      "bound-servers": [
        "10.10.10.10"
      ]
      "_links": {
        "self": {
          "href": "/api/name-services/nis/6a52023b-7066-11e8-b9b8-005056b41bd1"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/name-services/nis?bound_servers=10*"
    }
  }
}
```
---
### Retrieving the NIS configuration of a specific SVM
---
```
# The API:
/api/name-services/nis/{svm.uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/nis/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/hal+json"
# The response:
{
  "svm": {
    "uuid": "179d3c85-7053-11e8-b9b8-005056b41bd1",
    "name": "vs1"
  },
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
---
## Creating a NIS configuration
The NIS POST endpoint creates a NIS configuration for the specified SVM.
## Example
The following example shows a POST operation:
```
# The API:
/api/name-services/nis
# The call:
curl -X POST "https://<mgmt-ip>/api/name-services/nis" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"svm\": { \"uuid\": \"179d3c85-7053-11e8-b9b8-005056b41bd1\" }, \"domain\": \"domainA.example.com\", \"servers\": [ \"10.10.10.10\",\"example.com\" ]}"
```
---
## Updating the NIS configuration
The NIS PATCH endpoint updates the NIS configuration for the specified NIS server.
## Examples
### Updating the domain
---
```
# The API:
/api/name-services/nis/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/name-services/nis/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"domain\": \"domainC.example.com\", \"servers\": [ \"13.13.13.13\" ]}"
```
---
### Updating the server
---
```
# The API:
/api/name-services/nis/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/name-services/nis/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"servers\": [ \"14.14.14.14\" ]}"
```
---
## Deleting a NIS configuration
The NIS DELETE endpoint deletes the NIS configuration for the specified SVM.
## Example
The following example shows a DELETE operation:
---
```
# The API:
/api/name-services/nis/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/name-services/nis/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/hal+json"
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


__all__ = ["NisService", "NisServiceSchema"]
__pdoc__ = {
    "NisServiceSchema.resource": False,
    "NisServiceSchema.patchable_fields": False,
    "NisServiceSchema.postable_fields": False,
}


class NisServiceSchema(ResourceSchema):
    """The fields of the NisService object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the nis_service. """

    bound_servers = fields.List(fields.Str, data_key="bound_servers")
    r""" The bound_servers field of the nis_service. """

    domain = fields.Str(
        data_key="domain",
        validate=len_validation(minimum=1, maximum=64),
    )
    r""" The NIS domain to which this configuration belongs. """

    servers = fields.List(fields.Str, data_key="servers")
    r""" A list of hostnames or IP addresses of NIS servers used
by the NIS domain configuration. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the nis_service. """

    @property
    def resource(self):
        return NisService

    @property
    def patchable_fields(self):
        return [
            "domain",
            "servers",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "domain",
            "servers",
            "svm.name",
            "svm.uuid",
        ]

class NisService(Resource):
    """Allows interaction with NisService objects on the host"""

    _schema = NisServiceSchema
    _path = "/api/name-services/nis"
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
        r"""Retrieves NIS domain configurations of all the SVMs. The bound_servers field indicates the successfully bound NIS servers. Lookups and authentications fail if there are no bound servers.
### Related ONTAP commands
* `vserver services name-service nis-domain show`
* `vserver services name-service nis-domain show-bound`
### Learn more
* [`DOC /name-services/nis`](#docs-name-services-name-services_nis)
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
        r"""Updates NIS domain and server configuration of an SVM.<br/>
### Important notes
  - Both NIS domain and servers can be modified.
  - Domains and servers cannot be empty.
  - Both FQDNs and IP addresses are supported for the servers field.
  - If the domain is modified, NIS servers must also be specified.
  - IPv6 must be enabled if IPv6 family addresses are specified for the servers field.
### Related ONTAP commands
* `vserver services name-service nis-domain modify`
### Learn more
* [`DOC /name-services/nis`](#docs-name-services-name-services_nis)
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
        r"""Deletes the NIS domain configuration of an SVM. NIS can be removed as a source from ns-switch if NIS is not used for lookups.
### Related ONTAP commands
* `vserver services name-service nis-domain delete`
### Learn more
* [`DOC /name-services/nis`](#docs-name-services-name-services_nis)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves NIS domain configurations of all the SVMs. The bound_servers field indicates the successfully bound NIS servers. Lookups and authentications fail if there are no bound servers.
### Related ONTAP commands
* `vserver services name-service nis-domain show`
* `vserver services name-service nis-domain show-bound`
### Learn more
* [`DOC /name-services/nis`](#docs-name-services-name-services_nis)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves NIS domain and server configurations of an SVM. Both NIS domain and servers are displayed by default. The bound_servers field indicates the successfully bound NIS servers.
### Related ONTAP commands
* `vserver services name-service nis-domain show`
* `vserver services name-service nis-domain show-bound`
### Learn more
* [`DOC /name-services/nis`](#docs-name-services-name-services_nis)
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
        r"""Creates an NIS domain and server confguration for a data SVM.
NIS configuration for the cluster is managed via [`/api/security/authentication/cluster/nis`](#docs-security-security_authentication_cluster_nis).<br/>
### Important notes
  - Each SVM can have one NIS domain configuration.
  - Multiple SVMs can be configured with the same NIS domain. Specify the NIS domain and NIS servers as input.Domain name and servers fields cannot be empty.
  - Both FQDNs and IP addresses are supported for the servers field.
  - IPv6 must be enabled if IPv6 family addresses are specified in the servers field.
  - A maximum of ten NIS servers are supported.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the NIS configuration.
* `domain` - NIS domain to which the configuration belongs.
* `servers` - List of NIS server IP addresses.
### Related ONTAP commands
* `vserver services name-service nis-domain create`
### Learn more
* [`DOC /name-services/nis`](#docs-name-services-name-services_nis)
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
        r"""Updates NIS domain and server configuration of an SVM.<br/>
### Important notes
  - Both NIS domain and servers can be modified.
  - Domains and servers cannot be empty.
  - Both FQDNs and IP addresses are supported for the servers field.
  - If the domain is modified, NIS servers must also be specified.
  - IPv6 must be enabled if IPv6 family addresses are specified for the servers field.
### Related ONTAP commands
* `vserver services name-service nis-domain modify`
### Learn more
* [`DOC /name-services/nis`](#docs-name-services-name-services_nis)
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
        r"""Deletes the NIS domain configuration of an SVM. NIS can be removed as a source from ns-switch if NIS is not used for lookups.
### Related ONTAP commands
* `vserver services name-service nis-domain delete`
### Learn more
* [`DOC /name-services/nis`](#docs-name-services-name-services_nis)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


