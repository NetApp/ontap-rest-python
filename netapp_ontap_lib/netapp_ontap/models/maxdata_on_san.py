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


__all__ = ["MaxdataOnSan", "MaxdataOnSanSchema"]
__pdoc__ = {
    "MaxdataOnSanSchema.resource": False,
    "MaxdataOnSan": False,
}


class MaxdataOnSanSchema(ResourceSchema):
    """The fields of the MaxdataOnSan object"""

    app_type = fields.Str(data_key="app_type")
    r""" Type of the application that is being deployed on the L2.

Valid choices:

* mongodb
* oracle
* san """

    application_components = fields.List(fields.Nested("netapp_ontap.models.maxdata_on_san_application_components.MaxdataOnSanApplicationComponentsSchema", unknown=EXCLUDE), data_key="application_components")
    r""" The list of application components to be created. """

    metadata = fields.List(fields.Nested("netapp_ontap.models.maxdata_on_san_metadata.MaxdataOnSanMetadataSchema", unknown=EXCLUDE), data_key="metadata")
    r""" The metadata field of the maxdata_on_san. """

    new_igroups = fields.List(fields.Nested("netapp_ontap.models.maxdata_on_san_new_igroups.MaxdataOnSanNewIgroupsSchema", unknown=EXCLUDE), data_key="new_igroups")
    r""" The list of initiator groups to create. """

    ocsm_url = fields.Str(data_key="ocsm_url")
    r""" The OnCommand System Manager URL for this application. """

    os_type = fields.Str(data_key="os_type")
    r""" The name of the host OS running the application.

Valid choices:

* aix
* hpux
* hyper_v
* linux
* netware
* openvms
* solaris
* solaris_efi
* vmware
* windows
* windows_2008
* windows_gpt
* xen """

    @property
    def resource(self):
        return MaxdataOnSan

    @property
    def patchable_fields(self):
        return [
            "application_components",
            "new_igroups",
        ]

    @property
    def postable_fields(self):
        return [
            "app_type",
            "application_components",
            "metadata",
            "new_igroups",
            "os_type",
        ]


class MaxdataOnSan(Resource):  # pylint: disable=missing-docstring

    _schema = MaxdataOnSanSchema
