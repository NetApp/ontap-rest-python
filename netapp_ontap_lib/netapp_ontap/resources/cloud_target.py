# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Retrieving a collection of cloud targets
The cloud targets GET API retrieves all cloud targets defined in the cluster.
## Creating cloud targets
The cluster administrator tells ONTAP how to connect to a cloud target. The following pre-requisites must be met before creating an object store configuration in ONTAP.
A valid data bucket or container must be created with the object store provider. This assumes that the user has valid account credentials with the object store provider to access the data bucket.
The ONTAP node must be able to connect to the object store. </br>
This includes:
  - Fast, reliable connectivity to the object store.
  - An inter-cluster LIF (logical interface) must be configured on the cluster. ONTAP verifies connectivity prior to saving this configuration information.
  - If SSL/TLS authentication is required, then valid certificates must be installed.
  - FabricPool license (required for all object stores except SGWS).
## Deleting cloud targets
If a cloud target is used by an aggregate, then the aggregate must be deleted before the cloud target can be deleted.
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["CloudTarget", "CloudTargetSchema"]
__pdoc__ = {
    "CloudTargetSchema.resource": False,
    "CloudTargetSchema.patchable_fields": False,
    "CloudTargetSchema.postable_fields": False,
}


class CloudTargetSchema(ResourceSchema):
    """The fields of the CloudTarget object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cloud_target. """

    access_key = fields.Str(
        data_key="access_key",
    )
    r""" Access key ID for AWS_S3 and other S3 compatible provider types. """

    authentication_type = fields.Str(
        data_key="authentication_type",
        validate=enum_validation(['key', 'cap', 'ec2_iam', 'gcp_sa']),
    )
    r""" Authentication used to access the target. Snapmirror does not yet support CAP. Required in POST.

Valid choices:

* key
* cap
* ec2_iam
* gcp_sa """

    azure_account = fields.Str(
        data_key="azure_account",
    )
    r""" Azure account """

    azure_private_key = fields.Str(
        data_key="azure_private_key",
    )
    r""" Azure access key """

    cap_url = fields.Str(
        data_key="cap_url",
    )
    r""" This parameter is available only when auth-type is CAP. It specifies a full URL of the request to a CAP server for retrieving temporary credentials (access-key, secret-pasword, and session token) for accessing the object store.

Example: https://123.45.67.89:1234/CAP/api/v1/credentials?agency=myagency&mission=mymission&role=myrole """

    certificate_validation_enabled = fields.Boolean(
        data_key="certificate_validation_enabled",
    )
    r""" Is SSL/TLS certificate validation enabled? The default value is true. This can only be modified for SGWS, IBM_COS, and ONTAP_S3 provider types. """

    cluster = fields.Nested("netapp_ontap.models.cloud_target_cluster.CloudTargetClusterSchema", data_key="cluster", unknown=EXCLUDE)
    r""" The cluster field of the cloud_target. """

    container = fields.Str(
        data_key="container",
    )
    r""" Data bucket/container name

Example: bucket1 """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the cloud_target. """

    name = fields.Str(
        data_key="name",
    )
    r""" Cloud target name """

    owner = fields.Str(
        data_key="owner",
        validate=enum_validation(['fabricpool', 'snapmirror']),
    )
    r""" Owner of the target. Allowed values are FabricPool or SnapMirror. A target can be used by only one feature.

Valid choices:

