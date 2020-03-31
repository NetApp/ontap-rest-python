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


__all__ = ["ApplicationStatisticsIops1", "ApplicationStatisticsIops1Schema"]
__pdoc__ = {
    "ApplicationStatisticsIops1Schema.resource": False,
    "ApplicationStatisticsIops1": False,
}


class ApplicationStatisticsIops1Schema(ResourceSchema):
    """The fields of the ApplicationStatisticsIops1 object"""

    per_tb = fields.Integer(data_key="per_tb")
    r""" The number of IOPS per terabyte of logical space currently being used by the application. """

    total = fields.Integer(data_key="total")
    r""" The total number of IOPS being used by the application. """

    @property
    def resource(self):
        return ApplicationStatisticsIops1

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationStatisticsIops1(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationStatisticsIops1Schema
