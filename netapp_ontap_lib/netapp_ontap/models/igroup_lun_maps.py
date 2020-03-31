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


__all__ = ["IgroupLunMaps", "IgroupLunMapsSchema"]
__pdoc__ = {
    "IgroupLunMapsSchema.resource": False,
    "IgroupLunMaps": False,
}


class IgroupLunMapsSchema(ResourceSchema):
    """The fields of the IgroupLunMaps object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the igroup_lun_maps. """

    logical_unit_number = fields.Integer(data_key="logical_unit_number")
    r""" The logical unit number assigned to the LUN for initiators in the initiator group. """

    lun = fields.Nested("netapp_ontap.models.igroup_lun.IgroupLunSchema", unknown=EXCLUDE, data_key="lun")
    r""" The lun field of the igroup_lun_maps. """

    @property
    def resource(self):
        return IgroupLunMaps

    @property
    def patchable_fields(self):
        return [
            "lun",
        ]

    @property
    def postable_fields(self):
        return [
            "lun",
        ]


class IgroupLunMaps(Resource):  # pylint: disable=missing-docstring

    _schema = IgroupLunMapsSchema
