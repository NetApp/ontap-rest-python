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


__all__ = ["SvmSnapmirror", "SvmSnapmirrorSchema"]
__pdoc__ = {
    "SvmSnapmirrorSchema.resource": False,
    "SvmSnapmirror": False,
}


class SvmSnapmirrorSchema(ResourceSchema):
    """The fields of the SvmSnapmirror object"""

    is_protected = fields.Boolean(data_key="is_protected")
    r""" Specifies whether the SVM is a SnapMirror source SVM, using SnapMirror to protect its data. """

    protected_volumes_count = fields.Integer(data_key="protected_volumes_count")
    r""" Specifies the number of SVM DR protected volumes in the SVM. """

    @property
    def resource(self):
        return SvmSnapmirror

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]


class SvmSnapmirror(Resource):  # pylint: disable=missing-docstring

    _schema = SvmSnapmirrorSchema
