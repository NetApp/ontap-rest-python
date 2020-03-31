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


__all__ = ["SnaplockLogVolume", "SnaplockLogVolumeSchema"]
__pdoc__ = {
    "SnaplockLogVolumeSchema.resource": False,
    "SnaplockLogVolume": False,
}


class SnaplockLogVolumeSchema(ResourceSchema):
    """The fields of the SnaplockLogVolume object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the snaplock_log_volume. """

    max_log_size = fields.Integer(data_key="max_log_size")
    r""" Maximum size of log file in bytes

Example: 20971520 """

    retention_period = fields.Str(data_key="retention_period")
    r""" Specifies the default log record retention period. The retention period value represents a duration and must be specified in the ISO-8601 duration format. The retention period can be in years, months, days, hours, minutes and seconds. A period specified for years, months and days is represented in the ISO-8601 format as "P<num>Y", "P<num>M", "P<num>D" respectively. For example "P10Y" represents a duration of 10 years. A duration in hours, minutes and seconds is represented by "PT<num>H", "PT<num>M", and "PT<num>S" respectively. The period string must contain only a single time element i.e. either years, months, days, hours, minutes or seconds. A duration which combines different periods is not supported, example "P1Y10M" is not supported. Apart from the duration specified in the ISO-8601 format, the retention period field also accepts the string "infinite".

Example: P30M """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", unknown=EXCLUDE, data_key="volume")
    r""" The volume field of the snaplock_log_volume. """

    @property
    def resource(self):
        return SnaplockLogVolume

    @property
    def patchable_fields(self):
        return [
            "max_log_size",
            "retention_period",
            "volume.name",
            "volume.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "max_log_size",
            "retention_period",
            "volume.name",
            "volume.uuid",
        ]


class SnaplockLogVolume(Resource):  # pylint: disable=missing-docstring

    _schema = SnaplockLogVolumeSchema
