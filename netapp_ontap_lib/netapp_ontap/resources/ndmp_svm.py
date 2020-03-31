# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

You can use this API to manage NDMP configurations of SVMs.
### Examples
Updates the "enable" field:
   <br/>
   ```
   PATCH "/api/protocols/ndmp/svms/9b372ce7-3a4b-11e9-a7f8-0050568e3d73" '{"enabled":"false"}'
   ```
   <br/>
Updates the "authentication_types" field:
   <br/>
   ```
   PATCH "/api/protocols/ndmp/svms/9b372ce7-3a4b-11e9-a7f8-0050568e3d73" '{"authentication_types":["challenge"]}'
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


__all__ = ["NdmpSvm", "NdmpSvmSchema"]
__pdoc__ = {
    "NdmpSvmSchema.resource": False,
    "NdmpSvmSchema.patchable_fields": False,
    "NdmpSvmSchema.postable_fields": False,
}


class NdmpSvmSchema(ResourceSchema):
    """The fields of the NdmpSvm object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ndmp_svm. """

    authentication_types = fields.List(fields.Str, data_key="authentication_types")
    r""" NDMP authentication types.

Example: ["plaintext","challenge"] """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Is the NDMP service enabled on the SVM?

Example: true """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the ndmp_svm. """

    @property
    def resource(self):
        return NdmpSvm

    @property
    def patchable_fields(self):
        return [
            "authentication_types",
            "enabled",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "authentication_types",
            "enabled",
            "svm.name",
            "svm.uuid",
        ]

class NdmpSvm(Resource):
    """Allows interaction with NdmpSvm objects on the host"""

    _schema = NdmpSvmSchema
    _path = "/api/protocols/ndmp/svms"
    @property
    def _keys(self):
        return ["svm.uuid"]

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
        r"""Retrieves NDMP configurations for all SVMs.
### Related ONTAP commands
* `vserver services ndmp show`
### Learn more
* [`DOC /protocols/ndmp/svms`](#docs-ndmp-protocols_ndmp_svms)
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
        r"""Updates the NDMP configuration for a specific SVM.
### Related ONTAP commands
* `vserver services ndmp modify`
### Learn more
* [`DOC /protocols/ndmp/svms`](#docs-ndmp-protocols_ndmp_svms)
"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves NDMP configurations for all SVMs.
### Related ONTAP commands
* `vserver services ndmp show`
### Learn more
* [`DOC /protocols/ndmp/svms`](#docs-ndmp-protocols_ndmp_svms)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an NDMP configuration for a specific SVM.
### Related ONTAP commands
* `vserver services ndmp show`
### Learn more
* [`DOC /protocols/ndmp/svms`](#docs-ndmp-protocols_ndmp_svms)
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
        r"""Updates the NDMP configuration for a specific SVM.
### Related ONTAP commands
* `vserver services ndmp modify`
### Learn more
* [`DOC /protocols/ndmp/svms`](#docs-ndmp-protocols_ndmp_svms)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



