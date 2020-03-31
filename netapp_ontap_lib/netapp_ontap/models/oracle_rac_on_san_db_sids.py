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


__all__ = ["OracleRacOnSanDbSids", "OracleRacOnSanDbSidsSchema"]
__pdoc__ = {
    "OracleRacOnSanDbSidsSchema.resource": False,
    "OracleRacOnSanDbSids": False,
}


class OracleRacOnSanDbSidsSchema(ResourceSchema):
    """The fields of the OracleRacOnSanDbSids object"""

    igroup_name = fields.Str(data_key="igroup_name")
    r""" The name of the initiator group through which the contents of this application will be accessed. Modification of this parameter is a disruptive operation. All LUNs in the application component will be unmapped from the current igroup and re-mapped to the new igroup. """

    @property
    def resource(self):
        return OracleRacOnSanDbSids

    @property
    def patchable_fields(self):
        return [
            "igroup_name",
        ]

    @property
    def postable_fields(self):
        return [
            "igroup_name",
        ]


class OracleRacOnSanDbSids(Resource):  # pylint: disable=missing-docstring

    _schema = OracleRacOnSanDbSidsSchema
