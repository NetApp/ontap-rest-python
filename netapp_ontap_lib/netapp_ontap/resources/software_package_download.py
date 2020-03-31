# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SoftwarePackageDownload", "SoftwarePackageDownloadSchema"]
__pdoc__ = {
    "SoftwarePackageDownloadSchema.resource": False,
    "SoftwarePackageDownloadSchema.patchable_fields": False,
    "SoftwarePackageDownloadSchema.postable_fields": False,
}


class SoftwarePackageDownloadSchema(ResourceSchema):
    """The fields of the SoftwarePackageDownload object"""

    password = fields.Str(
        data_key="password",
    )
    r""" Password for download

Example: admin_password """

    url = fields.Str(
        data_key="url",
    )
    r""" HTTP or FTP URL of the package through a server

Example: http://server/package """

    username = fields.Str(
        data_key="username",
    )
    r""" Username for download

Example: admin """

    @property
    def resource(self):
        return SoftwarePackageDownload

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "password",
            "url",
            "username",
        ]

class SoftwarePackageDownload(Resource):
    """Allows interaction with SoftwarePackageDownload objects on the host"""

    _schema = SoftwarePackageDownloadSchema
    _path = "/api/cluster/software/download"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the software download status.
### Related ONTAP commands
* `cluster image package check-download-progress`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
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
        r"""Downloads a software package from the server.
### Required properties
* `url` - URL location of the software package
### Recommended optional parameters
* `username` - Username of HTTPS/FTP server
* `password` - Password of HTTPS/FTP server
### Related ONTAP commands
* `cluster image package get`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member




