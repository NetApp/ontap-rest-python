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


__all__ = ["LunLunMaps", "LunLunMapsSchema"]
__pdoc__ = {
    "LunLunMapsSchema.resource": False,
    "LunLunMaps": False,
}


class LunLunMapsSchema(ResourceSchema):
    """The fields of the LunLunMaps object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the lun_lun_maps. """

    igroup = fields.Nested("netapp_ontap.models.lun_igroup.LunIgroupSchema", unknown=EXCLUDE, data_key="igroup")
    r""" The igroup field of the lun_lun_maps. """

    logical_unit_number = fields.Integer(data_key="logical_unit_number")
    r""" The logical unit number assigned to the LUN for initiators in the initiator group. """

    @property
    def resource(self):
        return LunLunMaps

    @property
    def patchable_fields(self):
        return [
            "igroup",
        ]

    @property
    def postable_fields(self):
        return [
            "igroup",
        ]


class LunLunMaps(Resource):  # pylint: disable=missing-docstring

    _schema = LunLunMapsSchema
