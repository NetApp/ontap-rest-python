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


__all__ = ["IscsiSessionInitiator", "IscsiSessionInitiatorSchema"]
__pdoc__ = {
    "IscsiSessionInitiatorSchema.resource": False,
    "IscsiSessionInitiator": False,
}


class IscsiSessionInitiatorSchema(ResourceSchema):
    """The fields of the IscsiSessionInitiator object"""

    alias = fields.Str(data_key="alias")
    r""" The initiator alias.


Example: initiator_alias1 """

    name = fields.Str(data_key="name")
    r""" The world wide unique name of the initiator.


Example: iqn.1992-01.example.com:string """

    @property
    def resource(self):
        return IscsiSessionInitiator

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class IscsiSessionInitiator(Resource):  # pylint: disable=missing-docstring

    _schema = IscsiSessionInitiatorSchema
