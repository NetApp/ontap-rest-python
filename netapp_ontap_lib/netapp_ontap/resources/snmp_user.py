# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Defines, retrieves, updates and deletes an individual SNMP user.
## Examples
### Retrieves the details of an SNMP user
    <br/>
    ```
    # The API:
    GET "/api/support/snmp/users/{engine_id}/{name}"
    # The call:
    curl -H "accept: application/hal+json" -X GET "https://<mgmt-ip>/api/support/snmp/users/80000315056622e52625a9e911a981005056bb1dcb/snmpv1user2"
    # The response:
    {
      "engine_id": "80000315056622e52625a9e911a981005056bb1dcb",
      "name": "snmpv1user2",
      "scope": "cluster",
      "owner": {
        "name": "cluster-1",
        "uuid": "26e52266-a925-11e9-a981-005056bb1dcb"
      },
      "authentication_method": "community",
      "_links": {
        "self": {
          "href": "/api/support/snmp/users/80000315056622e52625a9e911a981005056bb1dcb/snmpv1user2"
        }
      }
    }
    <br/>
### Updates the comment parameter for an individual SNMP user
    <br/>
    ```
    # The API:
    PATCH "/api/support/snmp/users/{engine_id}/{name}"
    # The call:
    curl -H "accept: application/json" -H "Content-Type: application/json" -X PATCH "https://<mgmt-ip>/api/support/snmp/users/8000031505b67667a26975e9118a480050568e6f74/public" -d '{"comment":"Default SNMP community"}'
    # The response:
    200 OK
