# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API returns an object 'onboard_key_manager_configurable_status' which details whether the Onboard Key Manager can be configured on the cluster or not.
## Examples
### Retrieving information about the security configured on the cluster
The following example shows how to retrieve the key manager configiration of the cluster.
```
# The API:
GET /api/security:
# The call:
curl -X GET 'https://<mgmt-ip>/api/security?fields=*' -H 'accept: application/hal+json'
# The response:
{
  {
    "onboard_key_manager_configurable_status": {
      "supported": "false",
      "message": "Onboard Key Manager cannot be configured on the cluster. There are no self-encrypting disks in the cluster, and the following nodes do not support volume granular encryption: ntap-vsim2.",
      "code": 65537300
    },
  },
}
```
---
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


__all__ = ["SecurityConfig", "SecurityConfigSchema"]
__pdoc__ = {
    "SecurityConfigSchema.resource": False,
    "SecurityConfigSchema.patchable_fields": False,
    "SecurityConfigSchema.postable_fields": False,
}


class SecurityConfigSchema(ResourceSchema):
    """The fields of the SecurityConfig object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the security_config. """

    onboard_key_manager_configurable_status = fields.Nested("netapp_ontap.models.onboard_key_manager_configurable_status.OnboardKeyManagerConfigurableStatusSchema", data_key="onboard_key_manager_configurable_status", unknown=EXCLUDE)
    r""" The onboard_key_manager_configurable_status field of the security_config. """

    @property
    def resource(self):
        return SecurityConfig

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]

class SecurityConfig(Resource):
    """Allows interaction with SecurityConfig objects on the host"""

    _schema = SecurityConfigSchema
    _path = "/api/security"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves information about the security configured on the cluster.

### Learn more
* [`DOC /security`](#docs-security-security)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





