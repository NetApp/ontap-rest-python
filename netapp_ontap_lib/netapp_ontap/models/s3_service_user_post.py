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


__all__ = ["S3ServiceUserPost", "S3ServiceUserPostSchema"]
__pdoc__ = {
    "S3ServiceUserPostSchema.resource": False,
    "S3ServiceUserPost": False,
}


class S3ServiceUserPostSchema(ResourceSchema):
    """The fields of the S3ServiceUserPost object"""

    links = fields.Nested("netapp_ontap.models.collection_links.CollectionLinksSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the s3_service_user_post. """

    access_key = fields.Str(data_key="access_key")
    r""" Specifies the access key for the user.

Example: Pz3SB54G2B_6dsXQPrA5HrTPcf478qoAW6_Xx6qyqZ948AgZ_7YfCf_9nO87YoZmskxx3cq41U2JAH2M3_fs321B4rkzS3a_oC5_8u7D8j_45N8OsBCBPWGD_1d_ccfq """

    name = fields.Str(data_key="name")
    r""" The name of the user.

Example: user-1 """

    secret_key = fields.Str(data_key="secret_key")
    r""" Specifies the secret key for the user.

Example: A20_tDhC_cux2C2BmtL45bXB_a_Q65c_96FsAcOdo14Az8V31jBKDTc0uCL62Bh559gPB8s9rrn0868QrF38_1dsV2u1_9H2tSf3qQ5xp9NT259C6z_GiZQ883Qn63X1 """

    @property
    def resource(self):
        return S3ServiceUserPost

    @property
    def patchable_fields(self):
        return [
            "links",
        ]

    @property
    def postable_fields(self):
        return [
            "links",
        ]


class S3ServiceUserPost(Resource):  # pylint: disable=missing-docstring

    _schema = S3ServiceUserPostSchema