### Deletes an individual SNMP user in the cluster
    <br/>
    ```
    # The API:
    DELETE "/api/support/snmp/users/{engine_id}/{name}"
    # The call:
    curl -H "accept: application/json" -H "Content-Type: application/json" -X DELETE "https://<mgmt-ip>/api/support/snmp/users/8000031505b67667a26975e9118a480050568e6f74/snmpuser"
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


__all__ = ["SnmpUser", "SnmpUserSchema"]
__pdoc__ = {
    "SnmpUserSchema.resource": False,
    "SnmpUserSchema.patchable_fields": False,
    "SnmpUserSchema.postable_fields": False,
}


class SnmpUserSchema(ResourceSchema):
    """The fields of the SnmpUser object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snmp_user. """

    authentication_method = fields.Str(
        data_key="authentication_method",
        validate=enum_validation(['community', 'usm', 'both']),
    )
    r""" Optional authentication method.

Valid choices:

* community
* usm
* both """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=128),
    )
    r""" Optional comment text.

Example: This is a comment. """

    engine_id = fields.Str(
        data_key="engine_id",
    )
    r""" Optional SNMPv3 engine identifier. For a local SNMP user belonging to the administrative Storage Virtual Machine (SVM), the default value of this parameter is the SNMPv3 engine identifier for the administrative SVM. For a local SNMP user belonging to a data SVM, the default value of this parameter is the SNMPv3 engine identifier for that data SVM. For an SNMPv1/SNMPv2c community, this parameter should not be specified in "POST" method. For a remote switch SNMPv3 user, this parameter specifies the SNMPv3 engine identifier for the remote switch. This parameter can also optionally specify a custom engine identifier.

Example: 80000315055415ab26d4aae811ac4d005056bb792e """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=0, maximum=32),
    )
    r""" SNMP user name.

Example: snmpv3user2 """

    owner = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="owner", unknown=EXCLUDE)
    r""" The owner field of the snmp_user. """

    scope = fields.Str(
        data_key="scope",
    )
    r""" Set to "svm" for data Storage Virtual Machine (SVM) SNMP users and to "cluster" for administrative SVM SNMP users. """

    snmpv3 = fields.Nested("netapp_ontap.models.usm.UsmSchema", data_key="snmpv3", unknown=EXCLUDE)
    r""" The snmpv3 field of the snmp_user. """

    switch_address = fields.Str(
        data_key="switch_address",
    )
    r""" Optional remote switch address. It can be an IPv4 address or an IPv6 address. A remote switch can be queried over SNMPv3 using ONTAP SNMP client functionality. Querying such a switch requires an SNMPv3 user (remote switch user) to be configured on the switch. Since ONTAP requires remote switch user's SNMPv3 credentials (to query it), this user must be configured in ONTAP as well. This parameter is specified when configuring such a user.

Example: 10.23.34.45 """

    @property
    def resource(self):
        return SnmpUser

    @property
    def patchable_fields(self):
        return [
            "comment",
            "owner.name",
            "owner.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "authentication_method",
            "comment",
            "engine_id",
            "name",
            "owner.name",
            "owner.uuid",
            "switch_address",
        ]

class SnmpUser(Resource):
    r""" An SNMP user can be an SNMPv1/SNMPv2c user or an SNMPv3 user. SNMPv1/SNMPv2c user is also called a "community" user. An SNMPv3 user, also called a User-based Security Model (USM) user, can be a local SNMPv3 user or a remote SNMPv3 user. A local SNMPv3 user can be used for querying ONTAP SNMP server over SNMPv3 and/or for sending SNMPv3 traps. The local SNMPv3 user used for sending SNMPv3 traps must be configured with the same authentication and privacy credentials on the traphost receiver as well. A remote SNMPv3 user is also configured on a remote switch and used by ONTAP SNMP client functionality to query the remote switch over SNMPv3. An SNMP user is scoped to its owning Storage Virtual Machine (SVM). Owning SVM could be a data SVM or the administrative SVM. """

    _schema = SnmpUserSchema
    _path = "/api/support/snmp/users"
    @property
    def _keys(self):
        return ["engine_id", "name"]

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
        r"""Retrieves the list of SNMP users on the cluster.
### Related ONTAP commands
* `security snmpusers`
* `security login show -application snmp`
### Learn more
* [`DOC /support/snmp/users`](#docs-support-support_snmp_users)
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
        r"""Updates the comment parameter of an SNMP user.
### Optional properties
* `comment` - Comment text.
### Related ONTAP commands
* `security login modify`
### Learn more
* [`DOC /support/snmp/users/{engine_id}/{name}`](#docs-support-support_snmp_users_{engine_id}_{name})
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
        r"""Deletes an SNMP user. The engine ID can be the engine ID of the administrative SVM or a data SVM. It can also be the SNMPv3 engine ID of a remote switch.
### Related ONTAP commands
* `security login delete`
* `system snmp community delete`
### Learn more
* [`DOC /support/snmp/users/{engine_id}/{name}`](#docs-support-support_snmp_users_{engine_id}_{name})
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the list of SNMP users on the cluster.
### Related ONTAP commands
* `security snmpusers`
* `security login show -application snmp`
### Learn more
* [`DOC /support/snmp/users`](#docs-support-support_snmp_users)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the details of an SNMP user. The engine ID can be the engine ID of the administrative SVM or a data SVM. It can also be the SNMPv3 engine ID of a remote switch.
### Related ONTAP commands
* `security snmpusers -vserver <SVM Name> -username <User Name>`
* `security login show -application snmp -vserver <SVM Name> -user-or-group-name <User Name>`
### Learn more
* [`DOC /support/snmp/users/{engine_id}/{name}`](#docs-support-support_snmp_users_{engine_id}_{name})
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
        r"""Creates either a cluster-scoped or an SVM-scoped SNMP user. This user can be an SNMPv1 or SNMPv2c community user or an SNMPv3 user. An SNMPv3 user can be a local SNMPv3 user or a remote SNMPv3 user.
### Required properties
* `owner` - Name and UUID of owning SVM.
* `engine_id` - Engine ID of owning SVM or remote switch.
* `name` - SNMP user name
* `authentication_method` - Authentication method
### Optional properties
* `switch_address` - Optional remote switch address
* `snmpv3` - SNMPv3-specific credentials
* `comment` - Comment text
### Default property values
* `snmpv3.authentication_protocol` - none
* `snmpv3.privacy_protocol` - none
### Related ONTAP commands
* `security login create`
* `system snmp community add`
### Learn more
* [`DOC /support/snmp/users`](#docs-support-support_snmp_users)
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
        r"""Updates the comment parameter of an SNMP user.
### Optional properties
* `comment` - Comment text.
### Related ONTAP commands
* `security login modify`
### Learn more
* [`DOC /support/snmp/users/{engine_id}/{name}`](#docs-support-support_snmp_users_{engine_id}_{name})
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
        r"""Deletes an SNMP user. The engine ID can be the engine ID of the administrative SVM or a data SVM. It can also be the SNMPv3 engine ID of a remote switch.
### Related ONTAP commands
* `security login delete`
* `system snmp community delete`
### Learn more
* [`DOC /support/snmp/users/{engine_id}/{name}`](#docs-support-support_snmp_users_{engine_id}_{name})
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


