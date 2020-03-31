# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

##  Export Policies
### 1) Retrieve the export policy details
---
```
# The API:
GET /api/protocols/nfs/export-policies
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/nfs/export-policies"
```
---
### 2) Create an export policy for an SVM
---
```
# The API:
POST /api/protocols/nfs/export-policies
# The call:
curl -d "@test_post_policy_single_rule.txt" -X POST "https://<mgmt-ip>/api/protocols/nfs/export-policies"
test_post_policy_single_rule.txt(body):
{
  "name": "P1",
  "rules":[
    {
      "clients": [
        {
          "match": "host1"
        }
      ],
      "ro_rule": [
        "krb5"
      ],
      "rw_rule": [
        "ntlm"
      ],
      "anonymous_user": "anon1"
    },
    {
      "clients": [
        {
          "match": "host2"
        }
      ],
      "ro_rule": [
        "sys"
      ],
      "rw_rule": [
        "ntlm"
      ],
      "superuser": [
        "any"
      ]
    }
  ]
}
```
---
### 3) Update an export policy for an SVM
---
```
# The API:
PATCH /api/protocols/nfs/export-policies/{policy.id}
# The call:
curl -d "@test_patch_policy.txt" -X PATCH "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934594"
test_patch_policy.txt(body):
{
  "name": "S1",
  "rules":[
    {
      "clients": [
        {
          "match": "host4"
        }
      ],
      "ro_rule": [
        "krb5"
      ],
      "rw_rule": [
        "ntlm"
      ]
    }
  ]
}
```
---
### 4) Delete an export policy for an SVM
---
```
# The API:
DELETE /api/protocols/nfs/export-policies/{policy.id}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934594"
```
---
##  Export Rules
### 1) Retrieve the export policy rule details for an export policy
---
```
# The API:
GET /api/protocols/nfs/export-policies/{policy.id}/rules
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934595/rules"
```
---
### 2) Create an export policy rule for an export policy
---
```
# The API:
POST /api/protocols/nfs/export-policies/{policy.id}/rules
# The call:
curl -d "<@test_patch_export_rule.txt>" -X POST "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934595/rules"
test_patch_export_rule.txt(body):
{
  "clients": [
    {
      "match": "host2"
    }
  ],
  "ro_rule": [
    "sys"
  ],
  "rw_rule": [
    "ntlm"
  ]
}
```
---
### 3) Update an export policy rule for an export policy
---
```
# The API:
PATCH /api/protocols/nfs/export-policies/{policy.id}/rules/{index}
# The call:
curl -d "@test_patch_export_rule.txt" -X PATCH "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934595/rules/5"
test_patch_export_rule.txt(body):
{
  "new_index": "10",
  "clients": [
    {
      "match": "host4"
    }
  ],
  "ro_rule": [
    "sys"
  ],
  "rw_rule": [
    "krb5"
  ]
}
```
---
### 4) Delete an export policy rule for an export policy
---
```
# The API:
DELETE /api/protocols/nfs/export-policies/{policy.id}/rules/{index}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934595/rules/15"
```
---
##  Export Clients
### 1) Retrieve the export client matches of an export policy rule
---
```
# The API:
GET /api/protocols/nfs/export-policies/{policy.id}/rules/{index}/clients
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934593/rules/2/clients"
```
---
### 2) Add an export client match to an export policy rule
---
```
# The API:
POST /api/protocols/nfs/export-policies/{policy.id}/rules/{index}/clients
# The call:
curl -d "@add_client_match.txt"" -X POST "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934593/rules/1/clients"
add_client_match.txt(body):
{
  "match" : "host4"
}
```
---
### 3) Delete an export client match from an export policy rule
---
```
# The API:
DELETE /api/protocols/nfs/export-policies/{policy.id}/rules/{index}/clients/{match}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/nfs/export-policies/8589934593/rules/1/clients/host1,host2"
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


__all__ = ["ExportPolicy", "ExportPolicySchema"]
__pdoc__ = {
    "ExportPolicySchema.resource": False,
    "ExportPolicySchema.patchable_fields": False,
    "ExportPolicySchema.postable_fields": False,
}


class ExportPolicySchema(ResourceSchema):
    """The fields of the ExportPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the export_policy. """

    id = fields.Integer(
        data_key="id",
    )
    r""" Export Policy ID """

    name = fields.Str(
        data_key="name",
    )
    r""" Export Policy Name """

    rules = fields.List(fields.Nested("netapp_ontap.resources.export_rule.ExportRuleSchema", unknown=EXCLUDE), data_key="rules")
    r""" Rules of the Export Policy. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the export_policy. """

    @property
    def resource(self):
        return ExportPolicy

    @property
    def patchable_fields(self):
        return [
            "name",
            "rules",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
            "rules",
            "svm.name",
            "svm.uuid",
        ]

class ExportPolicy(Resource):
    """Allows interaction with ExportPolicy objects on the host"""

    _schema = ExportPolicySchema
    _path = "/api/protocols/nfs/export-policies"
    @property
    def _keys(self):
        return ["id"]

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
        r"""Retrieves export policies.
### Related ONTAP commands
* `vserver export-policy show`
* `vserver export-policy rule show`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
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
        r"""Updates the properties of an export policy to change an export policy name or replace all export policy rules.
### Related ONTAP commands
* `vserver export-policy rename`
* `vserver export-policy rule delete`
* `vserver export-policy rule create`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
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
        r"""Deletes an export policy.
### Related ONTAP commands
* `vserver export-policy delete`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves export policies.
### Related ONTAP commands
* `vserver export-policy show`
* `vserver export-policy rule show`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an export policy.
### Related ONTAP commands
* `vserver export-policy show`
* `vserver export-policy rule show`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
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
        r"""Creates an export policy. An SVM can have any number of export policies to define rules for which clients can access data exported by the SVM. A policy with no rules prohibits access.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create an export policy.
* `name`  - Name of the export policy.
### Recommended optional properties
* `rules`  - Rule(s) of an export policy. Used to create the export rule and populate the export policy with export rules in a single request.
### Related ONTAP commands
* `vserver export-policy create`
* `vserver export-policy rule create`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
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
        r"""Updates the properties of an export policy to change an export policy name or replace all export policy rules.
### Related ONTAP commands
* `vserver export-policy rename`
* `vserver export-policy rule delete`
* `vserver export-policy rule create`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
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
        r"""Deletes an export policy.
### Related ONTAP commands
* `vserver export-policy delete`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


