# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
The FPolicy engine allows you to configure the external servers to which the file access notifications are sent. As part of FPolicy engine configuration, you can configure the server(s) to which the notification is sent, an optional set of secondary server(s) to which the notification is sent in the case of the primary server(s) failure, the port number for FPolicy application and the type of the engine, synchronous or asynchronous. </br>
For the synchronous engine, ONTAP will wait for a response from the FPolicy application before it allows the operation. With an asynchronous engine, ONTAP proceeds with the operation processing after sending the notification to the FPolicy application. An engine can belong to multiple FPolicy policies.
## Examples
### Creating an FPolicy engine
---
```
# The API:
POST /protocols/fpolicy/{svm.uuid}/engines
#The call:
curl -X POST "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/engines/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"name\": \"engine0\", \"port\": 9876, \"primary_servers\": [ \"10.132.145.22\", \"10.140.101.109\" ], \"secondary_servers\": [ \"10.132.145.20\", \"10.132.145.21\" ], \"type\": \"synchronous\"}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "name": "engine0",
      "primary_servers": [
        "10.132.145.22",
        "10.140.101.109"
      ],
      "secondary_servers": [
        "10.132.145.20",
        "10.132.145.21"
      ],
      "port": 9876,
      "type": "synchronous"
    }
  ]
}
```
---
### Creating an FPolicy engine with the minimum required fields
---
```
# The API:
POST /protocols/fpolicy/{svm.uuid}/engines
#The call:
curl -X POST "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/engines/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"name\": \"engine0\", \"port\": 9876, \"primary_servers\": [ \"10.132.145.22\", \"10.140.101.109\" ], \"type\": \"synchronous\"}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "name": "engine0",
      "primary_servers": [
        "10.132.145.22",
        "10.140.101.109"
      ],
      "port": 9876,
      "type": "synchronous"
    }
  ]
}
```
---
### Retrieving an FPolicy engine configuration for a particular SVM
---
```
# The API:
GET /protocols/fpolicy/{svm.uuid}/engines
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/engines/?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "4f643fb4-fd21-11e8-ae49-0050568e2c1e"
      },
      "name": "cifs",
      "primary_servers": [
        "10.20.20.10"
      ],
      "port": 9876,
      "type": "synchronous"
    },
    {
      "svm": {
        "uuid": "4f643fb4-fd21-11e8-ae49-0050568e2c1e"
      },
      "name": "nfs",
      "primary_servers": [
        "10.23.140.64",
        "10.140.101.109"
      ],
      "secondary_servers": [
        "10.132.145.20",
        "10.132.145.22"
      ],
      "port": 9876,
      "type": "synchronous"
    }
  ],
  "num_records": 2
}
```
---
### Retrieving a specific FPolicy engine configuration for an SVM
---
```
# The Api:
GET /protocols/fpolicy/{svm.uuid}/engines/{name}
#The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/engines/cifs?fields=*" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "4f643fb4-fd21-11e8-ae49-0050568e2c1e"
   },
   "name": "cifs",
   "primary_servers": [
     "10.20.20.10"
   ],
   "port": 9876,
   "type": "synchronous"
}
```
---
### Updating an FPolicy engine for an SVM
---
```
# The API:
PATCH /protocols/fpolicy/{svm.uuid}/engines/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/engines/cifs" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"port\": 6666, \"secondary_servers\": [ \"10.132.145.20\", \"10.132.145.21\" ], \"type\": \"synchronous\"}"
```
---
### Updating all the attributes of a specific FPolicy engine for an SVM
---
```
# The API:
PATCH /protocols/fpolicy/{svm.uuid}/engines/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/engines/cifs" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"port\": 9876, \"primary_servers\": [ \"10.132.145.20\", \"10.140.101.109\" ], \"secondary_servers\": [ \"10.132.145.23\", \"10.132.145.21\" ], \"type\": \"synchronous\"}"
```
---
### Deleting a specific FPolicy engine for an SVM
---
```
# The API:
DELETE /protocols/fpolicy/{svm.uuid}/engines/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/fpolicy/4f643fb4-fd21-11e8-ae49-0050568e2c1e/events/cifs" -H "accept: application/json"
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


__all__ = ["FpolicyEngine", "FpolicyEngineSchema"]
__pdoc__ = {
    "FpolicyEngineSchema.resource": False,
    "FpolicyEngineSchema.patchable_fields": False,
    "FpolicyEngineSchema.postable_fields": False,
}


class FpolicyEngineSchema(ResourceSchema):
    """The fields of the FpolicyEngine object"""

    name = fields.Str(
        data_key="name",
    )
    r""" Specifies the name to assign to the external server configuration.

Example: fp_ex_eng """

    port = fields.Integer(
        data_key="port",
    )
    r""" Port number of the FPolicy server application.

Example: 9876 """

    primary_servers = fields.List(fields.Str, data_key="primary_servers")
    r""" The primary_servers field of the fpolicy_engine.

Example: ["10.132.145.20","10.140.101.109"] """

    secondary_servers = fields.List(fields.Str, data_key="secondary_servers")
    r""" The secondary_servers field of the fpolicy_engine.

Example: ["10.132.145.20","10.132.145.21"] """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['synchronous', 'asynchronous']),
    )
    r""" The notification mode determines what ONTAP does after sending notifications to FPolicy servers.
  The possible values are:

    * synchronous  - After sending a notification, wait for a response from the FPolicy server.
    * asynchronous - After sending a notification, file request processing continues.


Valid choices:

* synchronous
* asynchronous """

    @property
    def resource(self):
        return FpolicyEngine

    @property
    def patchable_fields(self):
        return [
            "port",
            "primary_servers",
            "secondary_servers",
            "type",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "port",
            "primary_servers",
            "secondary_servers",
            "type",
        ]

class FpolicyEngine(Resource):
    r""" The engine defines how ONTAP makes and manages connections to external FPolicy servers. """

    _schema = FpolicyEngineSchema
    _path = "/api/protocols/fpolicy/{svm[uuid]}/engines"
    @property
    def _keys(self):
        return ["svm.uuid", "name"]

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
        r"""Retrieves FPolicy engine configurations of all the engines for a specified SVM. ONTAP allows creation of cluster-level FPolicy engines that act as a template for all the SVMs belonging to the cluster. These cluster-level FPolicy engines are also retrieved for the specified SVM.
### Related ONTAP commands
* `fpolicy policy external-engine show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/engines`](#docs-NAS-protocols_fpolicy_{svm.uuid}_engines)
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
        r"""Updates a specific FPolicy engine configuration of an SVM. Modification of an FPolicy engine that is attached to one or more enabled FPolicy policies is not allowed.
### Related ONTAP commands
* `fpolicy policy external-engine modify`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/engines`](#docs-NAS-protocols_fpolicy_{svm.uuid}_engines)
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
        r"""Deletes the FPolicy external engine configuration. Deletion of an FPolicy engine that is attached to one or more FPolicy policies is not allowed.
### Related ONTAP commands
* `fpolicy policy external-engine modify`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/engines`](#docs-NAS-protocols_fpolicy_{svm.uuid}_engines)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves FPolicy engine configurations of all the engines for a specified SVM. ONTAP allows creation of cluster-level FPolicy engines that act as a template for all the SVMs belonging to the cluster. These cluster-level FPolicy engines are also retrieved for the specified SVM.
### Related ONTAP commands
* `fpolicy policy external-engine show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/engines`](#docs-NAS-protocols_fpolicy_{svm.uuid}_engines)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a particular FPolicy engine configuration of a specifed SVM. A cluster-level FPolicy engine configuration cannot be retrieved for a data SVM.
### Related ONTAP commands
* `fpolicy policy external-engine show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/engines`](#docs-NAS-protocols_fpolicy_{svm.uuid}_engines)
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
        r"""Creates an FPolicy engine configuration for a specified SVM. FPolicy engine creation is allowed only on data SVMs.
### Required properties
* `svm.uuid` - Existing SVM in which to create the FPolicy engine.
* `name` - Name of external engine.
* `port` - Port number of the FPolicy server application.
* `primary_servers` - List of primary FPolicy servers to which the node will send notifications.
### Recommended optional properties
* `secondary_servers` - It is recommended to configure secondary FPolicy server to which the node will send notifications when the primary server is down.
### Default property values
* `type` - _synchronous_
### Related ONTAP commands
* `fpolicy policy external-engine create`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/engines`](#docs-NAS-protocols_fpolicy_{svm.uuid}_engines)
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
        r"""Updates a specific FPolicy engine configuration of an SVM. Modification of an FPolicy engine that is attached to one or more enabled FPolicy policies is not allowed.
### Related ONTAP commands
* `fpolicy policy external-engine modify`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/engines`](#docs-NAS-protocols_fpolicy_{svm.uuid}_engines)
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
        r"""Deletes the FPolicy external engine configuration. Deletion of an FPolicy engine that is attached to one or more FPolicy policies is not allowed.
### Related ONTAP commands
* `fpolicy policy external-engine modify`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/engines`](#docs-NAS-protocols_fpolicy_{svm.uuid}_engines)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


