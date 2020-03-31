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


__all__ = ["NodeHaGivebackFailure", "NodeHaGivebackFailureSchema"]
__pdoc__ = {
    "NodeHaGivebackFailureSchema.resource": False,
    "NodeHaGivebackFailure": False,
}


class NodeHaGivebackFailureSchema(ResourceSchema):
    """The fields of the NodeHaGivebackFailure object"""

    code = fields.Integer(data_key="code")
    r""" Message code

Example: 852126 """

    message = fields.Str(data_key="message")
    r""" Detailed message based on the state.

Example: Failed to initiate giveback. Run the "storage failover show-giveback" command for more information. """

    @property
    def resource(self):
        return NodeHaGivebackFailure

    @property
    def patchable_fields(self):
        return [
            "code",
            "message",
        ]

    @property
    def postable_fields(self):
        return [
            "code",
            "message",
        ]


class NodeHaGivebackFailure(Resource):  # pylint: disable=missing-docstring

    _schema = NodeHaGivebackFailureSchema
