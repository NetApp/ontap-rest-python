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


__all__ = ["FcPortSpeed", "FcPortSpeedSchema"]
__pdoc__ = {
    "FcPortSpeedSchema.resource": False,
    "FcPortSpeed": False,
}


class FcPortSpeedSchema(ResourceSchema):
    """The fields of the FcPortSpeed object"""

    configured = fields.Str(data_key="configured")
    r""" The configured speed of the FC port in gigabits per second.


Valid choices:

* 1
* 2
* 4
* 8
* 10
* 16
* 32
* auto """

    maximum = fields.Str(data_key="maximum")
    r""" The maximum speed supported by the FC port in gigabits per second.


Valid choices:

* 1
* 2
* 4
* 8
* 10
* 16
* 32
* auto """

    @property
    def resource(self):
        return FcPortSpeed

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class FcPortSpeed(Resource):  # pylint: disable=missing-docstring

    _schema = FcPortSpeedSchema
