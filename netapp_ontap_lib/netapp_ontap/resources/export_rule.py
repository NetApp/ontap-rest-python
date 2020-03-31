# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["ExportRule", "ExportRuleSchema"]
__pdoc__ = {
    "ExportRuleSchema.resource": False,
    "ExportRuleSchema.patchable_fields": False,
    "ExportRuleSchema.postable_fields": False,
}


class ExportRuleSchema(ResourceSchema):
    """The fields of the ExportRule object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the export_rule. """

    anonymous_user = fields.Str(
        data_key="anonymous_user",
    )
    r""" User ID To Which Anonymous Users Are Mapped. """

    clients = fields.List(fields.Nested("netapp_ontap.resources.export_client.ExportClientSchema", unknown=EXCLUDE), data_key="clients")
    r""" Array of client matches """

    index = fields.Integer(
        data_key="index",
    )
    r""" Index of the rule within the export policy. """

    protocols = fields.List(fields.Str, data_key="protocols")
    r""" The protocols field of the export_rule. """

    ro_rule = fields.List(fields.Str, data_key="ro_rule")
    r""" Authentication flavors that the read-only access rule governs """

    rw_rule = fields.List(fields.Str, data_key="rw_rule")
    r""" Authentication flavors that the read/write access rule governs """

    superuser = fields.List(fields.Str, data_key="superuser")
    r""" Authentication flavors that the superuser security type governs """

    @property
    def resource(self):
        return ExportRule

    @property
    def patchable_fields(self):
        return [
            "anonymous_user",
            "clients",
            "protocols",
            "ro_rule",
            "rw_rule",
            "superuser",
        ]

    @property
    def postable_fields(self):
        return [
            "anonymous_user",
            "clients",
            "protocols",
            "ro_rule",
            "rw_rule",
            "superuser",
        ]

class ExportRule(Resource):
    """Allows interaction with ExportRule objects on the host"""

    _schema = ExportRuleSchema
    _path = "/api/protocols/nfs/export-policies/{policy[id]}/rules"
    @property
    def _keys(self):
        return ["policy.id", "index"]

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
        r"""Retrieves export policy rules.
### Related ONTAP commands
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
        r"""Updates the properties of an export policy rule to change an export policy rule's index or fields.
### Related ONTAP commands
* `vserver export-policy rule modify`
* `vserver export-policy rule setindex`
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
        r"""Deletes an export policy rule.
### Related ONTAP commands
* `vserver export-policy rule delete`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves export policy rules.
### Related ONTAP commands
* `vserver export-policy rule show`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an export policy rule
### Related ONTAP commands
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
        r"""Creates an export policy rule.
### Required properties
* `policy.id`  - Existing export policy for which to create an export rule.
* `clients.match`  - List of clients (hostnames, ipaddresses, netgroups, domains) to which the export rule applies.
* `ro_rule`  - Used to specify the security type for read-only access to volumes that use the export rule.
* `rw_rule`  - Used to specify the security type for read-write access to volumes that use the export rule.
### Default property values
If not specified in POST, the following default property values are assigned:
* `protocols` - _any_
* `anonymous_user` - _none_
* `superuser` - _any_
### Related ONTAP commands
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
        r"""Updates the properties of an export policy rule to change an export policy rule's index or fields.
### Related ONTAP commands
* `vserver export-policy rule modify`
* `vserver export-policy rule setindex`
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
        r"""Deletes an export policy rule.
### Related ONTAP commands
* `vserver export-policy rule delete`
### Learn more
* [`DOC /protocols/nfs/export-policies`](#docs-NAS-protocols_nfs_export-policies)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


