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


__all__ = ["ZappNvmeComponentsSubsystem", "ZappNvmeComponentsSubsystemSchema"]
__pdoc__ = {
    "ZappNvmeComponentsSubsystemSchema.resource": False,
    "ZappNvmeComponentsSubsystem": False,
}


class ZappNvmeComponentsSubsystemSchema(ResourceSchema):
    """The fields of the ZappNvmeComponentsSubsystem object"""

    hosts = fields.List(fields.Nested("netapp_ontap.models.zapp_nvme_components_subsystem_hosts.ZappNvmeComponentsSubsystemHostsSchema", unknown=EXCLUDE), data_key="hosts")
    r""" The hosts field of the zapp_nvme_components_subsystem. """

    name = fields.Str(data_key="name")
    r""" The name of the subsystem accessing the component. If neither the name nor the UUID is provided, the name defaults to &lt;application-name&gt;_&lt;component-name&gt;, whether that subsystem already exists or not. """

    os_type = fields.Str(data_key="os_type")
    r""" The name of the host OS accessing the component. The default value is the host OS that is running the application.

Valid choices:

* linux
* vmware
* windows """

    uuid = fields.Str(data_key="uuid")
    r""" The UUID of an existing subsystem to be granted access to the component. Usage: &lt;UUID&gt; """

    @property
    def resource(self):
        return ZappNvmeComponentsSubsystem

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "hosts",
            "name",
            "os_type",
            "uuid",
        ]


class ZappNvmeComponentsSubsystem(Resource):  # pylint: disable=missing-docstring

    _schema = ZappNvmeComponentsSubsystemSchema
