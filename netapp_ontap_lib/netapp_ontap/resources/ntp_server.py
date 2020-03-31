# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
You can use this API to add external NTP servers to a cluster, update the configuration, use NTP keys, and retrieve the
current NTP server configuration.
## Adding an NTP server to a cluster
To add an NTP server to a cluster, issue a POST /cluster/ntp/servers request.
### Fields used for adding an NTP server
Except for the name of the NTP server (host name or IP address), which is specified by the server, all fields are optional:

* `version`
* `key`
###
If the key is provided in POST, `authentication_enabled` is set to `true` by default.
## Examples
### Adding an NTP server
```
# Body
body =
{
  "server": "time.nist.gov"
}
# Request
curl -X POST "https://<mgmt-ip>/api/cluster/ntp/servers" -d body
```
---
### Adding an NTP server with an authentication key
```
# Body
body =
{
  "server": "time.nist.gov",
  "key": { "id": 10 }
}
# Request
curl -X POST "https://<mgmt-ip>/api/cluster/ntp/servers" -d body
```
---
### Enabling a previously configured shared key (ID, type, and value) for an NTP server
A combination of key number or identifier (ID), type of key, and shared key value is created with /api/cluster/ntp/keys.
This operation will validate the NTP authentication works.
```
# Body
body =
{
  "key": { "id": 10 },
  "authentication_enabled": true
}
# Request
curl -X PATCH "https://<mgmt-ip>/api/cluster/ntp/servers/time.nist.gov" -d body
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


__all__ = ["NtpServer", "NtpServerSchema"]
__pdoc__ = {
    "NtpServerSchema.resource": False,
    "NtpServerSchema.patchable_fields": False,
    "NtpServerSchema.postable_fields": False,
}


class NtpServerSchema(ResourceSchema):
    """The fields of the NtpServer object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ntp_server. """

    authentication_enabled = fields.Boolean(
        data_key="authentication_enabled",
    )
    r""" Set NTP symmetric authentication on (true) or off (false).

Example: true """

    key = fields.Nested("netapp_ontap.resources.ntp_key.NtpKeySchema", data_key="key", unknown=EXCLUDE)
    r""" The key field of the ntp_server. """

    server = fields.Str(
        data_key="server",
    )
    r""" NTP server host name, IPv4, or IPv6 address.

Example: time.nist.gov """

    version = fields.Str(
        data_key="version",
        validate=enum_validation(['3', '4', 'auto']),
    )
    r""" NTP protocol version for server. Valid versions are 3, 4, or auto.

Valid choices:

* 3
* 4
* auto """

    @property
    def resource(self):
        return NtpServer

    @property
    def patchable_fields(self):
        return [
            "authentication_enabled",
            "key.id",
            "version",
        ]

    @property
    def postable_fields(self):
        return [
            "key.id",
            "server",
            "version",
        ]

class NtpServer(Resource):
    """Allows interaction with NtpServer objects on the host"""

    _schema = NtpServerSchema
    _path = "/api/cluster/ntp/servers"
    @property
    def _keys(self):
        return ["server"]

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
        r"""Retrieves the collection of external NTP time servers ONTAP uses for time adjustment and correction.
### Related ONTAP commands
* `cluster time-service ntp server show`
### Learn more
* [`DOC /cluster/ntp/servers`](#docs-cluster-cluster_ntp_servers)
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
        r"""Updates the configuration of an NTP server used by the ONTAP cluster after validation.
Patchable fields are:
* `version`
* `key.id`
* `authentication_enabled`
</br>
If `authentication_enabled` is modified to `false`, the associated NTP key is removed from the server instance.
If `authentication_enabled` is modified to `true`, you must provide an NTP key ID in the PATCH body.
### Related ONTAP commands
* `cluster time-service ntp server modify`
### Learn more
* [`DOC /cluster/ntp/servers`](#docs-cluster-cluster_ntp_servers)
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
        r"""Deletes an external NTP server used by ONTAP.
### Related ONTAP commands
* `cluster time-service ntp server delete`
### Learn more
* [`DOC /cluster/ntp/servers`](#docs-cluster-cluster_ntp_servers)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the collection of external NTP time servers ONTAP uses for time adjustment and correction.
### Related ONTAP commands
* `cluster time-service ntp server show`
### Learn more
* [`DOC /cluster/ntp/servers`](#docs-cluster-cluster_ntp_servers)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the configuration of an external NTP server used by ONTAP.
### Related ONTAP commands
* `cluster time-service ntp server show`
### Learn more
* [`DOC /cluster/ntp/servers`](#docs-cluster-cluster_ntp_servers)
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
        r"""Validates the provided external NTP time server for usage and configures ONTAP so that all nodes in the cluster use it.
The required fields are:
* `server`
### Default property values
If not specified in POST, the following default property values are assigned:
* `version` - auto
* `key` - not set
###
If the key is provided in POST, `authentication_enabled` is set to `true` by default.
### Related ONTAP commands
* `cluster time-service ntp server create`
### Learn more
* [`DOC /cluster/ntp/servers`](#docs-cluster-cluster_ntp_servers)
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
        r"""Updates the configuration of an NTP server used by the ONTAP cluster after validation.
Patchable fields are:
* `version`
* `key.id`
* `authentication_enabled`
</br>
If `authentication_enabled` is modified to `false`, the associated NTP key is removed from the server instance.
If `authentication_enabled` is modified to `true`, you must provide an NTP key ID in the PATCH body.
### Related ONTAP commands
* `cluster time-service ntp server modify`
### Learn more
* [`DOC /cluster/ntp/servers`](#docs-cluster-cluster_ntp_servers)
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
        r"""Deletes an external NTP server used by ONTAP.
### Related ONTAP commands
* `cluster time-service ntp server delete`
### Learn more
* [`DOC /cluster/ntp/servers`](#docs-cluster-cluster_ntp_servers)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


