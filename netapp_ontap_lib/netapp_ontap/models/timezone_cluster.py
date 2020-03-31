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


__all__ = ["TimezoneCluster", "TimezoneClusterSchema"]
__pdoc__ = {
    "TimezoneClusterSchema.resource": False,
    "TimezoneCluster": False,
}


class TimezoneClusterSchema(ResourceSchema):
    """The fields of the TimezoneCluster object"""

    name = fields.Str(data_key="name")
    r""" The ONTAP time zone name or identification in either IANA time zone format "Area/Location", or an ONTAP traditional time zone.
</br>
The initial first node in cluster setting for time zone is "Etc/UTC".
"Etc/UTC" is the IANA timezone "Area/Location" specifier for
Coordinated Universal Time (UTC), which is an offset of 0.
### IANA time zone format
The IANA time zone, formatted as "Area/Location", is based on geographic areas that have had the same time zone offset for many years.
</br>
"Location" represents a compound name using additional forward slashes.
</br>
An example of the "Area/Location" time zone is "America/New_York" and represents most of the United States Eastern Time Zone.
Examples of "Area/Location" with "Location" as a compound name are "America/Argentina/Buenos_Aires" and "America/Indiana/Indianapolis".
### ONTAP traditional time zone
Examples of the traditional time zones are "EST5EDT" for the United States Eastern Time Zone and "CET" for Central European Time Zone.


Example: America/New_York """

    @property
    def resource(self):
        return TimezoneCluster

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class TimezoneCluster(Resource):  # pylint: disable=missing-docstring

    _schema = TimezoneClusterSchema
