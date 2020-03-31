# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Fibre Channel (FC) interfaces are the logical endpoints for FC network connections to an SVM. An FC interface provides FC access to storage within the interface SVM using either Fibre Channel Protocol or NVMe over FC (NVMe/FC).<br/>
The Fibre Channel interface REST API allows you to create, delete, update, and discover FC interfaces, and obtain status information for FC interfaces.<br/>
An FC interface is created on an FC port which is located on a cluster node. The FC port must be specified to identify the location of the interface for a POST or PATCH request that relocates an interface. You can identify the port by supplying either the node and port names or the port UUID.
## Examples
### Creating an FC interface using the port node and name to identify the location
This example uses the `return_records` query parameter to retrieve the newly created FC interface in the POST response.
<br/>
```
# The API:
POST /api/network/fc/interfaces
# The call:
curl -X POST 'https://<mgmt-ip>/api/network/fc/interfaces?return_records=true' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm1" }, "name": "lif1", "location": { "port": { "name": "0a", "node": { "name": "node1" } } }, "data_protocol": "fcp" }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "cf300f5c-db83-11e8-bd46-005056bba0e0",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/cf300f5c-db83-11e8-bd46-005056bba0e0"
          }
        }
      },
      "uuid": "f6045b92-dec7-11e8-a733-005056bba0e0",
      "name": "lif1",
      "location": {
        "node": {
          "uuid": "bafe9b9f-db81-11e8-bd46-005056bba0e0",
          "name": "node1",
          "_links": {
            "self": {
              "href": "/api/cluster/nodes/bafe9b9f-db81-11e8-bd46-005056bba0e0"
            }
          }
        },
        "port": {
          "uuid": "300c1ae3-db82-11e8-bd46-005056bba0e0",
          "name": "0a",
          "node": {
            "name": "node1"
          },
          "_links": {
            "self": {
              "href": "/api/network/fc/ports/300c1ae3-db82-11e8-bd46-005056bba0e0"
            }
          }
        }
      },
      "enabled": true,
      "state": "down",
      "data_protocol": "fcp",
      "wwpn": "20:04:00:50:56:bb:a0:e0",
      "wwnn": "20:00:00:50:56:bb:a0:e0",
      "port_address": "9da2cb1",
      "_links": {
        "self": {
          "href": "/api/network/fc/interfaces/f6045b92-dec7-11e8-a733-005056bba0e0"
        }
      }
    }
  ]
}
```
---
### Creating an FC interface using the port UUID to identify the location
This example uses the `return_records` query parameter to retrieve the newly created FC interface in the POST response.
<br/>
```
# The API:
POST /api/network/fc/interfaces
# The call:
curl -X POST 'https://<mgmt-ip>/api/network/fc/interfaces?return_records=true' -H 'accept: application/hal+json' -d '{ "svm": { "name": "svm3" }, "name": "lif2", "location": { "port": { "uuid": "24bb636a-db83-11e8-9a49-005056bb1ec6" } }, "data_protocol": "fc_nvme" }'
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "a5060466-dbab-11e8-bd46-005056bba0e0",
        "name": "svm3",
        "_links": {
          "self": {
            "href": "/api/svm/svms/a5060466-dbab-11e8-bd46-005056bba0e0"
          }
        }
      },
      "uuid": "cdeb5591-dec9-11e8-a733-005056bba0e0",
      "name": "lif2",
      "location": {
        "node": {
          "uuid": "e85aa147-db83-11e8-9a48-005056bb1ec6",
          "name": "node3",
          "_links": {
            "self": {
              "href": "/api/cluster/nodes/e85aa147-db83-11e8-9a48-005056bb1ec6"
            }
          }
        },
        "port": {
          "uuid": "24bb636a-db83-11e8-9a49-005056bb1ec6",
          "name": "1b",
          "node": {
            "name": "node3"
          },
          "_links": {
            "self": {
              "href": "/api/network/fc/ports/24bb636a-db83-11e8-9a49-005056bb1ec6"
            }
          }
        }
      },
      "enabled": true,
      "state": "down",
      "data_protocol": "fc_nvme",
      "wwpn": "20:05:00:50:56:bb:a0:e0",
      "wwnn": "20:02:00:50:56:bb:a0:e0",
      "port_address": "612e202b",
      "_links": {
        "self": {
          "href": "/api/network/fc/interfaces/cdeb5591-dec9-11e8-a733-005056bba0e0"
        }
      }
    }
  ]
}
```
---
### Retrieving all properties for all FC interfaces
This example uses the `fields` query parameter to retrieve all properties.
<br/>
```
# The API:
GET /api/network/fc/interfaces
# The call:
curl -X GET 'https://<mgmt-ip>/api/network/fc/interfaces?fields=*' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "a5060466-dbab-11e8-bd46-005056bba0e0",
        "name": "svm3",
        "_links": {
          "self": {
            "href": "/api/svm/svms/a5060466-dbab-11e8-bd46-005056bba0e0"
          }
        }
      },
      "uuid": "cdeb5591-dec9-11e8-a733-005056bba0e0",
      "name": "lif2",
      "location": {
        "node": {
          "uuid": "e85aa147-db83-11e8-9a48-005056bb1ec6",
          "name": "node3",
          "_links": {
            "self": {
              "href": "/api/cluster/nodes/e85aa147-db83-11e8-9a48-005056bb1ec6"
            }
          }
        },
        "port": {
          "uuid": "24bb636a-db83-11e8-9a49-005056bb1ec6",
          "name": "1b",
          "node": {
            "name": "node3"
          },
          "_links": {
            "self": {
              "href": "/api/network/fc/ports/24bb636a-db83-11e8-9a49-005056bb1ec6"
            }
          }
        }
      },
      "enabled": true,
      "state": "down",
      "data_protocol": "fc_nvme",
      "wwpn": "20:05:00:50:56:bb:a0:e0",
      "wwnn": "20:02:00:50:56:bb:a0:e0",
      "port_address": "612e202b",
      "_links": {
        "self": {
          "href": "/api/network/fc/interfaces/cdeb5591-dec9-11e8-a733-005056bba0e0"
        }
      }
    },
    {
      "svm": {
        "uuid": "cf300f5c-db83-11e8-bd46-005056bba0e0",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/cf300f5c-db83-11e8-bd46-005056bba0e0"
          }
        }
      },
      "uuid": "f6045b92-dec7-11e8-a733-005056bba0e0",
      "name": "lif1",
      "location": {
        "node": {
          "uuid": "bafe9b9f-db81-11e8-bd46-005056bba0e0",
          "name": "node1",
          "_links": {
            "self": {
              "href": "/api/cluster/nodes/bafe9b9f-db81-11e8-bd46-005056bba0e0"
            }
          }
        },
        "port": {
          "uuid": "300c1ae3-db82-11e8-bd46-005056bba0e0",
          "name": "0a",
          "node": {
            "name": "node1"
          },
          "_links": {
            "self": {
              "href": "/api/network/fc/ports/300c1ae3-db82-11e8-bd46-005056bba0e0"
            }
          }
        }
      },
      "enabled": true,
      "state": "down",
      "data_protocol": "fcp",
      "wwpn": "20:04:00:50:56:bb:a0:e0",
      "wwnn": "20:00:00:50:56:bb:a0:e0",
      "port_address": "9da2cb1",
      "_links": {
        "self": {
          "href": "/api/network/fc/interfaces/f6045b92-dec7-11e8-a733-005056bba0e0"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/network/fc/interfaces?fields=*"
    }
  }
}
```
---
### Retrieving a list of selected FC interfaces
This example uses property query parameters to retrieve FC interfaces configured for the FC Protocol that are set to _up_.
<br/>
```
# The API:
GET /api/network/fc/interfaces
# The call:
curl -X GET 'https://<mgmt-ip>/api/network/fc/interfaces?data_protocol=fcp&state=up' -H 'accept: application/hal+json'
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "cf300f5c-db83-11e8-bd46-005056bba0e0",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/cf300f5c-db83-11e8-bd46-005056bba0e0"
          }
        }
      },
      "uuid": "f6045b92-dec7-11e8-a733-005056bba0e0",
      "name": "lif1",
      "state": "up",
      "data_protocol": "fcp",
      "_links": {
        "self": {
          "href": "/api/network/fc/interfaces/f6045b92-dec7-11e8-a733-005056bba0e0"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/network/fc/interfaces?data_protocol=fcp&state=up"
    }
  }
}
```
---
### Retrieving a specific FC interface
```
# The API:
GET /api/network/fc/interfaces/{uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/network/fc/interfaces/cdeb5591-dec9-11e8-a733-005056bba0e0' -H 'accept: application/hal+json'
# The response:
{
  "svm": {
    "uuid": "a5060466-dbab-11e8-bd46-005056bba0e0",
    "name": "svm3",
    "_links": {
      "self": {
        "href": "/api/svm/svms/a5060466-dbab-11e8-bd46-005056bba0e0"
      }
    }
  },
  "uuid": "cdeb5591-dec9-11e8-a733-005056bba0e0",
  "name": "lif2",
  "location": {
    "node": {
      "uuid": "e85aa147-db83-11e8-9a48-005056bb1ec6",
      "name": "node3",
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/e85aa147-db83-11e8-9a48-005056bb1ec6"
        }
      }
    },
    "port": {
      "uuid": "24bb636a-db83-11e8-9a49-005056bb1ec6",
      "name": "1b",
      "node": {
        "name": "node3"
      },
      "_links": {
        "self": {
          "href": "/api/network/fc/ports/24bb636a-db83-11e8-9a49-005056bb1ec6"
        }
      }
    }
  },
  "enabled": true,
  "state": "down",
  "data_protocol": "fc_nvme",
  "wwpn": "20:05:00:50:56:bb:a0:e0",
  "wwnn": "20:02:00:50:56:bb:a0:e0",
  "port_address": "612e202b",
  "_links": {
    "self": {
      "href": "/api/network/fc/interfaces/cdeb5591-dec9-11e8-a733-005056bba0e0"
    }
  }
}
```
---
## Disabling an FC interface
When updating certain properties or deleting an FC interface, the interface must first be disabled using the following:
<br/>
```
# The API:
PATCH /api/network/fc/interfaces/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/network/fc/interfaces/f6045b92-dec7-11e8-a733-005056bba0e0' -H 'accept: application/hal+json' -d '{ "enabled": false }'
```
---
### Moving an FC interface to a new node and port
To move an FC interface to another node or port, the destination FC port must be specified in a PATCH request. Either the port UUID or node and port names can be used to identify the port.<br/>
Note that only FC interfaces configured for the FC Protocol can be moved. FC interfaces configured for NVMe/FC cannot be moved. The interface must also be set to the disabled state before being moved.
<br/>
```
# The API:
PATCH /api/network/fc/interfaces/{uuid}
# The call:
curl -X PATCH 'https://<mgmt-ip>/api/network/fc/interfaces/f6045b92-dec7-11e8-a733-005056bba0e0' -H 'accept: application/hal+json' -d '{ "location": { "port": { "uuid": "a1dc7aa5-db83-11e8-9ef7-005056bbbbcc" } } }'
```
---
### Deleting an FC interface
The FC interface must be disabled before being deleted.
<br/>
```
# The API:
DELETE /api/network/fc/interfaces/{uuid}
# The call:
curl -X DELETE 'https://<mgmt-ip>/api/network/fc/interfaces/f6045b92-dec7-11e8-a733-005056bba0e0' -H 'accept: application/hal+json'
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["FcInterface", "FcInterfaceSchema"]
__pdoc__ = {
    "FcInterfaceSchema.resource": False,
    "FcInterfaceSchema.patchable_fields": False,
    "FcInterfaceSchema.postable_fields": False,
}


class FcInterfaceSchema(ResourceSchema):
    """The fields of the FcInterface object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the fc_interface. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" A user configurable comment. Optional in POST; valid in PATCH. To clear a prior comment, set the property to an empty string in PATCH. """

    data_protocol = fields.Str(
        data_key="data_protocol",
        validate=enum_validation(['fcp', 'fc_nvme']),
    )
    r""" The data protocol for which the FC interface is configured. Required in POST.


Valid choices:

* fcp
* fc_nvme """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The administrative state of the FC interface. The FC interface can be disabled to block all FC communication with the SVM through this interface. Optional in POST and PATCH; defaults to _true_ (enabled) in POST. """

    location = fields.Nested("netapp_ontap.models.fc_interface_location.FcInterfaceLocationSchema", data_key="location", unknown=EXCLUDE)
    r""" The location field of the fc_interface. """

    name = fields.Str(
        data_key="name",
    )
    r""" The name of the FC interface. Required in POST; optional in PATCH.


Example: lif1 """

    port_address = fields.Str(
        data_key="port_address",
    )
    r""" The port address of the FC interface. Each FC port in an FC switched fabric has its own unique FC port address for routing purposes. The FC port address is assigned by a switch in the fabric when that port logs in to the fabric. This property refers to the address given by a switch to the FC interface when the SVM performs a port login (PLOGI).<br/>
This is useful for obtaining statistics and diagnostic information from FC switches.<br/>
This is a hexadecimal encoded numeric value.


Example: 5060F """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['up', 'down']),
    )
    r""" The current operational state of the FC interface. The state is set to _down_ if the interface is not enabled.<br/>
If the node hosting the port is down or unavailable, no state value is returned.


Valid choices:

* up
* down """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the fc_interface. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the FC interface. Required in the URL.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    wwnn = fields.Str(
        data_key="wwnn",
    )
    r""" The world wide node name (WWNN) of the FC interface SVM. The WWNN is generated by ONTAP when Fibre Channel Protocol or the NVMe service is created for the FC interface SVM.


Example: 20:00:00:50:56:b4:13:01 """

    wwpn = fields.Str(
        data_key="wwpn",
    )
    r""" The world wide port name (WWPN) of the FC interface. The WWPN is generated by ONTAP when the FC interface is created.


Example: 20:00:00:50:56:b4:13:a8 """

    @property
    def resource(self):
        return FcInterface

    @property
    def patchable_fields(self):
        return [
            "comment",
            "enabled",
            "location",
            "name",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "comment",
            "data_protocol",
            "enabled",
            "location",
            "name",
            "svm.name",
            "svm.uuid",
        ]

class FcInterface(Resource):
    r""" A Fibre Channel (FC) interface is the logical endpoint for FC network connections to an SVM. An FC interface provides FC access to storage within the interface SVM using either Fibre Channel Protocol or NVMe over Fibre Channel (NVMe/FC).<br/>
An FC interface is created on an FC port which is located on a cluster node. The FC port must be specified to identify the location of the interface for a POST or PATCH operation that relocates an interface. You can identify the port by supplying either the node and port names or the port UUID. """

    _schema = FcInterfaceSchema
    _path = "/api/network/fc/interfaces"
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
        r"""Retrieves FC interfaces.
### Related ONTAP commands
* `network interface show`
* `vserver fcp interface show`
### Learn more
* [`DOC /network/fc/interfaces`](#docs-networking-network_fc_interfaces)
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
        r"""Updates an FC interface.
### Related ONTAP commands
* `network interface modify`
### Learn more
* [`DOC /network/fc/interfaces`](#docs-networking-network_fc_interfaces)
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
        r"""Deletes an FC interface.
### Related ONTAP commands
* `network interface delete`
### Learn more
* [`DOC /network/fc/interfaces`](#docs-networking-network_fc_interfaces)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves FC interfaces.
### Related ONTAP commands
* `network interface show`
* `vserver fcp interface show`
### Learn more
* [`DOC /network/fc/interfaces`](#docs-networking-network_fc_interfaces)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an FC interface.
### Related ONTAP commands
* `network interface show`
* `vserver fcp interface show`
### Learn more
* [`DOC /network/fc/interfaces`](#docs-networking-network_fc_interfaces)
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
        r"""Creates an FC interface.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the FC interface.
* `name` - Name of the FC interface.
* `location.port.uuid` or both `location.port.name` and `location.port.node.name` - FC port on which to create the FC interface.
* `data_protocol` - Data protocol for the FC interface.
### Default property values
If not specified in POST, the following default property values are assigned.
* `enabled` - _true_
### Related ONTAP commands
* `network interface create`
### Learn more
* [`DOC /network/fc/interfaces`](#docs-networking-network_fc_interfaces)
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
        r"""Updates an FC interface.
### Related ONTAP commands
* `network interface modify`
### Learn more
* [`DOC /network/fc/interfaces`](#docs-networking-network_fc_interfaces)
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
        r"""Deletes an FC interface.
### Related ONTAP commands
* `network interface delete`
### Learn more
* [`DOC /network/fc/interfaces`](#docs-networking-network_fc_interfaces)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


