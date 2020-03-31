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


__all__ = ["ApplicationStatisticsSpace", "ApplicationStatisticsSpaceSchema"]
__pdoc__ = {
    "ApplicationStatisticsSpaceSchema.resource": False,
    "ApplicationStatisticsSpace": False,
}


class ApplicationStatisticsSpaceSchema(ResourceSchema):
    """The fields of the ApplicationStatisticsSpace object"""

    available = fields.Integer(data_key="available")
    r""" The available amount of space left in the application component. Note that this field has limited meaning for SAN applications. Space may be considered used from ONTAP's perspective while the host filesystem still considers it available. """

    logical_used = fields.Integer(data_key="logical_used")
    r""" The amount of space that would currently be used if no space saving features were enabled. For example, if compression were the only space saving feature enabled, this field would represent the uncompressed amount of space used. """

    provisioned = fields.Integer(data_key="provisioned")
    r""" The originally requested amount of space that was provisioned for the application component. """

    reserved_unused = fields.Integer(data_key="reserved_unused")
    r""" The amount of space reserved for system features such as Snapshot copies that has not yet been used. """

    savings = fields.Integer(data_key="savings")
    r""" The amount of space saved by all enabled space saving features. """

    used = fields.Integer(data_key="used")
    r""" The amount of space that is currently being used by the application component. Note that this includes any space reserved by the system for features such as Snapshot copies. """

    used_excluding_reserves = fields.Integer(data_key="used_excluding_reserves")
    r""" The amount of space that is currently being used, excluding any space that is reserved by the system for features such as Snapshot copies. """

    used_percent = fields.Integer(data_key="used_percent")
    r""" The percentage of the originally provisioned space that is currently being used by the application component. """

    @property
    def resource(self):
        return ApplicationStatisticsSpace

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class ApplicationStatisticsSpace(Resource):  # pylint: disable=missing-docstring

    _schema = ApplicationStatisticsSpaceSchema
