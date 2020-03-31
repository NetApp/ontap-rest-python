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


__all__ = ["SvmNsswitch", "SvmNsswitchSchema"]
__pdoc__ = {
    "SvmNsswitchSchema.resource": False,
    "SvmNsswitch": False,
}


class SvmNsswitchSchema(ResourceSchema):
    """The fields of the SvmNsswitch object"""

    group = fields.List(fields.Str, data_key="group")
    r""" Group sources """

    hosts = fields.List(fields.Str, data_key="hosts")
    r""" Host sources """

    namemap = fields.List(fields.Str, data_key="namemap")
    r""" NameMap sources """

    netgroup = fields.List(fields.Str, data_key="netgroup")
    r""" NetGroup sources """

    passwd = fields.List(fields.Str, data_key="passwd")
    r""" Password sources """

    @property
    def resource(self):
        return SvmNsswitch

    @property
    def patchable_fields(self):
        return [
            "group",
            "hosts",
            "namemap",
            "netgroup",
            "passwd",
        ]

    @property
    def postable_fields(self):
        return [
            "group",
            "hosts",
            "namemap",
            "netgroup",
            "passwd",
        ]


class SvmNsswitch(Resource):  # pylint: disable=missing-docstring

    _schema = SvmNsswitchSchema
