# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
The following operations are supported:

* Creation: POST network/ip/interfaces
* Collection Get: GET network/ip/interfaces
* Instance Get: GET network/ip/interfaces/{uuid}
* Instance Patch: PATCH network/ip/interfaces/{uuid}
* Instance Delete: DELETE network/ip/interfaces/{uuid}
## Retrieving network interface information
The IP interfaces GET API retrieves and displays relevant information pertaining to the interfaces configured in the cluster. The response can contain a list of multiple interfaces or a specific interface. The fields returned in the response vary for different interfaces and configurations.
## Examples
### Retrieving all interfaces in the cluster
The following example shows the list of all interfaces configured in a cluster.
<br/>
---
```
# The API:
/api/network/ip/interfaces
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/interfaces" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "14531286-59fc-11e8-ba55-005056b4340f",
      "name": "user-cluster-01_mgmt1",
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/14531286-59fc-11e8-ba55-005056b4340f"
        }
      }
    },
    {
      "uuid": "145318ba-59fc-11e8-ba55-005056b4340f",
      "name": "user-cluster-01_clus2",
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/145318ba-59fc-11e8-ba55-005056b4340f"
        }
      }
    },
    {
      "uuid": "14531e45-59fc-11e8-ba55-005056b4340f",
      "name": "user-cluster-01_clus1",
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/14531e45-59fc-11e8-ba55-005056b4340f"
        }
      }
    },
    {
      "uuid": "245979de-59fc-11e8-ba55-005056b4340f",
      "name": "cluster_mgmt",
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/245979de-59fc-11e8-ba55-005056b4340f"
        }
      }
    },
    {
      "uuid": "c670707c-5a11-11e8-8fcb-005056b4340f",
      "name": "lif1",
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/c670707c-5a11-11e8-8fcb-005056b4340f"
        }
      }
    }
  ],
  "num_records": 5,
  "_links": {
    "self": {
      "href": "/api/network/ip/interfaces"
    }
  }
}
```
---
### Retrieving a specific Cluster-scoped interface
The following example shows the response when a specific Cluster-scoped interface is requested. The system returns an error when there is no interface with the requested UUID. SVM information is not returned for Cluster-scoped interfaces.
<br/>
---
```
# The API:
/api/network/ip/interfaces/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/interfaces/245979de-59fc-11e8-ba55-005056b4340f" -H "accept: application/hal+json"
# The response:
{
  "uuid": "245979de-59fc-11e8-ba55-005056b4340f",
  "name": "cluster_mgmt",
  "ip": {
    "address": "10.63.41.6",
    "netmask": "18",
    "family": "ipv4",
  },
  "enabled": true,
  "state": "up",
  "scope": "cluster",
  "ipspace": {
    "uuid": "114ecfb5-59fc-11e8-ba55-005056b4340f",
    "name": "Default",
    "_links": {
      "self": {
              "href": "/api/network/ipspaces/114ecfb5-59fc-11e8-ba55-005056b4340f"
      }
    }
  },
  "services": [
    "management_core",
    "management_autosupport",
    "management_access"
  ],
  "location": {
    "is_home": true,
    "auto_revert": false,
    "failover": "broadcast_domain_only",
    "node": {
      "uuid": "c1db2904-1396-11e9-bb7d-005056acfcbb",
      "name": "user-cluster-01-a",
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/c1db2904-1396-11e9-bb7d-005056acfcbb"
        }
      }
    },
    "port": {
      "uuid": "c84d5337-1397-11e9-87c2-005056acfcbb",
      "name": "e0d",
      "node": {
        "name": "user-cluster-01-a"
      },
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/c84d5337-1397-11e9-87c2-005056acfcbb"
        }
      }
    },
    "home_node": {
      "uuid": "c1db2904-1396-11e9-bb7d-005056acfcbb",
      "name": "user-cluster-01-a",
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/c1db2904-1396-11e9-bb7d-005056acfcbb"
        }
      }
    },
    "home_port": {
      "uuid": "c84d5337-1397-11e9-87c2-005056acfcbb",
      "name": "e0d",
      "node": {
        "name": "user-cluster-01-a"
      },
      "_links": {
        "self": {
          "href": "/api/network/ethernet/ports/c84d5337-1397-11e9-87c2-005056acfcbb"
        }
      }
    }
  },
  "service_policy": {
    "uuid": "9e0f4151-141b-11e9-851e-005056ac1ce0",
    "name": "default-management"
  },
  "vip": false,
  "_links": {
    "self": {
      "href": "/api/network/ip/interfaces/245979de-59fc-11e8-ba55-005056b4340f"
    }
  }
}
```
---
### Retrieving a specific SVM-scoped interface using a filter
The following example shows the response when a specific SVM-scoped interface is requested. The SVM object is only included for SVM-scoped interfaces.
<br/>
---
```
# The API:
/api/network/ip/interfaces
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/interfaces?name=lif1&fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "c670707c-5a11-11e8-8fcb-005056b4340f",
      "name": "lif1",
      "ip": {
        "address": "10.10.10.11",
        "netmask": "24",
        "family": "ipv4",
      },
      "enabled": true,
      "state": "up",
      "scope": "svm",
      "ipspace": {
        "uuid": "114ecfb5-59fc-11e8-ba55-005056b4340f",
        "name": "Default",
        "_links": {
          "self": {
            "href": "/api/network/ipspaces/114ecfb5-59fc-11e8-ba55-005056b4340f"
          }
        }
      },
      "svm": {
        "uuid": "c2134665-5a11-11e8-8fcb-005056b4340f",
        "name": "user_vs0",
        "_links": {
          "self": {
            "href": "/api/svm/svms/c2134665-5a11-11e8-8fcb-005056b4340f"
          }
        }
      },
      "services": [
        "data_core",
        "data_nfs",
        "data_cifs",
        "data_flexcache"
      ],
      "location": {
        "is_home": true,
        "auto_revert": false,
        "failover": "broadcast_domain_only",
        "node": {
          "uuid": "c1db2904-1396-11e9-bb7d-005056acfcbb",
          "name": "user-cluster-01-a",
          "_links": {
            "self": {
              "href": "/api/cluster/nodes/c1db2904-1396-11e9-bb7d-005056acfcbb"
            }
          }
        },
        "port": {
          "uuid": "c84d5337-1397-11e9-87c2-005056acfcbb",
          "name": "e0d",
          "node": {
            "name": "user-cluster-01-a"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/c84d5337-1397-11e9-87c2-005056acfcbb"
            }
          }
        },
        "home_node": {
          "uuid": "c1db2904-1396-11e9-bb7d-005056acfcbb",
          "name": "user-cluster-01-a",
          "_links": {
            "self": {
              "href": "/api/cluster/nodes/c1db2904-1396-11e9-bb7d-005056acfcbb"
            }
          }
        },
        "home_port": {
          "uuid": "c84d5337-1397-11e9-87c2-005056acfcbb",
          "name": "e0d",
          "node": {
            "name": "user-cluster-01-a"
          },
          "_links": {
            "self": {
              "href": "/api/network/ethernet/ports/c84d5337-1397-11e9-87c2-005056acfcbb"
            }
          }
        }
      },
      "service_policy": {
        "uuid": "9e53525f-141b-11e9-851e-005056ac1ce0",
        "name": "default-data-files"
      },
      "vip": false,
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/c670707c-5a11-11e8-8fcb-005056b4340f"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/network/ip/interfaces?name=lif1&fields=*"
    }
  }
}
```
---
### Retrieving specific fields and limiting the output using filters
The following example shows the response when a filter is applied (location.home_port.name=e0a) and only certain fields are requested. Filtered fields are in the output in addition to the default fields and requested fields.
<br/>
---
```
# The API:
/api/network/ip/interfaces
# The call:
curl -X GET "https://<mgmt-ip>/api/network/ip/interfaces?location.home_port.name=e0a&fields=location.home_node.name,service_policy.name,ip.address,enabled" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "uuid": "1d1c9dc8-4f17-11e9-9553-005056ac918a",
      "name": "user-cluster-01-a_clus1",
      "ip": {
        "address": "192.168.170.24"
      },
      "enabled": true,
      "location": {
        "home_node": {
          "name": "user-cluster-01-a"
        },
        "home_port": {
          "name": "e0a"
        }
      },
      "service_policy": {
        "name": "default-cluster"
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/1d1c9dc8-4f17-11e9-9553-005056ac918a"
        }
      }
    },
    {
      "uuid": "d07782c1-4f16-11e9-86e7-005056ace7ee",
      "name": "user-cluster-01-b_clus1",
      "ip": {
        "address": "192.168.170.22"
      },
      "enabled": true,
      "location": {
        "home_node": {
          "name": "user-cluster-01-b"
        },
        "home_port": {
          "name": "e0a"
        }
      },
      "service_policy": {
        "name": "default-cluster"
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/d07782c1-4f16-11e9-86e7-005056ace7ee"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/network/ip/interfaces?location.home_port.name=e0a&fields=location.home_node.name,service_policy.name,ip.address,enabled"
    }
  }
}
```
---
## Creating IP interfaces
You can use the IP interfaces POST API to create IP interfaces as shown in the following examples.
<br/>
---
## Examples
### Creating a Cluster-scoped IP interface using names
The following example shows the record returned after the creation of an IP interface on "e0d".
<br/>
---
```
# The API:
/api/network/ip/interfaces
# The call:
curl -X POST "https://<mgmt-ip>/api/network/ip/interfaces?return_records=true" -H "accept: application/hal+json" -d '{ "name": "cluster_mgmt", "ip": { "address": "10.63.41.6", "netmask": "18" }, "enabled": true, "scope": "cluster", "ipspace": { "name": "Default" }, "location": { "auto_revert": false, "failover": "broadcast_domain_only", "home_port": { "name": "e0d", "node": { "name": "user-cluster-01-a" } } }, "service_policy": { "name": "default-management" } }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "245979de-59fc-11e8-ba55-005056b4340f",
      "name": "cluster_mgmt",
      "ip": {
        "address": "10.63.41.6",
        "netmask": "18"
      },
      "enabled": true,
      "scope": "cluster",
      "ipspace": {
        "name": "Default"
      },
      "location": {
        "auto_revert": false,
        "failover": "broadcast_domain_only",
        "home_port": {
          "name": "e0d",
          "node": {
            "name": "user-cluster-01-a"
          }
        },
      },
      "service_policy": {
        "name": "default-management"
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/245979de-59fc-11e8-ba55-005056b4340f"
        }
      }
    }
  ]
}
```
---
### Creating a SVM-scoped IP interface using a mix of parameter types
The following example shows the record returned after the creation of a IP interface by specifying a broadcast domain as the location.
<br/>
---
```
# The API:
/api/network/ip/interfaces
# The call:
curl -X POST "https://<mgmt-ip>/api/network/ip/interfaces?return_records=true" -H "accept: application/hal+json" -d '{ "name": "Data1", "ip": { "address": "10.234.101.116", "netmask": "255.255.240.0" }, "enabled": true, "scope": "svm", "svm": { "uuid": "137f3618-1e89-11e9-803e-005056a7646a" }, "location": { "auto_revert": true, "broadcast_domain": { "name": "Default" } }, "service_policy": { "name": "default-data-files" } }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "80d271c9-1f43-11e9-803e-005056a7646a",
      "name": "Data1",
      "ip": {
        "address": "10.234.101.116",
        "netmask": "20"
      },
      "enabled": true,
      "scope": "svm",
      "svm": {
        "uuid": "137f3618-1e89-11e9-803e-005056a7646a",
        "name": "vs0",
        "_links": {
          "self": {
            "href": "/api/svm/svms/137f3618-1e89-11e9-803e-005056a7646a"
          }
        }
      },
      "location": {
        "auto_revert": true
      },
      "service_policy": {
        "name": "default-data-files"
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/80d271c9-1f43-11e9-803e-005056a7646a"
        }
      }
    }
  ]
}
```
---
### Creating a Cluster-scoped IP interface without specifying the scope parameter
The following example shows the record returned after creating an IP interface on "e0d" without specifying the scope parameter. The scope is "cluster" if an "svm" is not specified.
<br/>
---
```
# The API:
/api/network/ip/interfaces
# The call:
curl -X POST "https://<mgmt-ip>/api/network/ip/interfaces?return_records=true" -H "accept: application/hal+json" -d '{ "name": "cluster_mgmt", "ip": { "address": "10.63.41.6", "netmask": "18" }, "enabled": true, "ipspace": { "name": "Default" }, "location": { "auto_revert": false, "home_port": { "name": "e0d", "node": { "name": "user-cluster-01-a" } } }, "service_policy": { "name": "default-management" } }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "245979de-59fc-11e8-ba55-005056b4340f",
      "name": "cluster_mgmt",
      "ip": {
        "address": "10.63.41.6",
        "netmask": "18"
      },
      "enabled": true,
      "scope": "cluster",
      "ipspace": {
        "name": "Default"
      },
      "location": {
        "auto_revert": false,
        "home_port": {
          "name": "e0d",
          "node": {
            "name": "user-cluster-01-a"
          }
        }
      },
      "service_policy": {
        "name": "default-management"
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/245979de-59fc-11e8-ba55-005056b4340f"
        }
      }
    }
  ]
}
```
---
### Creating an SVM-scoped IP interface without specifying the scope parameter
The following example shows the record returned after creating an IP interface on "e0d" without specifying the scope parameter. The scope is "svm" if the "svm" field is specified.
<br/>
---
```
# The API:
/api/network/ip/interfaces
# The call:
curl -X POST "https://<mgmt-ip>/api/network/ip/interfaces?return_records=true" -H "accept: application/hal+json" -d '{ "name": "Data1", "ip": { "address": "10.234.101.116", "netmask": "255.255.240.0" }, "enabled": true, "svm": { "uuid": "137f3618-1e89-11e9-803e-005056a7646a" }, "location": { "auto_revert": true, "broadcast_domain": { "name": "Default" } }, "service_policy": { "name": "default-data-files" } }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "uuid": "80d271c9-1f43-11e9-803e-005056a7646a",
      "name": "Data1",
      "ip": {
        "address": "10.234.101.116",
        "netmask": "20"
      },
      "enabled": true,
      "scope": "svm",
      "svm": {
        "uuid": "137f3618-1e89-11e9-803e-005056a7646a",
        "name": "vs0",
        "_links": {
          "self": {
            "href": "/api/svms/137f3618-1e89-11e9-803e-005056a7646a"
          }
        }
      },
      "location": {
        "auto_revert": true
      },
      "service_policy": {
        "name": "default-data-files"
      },
      "_links": {
        "self": {
          "href": "/api/network/ip/interfaces/80d271c9-1f43-11e9-803e-005056a7646a"
        }
      }
    }
  ]
}
```
---
## Updating IP interfaces
You can use the IP interfaces PATCH API to update the attributes of an IP interface.
<br/>
---
## Examples
### Updating the auto revert flag of an IP interface
The following example shows how the PATCH request changes the auto revert flag to 'false'.
<br/>
---
```
# The API:
/api/network/ip/interfaces/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/ip/interfaces/80d271c9-1f43-11e9-803e-005056a7646a" -H "accept: application/hal+json" -d '{ "location": { "auto_revert": "false" } }'
{
}
```
---
### Updating the service policy of an IP interface
The following example shows how the PATCH request changes the service policy to 'default-management'.
<br/>
---
```
# The API:
/api/network/ip/interfaces/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/network/ip/interfaces/80d271c9-1f43-11e9-803e-005056a7646a" -H "accept: application/hal+json" -d '{ "service_policy": "default-management" }'
{
}
```
---
## Deleting IP interfaces
You can use the IP interfaces DELETE API to delete an IP interface in the cluster.
<br/>
---
## Example
### Deleting an IP Interface
The following DELETE request deletes a network IP interface.
<br/>
---
```
# The API:
/api/network/ip/interfaces/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/network/ip/interfaces/80d271c9-1f43-11e9-803e-005056a7646a"
{
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


__all__ = ["IpInterface", "IpInterfaceSchema"]
__pdoc__ = {
    "IpInterfaceSchema.resource": False,
    "IpInterfaceSchema.patchable_fields": False,
    "IpInterfaceSchema.postable_fields": False,
}


class IpInterfaceSchema(ResourceSchema):
    """The fields of the IpInterface object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ip_interface. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The administrative state of the interface. """

    ip = fields.Nested("netapp_ontap.models.ip_info.IpInfoSchema", data_key="ip", unknown=EXCLUDE)
    r""" The ip field of the ip_interface. """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the ip_interface. """

    location = fields.Nested("netapp_ontap.models.ip_interface_location.IpInterfaceLocationSchema", data_key="location", unknown=EXCLUDE)
    r""" The location field of the ip_interface. """

    name = fields.Str(
        data_key="name",
    )
    r""" Interface name

Example: dataLif1 """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" for interfaces owned by an SVM. Otherwise, set to "cluster".

Valid choices:

* svm
* cluster """

    service_policy = fields.Nested("netapp_ontap.resources.ip_service_policy.IpServicePolicySchema", data_key="service_policy", unknown=EXCLUDE)
    r""" The service_policy field of the ip_interface. """

    services = fields.List(fields.Str, data_key="services")
    r""" The services associated with the interface. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['up', 'down']),
    )
    r""" The operational state of the interface.

Valid choices:

* up
* down """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the ip_interface. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The UUID that uniquely identifies the interface.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    vip = fields.Boolean(
        data_key="vip",
    )
    r""" True for a VIP interface, whose location is announced via BGP. """

    @property
    def resource(self):
        return IpInterface

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "ip",
            "location",
            "name",
            "service_policy.name",
            "service_policy.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "ip",
            "ipspace.name",
            "ipspace.uuid",
            "location",
            "name",
            "scope",
            "service_policy.name",
            "service_policy.uuid",
            "svm.name",
            "svm.uuid",
            "vip",
        ]

class IpInterface(Resource):
    """Allows interaction with IpInterface objects on the host"""

    _schema = IpInterfaceSchema
    _path = "/api/network/ip/interfaces"
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
        r"""Retrieves the details of all IP interfaces.
### Related ONTAP Commands
* `network interface show`

### Learn more
* [`DOC /network/ip/interfaces`](#docs-networking-network_ip_interfaces)"""
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
        r"""Updates an IP interface.
### Related ONTAP commands
* `network interface migrate`
* `network interface modify`
* `network interface rename`
* `network interface revert`

### Learn more
* [`DOC /network/ip/interfaces`](#docs-networking-network_ip_interfaces)"""
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
        r"""Deletes an IP interface.
### Related ONTAP commands
* `network interface delete`

### Learn more
* [`DOC /network/ip/interfaces`](#docs-networking-network_ip_interfaces)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the details of all IP interfaces.
### Related ONTAP Commands
* `network interface show`

### Learn more
* [`DOC /network/ip/interfaces`](#docs-networking-network_ip_interfaces)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves details for a specific IP interface.
### Related ONTAP commands
* `network interface show`

### Learn more
* [`DOC /network/ip/interfaces`](#docs-networking-network_ip_interfaces)"""
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
        r"""Creates a new Cluster-scoped or SVM-scoped interface.<br/>
### Required properties
* `name` - Name of the interface to create.
* `ip.address` - IP address for the interface.
* `ip.netmask` - IP subnet of the interface.
* `ipspace.name` or `ipspace.uuid`
  * Required for Cluster-scoped interfaces.
  * Optional for SVM-scoped interfaces.
* `svm.name` or `svm.uuid`
  * Required for an SVM-scoped interface.
  * Invalid for a Cluster-scoped interface.
* `location.home_port` or `location.home_node` or `location.broadcast_domain` - One of these properties must be set to a value to define where the interface will be located.
### Recommended property values
* `service_policy`
  * `for SVM scoped interfaces`
    * _default-data-files_ for interfaces carrying file-oriented NAS data traffic
    * _default-data-blocks_ for interfaces carrying block-oriented SAN data traffic
    * _default-management_ for interfaces carrying SVM management requests
  * `for Cluster scoped interfaces`
    * _default-intercluster_ for interfaces carrying cluster peering traffic
    * _default-management_ for interfaces carrying system management requests
    * _default-route-announce_ for interfaces carrying BGP peer connections
### Default property values
If not specified in POST, the following default property values are assigned:
* `scope`
  * _svm_ if svm parameter is specified.
  * _cluster_ if svm parameter is not specified
* `enabled` - _true_
* `location.auto_revert` - _true_
* `service_policy`
  * _default-data-files_ if scope is `svm`
  * _default-management_ if scope is `cluster` and IPspace is not `Cluster`
  * _default-cluster_ if scope is `svm` and IPspace is `Cluster`
* `failover` - Selects the least restrictive failover policy supported by all the services in the service policy.
### Related ONTAP commands
* `network interface create`

### Learn more
* [`DOC /network/ip/interfaces`](#docs-networking-network_ip_interfaces)"""
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
        r"""Updates an IP interface.
### Related ONTAP commands
* `network interface migrate`
* `network interface modify`
* `network interface rename`
* `network interface revert`

### Learn more
* [`DOC /network/ip/interfaces`](#docs-networking-network_ip_interfaces)"""
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
        r"""Deletes an IP interface.
### Related ONTAP commands
* `network interface delete`

### Learn more
* [`DOC /network/ip/interfaces`](#docs-networking-network_ip_interfaces)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


