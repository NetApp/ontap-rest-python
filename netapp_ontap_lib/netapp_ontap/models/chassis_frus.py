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


__all__ = ["ChassisFrus", "ChassisFrusSchema"]
__pdoc__ = {
    "ChassisFrusSchema.resource": False,
    "ChassisFrus": False,
}


class ChassisFrusSchema(ResourceSchema):
    """The fields of the ChassisFrus object"""

    id = fields.Str(data_key="id")
    r""" The id field of the chassis_frus. """

    state = fields.Str(data_key="state")
    r""" The state field of the chassis_frus.

Valid choices:

* ok
* error """

    type = fields.Str(data_key="type")
    r""" The type field of the chassis_frus.

Valid choices:

* fan
* psu """

    @property
    def resource(self):
        return ChassisFrus

    @property
    def patchable_fields(self):
        return [
            "id",
            "state",
            "type",
        ]

    @property
    def postable_fields(self):
        return [
            "id",
            "state",
            "type",
        ]


class ChassisFrus(Resource):  # pylint: disable=missing-docstring

    _schema = ChassisFrusSchema
