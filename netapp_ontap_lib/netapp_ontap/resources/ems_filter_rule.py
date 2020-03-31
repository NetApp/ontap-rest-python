# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Manages a specific instance of a rule within a filter.
See the documentation for [/support/ems/filters](#/docs/support/support_ems_filters) for details on the various properties in a rule.
## Examples
### Retrieving a single instance of a rule
```JSON
# API
GET /api/support/ems/filters/no-info-debug-events/rules/1
# Response
200 OK
# JSON Body
{
  "name": "no-info-debug-events",
  "index": 1,
  "type": "include",
  "message_criteria": {
    "name_pattern": "*",
    "severities": "emergency,alert,error,notice",
    "snmp_trap_types": "*",
    "_links": {
      "self": {
        "href": "/api/support/ems/messages?name=*&severity=emergency,alert,error,notice&snmp_trap_type=*"
      }
    }
  },
  "_links": {
    "self": {
      "href": "/api/support/ems/filters/no-info-debug-events/rules/1"
    }
  }
}
```
### Updating an existing rule to use severity emergency
```JSON
# API
PATCH /api/support/ems/filters/test-filter/rules/1
# JSON Body
{
  "message_criteria": {
    "severities": "emergency"
  }
}
# Response
200 OK
```
### Deleting a rule from an existing filter
```JSON
# API
DELETE /api/support/ems/filters/test-filter/rules/1
# Response
200 OK
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["EmsFilterRule", "EmsFilterRuleSchema"]
__pdoc__ = {
    "EmsFilterRuleSchema.resource": False,
    "EmsFilterRuleSchema.patchable_fields": False,
    "EmsFilterRuleSchema.postable_fields": False,
}


class EmsFilterRuleSchema(ResourceSchema):
    """The fields of the EmsFilterRule object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ems_filter_rule. """

    index = fields.Integer(
        data_key="index",
    )
    r""" Rule index. Rules are evaluated in ascending order. If a rule's index order is not specified during creation, the rule is appended to the end of the list.

Example: 1 """

    message_criteria = fields.Nested("netapp_ontap.models.ems_filter_rule_message_criteria.EmsFilterRuleMessageCriteriaSchema", data_key="message_criteria", unknown=EXCLUDE)
    r""" The message_criteria field of the ems_filter_rule. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['include', 'exclude']),
    )
    r""" Rule type

Valid choices:

* include
* exclude """

    @property
    def resource(self):
        return EmsFilterRule

    @property
    def patchable_fields(self):
        return [
            "index",
            "message_criteria",
            "type",
        ]

    @property
    def postable_fields(self):
        return [
            "index",
            "message_criteria",
            "type",
        ]

class EmsFilterRule(Resource):
    r""" Rule for an event filter """

    _schema = EmsFilterRuleSchema
    _path = "/api/support/ems/filters/{ems_filter[name]}/rules"
    @property
    def _keys(self):
        return ["ems_filter.name", "index"]

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
        r"""Retrieves event filter rules.
### Related ONTAP commands
* `event filter show`

### Learn more
* [`DOC /support/ems/filters/{name}/rules`](#docs-support-support_ems_filters_{name}_rules)"""
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
        r"""Updates an event filter rule.
### Recommended optional properties
* `message_criteria` - New criteria on which a rule is to match an event.
### Related ONTAP commands
* `event filter rule add`
* `event filter rule delete`

### Learn more
* [`DOC /support/ems/filters/{name}/rules/{index}`](#docs-support-support_ems_filters_{name}_rules_{index})"""
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
        r"""Deletes an event filter rule.
### Related ONTAP commands
* `event filter rule delete`

### Learn more
* [`DOC /support/ems/filters/{name}/rules/{index}`](#docs-support-support_ems_filters_{name}_rules_{index})"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves event filter rules.
### Related ONTAP commands
* `event filter show`

### Learn more
* [`DOC /support/ems/filters/{name}/rules`](#docs-support-support_ems_filters_{name}_rules)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an event filter rule.
### Related ONTAP commands
* `event filter show`

### Learn more
* [`DOC /support/ems/filters/{name}/rules/{index}`](#docs-support-support_ems_filters_{name}_rules_{index})"""
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
        r"""Creates an event filter rule.
### Required properties
* `message_criteria` - Criteria on which a rule is to match an event.
### Recommended optional properties
* `index` - One-based position index of the new rule.
### Related ONTAP commands
* `event filter rule add`

### Learn more
* [`DOC /support/ems/filters/{name}/rules`](#docs-support-support_ems_filters_{name}_rules)"""
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
        r"""Updates an event filter rule.
### Recommended optional properties
* `message_criteria` - New criteria on which a rule is to match an event.
### Related ONTAP commands
* `event filter rule add`
* `event filter rule delete`

### Learn more
* [`DOC /support/ems/filters/{name}/rules/{index}`](#docs-support-support_ems_filters_{name}_rules_{index})"""
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
        r"""Deletes an event filter rule.
### Related ONTAP commands
* `event filter rule delete`

### Learn more
* [`DOC /support/ems/filters/{name}/rules/{index}`](#docs-support-support_ems_filters_{name}_rules_{index})"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


