# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Manages a specific instance of a license package.
####
## Examples
### Retrieving information for a specific license package
This example shows how to retrieve information about the specific feature package `fabricpool`.
####
```JSON
# API
GET /cluster/licensing/licenses/fabricpool/
# Response
200 OK
# JSON Body
{
  "name": "fabricpool",
  "scope": "cluster",
  "state": "compliant",
  "licenses": [
  {
    "owner": "testcluster-1",
    "serial_number": "123456789",
    "state": "compliant",
    "capacity": {
    "maximum_size": 109951162777600,
    "used_size": 0
    }
  }
  ],
  "_links": {
  "self": {
    "href": "/api/cluster/licensing/licenses/fabricpool/"
  }
  }
}
```
### Deleting a specific license
This example show how to delete a CIFS site license.
####
```JSON
# API
DELETE /cluster/licensing/licenses/cifs/?serial_number=1-80-000011"
# JSON Body
{}
# Response
200 OK
```
### Deleting with a query
####
The following example shows how to delete all NFS licenses specified with the '*' query.
####
```JSON
# API
DELETE /cluster/licensing/licenses/nfs/?serial_number=*"
# JSON Body
{}
# Response
200 OK
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["LicensePackage", "LicensePackageSchema"]
__pdoc__ = {
    "LicensePackageSchema.resource": False,
    "LicensePackageSchema.patchable_fields": False,
    "LicensePackageSchema.postable_fields": False,
}


class LicensePackageSchema(ResourceSchema):
    """The fields of the LicensePackage object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the license_package. """

    keys = fields.List(fields.Str, data_key="keys")
    r""" The keys field of the license_package. """

    licenses = fields.List(fields.Nested("netapp_ontap.models.license.LicenseSchema", unknown=EXCLUDE), data_key="licenses")
    r""" Installed licenses of the package. """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the license.

Example: NFS """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['not_available', 'site', 'cluster', 'node']),
    )
    r""" Scope of the license.

Valid choices:

* not_available
* site
* cluster
* node """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['compliant', 'noncompliant', 'unlicensed', 'unknown']),
    )
    r""" Summary state of package based on all installed licenses.

Valid choices:

* compliant
* noncompliant
* unlicensed
* unknown """

    @property
    def resource(self):
        return LicensePackage

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "keys",
        ]

class LicensePackage(Resource):
    """Allows interaction with LicensePackage objects on the host"""

    _schema = LicensePackageSchema
    _path = "/api/cluster/licensing/licenses"
    @property
    def _keys(self):
        return ["name"]

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
        r"""Retrieves a collection of license packages.
### Related ONTAP commands
* `system license show-status`
* `system license show`

### Learn more
* [`DOC /cluster/licensing/licenses`](#docs-cluster-cluster_licensing_licenses)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member


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
        r"""Deletes a license.
### Related ONTAP commands
* `system license delete`

### Learn more
* [`DOC /cluster/licensing/licenses/{name}`](#docs-cluster-cluster_licensing_licenses_{name})"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of license packages.
### Related ONTAP commands
* `system license show-status`
* `system license show`

### Learn more
* [`DOC /cluster/licensing/licenses`](#docs-cluster-cluster_licensing_licenses)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific license package.
### Related ONTAP commands
* `system license show`
* `system license show-status`

### Learn more
* [`DOC /cluster/licensing/licenses/{name}`](#docs-cluster-cluster_licensing_licenses_{name})"""
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
        r"""Installs one or more feature licenses.
### Required properties
* `keys` - Array containing a list of NLF or 26-character license keys.
### Related ONTAP commands
* `system license add`

### Learn more
* [`DOC /cluster/licensing/licenses`](#docs-cluster-cluster_licensing_licenses)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member


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
        r"""Deletes a license.
### Related ONTAP commands
* `system license delete`

### Learn more
* [`DOC /cluster/licensing/licenses/{name}`](#docs-cluster-cluster_licensing_licenses_{name})"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


