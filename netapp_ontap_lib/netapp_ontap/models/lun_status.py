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


__all__ = ["LunStatus", "LunStatusSchema"]
__pdoc__ = {
    "LunStatusSchema.resource": False,
    "LunStatus": False,
}


class LunStatusSchema(ResourceSchema):
    """The fields of the LunStatus object"""

    container_state = fields.Str(data_key="container_state")
    r""" The state of the volume and aggregate that contain the LUN. LUNs are only available when their containers are available.


Valid choices:

* online
* aggregate_offline
* volume_offline """

    mapped = fields.Boolean(data_key="mapped")
    r""" Reports if the LUN is mapped to one or more initiator groups.<br/>
There is an added cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more. """

    read_only = fields.Boolean(data_key="read_only")
    r""" Reports if the LUN allows only read access. """

    state = fields.Str(data_key="state")
    r""" The state of the LUN. Normal states for a LUN are _online_ and _offline_. Other states indicate errors.


Valid choices:

* foreign_lun_error
* nvfail
* offline
* online
* space_error """

    @property
    def resource(self):
        return LunStatus

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class LunStatus(Resource):  # pylint: disable=missing-docstring

    _schema = LunStatusSchema