* fabricpool
* snapmirror """

    port = fields.Integer(
        data_key="port",
    )
    r""" Port number of the object store that ONTAP uses when establishing a connection. Required in POST. """

    provider_type = fields.Str(
        data_key="provider_type",
    )
    r""" Type of cloud provider. Allowed values depend on owner type. For FabricPool, AliCloud, AWS_S3, Azure_Cloud, GoggleCloud, IBM_COS, SGWS, and ONTAP_S3 are allowed. For SnapMirror, the valid values are AWS_S3 or SGWS. """

    secret_password = fields.Str(
        data_key="secret_password",
    )
    r""" Secret access key for AWS_S3 and other S3 compatible provider types. """

    server = fields.Str(
        data_key="server",
    )
    r""" Fully qualified domain name of the object store server. Required on POST.  For Amazon S3, server name must be an AWS regional endpoint in the format s3.amazonaws.com or s3-<region>.amazonaws.com, for example, s3-us-west-2.amazonaws.com. The region of the server and the bucket must match. For Azure, if the server is a "blob.core.windows.net" or a "blob.core.usgovcloudapi.net", then a value of azure-account followed by a period is added in front of the server. """

    server_side_encryption = fields.Str(
        data_key="server_side_encryption",
        validate=enum_validation(['none', 'sse_s3']),
    )
    r""" Encryption of data at rest by the object store server for AWS_S3 and other S3 compatible provider types. This is an advanced property. In most cases it is best not to change default value of "sse_s3" for object store servers which support SSE-S3 encryption. The encryption is in addition to any encryption done by ONTAP at a volume or at an aggregate level. Note that changing this option does not change encryption of data which already exist in the object store.

Valid choices:

* none
* sse_s3 """

    snapmirror_use = fields.Str(
        data_key="snapmirror_use",
        validate=enum_validation(['data', 'metadata']),
    )
    r""" Use of the cloud target by SnapMirror.

Valid choices:

* data
* metadata """

    ssl_enabled = fields.Boolean(
        data_key="ssl_enabled",
    )
    r""" SSL/HTTPS enabled or not """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the cloud_target. """

    use_http_proxy = fields.Boolean(
        data_key="use_http_proxy",
    )
    r""" Use HTTP proxy when connecting to the object store. """

    used = fields.Integer(
        data_key="used",
    )
    r""" The amount of cloud space used by all the aggregates attached to the target, in bytes. This field is only populated for FabricPool targets. The value is recalculated once every 5 minutes. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Cloud target UUID """

    @property
    def resource(self):
        return CloudTarget

    @property
    def patchable_fields(self):
        return [
            "access_key",
            "authentication_type",
            "azure_account",
            "azure_private_key",
            "cap_url",
            "certificate_validation_enabled",
            "cluster",
            "name",
            "port",
            "secret_password",
            "server",
            "server_side_encryption",
            "snapmirror_use",
            "ssl_enabled",
            "svm.name",
            "svm.uuid",
            "use_http_proxy",
        ]

    @property
    def postable_fields(self):
        return [
            "access_key",
            "authentication_type",
            "azure_account",
            "azure_private_key",
            "cap_url",
            "certificate_validation_enabled",
            "cluster",
            "container",
            "ipspace.name",
            "ipspace.uuid",
            "name",
            "owner",
            "port",
            "provider_type",
            "secret_password",
            "server",
            "server_side_encryption",
            "snapmirror_use",
            "ssl_enabled",
            "svm.name",
            "svm.uuid",
            "use_http_proxy",
        ]

class CloudTarget(Resource):
    """Allows interaction with CloudTarget objects on the host"""

    _schema = CloudTargetSchema
    _path = "/api/cloud/targets"
    @property
    def _keys(self):
        return ["uuid"]

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves the collection of cloud targets in the cluster.
### Related ONTAP commands
* `storage aggregate object-store config show`

