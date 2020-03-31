# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

# Overview
You can use this API to add nodes to a cluster, update node-specific configurations, and retrieve the current node configuration details.
## Adding a node to a cluster
You can add a node to a cluster by issuing a POST /cluster/nodes request to a node currently in the cluster. All nodes must be running the same version of ONTAP to use this API. Mixed version joins are not supported in this release. You can provide properties as fields in the body of the POST request to configure node-specific settings. On a successful request, POST /cluster/nodes returns a status code of 202 and job information in the body of the request. You can use the /cluster/jobs APIs to track the status of the node add job.
### Fields used for adding a node
Fields used for the /cluster/nodes APIs fall into the following categories:

* Required node fields
* Optional fields
* Network interface fields
* Records field
### Required node fields
The following field is required for any POST /cluster/nodes request:

* cluster_interface.ip.address
### Optional fields
All of the following fields are used to set up additional cluster-wide configurations:

* name
* location
* records
### Network interface fields
You can set a node-specific configuration for each node by using the POST /cluster/nodes API. If you provide a field in the body of a node, provide it for all nodes in the POST body.
You can provide the node management interface for each node if all node management interfaces in the cluster use the same subnet mask. If the node management interfaces use different subnet masks, use the /network/ip/interfaces API to configure the node management interfaces.
### The records field
To add multiple nodes to the cluster in one request, provide an array named "records" with multiple node entries. Each node entry in "records" must follow the required and optional fields listed previously. When only adding a single node, you do not need a "records" field. See "Examples" for an example of how to use the "records" field.
### Create recommended aggregates parameter
When you set the "create_recommended_aggregates" parameter to "true", aggregates based on an optimal layout recommended by the system are created on each of the nodes being added to the cluster. The default setting is "false".
<br/>
---
## Modifying node configurations
The following fields can be used to modify a node configuration:

* name
* location
<br/>
---
## Modifying service processor configurations
When modifying the "service_processor" properties, the job returns success immediately if valid network information is passed in. The values remain in their old state until the network information changes have taken effect on the service processor. You can poll the modified properties until the values are updated.
<br/>
---
## Deleting a node from a cluster
You can delete a node from the cluster. Before deleting a node from the cluster, shut down all of the node's shared resources, such as virtual interfaces to clients. If any of the node's shared resources are still active, the command fails.
You can use the "force" flag to forcibly remove a node that is down and cannot be brought online to remove its shared resources. This flag is set to "false" by default.
<br/>
---
## Node state
The node "state" field in the /cluster/nodes API represents the current operational state of individual nodes.
Note that the state of a node is a transient value and can change depending on the current condition of the node, especially during reboot, takeover, and giveback.
Possible values for the node state are:

* <i>up</i> - Node is fully operational and is able to accept and handle management requests. It is connected to a majority of healthy (up) nodes in the cluster through the cluster interconnect and all critical services are online.
* <i>booting</i> - Node is starting up and is not yet fully functional. It might not yet be accessible through the management interface or cluster interconnect. One or more critical services are offline on the node and the node is not taken over. The HA partner reports the node's firmware state as "SF_BOOTING", "SF_BOOTED", or "SF_CLUSTERWAIT".
* <i>down</i> - Node is known to be down.  It cannot be reached through the management interface or cluster interconnect. The HA partner can be reached and reports that the node is halted/rebooted without takeover. Or, the HA partner cannot be reached (or no SFO configured) but the node shutdown request has been recorded by the quorum change coordinator. The state is reported by the node's HA partner.
* <i>taken_over</i> - Node is taken over by its HA partner. The state is reported by the node's HA partner.
* <i>waiting_for_giveback</i> - Node is taken over by its HA partner and is now ready and waiting for giveback. To bring the node up, either issue the "giveback" command to the HA partner node or wait for auto-giveback, if enabled. The state is reported by the node's HA partner.
* <i>degraded</i> - Node is known to be up but is not yet fully functional. The node can be reached through the cluster interconnect but one or more critical services are offline. Or, the node is not reachable but the node's HA partner can be reached and reports that the node is up with firmware state "SF_UP".
* <i>unknown</i> - Node state cannot be determined.
<br/>
---
## HA
The "ha" field in the /cluster/nodes API shows the takeover and giveback states of the node along with the current values of the HA fields "enabled"and "auto_giveback".
You can modify the HA fields "enabled" and "auto_giveback", which will change the HA states of the node.
### Takeover
The takeover "state" field shows the different takeover states of the node. When the state is "failed", the "code" and "message" fields display.
Possible values for takeover states are:

