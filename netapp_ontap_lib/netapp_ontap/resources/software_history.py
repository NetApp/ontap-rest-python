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


__all__ = ["SoftwareHistory", "SoftwareHistorySchema"]
__pdoc__ = {
    "SoftwareHistorySchema.resource": False,
    "SoftwareHistorySchema.patchable_fields": False,
    "SoftwareHistorySchema.postable_fields": False,
}


class SoftwareHistorySchema(ResourceSchema):
    """The fields of the SoftwareHistory object"""

    end_time = fields.DateTime(
        data_key="end_time",
    )
    r""" Completion time of this installation request.

Example: 2019-02-02T20:00:00.000+0000 """

    from_version = fields.Str(
        data_key="from_version",
    )
    r""" Previous version of node

Example: ONTAP_X1 """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the software_history. """

    start_time = fields.DateTime(
        data_key="start_time",
    )
    r""" Start time of this installation request.

Example: 2019-02-02T19:00:00.000+0000 """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['successful', 'canceled']),
    )
    r""" Status of this installation request.

Valid choices:

* successful
* canceled """

    to_version = fields.Str(
        data_key="to_version",
    )
    r""" Updated version of node

Example: ONTAP_X2 """

    @property
    def resource(self):
        return SoftwareHistory

    @property
    def patchable_fields(self):
        return [
            "node.name",
            "node.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "node.name",
            "node.uuid",
        ]

class SoftwareHistory(Resource):
    """Allows interaction with SoftwareHistory objects on the host"""

    _schema = SoftwareHistorySchema
    _path = "/api/cluster/software/history"

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
        r"""Retrieves the history details for software installation requests.
### Related ONTAP commands
* `cluster image show-update-history`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the history details for software installation requests.
### Related ONTAP commands
* `cluster image show-update-history`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member






