# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Applications support Snapshot copies across all member storage elements. These Snapshot copies can be created and restored at any time or as scheduled. Most applications have hourly Snapshot copies enabled by default, unless the RPO setting is overridden during the creation of the application. An application Snapshot copy can be flagged as either _application consistent_, or _crash consistent_. From an ONTAP perspective, there is no difference between these two consistency types. These types are available for record keeping so that Snapshot copies taken after the application is quiesced (application consistent) can be tracked separately from those Snapshot copies taken without first quiescing the application (crash consistent). By default, all application Snapshot copies are flagged to be _crash consistent_, and Snapshot copies taken at a scheduled time are also considered _crash consistent_.<br/>
The functionality provided by these APIs is not integrated with the host application. Snapshot copies have limited value without host coordination, so the use of the SnapCenter Backup Management suite is recommended to ensure correct interaction between host applications and ONTAP.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["ApplicationSnapshot", "ApplicationSnapshotSchema"]
__pdoc__ = {
    "ApplicationSnapshotSchema.resource": False,
    "ApplicationSnapshotSchema.patchable_fields": False,
    "ApplicationSnapshotSchema.postable_fields": False,
}


class ApplicationSnapshotSchema(ResourceSchema):
    """The fields of the ApplicationSnapshot object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the application_snapshot. """

    application = fields.Nested("netapp_ontap.models.application_snapshot_application.ApplicationSnapshotApplicationSchema", data_key="application", unknown=EXCLUDE)
    r""" The application field of the application_snapshot. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=255),
    )
    r""" Comment. Valid in POST. """

    components = fields.List(fields.Nested("netapp_ontap.models.application_snapshot_components.ApplicationSnapshotComponentsSchema", unknown=EXCLUDE), data_key="components")
    r""" The components field of the application_snapshot. """

    consistency_type = fields.Str(
        data_key="consistency_type",
        validate=enum_validation(['crash', 'application']),
    )
    r""" Consistency type. This is for categorization purposes only. A Snapshot copy should not be set to 'application consistent' unless the host application is quiesced for the Snapshot copy. Valid in POST.

Valid choices:

* crash
* application """

    create_time = fields.Str(
        data_key="create_time",
    )
    r""" Creation time """

    is_partial = fields.Boolean(
        data_key="is_partial",
    )
    r""" A partial Snapshot copy means that not all volumes in an application component were included in the Snapshot copy. """

    name = fields.Str(
        data_key="name",
    )
    r""" The Snapshot copy name. Valid in POST. """

    svm = fields.Nested("netapp_ontap.models.application_component_svm.ApplicationComponentSvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the application_snapshot. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The Snapshot copy UUID. Valid in URL. """

    @property
    def resource(self):
        return ApplicationSnapshot

    @property
    def patchable_fields(self):
        return [
            "application",
            "comment",
            "consistency_type",
            "name",
            "svm",
        ]

    @property
    def postable_fields(self):
        return [
            "application",
            "comment",
            "consistency_type",
            "name",
            "svm",
        ]

class ApplicationSnapshot(Resource):
    """Allows interaction with ApplicationSnapshot objects on the host"""

    _schema = ApplicationSnapshotSchema
    _path = "/api/application/applications/{application[uuid]}/snapshots"
    @property
    def _keys(self):
        return ["application.uuid", "uuid"]

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
        r"""Retrieves Snapshot copies of an application.
### Query examples
The following query returns all Snapshot copies from May 4, 2017 EST. For readability, the colon (`:`) is left in this example. For an actual call, they should be escaped as `%3A`.<br/><br/>
```
GET /application/applications/{application.uuid}/snapshots?create_time=2017-05-04T00:00:00-05:00..2017-05-04T23:59:59-05:00
```
<br/>The following query returns all Snapshot copies that have been flagged as _application consistent_.<br/><br/>
```
GET /application/applications/{application.uuid}/snapshots?consistency_type=application
```
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
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
        r"""Delete a Snapshot copy of an application
### Query examples
Individual Snapshot copies can be destroyed with no query parameters, or a range of Snapshot copies can be destroyed at one time using a query.<br/>
The following query deletes all application Snapshot copies created before May 4, 2017<br/><br/>
```
DELETE /application/applications/{application.uuid}/snapshots?create_time=<2017-05-04T00:00:00-05:00
```

### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves Snapshot copies of an application.
### Query examples
The following query returns all Snapshot copies from May 4, 2017 EST. For readability, the colon (`:`) is left in this example. For an actual call, they should be escaped as `%3A`.<br/><br/>
```
GET /application/applications/{application.uuid}/snapshots?create_time=2017-05-04T00:00:00-05:00..2017-05-04T23:59:59-05:00
```
<br/>The following query returns all Snapshot copies that have been flagged as _application consistent_.<br/><br/>
```
GET /application/applications/{application.uuid}/snapshots?consistency_type=application
```
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
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
* [`GET /application/applications/{uuid}/snapshots`](#operations-application-application_snapshot_create)
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
        r"""Creates a Snapshot copy of the application.
### Required properties
* `name`
### Recommended optional properties
* `consistency_type` - Track whether this snapshot is _application_ or _crash_ consistent.
### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)
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
        r"""Delete a Snapshot copy of an application
### Query examples
Individual Snapshot copies can be destroyed with no query parameters, or a range of Snapshot copies can be destroyed at one time using a query.<br/>
The following query deletes all application Snapshot copies created before May 4, 2017<br/><br/>
```
DELETE /application/applications/{application.uuid}/snapshots?create_time=<2017-05-04T00:00:00-05:00
```

### Learn more
* [`DOC /application/applications/{application.uuid}/snapshots`](#docs-application-application_applications_{application.uuid}_snapshots)"""
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
        r"""Restore an application snapshot<br/>
Restoring an application Snapshot copy reverts all storage elements in the Snapshot copy to the state in which the Snapshot copy was in when the Snapshot copy was taken. This restoration does not apply to access settings that might have changed since the Snapshot copy was created.
### Learn more
* [`DOC /application`](#docs-application-overview)
* [`DOC Asynchronous operations`](#docs-docs-Synchronous-and-asynchronous-operations)
"""
        return super()._action(
            "restore", body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    restore.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._action.__doc__)  # pylint: disable=no-member

