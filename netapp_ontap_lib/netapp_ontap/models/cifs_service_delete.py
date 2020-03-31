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


__all__ = ["CifsServiceDelete", "CifsServiceDeleteSchema"]
__pdoc__ = {
    "CifsServiceDeleteSchema.resource": False,
    "CifsServiceDelete": False,
}


class CifsServiceDeleteSchema(ResourceSchema):
    """The fields of the CifsServiceDelete object"""

    ad_domain = fields.Nested("netapp_ontap.models.ad_domain.AdDomainSchema", unknown=EXCLUDE, data_key="ad_domain")
    r""" The ad_domain field of the cifs_service_delete. """

    @property
    def resource(self):
        return CifsServiceDelete

    @property
    def patchable_fields(self):
        return [
            "ad_domain",
        ]

    @property
    def postable_fields(self):
        return [
            "ad_domain",
        ]


class CifsServiceDelete(Resource):  # pylint: disable=missing-docstring

    _schema = CifsServiceDeleteSchema
