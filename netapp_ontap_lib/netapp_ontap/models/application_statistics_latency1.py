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


__all__ = ["ApplicationStatisticsLatency1", "ApplicationStatisticsLatency1Schema"]
__pdoc__ = {
    "ApplicationStatisticsLatency1Schema.resource": False,
    "ApplicationStatisticsLatency1": False,
}


class ApplicationStatisticsLatency1Schema(ResourceSchema):
    """The fields of the ApplicationStatisticsLatency1 object"""

    average = fields.Integer(data_key="average")
    r""" The cumulative average response time in microseconds for this application. """

    raw = fields.Integer(data_key="raw")
    r""" The cumulative response time in microseconds for this application. """

    @property
    def resource(self):
        return ApplicationStatisticsLatency1

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationStatisticsLatency1(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationStatisticsLatency1Schema
