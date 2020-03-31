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


__all__ = ["IscsiServiceTarget", "IscsiServiceTargetSchema"]
__pdoc__ = {
    "IscsiServiceTargetSchema.resource": False,
    "IscsiServiceTarget": False,
}


class IscsiServiceTargetSchema(ResourceSchema):
    """The fields of the IscsiServiceTarget object"""

    alias = fields.Str(data_key="alias")
    r""" The iSCSI target alias of the iSCSI service.<br/>
The target alias can contain one (1) to 128 characters and feature any printable character except space (" "). A PATCH request with an empty alias ("") clears the alias.<br/>
Optional in POST and PATCH. In POST, this defaults to the name of the SVM.


Example: svm1 """

    name = fields.Str(data_key="name")
    r""" The iSCSI target name of the iSCSI service. This is generated for the SVM during POST.<br/>
If required, the target name can be modified using the ONTAP command line.


Example: iqn.1992-08.com.netapp:sn.574caf71890911e8a6b7005056b4ea79:vs.2 """

    @property
    def resource(self):
        return IscsiServiceTarget

    @property
    def patchable_fields(self):
        return [
            "alias",
        ]

    @property
    def postable_fields(self):
        return [
            "alias",
        ]


class IscsiServiceTarget(Resource):  # pylint: disable=missing-docstring

    _schema = IscsiServiceTargetSchema
