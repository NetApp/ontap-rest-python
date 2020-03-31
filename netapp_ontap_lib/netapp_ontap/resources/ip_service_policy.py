# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Service policies are named groupings that define what services are supported by an IP interface. The network IP service-policies GET API retrieves and displays relevant information pertaining to the service policies configured in the cluster. The API retrieves the list of all service policies configured in the cluster or a specific service policy.
## Examples
### Retrieving all service policies in the cluster
The following output shows the collection of all service policies configured in a 2-node cluster. By default (without 'field=*' parameter), only the UUID and name fields are shown for each entry.
<br/>
---
```
# The API:
/api/network/ethernet/ip/service-policies
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/service-policies" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "e4e2f193-c1a3-11e8-bb9d-005056bb88c8",
      "name": "net-intercluster",
      "_links": {
        "self": {
          "href": "/api/network/ip/service-policies/e4e2f193-c1a3-11e8-bb9d-005056bb88c8"
        }
      }
    },
    {
      "uuid": "e4e3f6da-c1a3-11e8-bb9d-005056bb88c8",
      "name": "net-route-announce",
      "_links": {
        "self": {
          "href": "/api/network/ip/service-policies/e4e3f6da-c1a3-11e8-bb9d-005056bb88c8"
        }
      }
    },
    {
      "uuid": "e5111111-c1a3-11e8-bb9d-005056bb88c8",
      "name": "vserver-route-announce",
      "_links": {
        "self": {
          "href": "/api/network/ip/service-policies/e5111111-c1a3-11e8-bb9d-005056bb88c8"
        }
      }
    },
    {
      "uuid": "e6111111-c1a3-11e8-bb9d-005056bb88c8",
      "name": "data-route-announce",
      "_links": {
        "self": {
          "href": "/api/network/ip/service-policies/e6111111-c1a3-11e8-bb9d-005056bb88c8"
        }
      }
    }
  ],
  "num_records": 4,
  "_links": {
    "self": {
      "href": "/api/network/ip/service-policies/?return_records=true&return_timeout=15"
    }
  }
}
```
---
### Retrieving a specific service policy (scope=svm)
The following output displays the response when a specific "svm" scoped service policy is requested. Among other parameters, the response contains the svm parameters associated with the service policy. The system returns an error when there is no service policy with the requested UUID.
<br/>
---
```
# The API:
/api/network/ip/service-policies/{uuid}
# The call:
curl -X GET "http://<mgmt-ip>/api/network/ip/service-policies/dad323ff-4ce0-11e9-9372-005056bb91a8?fields=*" -H "accept: application/hal+json"
# The response:
{
  "uuid": "dad323ff-4ce0-11e9-9372-005056bb91a8",
  "name": "default-data-files",
  "scope": "svm",
  "svm": {
    "uuid": "d9060680-4ce0-11e9-9372-005056bb91a8",
    "name": "vs0",
    "_links": {
      "self": {
        "href": "/api/svm/svms/d9060680-4ce0-11e9-9372-005056bb91a8"
      }
    }
  },
  "ipspace": {
    "uuid": "45ec2dee-4ce0-11e9-9372-005056bb91a8",
    "name": "Default",
    "_links": {
      "self": {
        "href": "/api/network/ipspaces/45ec2dee-4ce0-11e9-9372-005056bb91a8"
      }
    }
  },
  "services": [
    "data_core",
    "data_nfs",
    "data_cifs",
    "data_flexcache"
  ],
  "_links": {
    "self": {
      "href": "/api/network/ip/service-policies/dad323ff-4ce0-11e9-9372-005056bb91a8"
    }
  }
}
```
---
### Retrieving a specific service policy (scope=svm) when requesting commonly used fields
The following output displays the response when commonly used fields are requested for a specific "svm" scoped service policy. Among other parameters, the response contains the svm parameters associated with the service policy. The system returns an error when there is no service policy with the requested UUID.
<br/>
---
```
# The API:
/api/network/ip/service-policies/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/service-policies/e0889ce6-1e6a-11e9-89d6-005056bbdc04?fields=name,scope,svm.name,ipspace.name" -H "accept: application/hal+json"
# The response:
{
  "uuid": "e0889ce6-1e6a-11e9-89d6-005056bbdc04",
  "name": "test_policy",
  "scope": "svm",
  "svm": {
    "name": "vs0",
  },
  "ipspace": {
    "name": "Default",
  },
  "_links": {
    "self": {
      "href": "/api/network/ip/service-policies/e0889ce6-1e6a-11e9-89d6-005056bbdc04"
    }
  }
}
```
---
### Retrieving a specific service policy (scope=cluster)
The following output displays the response when a specific cluster-scoped service policy is requested. The SVM object is not included for cluster-scoped service policies. A service policy with a scope of "cluster" is associated with an IPspace. The system returns an error when there is no service policy with the requested UUID.
<br/>
---
```
# The API:
/api/network/ip/service-policies/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/service-policies/4c6b72b9-0f6c-11e9-875d-005056bb21b8?fields=*" -H "accept: application/hal+json"
# The response:
{
  "uuid": "4c6b72b9-0f6c-11e9-875d-005056bb21b8",
  "name": "net-intercluster",
  "scope": "cluster",
  "ipspace": {
    "uuid": "4051f13e-0f6c-11e9-875d-005056bb21b8",
    "name": "Default",
    "_links": {
      "self": {
        "href": "/api/network/ipspaces/4051f13e-0f6c-11e9-875d-005056bb21b8"
      }
    }
  },
  "services": [
    "intercluster_core"
  ],
  "_links": {
    "self": {
      "href": "/api/network/ip/service-policies/4c6b72b9-0f6c-11e9-875d-005056bb21b8"
    }
  }
}
```
---
### Retrieving a specific service policy (scope=cluster) when requesting commonly used fields
The following output displays the response when commonly used fields are requested for a specific "cluster" scoped service policy. The SVM object is not included for cluster-scoped service policies. A service policy with a scope of "cluster" is associated with an IPspace. The system returns an error when there is no service policy with the requested UUID.
<br/>
---
```
# The API:
/api/network/ip/service-policies/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/service-policies/4c6b72b9-0f6c-11e9-875d-005056bb21b8?fields=name,scope,ipspace.name" -H "accept: application/hal+json"
# The response:
{
  "uuid": "4c6b72b9-0f6c-11e9-875d-005056bb21b8",
  "name": "net-intercluster",
  "scope": "cluster",
  "ipspace": {
    "name": "Default",
  },
  "services": [
    "intercluster_core"
  ],
  "_links": {
    "self": {
      "href": "/api/network/ip/service-policies/4c6b72b9-0f6c-11e9-875d-005056bb21b8"
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


__all__ = ["IpServicePolicy", "IpServicePolicySchema"]
__pdoc__ = {
    "IpServicePolicySchema.resource": False,
    "IpServicePolicySchema.patchable_fields": False,
    "IpServicePolicySchema.postable_fields": False,
}


class IpServicePolicySchema(ResourceSchema):
    """The fields of the IpServicePolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ip_service_policy. """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the ip_service_policy. """

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the ip_service_policy.

Example: default-intercluster """

    scope = fields.Str(
        data_key="scope",
    )
    r""" The scope field of the ip_service_policy. """

    services = fields.List(fields.Str, data_key="services")
    r""" The services field of the ip_service_policy. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the ip_service_policy. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the ip_service_policy.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return IpServicePolicy

    @property
    def patchable_fields(self):
        return [
            "ipspace.name",
            "ipspace.uuid",
            "name",
            "scope",
            "services",
            "svm.name",
            "svm.uuid",
            "uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "ipspace.name",
            "ipspace.uuid",
            "name",
            "scope",
            "services",
            "svm.name",
            "svm.uuid",
            "uuid",
        ]

class IpServicePolicy(Resource):
    """Allows interaction with IpServicePolicy objects on the host"""

    _schema = IpServicePolicySchema
    _path = "/api/network/ip/service-policies"
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
        r"""Retrieves a collection of service policies.
### Related ONTAP commands
* `network interface service-policy show`

### Learn more
* [`DOC /network/ip/service-policies`](#docs-networking-network_ip_service-policies)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of service policies.
### Related ONTAP commands
* `network interface service-policy show`

### Learn more
* [`DOC /network/ip/service-policies`](#docs-networking-network_ip_service-policies)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific service policy.
### Related ONTAP commands
* `network interface service-policy show`

### Learn more
* [`DOC /network/ip/service-policies`](#docs-networking-network_ip_service-policies)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





