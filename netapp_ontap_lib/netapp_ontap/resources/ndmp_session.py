# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

You can use this API to manage diagnostic information on NDMP sessions belonging to a specific SVM in the case of SVM-scope or to a specific node in the case of node-scope.
### Examples
Retrieves NDMP session details under node-scope:
<br/>
```
GET "/api/protocols/ndmp/sessions/9b372ce7-3a4b-11e9-a7f8-0050568e3d73/2000"
```
<br/>
Retrieves NDMP session details under SVM-scope:
<br/>
```
GET "/api/protocols/ndmp/sessions/13bb2092-458b-11e9-9c06-0050568ea604/2000:4000"
```
<br/>
Deletes NDMP session details under node-scope:
<br/>
```
DELETE "/api/protocols/ndmp/sessions/9b372ce7-3a4b-11e9-a7f8-0050568e3d73/2000"
```
<br/>
Deletes NDMP session details under SVM-scope:
<br/>
```
DELETE "/api/protocols/ndmp/sessions/13bb2092-458b-11e9-9c06-0050568ea604/2000:4000"
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


__all__ = ["NdmpSession", "NdmpSessionSchema"]
__pdoc__ = {
    "NdmpSessionSchema.resource": False,
    "NdmpSessionSchema.patchable_fields": False,
    "NdmpSessionSchema.postable_fields": False,
}


class NdmpSessionSchema(ResourceSchema):
    """The fields of the NdmpSession object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ndmp_session. """

    backup_engine = fields.Str(
        data_key="backup_engine",
        validate=enum_validation(['dump', 'smtape']),
    )
    r""" Indicates the NDMP backup engine.

Valid choices:

* dump
* smtape """

    client_address = fields.Str(
        data_key="client_address",
    )
    r""" Indicates the NDMP client address. """

    client_port = fields.Integer(
        data_key="client_port",
    )
    r""" Indicates the NDMP client port. """

    data = fields.Nested("netapp_ontap.models.ndmp_data.NdmpDataSchema", data_key="data", unknown=EXCLUDE)
    r""" Information about the NDMP data server. """

    data_path = fields.Str(
        data_key="data_path",
    )
    r""" Indicates the NDMP backup or restore path.

Example: /vserver1/vol1 """

    id = fields.Str(
        data_key="id",
    )
    r""" NDMP session identifier. """

    mover = fields.Nested("netapp_ontap.models.ndmp_mover.NdmpMoverSchema", data_key="mover", unknown=EXCLUDE)
    r""" Information about the NDMP mover. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the ndmp_session. """

    scsi = fields.Nested("netapp_ontap.models.ndmp_scsi.NdmpScsiSchema", data_key="scsi", unknown=EXCLUDE)
    r""" Information about the NDMP SCSI server. """

    source_address = fields.Str(
        data_key="source_address",
    )
    r""" Indicates the NDMP local address on which connection was established. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the ndmp_session. """

    tape_device = fields.Str(
        data_key="tape_device",
    )
    r""" Indicates the NDMP tape device.

Example: nrst0a """

    tape_mode = fields.Str(
        data_key="tape_mode",
    )
    r""" Indicates the NDMP tape device mode of operation. """

    @property
    def resource(self):
        return NdmpSession

    @property
    def patchable_fields(self):
        return [
            "backup_engine",
            "client_address",
            "client_port",
            "data",
            "data_path",
            "id",
            "mover",
            "node.name",
            "node.uuid",
            "scsi",
            "source_address",
            "svm.name",
            "svm.uuid",
            "tape_device",
            "tape_mode",
        ]

    @property
    def postable_fields(self):
        return [
            "backup_engine",
            "client_address",
            "client_port",
            "data",
            "data_path",
            "id",
            "mover",
            "node.name",
            "node.uuid",
            "scsi",
            "source_address",
            "svm.name",
            "svm.uuid",
            "tape_device",
            "tape_mode",
        ]

class NdmpSession(Resource):
    """Allows interaction with NdmpSession objects on the host"""

    _schema = NdmpSessionSchema
    _path = "/api/protocols/ndmp/sessions"
    @property
    def _keys(self):
        return ["owner.uuid", "session.id"]

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
        r"""Retrieves a collection of NDMP sessions. In the case of SVM-scope, if this API is executed on a data IP, it displays the list of NDMP sessions under the specified SVM; otherwise it displays the list of NDMP sessions for all the SVMs under the cluster. In the case of node-scope, it displays the list of NDMP sessions for all nodes.
### Related ONTAP commands
* `vserver services ndmp probe`
* `system services ndmp probe`
### Learn more
* [`DOC /protocols/ndmp/sessions`](#docs-ndmp-protocols_ndmp_sessions)
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
        r"""Deletes a specific NDMP session.
### Related ONTAP commands
* `vserver services ndmp kill`
* `system services ndmp kill`
### Learn more
* [`DOC /protocols/ndmp/sessions`](#docs-ndmp-protocols_ndmp_sessions)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of NDMP sessions. In the case of SVM-scope, if this API is executed on a data IP, it displays the list of NDMP sessions under the specified SVM; otherwise it displays the list of NDMP sessions for all the SVMs under the cluster. In the case of node-scope, it displays the list of NDMP sessions for all nodes.
### Related ONTAP commands
* `vserver services ndmp probe`
* `system services ndmp probe`
### Learn more
* [`DOC /protocols/ndmp/sessions`](#docs-ndmp-protocols_ndmp_sessions)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the details of a specific NDMP session.
### Related ONTAP commands
* `vserver services ndmp probe`
* `system services ndmp probe`
### Learn more
* [`DOC /protocols/ndmp/sessions`](#docs-ndmp-protocols_ndmp_sessions)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member



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
        r"""Deletes a specific NDMP session.
### Related ONTAP commands
* `vserver services ndmp kill`
* `system services ndmp kill`
### Learn more
* [`DOC /protocols/ndmp/sessions`](#docs-ndmp-protocols_ndmp_sessions)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


