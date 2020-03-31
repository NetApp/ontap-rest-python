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


__all__ = ["IgroupInitiatorNoRecords", "IgroupInitiatorNoRecordsSchema"]
__pdoc__ = {
    "IgroupInitiatorNoRecordsSchema.resource": False,
    "IgroupInitiatorNoRecords": False,
}


class IgroupInitiatorNoRecordsSchema(ResourceSchema):
    """The fields of the IgroupInitiatorNoRecords object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the igroup_initiator_no_records. """

    igroup = fields.Nested("netapp_ontap.models.igroup_initiator_igroup.IgroupInitiatorIgroupSchema", unknown=EXCLUDE, data_key="igroup")
    r""" The igroup field of the igroup_initiator_no_records. """

    name = fields.Str(data_key="name")
    r""" The FC WWPN, iSCSI IQN, or iSCSI EUI that identifies the host initiator. Valid in POST only and not allowed when the `records` property is used.<br/>
An FC WWPN consist of 16 hexadecimal digits grouped as 8 pairs separated by colons. The format for an iSCSI IQN is _iqn.yyyy-mm.reverse_domain_name:any_. The iSCSI EUI format consists of the _eui._ prefix followed by 16 hexadecimal characters.


Example: iqn.1998-01.com.corp.iscsi:name1 """

    @property
    def resource(self):
        return IgroupInitiatorNoRecords

    @property
    def patchable_fields(self):
        return [
            "igroup",
        ]

    @property
    def postable_fields(self):
        return [
            "igroup",
            "name",
        ]


class IgroupInitiatorNoRecords(Resource):  # pylint: disable=missing-docstring

    _schema = IgroupInitiatorNoRecordsSchema
