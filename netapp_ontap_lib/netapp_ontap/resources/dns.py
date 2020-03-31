# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Displays DNS information and controls the DNS subsytem. DNS domain name and DNS servers are required parameters.
## Retrieving DNS information
The DNS GET endpoint retrieves all of the DNS configurations for data SVMs.
DNS configuration for the cluster is retrieved via [`/api/cluster`](#docs-cluster-cluster).
## Examples
### Retrieving all of the fields for all of the DNS configurations
```
# The API:
/api/name-services/dns
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/dns?fields=*" -H "accept: application/hal+json"
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
      "domains": [
        "domainA.example.com"
      ],
      "servers": [
        "10.10.10.10"
      ]
      "_links": {
        "self": {
          "href": "/api/name-services/dns/179d3c85-7053-11e8-b9b8-005056b41bd1"
        }
      }
    },
    {
      "svm": {
        "uuid": "19076d35-6e27-11e8-b9b8-005056b41bd1",
        "name": "vs2"
        "_links": {
          "self": {
            "href": "/api/svm/svms/19076d35-6e27-11e8-b9b8-005056b41bd1"
          }
        }
      },
      "domains": [
        "sample.example.com"
      ],
      "servers": [
        "11.11.11.11",
        "22.22.22.22",
        "33.33.33.33"
      ]
      "_links": {
        "self": {
          "href": "/api/name-services/dns/19076d35-6e27-11e8-b9b8-005056b41bd1"
        }
      }
    }
  ],
  "num_records": 2
  "_links": {
    "self": {
      "href": "/api/name-services/dns?fields=*"
    }
  }
}
```
### Retrieving all DNS configurations whose domain name starts with _dom*_.
```
# The API:
/api/name-services/dns
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/dns?domains=dom*" -H "accept: application/hal+json"
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
      "domains": [
        "domainA.example.com"
      ]
      "_links": {
        "self": {
          "href": "/api/name-services/dns/179d3c85-7053-11e8-b9b8-005056b41bd1"
        }
      }
    }
  ],
  "num_records": 1
  "_links": {
    "self": {
      "href": "/api/name-services/dns?domains=dom*"
    }
  }
}
```
### Retrieving the DNS configuration for a specific SVM
```
# The API:
/api/name-services/dns/{svm.uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/dns/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/hal+json"
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
  "domains": [
    "domainA.example.com"
  ],
  "servers": [
    "10.10.10.10"
  ]
  "_links": {
    "self": {
      "href": "/api/name-services/dns/179d3c85-7053-11e8-b9b8-005056b41bd1"
    }
  }
}
```
## Creating a DNS configuration
The DNS POST endpoint creates a DNS configuration for the specified SVM.
## Example
The following example shows a POST operation:
```
# The API:
/api/name-services/dns
# The call:
      curl -X POST "https://<mgmt-ip>/api/name-services/dns" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"svm\": { \"uuid\": \"179d3c85-7053-11e8-b9b8-005056b41bd1\" }, \"domains\": [ \"domainA.example.com\" ], \"servers\": [ \"10.10.10.10\" ]}"
```
## Updating a DNS configuration
The DNS PATCH endpoint updates the DNS configuration for the specified SVM.
## Examples
### Updating both the DNS domains and servers
```
# The API:
/api/name-services/dns/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/name-services/dns/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"domains\": [ \"domainA.example.com\", \"domainB.example.com\" ], \"servers\": [ \"10.10.10.10\", \"10.10.10.11\" ]}"
```
### Updating the DNS servers only
```
# The API:
/api/name-services/dns/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/name-services/dns/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/hal+json" -H "Content-Type: application/json" -d "{ \"servers\": [ \"10.10.10.10\" ]}"
```
## Deleting a DNS configuration
The DNS DELETE endpoint deletes the DNS configuration for the specified SVM.
## Example
The following example shows a DELETE operation.
```
# The API:
/api/name-services/dns/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/name-services/dns/179d3c85-7053-11e8-b9b8-005056b41bd1" -H "accept: application/hal+json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Dns", "DnsSchema"]
__pdoc__ = {
    "DnsSchema.resource": False,
    "DnsSchema.patchable_fields": False,
    "DnsSchema.postable_fields": False,
}


class DnsSchema(ResourceSchema):
    """The fields of the Dns object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the dns. """

    domains = fields.List(fields.Str, data_key="domains")
    r""" The domains field of the dns. """

    servers = fields.List(fields.Str, data_key="servers")
    r""" The servers field of the dns. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the dns. """

    @property
    def resource(self):
        return Dns

    @property
    def patchable_fields(self):
        return [
            "domains",
            "servers",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "domains",
            "servers",
            "svm.name",
            "svm.uuid",
        ]

class Dns(Resource):
    """Allows interaction with Dns objects on the host"""

    _schema = DnsSchema
    _path = "/api/name-services/dns"
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
        r"""Retrieves the DNS configurations of all data SVMs.
DNS configuration for the cluster is retrieved and managed via [`/api/cluster`](#docs-cluster-cluster).
### Related ONTAP commands
* `vserver services name-service dns show`
* `vserver services name-service dns check`
### Learn more
* [`DOC /name-services/dns`](#docs-name-services-name-services_dns)
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
        r"""Updates DNS domain and server configurations of an SVM.
### Important notes
- Both DNS domains and servers can be modified.
- The domains and servers fields cannot be empty.
- IPv6 must be enabled if IPv6 family addresses are specified for the `servers` field.
- The DNS server specified using the `servers` field is validated during this operation.<br/>
The validation fails in the following scenarios:<br/>
1. The server is not a DNS server.
2. The server does not exist.
3. The server is unreachable.<br/>

### Learn more
* [`DOC /name-services/dns`](#docs-name-services-name-services_dns)"""
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
        r"""Deletes DNS domain configuration of the specified SVM.
### Related ONTAP commands
* `vserver services name-service dns delete`
### Learn more
* [`DOC /name-services/dns`](#docs-name-services-name-services_dns)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the DNS configurations of all data SVMs.
DNS configuration for the cluster is retrieved and managed via [`/api/cluster`](#docs-cluster-cluster).
### Related ONTAP commands
* `vserver services name-service dns show`
* `vserver services name-service dns check`
### Learn more
* [`DOC /name-services/dns`](#docs-name-services-name-services_dns)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves DNS domain and server configuration of an SVM. By default, both DNS domains and servers are displayed.
DNS configuration for the cluster is retrieved and managed via [`/api/cluster`](#docs-cluster-cluster).
### Related ONTAP commands
* `vserver services name-service dns show`
* `vserver services name-service dns check`
### Learn more
* [`DOC /name-services/dns`](#docs-name-services-name-services_dns)
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
        r"""Creates DNS domain and server configurations for an SVM.<br/>
### Important notes
- Each SVM can have only one DNS configuration.
- The domain name and the servers fields cannot be empty.
- IPv6 must be enabled if IPv6 family addresses are specified in the `servers` field.
- Configuring more than one DNS server is recommended to avoid a single point of failure.
- The DNS server specified using the `servers` field is validated during this operation.<br/>
</br> The validation fails in the following scenarios:<br/>
1. The server is not a DNS server.
2. The server does not exist.
3. The server is unreachable.<br/>

### Learn more
* [`DOC /name-services/dns`](#docs-name-services-name-services_dns)"""
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
        r"""Updates DNS domain and server configurations of an SVM.
### Important notes
- Both DNS domains and servers can be modified.
- The domains and servers fields cannot be empty.
- IPv6 must be enabled if IPv6 family addresses are specified for the `servers` field.
- The DNS server specified using the `servers` field is validated during this operation.<br/>
The validation fails in the following scenarios:<br/>
1. The server is not a DNS server.
2. The server does not exist.
3. The server is unreachable.<br/>

### Learn more
* [`DOC /name-services/dns`](#docs-name-services-name-services_dns)"""
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
        r"""Deletes DNS domain configuration of the specified SVM.
### Related ONTAP commands
* `vserver services name-service dns delete`
### Learn more
* [`DOC /name-services/dns`](#docs-name-services-name-services_dns)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


