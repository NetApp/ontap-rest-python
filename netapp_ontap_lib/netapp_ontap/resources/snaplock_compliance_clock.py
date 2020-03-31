# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

This API manages the ComplianceClock of the system. ComplianceClock determines the expiry time of the SnapLock objects in the system. The user can initialize the ComplianceClock once and when it is set, it cannot be changed by the user. ComplianceClock initialize is not supported in REST.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnaplockComplianceClock", "SnaplockComplianceClockSchema"]
__pdoc__ = {
    "SnaplockComplianceClockSchema.resource": False,
    "SnaplockComplianceClockSchema.patchable_fields": False,
    "SnaplockComplianceClockSchema.postable_fields": False,
}


class SnaplockComplianceClockSchema(ResourceSchema):
    """The fields of the SnaplockComplianceClock object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snaplock_compliance_clock. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the snaplock_compliance_clock. """

    time = fields.DateTime(
        data_key="time",
    )
    r""" Compliance clock time

Example: 2018-06-04T19:00:00.000+0000 """

    @property
    def resource(self):
        return SnaplockComplianceClock

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "node.name",
            "node.uuid",
        ]

class SnaplockComplianceClock(Resource):
    """Allows interaction with SnaplockComplianceClock objects on the host"""

    _schema = SnaplockComplianceClockSchema
    _path = "/api/storage/snaplock/compliance-clocks"
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
        r"""Retrieves the SnapLock ComplianceClock for all of the nodes in the cluster.
### Related ONTAP commands
* `snaplock compliance-clock show`
### Learn more
* [`DOC /storage/snaplock/compliance-clocks`](#docs-snaplock-storage_snaplock_compliance-clocks)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the SnapLock ComplianceClock for all of the nodes in the cluster.
### Related ONTAP commands
* `snaplock compliance-clock show`
### Learn more
* [`DOC /storage/snaplock/compliance-clocks`](#docs-snaplock-storage_snaplock_compliance-clocks)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the SnapLock ComplianceClock for a specific node.
### Related ONTAP commands
* `snaplock compliance-clock show`
### Learn more
* [`DOC /storage/snaplock/compliance-clocks`](#docs-snaplock-storage_snaplock_compliance-clocks)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





