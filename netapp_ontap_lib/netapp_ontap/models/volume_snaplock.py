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


__all__ = ["VolumeSnaplock", "VolumeSnaplockSchema"]
__pdoc__ = {
    "VolumeSnaplockSchema.resource": False,
    "VolumeSnaplock": False,
}


class VolumeSnaplockSchema(ResourceSchema):
    """The fields of the VolumeSnaplock object"""

    append_mode_enabled = fields.Boolean(data_key="append_mode_enabled")
    r""" Specifies if the volume append mode is enabled or disabled. When it is enabled, all the files created with write permissions on the volume are, by default, WORM appendable files. The user can append the data to a WORM appendable file but cannot modify the existing contents of the file nor delete the file until it expires.

Example: false """

    autocommit_period = fields.Str(data_key="autocommit_period")
    r""" Specifies the autocommit period for SnapLock volume. All files which are not modified for a period greater than the autocommit period of the volume are committed to the WORM state. The autocommit period value represents a duration and must be specified in the ISO-8601 duration format. The autocommit period can be in years, months, days, hours, and minutes. A period specified for years, months, and days is represented in the ISO-8601 format as "P<num>Y", "P<num>M", "P<num>D" respectively, for example "P10Y" represents a duration of 10 years. A duration in hours and minutes is represented by "PT<num>H" and "PT<num>M" respectively. The period string must contain only a single time element that is, either years, months, days, hours, or minutes. A duration which combines different periods is not supported, for example "P1Y10M" is not supported. Apart from the duration specified in the ISO-8601 format, the autocommit field also accepts the string "none".

Example: P30M """

    compliance_clock_time = fields.DateTime(data_key="compliance_clock_time")
    r""" This is the volume compliance clock time which is used to manage the SnapLock objects in the volume.

Example: 2018-06-04T19:00:00.000+0000 """

    expiry_time = fields.DateTime(data_key="expiry_time")
    r""" Expiry time of the volume.

Example: Wed Sep  5 11:02:42 GMT 2018 """

    is_audit_log = fields.Boolean(data_key="is_audit_log")
    r""" Indicates if this volume has been configured as SnapLock audit log volume for the SVM .

Example: true """

    litigation_count = fields.Integer(data_key="litigation_count")
    r""" Litigation count indicates the number of active legal-holds on the volume.

Example: 10 """

    privileged_delete = fields.Str(data_key="privileged_delete")
    r""" Specifies the privileged-delete attribute of a SnapLock volume. On a SnapLock Enterprise (SLE) volume, a designated privileged user can selectively delete files irrespective of the retention time of the file. SLE volumes can have privileged delete as disabled, enabled or permanently_disabled and for SnapLock Compliance (SLC) volumes it is always permanently_disabled.

Valid choices:

* disabled
* enabled
* permanently_disabled """

    retention = fields.Nested("netapp_ontap.models.volume_snaplock_retention.VolumeSnaplockRetentionSchema", unknown=EXCLUDE, data_key="retention")
    r""" The retention field of the volume_snaplock. """

    type = fields.Str(data_key="type")
    r""" The SnapLock type of the volume. <br>compliance &dash; A SnapLock Compliance(SLC) volume provides the highest level of WORM protection and an administrator cannot destroy a SLC volume if it contains unexpired WORM files. <br> enterprise &dash; An administrator can delete a SnapLock Enterprise(SLE) volume.<br> non_snaplock &dash; Indicates the volume is non-snaplock.

Valid choices:

* compliance
* enterprise
* non_snaplock """

    @property
    def resource(self):
        return VolumeSnaplock

    @property
    def patchable_fields(self):
        return [
            "append_mode_enabled",
            "autocommit_period",
            "privileged_delete",
            "retention",
        ]

    @property
    def postable_fields(self):
        return [
            "append_mode_enabled",
            "autocommit_period",
            "privileged_delete",
            "retention",
        ]


class VolumeSnaplock(Resource):  # pylint: disable=missing-docstring

    _schema = VolumeSnaplockSchema
