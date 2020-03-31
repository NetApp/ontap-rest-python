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


__all__ = ["ApplicationComponentSnapshot", "ApplicationComponentSnapshotSchema"]
__pdoc__ = {
    "ApplicationComponentSnapshotSchema.resource": False,
    "ApplicationComponentSnapshotSchema.patchable_fields": False,
    "ApplicationComponentSnapshotSchema.postable_fields": False,
}


class ApplicationComponentSnapshotSchema(ResourceSchema):
    """The fields of the ApplicationComponentSnapshot object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the application_component_snapshot. """

    application = fields.Nested("netapp_ontap.models.application_component_snapshot_application.ApplicationComponentSnapshotApplicationSchema", data_key="application", unknown=EXCLUDE)
    r""" The application field of the application_component_snapshot. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=255),
    )
    r""" Comment. Valid in POST """

    component = fields.Nested("netapp_ontap.models.application_component_snapshot_component.ApplicationComponentSnapshotComponentSchema", data_key="component", unknown=EXCLUDE)
    r""" The component field of the application_component_snapshot. """

    consistency_type = fields.Str(
        data_key="consistency_type",
        validate=enum_validation(['crash', 'application']),
    )
    r""" Consistency Type. This is for categorization only. A Snapshot copy should not be set to application consistent unless the host application is quiesced for the Snapshot copy. Valid in POST

Valid choices:

* crash
* application """

    create_time = fields.Str(
        data_key="create_time",
    )
    r""" Creation Time """

    is_partial = fields.Boolean(
        data_key="is_partial",
    )
    r""" A partial Snapshot copy means that not all volumes in an application component were included in the Snapshot copy. """

    name = fields.Str(
        data_key="name",
    )
    r""" Snapshot copy name. Valid in POST """

    svm = fields.Nested("netapp_ontap.models.application_component_snapshot_svm.ApplicationComponentSnapshotSvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the application_component_snapshot. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Snapshot copy UUID. Valid in URL """

    @property
    def resource(self):
        return ApplicationComponentSnapshot

    @property
    def patchable_fields(self):
        return [
            "application",
            "comment",
            "component",
            "consistency_type",
            "name",
            "svm",
        ]

    @property
    def postable_fields(self):
        return [
            "application",
            "comment",
            "component",
            "consistency_type",
            "name",
            "svm",
        ]

class ApplicationComponentSnapshot(Resource):
    """Allows interaction with ApplicationComponentSnapshot objects on the host"""

    _schema = ApplicationComponentSnapshotSchema
    _path = "/api/application/applications/{application[uuid]}/components/{component[uuid]}/snapshots"
    @property
    def _keys(self):
        return ["application.uuid", "component.uuid", "uuid"]

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
        r"""Retrieves Snapshot copies of an application component.<br/>
This endpoint is only supported for Maxdata template applications.<br/>
Component Snapshot copies are essentially more granular application Snapshot copies. There is no difference beyond the scope of the operation.
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
* [`GET /application/applications/{uuid}/snapshots`](#operations-application-application_snapshot_collection_get)
* [`DOC /application`](#docs-application-overview)
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
        r"""Delete a Snapshot copy of an application component.<br/>
This endpoint is only supported for Maxdata template applications.<br/>
Component Snapshot copies are essentially more granular application Snapshot copies. There is no difference beyond the scope of the operation.
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
* [`DELETE /application/applications/{uuid}/snapshots`](#operations-application-application_snapshot_delete)
* [`DOC /application`](#docs-application-overview)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves Snapshot copies of an application component.<br/>
This endpoint is only supported for Maxdata template applications.<br/>
Component Snapshot copies are essentially more granular application Snapshot copies. There is no difference beyond the scope of the operation.
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
* [`GET /application/applications/{uuid}/snapshots`](#operations-application-application_snapshot_collection_get)
* [`DOC /application`](#docs-application-overview)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieve a Snapshot copy of an application component.<br/>
This endpoint is only supported for Maxdata template applications.<br/>
Component Snapshot copies are essentially more granular application Snapshot copies. There is no difference beyond the scope of the operation.
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
* [`GET /application/applications/{uuid}/snapshots`](#operations-application-application_snapshot_get)
* [`DOC /application`](#docs-application-overview)
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
        r"""Creates a Snapshot copy of an application component.<br/>
This endpoint is only supported for Maxdata template applications.<br/>
### Required properties
* `name`
### Recommended optional properties
* `consistency_type` - Track whether this snapshot is _application_ or _crash_ consistent.
Component Snapshot copies are essentially more granular application Snapshot copies. There is no difference beyond the scope of the operation.
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
* [`GET /application/applications/{uuid}/snapshots`](#operations-application-application_snapshot_create)
* [`DOC /application`](#docs-application-overview)
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
        r"""Delete a Snapshot copy of an application component.<br/>
This endpoint is only supported for Maxdata template applications.<br/>
Component Snapshot copies are essentially more granular application Snapshot copies. There is no difference beyond the scope of the operation.
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
* [`DELETE /application/applications/{uuid}/snapshots`](#operations-application-application_snapshot_delete)
* [`DOC /application`](#docs-application-overview)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def restore(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Restore a Snapshot copy of an application component.<br/>
This endpoint is only supported for Maxdata template applications.<br/>
Component Snapshot copies are essentially more granular application Snapshot copies. There is no difference beyond the scope of the operation.
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
* [`POST /application/applications/{application.uuid}/snapshots/{uuid}/restore`](#operations-application-application_snapshot_restore)
* [`DOC /application`](#docs-application-overview)
* [`DOC Asynchronous operations`](#docs-docs-Synchronous-and-asynchronous-operations)
"""
        return super()._action(
            "restore", body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    restore.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._action.__doc__)  # pylint: disable=no-member

