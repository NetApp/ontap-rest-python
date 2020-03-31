# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

You can use this API to manage node configurations.
### Examples
Updates "enable" and "authentication_types" fields:
   <br/>
   ```
   PATCH "/api/protocols/ndmp/nodes/13bb2092-458b-11e9-9c06-0050568ea64e" '{"enable":"false","authentication_types":["plaintext"]}'
   ```
   <br/>
Updates the "user" field:
   <br/>
   ```
   PATCH "/api/protocols/ndmp/nodes/13bb2092-458b-11e9-9c06-0050568ea64e" '{"user":"user22"}'
   ```
   <br/>
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["NdmpNode", "NdmpNodeSchema"]
__pdoc__ = {
    "NdmpNodeSchema.resource": False,
    "NdmpNodeSchema.patchable_fields": False,
    "NdmpNodeSchema.postable_fields": False,
}


class NdmpNodeSchema(ResourceSchema):
    """The fields of the NdmpNode object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ndmp_node. """

    authentication_types = fields.List(fields.Str, data_key="authentication_types")
    r""" NDMP authentication types.

Example: ["plaintext","challenge"] """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Is the NDMP service enabled?

Example: true """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the ndmp_node. """

    password = fields.Str(
        data_key="password",
    )
    r""" NDMP password. This can only be set and cannot be read back. """

    user = fields.Str(
        data_key="user",
    )
    r""" NDMP user ID

Example: ndmp_user """

    @property
    def resource(self):
        return NdmpNode

    @property
    def patchable_fields(self):
        return [
            "authentication_types",
            "enabled",
            "node.name",
            "node.uuid",
            "password",
            "user",
        ]

    @property
    def postable_fields(self):
        return [
            "authentication_types",
            "enabled",
            "node.name",
            "node.uuid",
            "password",
            "user",
        ]

class NdmpNode(Resource):
    """Allows interaction with NdmpNode objects on the host"""

    _schema = NdmpNodeSchema
    _path = "/api/protocols/ndmp/nodes"
    @property
    def _keys(self):
        return ["node.uuid"]

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
        r"""Retrieves NDMP node configurations for all of the nodes.
### Related ONTAP commands
* `system services ndmp show`
### Learn more
* [`DOC /protocols/ndmp/nodes`](#docs-ndmp-protocols_ndmp_nodes)
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
        r"""Updates the NDMP node configuration for a specific node.
### Related ONTAP commands
* `system services ndmp modify`
### Learn more
* [`DOC /protocols/ndmp/nodes`](#docs-ndmp-protocols_ndmp_nodes)
"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves NDMP node configurations for all of the nodes.
### Related ONTAP commands
* `system services ndmp show`
### Learn more
* [`DOC /protocols/ndmp/nodes`](#docs-ndmp-protocols_ndmp_nodes)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an NDMP node configuration for a specific node.
### Related ONTAP commands
* `system services ndmp show`
### Learn more
* [`DOC /protocols/ndmp/nodes`](#docs-ndmp-protocols_ndmp_nodes)
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
        r"""Updates the NDMP node configuration for a specific node.
### Related ONTAP commands
* `system services ndmp modify`
### Learn more
* [`DOC /protocols/ndmp/nodes`](#docs-ndmp-protocols_ndmp_nodes)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



