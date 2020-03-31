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


__all__ = ["FcpServiceTarget", "FcpServiceTargetSchema"]
__pdoc__ = {
    "FcpServiceTargetSchema.resource": False,
    "FcpServiceTarget": False,
}


class FcpServiceTargetSchema(ResourceSchema):
    """The fields of the FcpServiceTarget object"""

    name = fields.Str(data_key="name")
    r""" The target name of the FC Protocol service. This is generated for the SVM during POST.<br/>
The FC Protocol target name is a world wide node name (WWNN).<br/>
If required, the target name can be modified using the ONTAP command line.


Example: 20:00:00:50:56:bb:b2:4b """

    @property
    def resource(self):
        return FcpServiceTarget

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class FcpServiceTarget(Resource):  # pylint: disable=missing-docstring

    _schema = FcpServiceTargetSchema
