# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Cluster wide SNMP configuration. You can configure or retrieve the following SNMP parameters using this endpoint:

* enable or disable SNMP
* enable or disable SNMP authentication traps
## Examples
### Disables SNMP protocol in the cluster.
    <br/>
    ```
    # The API:
    PATCH "/api/support/snmp"
    # The call
    curl -H "accept: application/json" -H "Content-Type: application/json" -X PATCH "https://<mgmt-ip>/api/support/snmp" -d '{"enabled":"false"}'
    # The response
    200 OK
### Enables SNMP authentication traps in the cluster.
    <br/>
    ```
    # The call
    curl -H "accept: application/json" -H "Content-Type: application/json" -X PATCH "https://<mgmt-ip>/api/support/snmp" -d '{"auth_traps_enabled":"true"}'
    # The response
    200 OK
### Enables SNMP protocol and SNMP authentication traps in the cluster.
    <br/>
    ```
    # The call
    curl -H "accept: application/json" -H "Content-Type: application/json" -X PATCH "https://<mgmt-ip>/api/support/snmp" -d '{"enabled":"true", "auth_traps_enabled":"true"}'
    # The response
    200 OK
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Snmp", "SnmpSchema"]
__pdoc__ = {
    "SnmpSchema.resource": False,
    "SnmpSchema.patchable_fields": False,
    "SnmpSchema.postable_fields": False,
}


class SnmpSchema(ResourceSchema):
    """The fields of the Snmp object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snmp. """

    auth_traps_enabled = fields.Boolean(
        data_key="auth_traps_enabled",
    )
    r""" Specifies whether to enable or disable SNMP authentication traps.

Example: true """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies whether to enable or disable SNMP.

Example: true """

    @property
    def resource(self):
        return Snmp

    @property
    def patchable_fields(self):
        return [
            "links",
            "auth_traps_enabled",
            "enabled",
        ]

    @property
    def postable_fields(self):
        return [
        ]

class Snmp(Resource):
    r""" Cluster-wide SNMP configuration. """

    _schema = SnmpSchema
    _path = "/api/support/snmp"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the cluster wide SNMP configuration.
### Related ONTAP commands
* `options snmp.enable`
* `system snmp show`
### Learn more
* [`DOC /support/snmp`](#docs-support-support_snmp)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member


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
        r"""Updates the cluster wide SNMP configuration, such as enabling or disabling SNMP and enabling or disabling authentication traps.
### Related ONTAP commands
* `options snmp.enable`
* `system snmp authtrap`
### Learn more
* [`DOC /support/snmp`](#docs-support-support_snmp)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



