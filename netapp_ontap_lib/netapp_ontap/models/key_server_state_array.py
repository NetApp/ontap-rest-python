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


__all__ = ["KeyServerStateArray", "KeyServerStateArraySchema"]
__pdoc__ = {
    "KeyServerStateArraySchema.resource": False,
    "KeyServerStateArray": False,
}


class KeyServerStateArraySchema(ResourceSchema):
    """The fields of the KeyServerStateArray object"""

    cluster_availability = fields.Boolean(data_key="cluster_availability")
    r""" Set to true when key server connectivity state is available on all nodes of the cluster. """

    records = fields.List(fields.Nested("netapp_ontap.models.key_server_state.KeyServerStateSchema", unknown=EXCLUDE), data_key="records")
    r""" An array of key server connectivity states for each node. """

    @property
    def resource(self):
        return KeyServerStateArray

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class KeyServerStateArray(Resource):  # pylint: disable=missing-docstring

    _schema = KeyServerStateArraySchema
