# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Name mapping is used to map CIFS identities to UNIX identities, Kerberos identities to UNIX identities, and UNIX identities to CIFS identities. It needs this information to obtain user credentials and provide proper file access regardless of whether they are connecting from an NFS client or a CIFS client. </br>
The system keeps a set of conversion rules for each Storage Virtual Machine (SVM). Each rule consists of two pieces: a pattern and a replacement. Conversions start at the beginning of the appropriate list and perform a substitution based on the first matching rule. The pattern is a UNIX-style regular expression. The replacement is a string containing escape sequences representing subexpressions from the pattern, as in the UNIX sed program.</br>
Name mappings are applied in the order in which they occur in the priority list; for example, a name mapping that occurs at position 2 in the priority list is applied before a name mapping that occurs at position 3. Each mapping direction (Kerberos-to-UNIX, Windows-to-UNIX, and UNIX-to-Windows) has its own priority list. You are prevented from creating two name mappings with the same pattern.<p/>
## Examples
### Creating a name-mapping with client_match as the ip-address
Use the following API to create a name-mapping. Note the <i>return_records=true</i> query parameter is used to obtain the newly created entry in the response.
<br/>
```
# The API:
POST /api//name-services/name-mappings
# The call:
curl -X POST "https://<mgmt-ip>/api/name-services/name-mappings?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"client_match\": \"10.254.101.111/28\", \"direction\": \"win_unix\", \"index\": 1, \"pattern\": \"ENGCIFS_AD_USER\", \"replacement\": \"unix_user1\", \"svm\": { \"name\": \"vs1\", \"uuid\": \"f71d3640-0226-11e9-8526-000c290a8c4b\" }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "f71d3640-0226-11e9-8526-000c290a8c4b",
        "name": "vs1"
      },
      "direction": "win_unix",
      "index": 1,
      "pattern": "ENGCIFS_AD_USER",
      "replacement": "unix_user1",
      "client_match": "10.254.101.111/28"
    }
  ]
}
```
### Creating a name-mapping with client_match as the hostname
Use the following API to create a name-mapping. Note the <i>return_records=true</i> query parameter is used to obtain the newly created entry in the response.
<br/>
```
# The API:
POST /api//name-services/name-mappings
# The call:
curl -X POST "https://<mgmt-ip>/api/name-services/name-mappings?return_records=true" -H "accept: application/json" -H "Content-Type: applicatio/json" -d "{ \"client_match\": \"google.com\", \"direction\": \"win_unix\", \"index\": 2, \"pattern\": \"ENGCIFS_AD_USER\", \"replacement\": \"unix_user1\", \"svm\": { \"name\": \"vs1\", \"uuid\": \"f71d3640-0226-11e9-8526-000c290a8c4b\" }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "f71d3640-0226-11e9-8526-000c290a8c4b",
        "name": "vs1"
      },
      "direction": "win_unix",
      "index": 2,
      "pattern": "ENGCIFS_AD_USER",
      "replacement": "unix_user1",
      "client_match": "google.com"
    }
  ]
}
```
### Retrieving all name-mapping configurations for all SVMs in the cluster
```
# The API:
GET /api/name-services/name-mappings
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/name-mappings?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "f71d3640-0226-11e9-8526-000c290a8c4b",
        "name": "vs1"
      },
      "direction": "win_unix",
      "index": 1,
      "pattern": "ENGCIFS_AD_USER",
      "replacement": "unix_user1",
      "client_match": "10.254.101.111/28"
    },
    {
      "svm": {
        "uuid": "f71d3640-0226-11e9-8526-000c290a8c4b",
        "name": "vs1"
      },
      "direction": "win_unix",
      "index": 2,
      "pattern": "ENGCIFS_AD_USER",
      "replacement": "unix_user1",
      "client_match": "google.com"
    }
  ],
  "num_records": 2
}
```
### Retrieving a name-mapping configuration for a specific SVM, and for the specified direction and index
---
```
# The API:
GET /api/name-services/name-mappings/{svm.uuid}/{direction}/{index}
# The call:
curl -X GET "https://<mgmt-ip>/api/name-services/name-mappings/f71d3640-0226-11e9-8526-000c290a8c4b/win_unix/1" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "f71d3640-0226-11e9-8526-000c290a8c4b",
    "name": "vs1"
  },
  "direction": "win_unix",
  "index": 1,
  "pattern": "ENGCIFS_AD_USER",
  "replacement": "unix_user1",
  "client_match": "10.254.101.111/28"
}
```
---
### Updating a specific name-mapping configuration
---
```
# The API:
PATCH /api//name-services/name-mappings/{svm.uuid}/{direction}/{index}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/name-services/name-mappings/f71d3640-0226-11e9-8526-000c290a8c4b/win_unix/1" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"client_match\": \"10.254.101.222/28\", \"pattern\": \"ENGCIFS_LOCAL_USER\", \"replacement\": \"pcuser\"}"
# swapping a specified namemapping entry by index
curl -X PATCH "https://<mgmt-ip>/api/name-services/name-mappings/f71d3640-0226-11e9-8526-000c290a8c4b/win-unix/3?new_index=1" -H "accept: application/json" -H "Content-Type: application/json" -d "{  \"pattern\": \"ENGCIFS_AD_USER\", \"replacement\": \"unix_user1\"}"
```
---
### Removing a specific name-mapping configuration
---
```
# The API:
DELETE /api/name-services/name-mappings/{svm.uuid}/{direction}/{index}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/name-services/name-mappings/f71d3640-0226-11e9-8526-000c290a8c4b/win_unix/1" -H "accept: application/json"
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


__all__ = ["NameMapping", "NameMappingSchema"]
__pdoc__ = {
    "NameMappingSchema.resource": False,
    "NameMappingSchema.patchable_fields": False,
    "NameMappingSchema.postable_fields": False,
}


class NameMappingSchema(ResourceSchema):
    """The fields of the NameMapping object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the name_mapping. """

    client_match = fields.Str(
        data_key="client_match",
    )
    r""" Client workstation IP Address which is matched when searching for the pattern.
  You can specify the value in any of the following formats:

* As an IPv4 address with a subnet mask expressed as a number of bits; for instance, 10.1.12.0/24
* As an IPv6 address with a subnet mask expressed as a number of bits; for instance, fd20:8b1e:b255:4071::/64
* As an IPv4 address with a network mask; for instance, 10.1.16.0/255.255.255.0
* As a hostname


Example: 10.254.101.111/28 """

    direction = fields.Str(
        data_key="direction",
        validate=enum_validation(['win_unix', 'unix_win', 'krb_unix']),
    )
    r""" Direction in which the name mapping is applied. The possible values are:

  * krb_unix  - Kerberos principal name to UNIX user name
  * win_unix  - Windows user name to UNIX user name
  * unix_win  - UNIX user name to Windows user name mapping


Valid choices:

* win_unix
* unix_win
* krb_unix """

    index = fields.Integer(
        data_key="index",
        validate=integer_validation(minimum=1, maximum=2147483647),
    )
    r""" Position in the list of name mappings.

Example: 1 """

    pattern = fields.Str(
        data_key="pattern",
    )
    r""" Pattern used to match the name while searching for a name that can be used as a replacement. The pattern is a UNIX-style regular expression. Regular expressions are case-insensitive when mapping from Windows to UNIX, and they are case-sensitive for mappings from Kerberos to UNIX and UNIX to Windows.

Example: ENGCIFS_AD_USER """

    replacement = fields.Str(
        data_key="replacement",
    )
    r""" The name that is used as a replacement, if the pattern associated with this entry matches.

Example: unix_user1 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the name_mapping. """

    @property
    def resource(self):
        return NameMapping

    @property
    def patchable_fields(self):
        return [
            "client_match",
            "pattern",
            "replacement",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "client_match",
            "direction",
            "index",
            "pattern",
            "replacement",
            "svm.name",
            "svm.uuid",
        ]

class NameMapping(Resource):
    r""" Name mapping is used to map CIFS identities to UNIX identities, Kerberos identities to UNIX identities, and UNIX identities to CIFS identities. It needs this information to obtain user credentials and provide proper file access regardless of whether they are connecting from an NFS client or a CIFS client. """

    _schema = NameMappingSchema
    _path = "/api/name-services/name-mappings"
    @property
    def _keys(self):
        return ["svm.uuid", "direction", "index"]

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
        r"""Retrieves the name mapping configuration for all SVMs.
### Related ONTAP commands
* `vserver name-mapping show`
### Learn more
* [`DOC /name-services/name-mappings`](#docs-name-services-name-services_name-mappings)
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
        r"""Updates the name mapping configuration of an SVM. The positions can be swapped by providing the `new_index` property.
Swapping is not allowed for entries that have `client_match` property configured.
### Related ONTAP commands
* `vserver name-mapping insert`
* `vserver name-mapping modify`
* `vserver name-mapping swap`
### Learn more
* [`DOC /name-services/name-mappings`](#docs-name-services-name-services_name-mappings)
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
        r"""Deletes the name mapping configuration.
### Related ONTAP commands
* `vserver name-mapping delete`
### Learn more
* [`DOC /name-services/name-mappings`](#docs-name-services-name-services_name-mappings)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the name mapping configuration for all SVMs.
### Related ONTAP commands
* `vserver name-mapping show`
### Learn more
* [`DOC /name-services/name-mappings`](#docs-name-services-name-services_name-mappings)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the name mapping configuration of an SVM.
### Related ONTAP commands
* `vserver name-mapping show`
### Learn more
* [`DOC /name-services/name-mappings`](#docs-name-services-name-services_name-mappings)
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
        r"""Creates name mappings for an SVM.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the name mapping.
* `index` - Name mapping's position in the priority list.
* `direction` - Direction of the name mapping.
* `pattern` - Pattern to match to. Maximum length is 256 characters.
* `replacement` - Replacement pattern to match to. Maximum length is 256 characters.
### Recommended optional properties
* `client_match` - Hostname or IP address added to match the pattern to the client's workstation IP address.
### Related ONTAP commands
* `vserver name-mapping create`
* `vserver name-mapping insert`
### Learn more
* [`DOC /name-services/name-mappings`](#docs-name-services-name-services_name-mappings)
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
        r"""Updates the name mapping configuration of an SVM. The positions can be swapped by providing the `new_index` property.
Swapping is not allowed for entries that have `client_match` property configured.
### Related ONTAP commands
* `vserver name-mapping insert`
* `vserver name-mapping modify`
* `vserver name-mapping swap`
### Learn more
* [`DOC /name-services/name-mappings`](#docs-name-services-name-services_name-mappings)
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
        r"""Deletes the name mapping configuration.
### Related ONTAP commands
* `vserver name-mapping delete`
### Learn more
* [`DOC /name-services/name-mappings`](#docs-name-services-name-services_name-mappings)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


