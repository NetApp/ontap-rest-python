# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
ONTAP home directory functionality can be used to create home directories for SMB users on the CIFS server and automatically offer each user a dynamic share to their home directory without creating an individual SMB share for each user.<p/>
The home directory search path is a set of absolute paths from the root of an SVM that directs ONTAP to search for home directories. If there are multiple search paths, ONTAP tries them in the order specified until it finds a valid path. To use the CIFS home directories feature, at least one home directory search path must be added for an SVM. <p/>
## Examples
### Creating a home directory search path
To create a home directory search path, use the following API. Note the <i>return_records=true</i> query parameter used to obtain the newly created entry in the response.
<br/>
```
# The API:
POST /api/protocols/cifs/home-directory/search-paths
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/cifs/home-directory/search-paths?return_records=true" -H "accept: applicaion/json" -H "Content-Type: application/json" -d "{ \"path\": \"/\", \"svm\": { \"name\": \"vs1\", \"uuid\": \"a41fd873-ecf8-11e8-899d-0050568e9333\" }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "a41fd873-ecf8-11e8-899d-0050568e9333",
        "name": "vs1"
      },
    "path": "/"
    }
  ]
}
```
---
### Retrieving the CIFS home directory search paths configuration for all SVMs in the cluster
```
# The API:
GET /protocols/cifs/home-directory/search-paths
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/home-directory/search-paths?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "2d96f9aa-f4ce-11e8-b075-0050568e278e",
        "name": "vs1"
      },
      "index": 1,
      "path": "/"
    },
    {
      "svm": {
        "uuid": "2d96f9aa-f4ce-11e8-b075-0050568e278e",
        "name": "vs1"
      },
        "index": 2,
        "path": "/a"
    },
    {
      "svm": {
        "uuid": "4f23449b-f4ce-11e8-b075-0050568e278e",
        "name": "vs2"
      },
      "index": 1,
      "path": "/"
    },
    {
      "svm": {
        "uuid": "4f23449b-f4ce-11e8-b075-0050568e278e",
        "name": "vs2"
      },
      "index": 2,
      "path": "/1"
    }
  ],
  "num_records": 4
}
```
### Retrieving a specific home directory searchpath configuration for an SVM
The configuration returned is identified by the UUID of its SVM and the index (position) in the list of search paths that is searched to  find a home directory of a user. <br/>
```
# The API:
GET /api/protocols/home-directory/search-paths/{svm.uuid}/{index}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/home-directory/search-paths/2d96f9aa-f4ce-11e8-b075-0050568e278e/2" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "2d96f9aa-f4ce-11e8-b075-0050568e278e",
    "name": "vs1"
  },
  "index": 2,
  "path": "/a"
}
```
### Reordering a specific home drectory search path in the list
An entry in the home directory search path list can be reordered to a new positin by specifying the 'new_index' field. The reordered configuration is identified by the UUID of its SVM and the index. <br/>
```
# The API:
PATCH /api/protocols/cifs/home-directory/search-paths/{svm.uuid}/{index}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/cifs/home-directory/search-paths/2d96f9aa-f4ce-11e8-b075-0050568e278e/2?new_index=1" -H "accept: application/json"
```
### Removing a specific home directory search path for an SVM
The entry being removed is identified by the UUID of its SVM and the index. <br/>
```
# The API:
DELETE /api/protocols/cifs/home-directory/search-paths/{svm.uuid}/{index}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/cifs/home-directory/search-paths/2d96f9aa-f4ce-11e8-b075-0050568e278e/2" -H "accept: application/json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["CifsSearchPath", "CifsSearchPathSchema"]
__pdoc__ = {
    "CifsSearchPathSchema.resource": False,
    "CifsSearchPathSchema.patchable_fields": False,
    "CifsSearchPathSchema.postable_fields": False,
}


class CifsSearchPathSchema(ResourceSchema):
    """The fields of the CifsSearchPath object"""

    index = fields.Integer(
        data_key="index",
    )
    r""" The position in the list of paths that is searched to find the home directory of the CIFS client. Not available in POST. """

    path = fields.Str(
        data_key="path",
    )
    r""" The file system path that is searched to find the home directory of the CIFS client.

Example: /HomeDirectory/EngDomain """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the cifs_search_path. """

    @property
    def resource(self):
        return CifsSearchPath

    @property
    def patchable_fields(self):
        return [
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "path",
            "svm.name",
            "svm.uuid",
        ]

class CifsSearchPath(Resource):
    r""" This is a list of CIFS home directory search paths. When a CIFS client connects to a home directory share, these paths are searched in the order indicated by the position field to find the home directory of the connected CIFS client. """

    _schema = CifsSearchPathSchema
    _path = "/api/protocols/cifs/home-directory/search-paths"
    @property
    def _keys(self):
        return ["svm.uuid", "index"]

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
        r"""Retrieves CIFS home directory search paths.
### Related ONTAP commands
* `cifs server home-directory search-path show`
### Learn more
* [`DOC /protocols/cifs/home-directory/search-paths`](#docs-NAS-protocols_cifs_home-directory_search-paths)
"""
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
        r"""Reorders a CIFS home directory search path.
### Related ONTAP commands
* `cifs server home-directory search-path reorder`
### Learn more
* [`DOC /protocols/cifs/home-directory/search-paths`](#docs-NAS-protocols_cifs_home-directory_search-paths)
"""
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
        r"""Deletes a CIFS home directory search path.
### Related ONTAP commands
* `cifs server home-directory search-path remove`
### Learn more
* [`DOC /protocols/cifs/home-directory/search-paths`](#docs-NAS-protocols_cifs_home-directory_search-paths)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves CIFS home directory search paths.
### Related ONTAP commands
* `cifs server home-directory search-path show`
### Learn more
* [`DOC /protocols/cifs/home-directory/search-paths`](#docs-NAS-protocols_cifs_home-directory_search-paths)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a CIFS home directory search path of an SVM.
### Related ONTAP commands
* `cifs server home-directory search-path show`
### Learn more
* [`DOC /protocols/cifs/home-directory/search-paths`](#docs-NAS-protocols_cifs_home-directory_search-paths)
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
        r"""Creates a home directory search path.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the home directory search path.
* `path` - Path in the owning SVM namespace that is used to search for home directories.
### Related ONTAP commands
* `cifs server home-directory search-path add`
### Learn more
* [`DOC /protocols/cifs/home-directory/search-paths`](#docs-NAS-protocols_cifs_home-directory_search-paths)
"""
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
        r"""Reorders a CIFS home directory search path.
### Related ONTAP commands
* `cifs server home-directory search-path reorder`
### Learn more
* [`DOC /protocols/cifs/home-directory/search-paths`](#docs-NAS-protocols_cifs_home-directory_search-paths)
"""
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
        r"""Deletes a CIFS home directory search path.
### Related ONTAP commands
* `cifs server home-directory search-path remove`
### Learn more
* [`DOC /protocols/cifs/home-directory/search-paths`](#docs-NAS-protocols_cifs_home-directory_search-paths)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