* <i>not_attempted</i> - Takeover operation is not started and takeover is possible.
* <i>not_possible</i> - Takeover operation is not possible. Check the failure message.
* <i>in_progress</i> - Takeover operation is in progress. The node is taking over its partner.
* <i>in_takeover</i> - Takeover operation is complete.
* <i>failed</i> - Takeover operation failed. Check the failure message.
###
Possible values for takeover failure code and messages are:

* <i>code</i>: 852130 <i>message</i>: Failed to initiate takeover. Run the \"storage failover show-takeover\" command for more information.
* <i>code</i>: 852131 <i>message</i>: Takeover cannot be completed. Reason: disabled.
### Giveback
The giveback "state" field shows the different giveback states of the node. When the state is "failed", the "code" and "message" fields display.
Possible values for giveback states are:

* <i>nothing_to_giveback</i> - Node does not have partner aggregates to giveback.
* <i>not_attempted</i> - Giveback operation is not started.
* <i>in_progress</i> - Giveback operation is in progress.
* <i>failed</i> - Giveback operation failed. Check the failure message.
###
Possible values for giveback failure codes and messages are:

* <i>code</i>: 852126 <i>message</i>: Failed to initiate giveback. Run the \"storage failover show-giveback\" command for more information.
<br/>
---
## Examples
The following examples show how to add nodes to a cluster, update node properties, shutdown and reboot a node, and remove a node from the cluster.
### Adding a single node with a minimal configuration
```
# Body
body =
{
  "cluster_interface": {
    "ip": {
      "address": "1.1.1.1"
    }
  }
}
# Request
curl -X POST "https://<mgmt-ip>/api/cluster/nodes" -d body
```
---
### Adding multiple nodes in the same request and creating recommended aggregates
```
# Body
body =
{
  "records": [
      {
          "name": "node1",
          "cluster_interface": {
            "ip": {
              "address": "1.1.1.1"
            }
          }
      },
      {
          "name": "node2",
          "cluster_interface": {
            "ip": {
              "address": "2.2.2.2"
            }
          }
      },
  ]
}
# Request
curl -X POST "https://<mgmt-ip>/api/cluster/nodes?create_recommended_aggregates=true" -d body
```
---
### Modifying a cluster-wide configuration
```
# Body
body =
{
  "name": "renamedNode",
  "location": "newLocation"
}
# Request
curl -X PATCH "https://<mgmt-ip>/api/cluster/nodes" -d body
```
---
### Shutting down a node
```
curl -X PATCH "https://<mgmt-ip>/api/cluster/nodes/{uuid}?action=shutdown"
```
---
### Deleting a node from a cluster
```
curl -X DELETE "https://<mgmt-ip>/api/cluster/nodes/{uuid}"
curl -X DELETE "https://<mgmt-ip>/api/cluster/nodes/{uuid}?force=true"
```
---
### Retrieving the state of all nodes in a cluster
```
#Request
curl -siku admin -X GET "https://<mgmt-ip>/api/cluster/nodes?fields=state"
#Response
{
  "records": [
    {
      "uuid": "54440ec3-6127-11e9-a959-005056bb76f9",
      "name": "node2",
      "state": "up",
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/54440ec3-6127-11e9-a959-005056bb76f9"
        }
      }
    },
    {
      "uuid": "e02dbef1-6126-11e9-b8fb-005056bb9ce4",
      "name": "node1",
      "state": "up",
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/e02dbef1-6126-11e9-b8fb-005056bb9ce4"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/cluster/nodes?fields=state"
    }
  }
}
```
---
### Retrieving takeover and giveback failure codes and messages
```
#Request
curl -siku admin -X GET "https://<mgmt-ip>/api/cluster/nodes?fields=ha"
#Response
{
  "records": [
    {
      "uuid": "54440ec3-6127-11e9-a959-005056bb76f9",
      "name": "node2",
      "ha": {
        "enabled": false,
        "auto_giveback": false,
        "partners": [
          {
            "uuid": "e02dbef1-6126-11e9-b8fb-005056bb9ce4",
            "name": "node1"
          }
        ],
        "giveback": {
              "state": "nothing_to_giveback"
        },
        "takeover": {
          "state": "not_possible",
          "failure": {
            "message": "Takeover cannot be completed. Reason: disabled.",
            "code": 852131
          }
        },
        "ports": [
          {
            "name": "e0h"
          },
          {
            "name": "N/A"
          }
        ]
      },
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/54440ec3-6127-11e9-a959-005056bb76f9"
        }
      }
    },
    {
      "uuid": "e02dbef1-6126-11e9-b8fb-005056bb9ce4",
      "name": "node1",
      "ha": {
        "enabled": false,
        "auto_giveback": false,
        "partners": [
          {
            "uuid": "54440ec3-6127-11e9-a959-005056bb76f9",
            "name": "node2"
          }
        ],
        "giveback": {
              "state": "nothing_to_giveback"
        },
        "takeover": {
          "state": "not_possible",
          "failure": {
            "message": "Takeover cannot be completed. Reason: disabled.",
            "code": 852131
          }
        },
        "ports": [
          {
            "name": "e0h"
          },
          {
            "name": "N/A"
          }
        ]
      },
      "_links": {
        "self": {
          "href": "/api/cluster/nodes/e02dbef1-6126-11e9-b8fb-005056bb9ce4"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/cluster/nodes?fields=state"
    }
  }
}
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Node", "NodeSchema"]
__pdoc__ = {
    "NodeSchema.resource": False,
    "NodeSchema.patchable_fields": False,
    "NodeSchema.postable_fields": False,
}


class NodeSchema(ResourceSchema):
    """The fields of the Node object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the node. """

    cluster_interface = fields.Nested("netapp_ontap.models.node_cluster_interface.NodeClusterInterfaceSchema", data_key="cluster_interface", unknown=EXCLUDE)
    r""" The cluster_interface field of the node. """

    cluster_interfaces = fields.List(fields.Nested("netapp_ontap.resources.ip_interface.IpInterfaceSchema", unknown=EXCLUDE), data_key="cluster_interfaces")
    r""" The cluster_interfaces field of the node. """

    controller = fields.Nested("netapp_ontap.models.node_controller.NodeControllerSchema", data_key="controller", unknown=EXCLUDE)
    r""" The controller field of the node. """

    date = fields.DateTime(
        data_key="date",
    )
    r""" The current or "wall clock" time of the node in ISO-8601 date, time, and time zone format.
The ISO-8601 date and time are localized based on the ONTAP cluster's timezone setting.


Example: 2019-04-17T15:49:26.000+0000 """

    ha = fields.Nested("netapp_ontap.models.node_ha.NodeHaSchema", data_key="ha", unknown=EXCLUDE)
    r""" The ha field of the node. """

    location = fields.Str(
        data_key="location",
    )
    r""" The location field of the node.

Example: rack 2 row 5 """

    management_interface = fields.Nested("netapp_ontap.models.node_management_interface.NodeManagementInterfaceSchema", data_key="management_interface", unknown=EXCLUDE)
    r""" The management_interface field of the node. """

    management_interfaces = fields.List(fields.Nested("netapp_ontap.resources.ip_interface.IpInterfaceSchema", unknown=EXCLUDE), data_key="management_interfaces")
    r""" The management_interfaces field of the node. """

    membership = fields.Str(
        data_key="membership",
        validate=enum_validation(['available', 'joining', 'member']),
    )
    r""" Possible values:

* <i>available</i> - A node is detected on the internal cluster network and can be added to the cluster.  Nodes that have a membership of "available" are not returned when a GET request is called when the cluster exists. Provide a query on the "membership" property for <i>available</i> to scan for nodes on the cluster network. Nodes that have a membership of "available" are returned automatically before a cluster is created.
* <i>joining</i> - Joining nodes are in the process of being added to the cluster. The node might be progressing through the steps to become a member or might have failed. The job to add the node or create the cluster provides details on the current progress of the node.
* <i>member</i> - Nodes that are members have successfully joined the cluster.


Valid choices:

* available
* joining
* member """

    model = fields.Str(
        data_key="model",
    )
    r""" The model field of the node.

Example: FAS3070 """

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the node.

Example: node-01 """

    serial_number = fields.Str(
        data_key="serial_number",
    )
    r""" The serial_number field of the node.

Example: 4048820-60-9 """

    service_processor = fields.Nested("netapp_ontap.models.service_processor.ServiceProcessorSchema", data_key="service_processor", unknown=EXCLUDE)
    r""" The service_processor field of the node. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['up', 'booting', 'down', 'taken_over', 'waiting_for_giveback', 'degraded', 'unknown']),
    )
    r""" State of the node:

* <i>up</i> - Node is up and operational.
* <i>booting</i> - Node is booting up.
* <i>down</i> - Node has stopped or is dumping core.
* <i>taken_over</i> - Node has been taken over by its HA partner and is not yet waiting for giveback.
* <i>waiting_for_giveback</i> - Node has been taken over by its HA partner and is waiting for the HA partner to giveback disks.
* <i>degraded</i> - Node has one or more critical services offline.
* <i>unknown</i> - Node or its HA partner cannot be contacted and there is no information on the node's state.


Valid choices:

* up
* booting
* down
* taken_over
* waiting_for_giveback
* degraded
* unknown """

    system_id = fields.Str(
        data_key="system_id",
    )
    r""" The system_id field of the node.

Example: 92027651 """

    system_machine_type = fields.Str(
        data_key="system_machine_type",
    )
    r""" OEM system machine type.

Example: 7Y56-CTOWW1 """

    uptime = fields.Integer(
        data_key="uptime",
    )
    r""" The total time, in seconds, that the node has been up.

Example: 300536 """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the node.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    vendor_serial_number = fields.Str(
        data_key="vendor_serial_number",
    )
    r""" OEM vendor serial number.

Example: 791603000068 """

    version = fields.Nested("netapp_ontap.models.version.VersionSchema", data_key="version", unknown=EXCLUDE)
    r""" The version field of the node. """

    vm = fields.Nested("netapp_ontap.models.node_vm.NodeVmSchema", data_key="vm", unknown=EXCLUDE)
    r""" The vm field of the node. """

    @property
    def resource(self):
        return Node

    @property
    def patchable_fields(self):
        return [
            "controller",
            "ha",
            "location",
            "name",
            "vm",
        ]

    @property
    def postable_fields(self):
        return [
            "cluster_interface",
            "controller",
            "ha",
            "location",
            "management_interface",
            "name",
            "vm",
        ]

class Node(Resource):
    r""" Complete node information """

    _schema = NodeSchema
    _path = "/api/cluster/nodes"
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
        r"""Retrieves the nodes in the cluster.
### Related ONTAP commands
* `system node show`

### Learn more
* [`DOC /cluster/nodes`](#docs-cluster-cluster_nodes)"""
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
        r"""Updates the node information or performs shutdown/reboot actions on a node.
### Related ONTAP commands
* `cluster ha modify`
* `storage failover modify`
* `system node modify`
* `system node reboot`
* `system service-processor network modify`

### Learn more
* [`DOC /cluster/nodes`](#docs-cluster-cluster_nodes)"""
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
        r"""Deletes a node from the cluster.
Note that before deleting a node from the cluster, you must shut down all of the node's shared resources, such as virtual interfaces to clients. If any of the node's shared resources are still active, the command fails.
### Optional parameters:
* `force` - Forcibly removes a node that is down and cannot be brought online to remove its shared resources. This flag is set to "false" by default.
### Related ONTAP commands
* `cluster remove-node`
### Learn more
* [`DOC /cluster/nodes`](#docs-cluster-cluster_nodes)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the nodes in the cluster.
### Related ONTAP commands
* `system node show`

### Learn more
* [`DOC /cluster/nodes`](#docs-cluster-cluster_nodes)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves information for the node.
### Related ONTAP commands
* `cluster add-node-status`
* `cluster date show`
* `cluster ha show`
* `network interface show`
* `network port show`
* `storage failover show`
* `system controller show`
* `system node show`
* `system node show-discovered`
* `system service-processor network show`
* `system service-processor show`
* `version`

### Learn more
* [`DOC /cluster/nodes`](#docs-cluster-cluster_nodes)"""
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
        r"""Adds a node or nodes to the cluster.
### Required properties
* `cluster_interface.ip.address`
### Related ONTAP commands
* `cluster add-node`
* `network interface create`
* `storage aggregate auto-provision`
* `system node modify`
* `system service-processor network modify`

### Learn more
* [`DOC /cluster/nodes`](#docs-cluster-cluster_nodes)"""
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
        r"""Updates the node information or performs shutdown/reboot actions on a node.
### Related ONTAP commands
* `cluster ha modify`
* `storage failover modify`
* `system node modify`
* `system node reboot`
* `system service-processor network modify`

### Learn more
* [`DOC /cluster/nodes`](#docs-cluster-cluster_nodes)"""
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
        r"""Deletes a node from the cluster.
Note that before deleting a node from the cluster, you must shut down all of the node's shared resources, such as virtual interfaces to clients. If any of the node's shared resources are still active, the command fails.
### Optional parameters:
* `force` - Forcibly removes a node that is down and cannot be brought online to remove its shared resources. This flag is set to "false" by default.
### Related ONTAP commands
* `cluster remove-node`
### Learn more
* [`DOC /cluster/nodes`](#docs-cluster-cluster_nodes)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


