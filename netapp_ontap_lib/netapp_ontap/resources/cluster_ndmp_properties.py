# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

You can use this API to manage NDMP mode: SVM-scope or node-scope.
### Examples
Updates NDMP mode to SVM:
   <br/>
   ```
   PATCH "/api/protocols/ndmp" '{"mode":"svm"}'
   ```
   <br/>
Updates NDMP mode to node:
   <br/>
   ```
   PATCH "/api/protocols/ndmp" '{"mode":"node"}'
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


__all__ = ["ClusterNdmpProperties", "ClusterNdmpPropertiesSchema"]
__pdoc__ = {
    "ClusterNdmpPropertiesSchema.resource": False,
    "ClusterNdmpPropertiesSchema.patchable_fields": False,
    "ClusterNdmpPropertiesSchema.postable_fields": False,
}


class ClusterNdmpPropertiesSchema(ResourceSchema):
    """The fields of the ClusterNdmpProperties object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cluster_ndmp_properties. """

    mode = fields.Str(
        data_key="mode",
        validate=enum_validation(['svm', 'node']),
    )
    r""" Indicates whether NDMP is in node-scoped or SVM-scoped mode.

Valid choices:

* svm
* node """

    @property
    def resource(self):
        return ClusterNdmpProperties

    @property
    def patchable_fields(self):
        return [
            "mode",
        ]

    @property
    def postable_fields(self):
        return [
            "mode",
        ]

class ClusterNdmpProperties(Resource):
    """Allows interaction with ClusterNdmpProperties objects on the host"""

    _schema = ClusterNdmpPropertiesSchema
    _path = "/api/protocols/ndmp"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the current NDMP mode.
### Related ONTAP commands
* `system services ndmp node-scope-mode status`
### Learn more
* [`DOC /protocols/ndmp`](#docs-ndmp-protocols_ndmp)
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
        r"""Updates the NDMP mode.
### Related ONTAP commands
* `system services ndmp node-scope-mode`
### Learn more
* [`DOC /protocols/ndmp`](#docs-ndmp-protocols_ndmp)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



