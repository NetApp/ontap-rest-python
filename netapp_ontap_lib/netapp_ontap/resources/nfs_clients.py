# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
ONTAP connected clients show functionality is mainly used to provide a list of currently connected NFS clients. It also provides a potential list of other NFS clients that can be connected but are currently idle.<p/>
The following are details of the fields retrieved for the Connected Clients GET API:<p/>
node.name: The node name hosting this record; basically the node hosting the "server_ip".
node.uuid: The node UUID hosting this record; basically the node hosting the "server_ip".
svm.name: The svm name to which the "server_ip" belongs to.
svm.uuid: The svm uuid to which the "server_ip" belongs to.
server_ip: All clients that are connected to this interface are displayed in rows.
client_ip: The IP address of the client that is connected to the interface.
volume.name: The name of the volume the client is accessing.
volume.uuid: The UUID of the volume the client is accessing.
protocol: The NFS protocol version over which client is accessing the volume.
idle_duration: The time elapsed since the last request was sent by the client for this volume.
local_request_count: A counter that tracks requests that are sent to the volume with fast-path to local node.
remote_request_count: A counter that tracks requests that are sent to the volume with slow-path to remote node.
## Example
### Retrieves connected client information
```
# The API:
GET /protocols/nfs/connected-clients
# The call:
curl -X GET "https://<cluster-mgmt-ip>/api/protocols/nfs/connected-clients?return_timeout=15&return_records=true" -H "accept: application/json"
# The response:
{
  "records": [
  {
     "svm": {
       "uuid": "c642db55-b8d0-11e9-9ad1-0050568e8480",
       "name": "vs1"
     },
     "node": {
       "uuid": "cc282893-b82f-11e9-a3ad-0050568e8480",
       "name": "vsim1"
     },
     "server_ip": "10.140.72.214",
     "client_ip": "10.140.137.57",
     "volume": {
       "name": "rvol1",
       "uuid": "c6bbc6f2-b8d0-11e9-9ad1-0050568e8480"
     },
     "protocol": "nfs4"
   },
   {
     "svm": {
       "uuid": "c642db55-b8d0-11e9-9ad1-0050568e8480",
       "name": "vs1"
     },
     "node": {
       "uuid": "cc282893-b82f-11e9-a3ad-0050568e8480",
       "name": "vsim1"
     },
     "server_ip": "10.140.72.214",
     "client_ip": "10.140.137.57",
     "volume": {
       "name": "vol1",
       "uuid": "d28d1999-b8d0-11e9-9ad1-0050568e8480"
     },
     "protocol": "nfs3"
   },
   {
     "svm": {
       "uuid": "c642db55-b8d0-11e9-9ad1-0050568e8480",
       "name": "vs1"
     },
     "node": {
       "uuid": "cc282893-b82f-11e9-a3ad-0050568e8480",
       "name": "vsim1"
     },
     "server_ip": "10.140.72.214",
     "client_ip": "10.140.137.57",
     "volume": {
       "name": "vol1",
       "uuid": "d28d1999-b8d0-11e9-9ad1-0050568e8480"
     },
     "protocol": "nfs4"
   }],
   "num_records": 3
}
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["NfsClients", "NfsClientsSchema"]
__pdoc__ = {
    "NfsClientsSchema.resource": False,
    "NfsClientsSchema.patchable_fields": False,
    "NfsClientsSchema.postable_fields": False,
}


class NfsClientsSchema(ResourceSchema):
    """The fields of the NfsClients object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the nfs_clients. """

    client_ip = fields.Str(
        data_key="client_ip",
    )
    r""" Specifies IP address of the client. """

    idle_duration = fields.Str(
        data_key="idle_duration",
    )
    r""" Specifies an ISO-8601 format of date and time to retrieve the idle time duration in hours, minutes, and seconds format.


Example: P4DT84H30M5S """

    local_request_count = fields.Integer(
        data_key="local_request_count",
    )
    r""" A counter that tracks requests that are sent to the volume with fast-path to local node. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the nfs_clients. """

    protocol = fields.Str(
        data_key="protocol",
        validate=enum_validation(['nfs', 'nfs3', 'nfs4', 'nfs4.1']),
    )
    r""" The NFS protocol version over which client is accessing the volume. The following values are supported:

* nfs - All NFS versions are considered
* nfs3 - NFS version 3 protocol
* nfs4 - NFS version 4 protocol
* nfs4.1 - NFS version 4 minor version 1 protocol


Valid choices:

* nfs
* nfs3
* nfs4
* nfs4.1 """

    remote_request_count = fields.Integer(
        data_key="remote_request_count",
    )
    r""" A counter that tracks requests that are sent to the volume with slow-path to remote node. """

    server_ip = fields.Str(
        data_key="server_ip",
    )
    r""" Specifies the IP address of the server. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the nfs_clients. """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the nfs_clients. """

    @property
    def resource(self):
        return NfsClients

    @property
    def patchable_fields(self):
        return [
            "client_ip",
            "idle_duration",
            "local_request_count",
            "node.name",
            "node.uuid",
            "remote_request_count",
            "server_ip",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "client_ip",
            "idle_duration",
            "local_request_count",
            "node.name",
            "node.uuid",
            "remote_request_count",
            "server_ip",
            "svm.name",
            "svm.uuid",
            "volume.name",
            "volume.uuid",
        ]

class NfsClients(Resource):
    """Allows interaction with NfsClients objects on the host"""

    _schema = NfsClientsSchema
    _path = "/api/protocols/nfs/connected-clients"

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
        r"""Retrieves the NFS configuration of SVMs.

### Learn more
* [`DOC /protocols/nfs/connected-clients`](#docs-NAS-protocols_nfs_connected-clients)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the NFS configuration of SVMs.

### Learn more
* [`DOC /protocols/nfs/connected-clients`](#docs-NAS-protocols_nfs_connected-clients)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






