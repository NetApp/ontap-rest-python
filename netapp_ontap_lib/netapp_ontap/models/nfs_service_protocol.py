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


__all__ = ["NfsServiceProtocol", "NfsServiceProtocolSchema"]
__pdoc__ = {
    "NfsServiceProtocolSchema.resource": False,
    "NfsServiceProtocol": False,
}


class NfsServiceProtocolSchema(ResourceSchema):
    """The fields of the NfsServiceProtocol object"""

    v3_enabled = fields.Boolean(data_key="v3_enabled")
    r""" Specifies whether NFSv3 protocol is enabled. """

    v40_enabled = fields.Boolean(data_key="v40_enabled")
    r""" Specifies whether NFSv4.0 protocol is enabled. """

    v40_features = fields.Nested("netapp_ontap.models.nfs_service_protocol_v40_features.NfsServiceProtocolV40FeaturesSchema", unknown=EXCLUDE, data_key="v40_features")
    r""" The v40_features field of the nfs_service_protocol. """

    v41_enabled = fields.Boolean(data_key="v41_enabled")
    r""" Specifies whether NFSv4.1 protocol is enabled. """

    v41_features = fields.Nested("netapp_ontap.models.nfs_service_protocol_v41_features.NfsServiceProtocolV41FeaturesSchema", unknown=EXCLUDE, data_key="v41_features")
    r""" The v41_features field of the nfs_service_protocol. """

    v4_id_domain = fields.Str(data_key="v4_id_domain")
    r""" Specifies the domain portion of the string form of user and group
names as defined by the NFSv4 protocol. """

    @property
    def resource(self):
        return NfsServiceProtocol

    @property
    def patchable_fields(self):
        return [
            "v3_enabled",
            "v40_enabled",
            "v40_features",
            "v41_enabled",
            "v41_features",
            "v4_id_domain",
        ]

    @property
    def postable_fields(self):
        return [
            "v3_enabled",
            "v40_enabled",
            "v40_features",
            "v41_enabled",
            "v41_features",
            "v4_id_domain",
        ]


class NfsServiceProtocol(Resource):  # pylint: disable=missing-docstring

    _schema = NfsServiceProtocolSchema