### Learn more
* [`DOC /cloud/targets`](#docs-cloud-cloud_targets)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the cloud target specified by the UUID with the fields in the body. This request starts a job and returns a link to that job.
### Related ONTAP commands
* `storage aggregate object-store config modify`

### Learn more
* [`DOC /cloud/targets`](#docs-cloud-cloud_targets)"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def delete_collection(
        cls,
        *args,
        body: Union[Resource, dict] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes the cloud target specified by the UUID. This request starts a job and returns a link to that job.
### Related ONTAP commands
* `storage aggregate object-store config delete`

### Learn more
* [`DOC /cloud/targets`](#docs-cloud-cloud_targets)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the collection of cloud targets in the cluster.
### Related ONTAP commands
* `storage aggregate object-store config show`

### Learn more
* [`DOC /cloud/targets`](#docs-cloud-cloud_targets)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the cloud target specified by the UUID.
### Related ONTAP commands
* `storage aggregate object-store config show`

### Learn more
* [`DOC /cloud/targets`](#docs-cloud-cloud_targets)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a cloud target.
### Required properties
* `name` - Name for the cloud target.
* `owner` - Owner of the target: _fabricpool_, _snapmirror_.
* `provider_type` - Type of cloud provider: _AWS_S3_, _Azure_Cloud_, _SGWS_, _IBM_COS_, _AliCloud_, _GoogleCloud_, _ONTAP_S3_.
* `server` - Fully qualified domain name of the object store server. Required when `provider_type` is one of the following: _SGWS_, _IBM_COS_, _AliCloud_.
* `container` - Data bucket/container name.
* `access_key` - Access key ID if `provider_type` is not _Azure_Cloud_ and `authentication_type` is _key_.
* `secret_password` - Secret access key if `provider_type` is not _Azure_Cloud_ and `authentication_type` is _key_.
* `azure_account` - Azure account if `provider_type` is _Azure_Cloud_.
* `azure_private_key` - Azure access key if `provider_type` is _Azure_Cloud_.
* `cap_url` - Full URL of the request to a CAP server for retrieving temporary credentials if `authentication_type` is _cap_.
* `svm.name` or `svm.uuid` - Name or UUID of SVM if `owner` is _snapmirror_.
* `snapmirror_use` - Use of the cloud target if `owner` is _snapmirror_: data, metadata.
### Recommended optional properties
* `authentication_type` - Authentication used to access the target: _key_, _cap_, _ec2_iam_, _gcp_sa_.
* `ssl_enabled` - SSL/HTTPS enabled or disabled.
* `port` - Port number of the object store that ONTAP uses when establishing a connection.
* `ipspace` - IPspace to use in order to reach the cloud target.
* `use_http_proxy` - Use the HTTP proxy when connecting to the object store server.
### Default property values
* `authentication_type`
  - _ec2_iam_ - if running in Cloud Volumes ONTAP in AWS
  - _gcp_sa_ - if running in Cloud Volumes ONTAP in GCP
  - _key_  - in all other cases.
* `server`
  - _s3.amazonaws.com_ - if `provider_type` is _AWS_S3_
  - _blob.core.windows.net_ - if `provider_type` is _Azure_Cloud_
  - _storage.googleapis.com_ - if `provider_type` is _GoogleCloud_
* `ssl_enabled` - _true_
* `port`
  - _443_ if `ssl_enabled` is _true_ and `provider_type` is not _SGWS_
  - _8082_ if `ssl_enabled` is _true_ and `provider_type` is _SGWS_
  - _80_ if `ssl_enabled` is _false_ and `provider_type` is not _SGWS_
  - _8084_ if `ssl_enabled` is _false_ and `provider_type` is _SGWS_
* `ipspace` - _Default_
* `certificate_validation_enabled` - _true_
* `ignore_warnings` - _false_
* `check_only` - _false_
* `use_http_proxy` - _false_
* `server_side_encryption`
  - _none_ - if `provider_type` is _ONTAP_S3_
  - _sse_s3_ - if `provider_type` is not _ONTAP_S3_
### Related ONTAP commands
* `storage aggregate object-store config create`

### Learn more
* [`DOC /cloud/targets`](#docs-cloud-cloud_targets)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the cloud target specified by the UUID with the fields in the body. This request starts a job and returns a link to that job.
### Related ONTAP commands
* `storage aggregate object-store config modify`

### Learn more
* [`DOC /cloud/targets`](#docs-cloud-cloud_targets)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes the cloud target specified by the UUID. This request starts a job and returns a link to that job.
### Related ONTAP commands
* `storage aggregate object-store config delete`

### Learn more
* [`DOC /cloud/targets`](#docs-cloud-cloud_targets)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


