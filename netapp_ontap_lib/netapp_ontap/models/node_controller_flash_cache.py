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


__all__ = ["NodeControllerFlashCache", "NodeControllerFlashCacheSchema"]
__pdoc__ = {
    "NodeControllerFlashCacheSchema.resource": False,
    "NodeControllerFlashCache": False,
}


class NodeControllerFlashCacheSchema(ResourceSchema):
    """The fields of the NodeControllerFlashCache object"""

    capacity = fields.Integer(data_key="capacity")
    r""" Size in bytes

Example: 1024000000000 """

    firmware_version = fields.Str(data_key="firmware_version")
    r""" The firmware_version field of the node_controller_flash_cache.

Example: NA05 """

    hardware_revision = fields.Str(data_key="hardware_revision")
    r""" The hardware_revision field of the node_controller_flash_cache.

Example: A1 """

    model = fields.Str(data_key="model")
    r""" The model field of the node_controller_flash_cache.

Example: X1970A """

    part_number = fields.Str(data_key="part_number")
    r""" The part_number field of the node_controller_flash_cache.

Example: 119-00207 """

    serial_number = fields.Str(data_key="serial_number")
    r""" The serial_number field of the node_controller_flash_cache.

Example: A22P5061550000187 """

    slot = fields.Str(data_key="slot")
    r""" The slot field of the node_controller_flash_cache.

Example: 6-1 """

    state = fields.Str(data_key="state")
    r""" The state field of the node_controller_flash_cache.

Valid choices:

* ok
* erasing
* erased
* failed
* removed """

    @property
    def resource(self):
        return NodeControllerFlashCache

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class NodeControllerFlashCache(Resource):  # pylint: disable=missing-docstring

    _schema = NodeControllerFlashCacheSchema
