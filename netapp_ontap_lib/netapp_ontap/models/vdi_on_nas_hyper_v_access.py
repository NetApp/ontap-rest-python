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


__all__ = ["VdiOnNasHyperVAccess", "VdiOnNasHyperVAccessSchema"]
__pdoc__ = {
    "VdiOnNasHyperVAccessSchema.resource": False,
    "VdiOnNasHyperVAccess": False,
}


class VdiOnNasHyperVAccessSchema(ResourceSchema):
    """The fields of the VdiOnNasHyperVAccess object"""

    service_account = fields.Str(data_key="service_account")
    r""" Hyper-V service account. """

    @property
    def resource(self):
        return VdiOnNasHyperVAccess

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "service_account",
        ]


class VdiOnNasHyperVAccess(Resource):  # pylint: disable=missing-docstring

    _schema = VdiOnNasHyperVAccessSchema
