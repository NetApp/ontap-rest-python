# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema


__all__ = ["ApplicationStatisticsLatency", "ApplicationStatisticsLatencySchema"]
__pdoc__ = {
    "ApplicationStatisticsLatencySchema.resource": False,
    "ApplicationStatisticsLatency": False,
}


class ApplicationStatisticsLatencySchema(ResourceSchema):
    """The fields of the ApplicationStatisticsLatency object"""

    average = fields.Integer(data_key="average")
    r""" The cumulative average response time in microseconds for this component. """

    raw = fields.Integer(data_key="raw")
    r""" The cumulative response time in microseconds for this component. """

    @property
    def resource(self):
        return ApplicationStatisticsLatency

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationStatisticsLatency(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationStatisticsLatencySchema
