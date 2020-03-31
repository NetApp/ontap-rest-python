# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Defines, retrieves or deletes an individual SNMP traphost.
## Examples
### Retrieves an individual traphost in the cluster
    <br/>
    ```
    # The API:
    GET "/api/support/snmp/traphosts/{host}"
    # The call
    curl -H "accept: application/hal+json" -X GET "https://<mgmt-ip>/api/support/snmp/traphosts/10.235.36.62"
    # The response
    {
      "host": "scspr0651011001.gdl.englab.netapp.com",
      "ip_address": "10.235.36.62",
      "user": {
        "name": "public",
        "_links": {
          "self": {
            "href": "/api/support/snmp/users/800003150558b57e8dbd9ce9119d82005056a7b4e5/public"
          }
        }
      },
      "_links": {
        "self": {
          "href": "/api/support/snmp/traphosts/10.235.36.62"
        }
      }
    }
    <br/>
### Deletes an individual traphost in the cluster
    <br/>
    ```
    # The API:
    DELETE "/api/support/snmp/traphosts/{host}"
    # The call:
    curl -H "accept: application/json" -H "Content-Type: application/json" -X DELETE "https://<mgmt-ip>/api/support/snmp/traphosts/3ffe:ffff:100:f102::1"
    # The response:
    200 OK
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnmpTraphost", "SnmpTraphostSchema"]
__pdoc__ = {
    "SnmpTraphostSchema.resource": False,
    "SnmpTraphostSchema.patchable_fields": False,
    "SnmpTraphostSchema.postable_fields": False,
}


class SnmpTraphostSchema(ResourceSchema):
    """The fields of the SnmpTraphost object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snmp_traphost. """

    host = fields.Str(
        data_key="host",
    )
    r""" Fully qualified domain name (FQDN), IPv4 address or IPv6 address of SNMP traphost.

Example: traphost.example.com """

    ip_address = fields.Str(
        data_key="ip_address",
    )
    r""" The ip_address field of the snmp_traphost. """

    user = fields.Nested("netapp_ontap.resources.snmp_user.SnmpUserSchema", data_key="user", unknown=EXCLUDE)
    r""" The user field of the snmp_traphost. """

    @property
    def resource(self):
        return SnmpTraphost

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "host",
            "ip_address",
            "user.name",
        ]

class SnmpTraphost(Resource):
    r""" SNMP manager or host machine that receives SNMP traps from ONTAP. """

    _schema = SnmpTraphostSchema
    _path = "/api/support/snmp/traphosts"
    @property
    def _keys(self):
        return ["host"]

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
        r"""Retrieves the list of SNMP traphosts along with the SNMP users configured for those traphosts.
### Related ONTAP commands
* `system snmp traphost show`
### Learn more
* [`DOC /support/snmp/traphosts`](#docs-support-support_snmp_traphosts)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member


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
        r"""Deletes an SNMP traphost.
### Learn more
* [`DOC /support/snmp/traphosts/{host}`](#docs-support-support_snmp_traphosts_{host})
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the list of SNMP traphosts along with the SNMP users configured for those traphosts.
### Related ONTAP commands
* `system snmp traphost show`
### Learn more
* [`DOC /support/snmp/traphosts`](#docs-support-support_snmp_traphosts)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the details of an SNMP traphost along with the SNMP user configured for that traphost.
### Learn more
* [`DOC /support/snmp/traphosts/{host}`](#docs-support-support_snmp_traphosts_{host})
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
        r"""Creates SNMP traphosts. While adding an SNMPv3 traphost, an SNMPv3 user configured in ONTAP must be specified. ONTAP uses this user's credentials to authenticate and/or encrypt traps sent to this SNMPv3 traphost. While adding an SNMPv1/SNMPv2c traphost, SNMPv1/SNMPv2c user or community need not be specified.
### Required properties
* `host` - Fully Qualified Domain Name (FQDN), IPv4 address or IPv6 address of SNMP traphost.
### Recommended optional properties
* If `host` refers to an SNMPv3 traphost, the following field is required:
  * `user` - SNMPv3 or User-based Security Model (USM) user.
* For an SNMPv1/SNMPv2c traphost, ONTAP automatically uses 'public' if 'public' is configured or no community is configured. Otherwise, ONTAP uses the first configured community.
### Related ONTAP commands
* `system snmp traphost add`
### Learn more
* [`DOC /support/snmp/traphosts`](#docs-support-support_snmp_traphosts)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member


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
        r"""Deletes an SNMP traphost.
### Learn more
* [`DOC /support/snmp/traphosts/{host}`](#docs-support-support_snmp_traphosts_{host})
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


