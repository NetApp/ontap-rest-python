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


__all__ = ["PerformanceMetricIoTypeRwt", "PerformanceMetricIoTypeRwtSchema"]
__pdoc__ = {
    "PerformanceMetricIoTypeRwtSchema.resource": False,
    "PerformanceMetricIoTypeRwt": False,
}


class PerformanceMetricIoTypeRwtSchema(ResourceSchema):
    """The fields of the PerformanceMetricIoTypeRwt object"""

    read = fields.Integer(data_key="read")
    r""" Performance metric for read I/O operations.

Example: 200 """

    total = fields.Integer(data_key="total")
    r""" Performance metric aggregated over all types of I/O operations.

Example: 1000 """

    write = fields.Integer(data_key="write")
    r""" Peformance metric for write I/O operations.

Example: 100 """

    @property
    def resource(self):
        return PerformanceMetricIoTypeRwt

    @property
    def patchable_fields(self):
        return [
            "read",
            "total",
            "write",
        ]

    @property
    def postable_fields(self):
        return [
            "read",
            "total",
            "write",
        ]


class PerformanceMetricIoTypeRwt(Resource):  # pylint: disable=missing-docstring

    _schema = PerformanceMetricIoTypeRwtSchema
