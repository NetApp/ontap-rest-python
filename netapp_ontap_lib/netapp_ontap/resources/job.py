# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
You can use this API to view and manipulate jobs. Jobs provide information about asynchronous operations. Some long-running jobs are paused or cancelled by calling a PATCH request. Individual operations indicate if they support PATCH requests on the job. After a job transitions to a terminal state, it is deleted after a default time of 300 seconds. Attempts to call a GET or PATCH request on the job returns a 404 error code After the job has been deleted.
## Example
The following examples show how to retrieve and update a job state:
### Retrieving job information
```
# The API:
/api/cluster/jobs/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/jobs/b5145e1d-b53b-11e8-8252-005056bbd8f5" -H "accept: application/json"
# The response:
{
    "uuid": "b5145e1d-b53b-11e8-8252-005056bbd8f5",
    "code": 0,
    "description": "Cluster Backup Job",
    "state": "running",
    "message": "creating_node_backups",
    "_links": {
        "self": {
            "href": "/api/cluster/jobs/b5145e1d-b53b-11e8-8252-005056bbd8f5"
        }
    }
}
```
---
### Updating a job that supports the new state
```
# The API:
/api/cluster/jobs/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/cluster/jobs/b5145e1d-b53b-11e8-8252-005056bbd8f5?action=cancel" -H "accept: application/json"
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


__all__ = ["Job", "JobSchema"]
__pdoc__ = {
    "JobSchema.resource": False,
    "JobSchema.patchable_fields": False,
    "JobSchema.postable_fields": False,
}


class JobSchema(ResourceSchema):
    """The fields of the Job object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the job. """

    code = fields.Integer(
        data_key="code",
    )
    r""" If the state indicates "failure", this is the final error code.

Example: 0 """

    description = fields.Str(
        data_key="description",
    )
    r""" The description of the job to help identify it independent of the UUID.

Example: App Snapshot Job """

    end_time = fields.DateTime(
        data_key="end_time",
    )
    r""" The time the job ended. """

    message = fields.Str(
        data_key="message",
    )
    r""" A message corresponding to the state of the job providing additional details about the current state.

Example: Complete: Successful """

    start_time = fields.DateTime(
        data_key="start_time",
    )
    r""" The time the job started. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['queued', 'running', 'paused', 'success', 'failure']),
    )
    r""" The state of the job.

Valid choices:

* queued
* running
* paused
* success
* failure """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the job.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return Job

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]

class Job(Resource):
    """Allows interaction with Job objects on the host"""

    _schema = JobSchema
    _path = "/api/cluster/jobs"
    @property
    def _keys(self):
        return ["uuid"]

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
        r"""Retrieves a list of recently running asynchronous jobs. After a job transitions to a failure or success state, it is deleted after a default time of 300 seconds.
### Learn more
* [`DOC /cluster/jobs`](#docs-cluster-cluster_jobs)"""
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
        r"""Updates the state of a specific asynchronous job.
### Learn more
* [`DOC /cluster/jobs`](#docs-cluster-cluster_jobs)"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member


    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of recently running asynchronous jobs. After a job transitions to a failure or success state, it is deleted after a default time of 300 seconds.
### Learn more
* [`DOC /cluster/jobs`](#docs-cluster-cluster_jobs)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the details of a specific asynchronous job. After a job transitions to a failure or success state, it is deleted after a default time of 300 seconds.
### Learn more
* [`DOC /cluster/jobs`](#docs-cluster-cluster_jobs)"""
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
        r"""Updates the state of a specific asynchronous job.
### Learn more
* [`DOC /cluster/jobs`](#docs-cluster-cluster_jobs)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



