# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
A worldwide port name (WWPN) is a unique 64-bit identifier for a Fibre Channel (FC) initiator. It is displayed as a 16-character hexadecimal value. SAN administrators might find it easier to identify FC initiators using an alias, especially in larger SANs.<br/>
The WWPN alias REST API allows you to create, delete, and discover aliases for WWPNs.<br/>
Multiple aliases can be created for a WWPN, but you cannot use the same alias for multiple WWPNs.<br/>
An alias can consist of up to 32 characters. Valid characters are:

* A through Z
* a through z
* numbers 0 through 9
* hyphen ("-")
* underscore ("_")
* left and right braces ("{", "}")
* period (".")
## Examples
### Creating a WWPN alias
```
# The API:
POST /api/network/fc/wwpn-aliases
# The call:
curl -X POST "https://<mgmt-ip>/api/network/fc/wwpn-aliases" -H "accept: application/json" -d '{ "svm": { "name": "svm1" }, "wwpn": "50:0a:09:82:b4:30:25:05", "alias": "alias3" }'
```
### Retrieving all properties of all WWPN aliases
The `fields` query parameter is used to request that all properties be returned.
<br/>
```
# The API:
GET /api/network/fc/wwpn-aliases
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/wwpn-aliases?fields=*" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "68589d3d-7efa-11e8-9eed-005056b43025",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/68589d3d-7efa-11e8-9eed-005056b43025"
          }
        }
      },
      "alias": "alias1",
      "wwpn": "20:00:00:50:56:b4:30:25",
      "_links": {
        "self": {
          "href": "/api/network/fc/wwpn-aliases/68589d3d-7efa-11e8-9eed-005056b43025/alias1"
        }
      }
    },
    {
      "svm": {
        "uuid": "68589d3d-7efa-11e8-9eed-005056b43025",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/68589d3d-7efa-11e8-9eed-005056b43025"
          }
        }
      },
      "alias": "alias2",
      "wwpn": "50:0a:09:82:b4:30:25:00",
      "_links": {
        "self": {
          "href": "/api/network/fc/wwpn-aliases/68589d3d-7efa-11e8-9eed-005056b43025/alias2"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/network/fc/wwpn-aliases"
    }
  }
}
```
---
### Retrieving all WWPN aliases named "alias1"
The `alias` query parameter is used to specify a query for the value "alias1".
<br/>
```
# The API:
GET /api/network/fc/wwpn-aliases
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/wwpn-aliases?alias=alias1" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "68589d3d-7efa-11e8-9eed-005056b43025",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/68589d3d-7efa-11e8-9eed-005056b43025"
          }
        }
      },
      "alias": "alias1",
      "wwpn": "20:00:00:50:56:b4:30:25",
      "_links": {
        "self": {
          "href": "/api/network/fc/wwpn-aliases/68589d3d-7efa-11e8-9eed-005056b43025/alias1"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/network/fc/wwpn-aliases?alias=alias1"
    }
  }
}
```
---
### Retrieving a specific WWPN alias
The alias to be returned is identified by the UUID of its SVM and the alias name.
<br/>
```
# The API:
GET /api/network/fc/wwpn-aliases/{svm.uuid}/{alias}
# The call:
curl -X GET "https://<mgmt-ip>/api/network/fc/wwpn-aliases/68589d3d-7efa-11e8-9eed-005056b43025/alias2" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "68589d3d-7efa-11e8-9eed-005056b43025",
        "name": "svm1",
        "_links": {
          "self": {
            "href": "/api/svm/svms/68589d3d-7efa-11e8-9eed-005056b43025"
          }
        }
      },
      "alias": "alias2",
      "wwpn": "50:0a:09:82:b4:30:25:00",
      "_links": {
        "self": {
          "href": "/api/network/fc/wwpn-aliases/68589d3d-7efa-11e8-9eed-005056b43025/alias1"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/network/fc/wwpn-aliases?alias=alias1"
    }
  }
}
```
---
### Deleting a WWPN alias
The alias to delete is identified by the UUID of its SVM and the alias name.
<br/>
```
# The API:
DELETE /api/network/fc/wwpn-aliases/{svm.uuid}/{alias}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/network/fc/wwpn-aliases/68589d3d-7efa-11e8-9eed-005056b43025/alias2" -H "accept: application/hal+json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["WwpnAlias", "WwpnAliasSchema"]
__pdoc__ = {
    "WwpnAliasSchema.resource": False,
    "WwpnAliasSchema.patchable_fields": False,
    "WwpnAliasSchema.postable_fields": False,
}


class WwpnAliasSchema(ResourceSchema):
    """The fields of the WwpnAlias object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the wwpn_alias. """

    alias = fields.Str(
        data_key="alias",
    )
    r""" The FC WWPN alias. Required in POST.


Example: host1 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the wwpn_alias. """

    wwpn = fields.Str(
        data_key="wwpn",
    )
    r""" The FC initiator WWPN. Required in POST.


Example: 2f:a0:00:a0:98:0b:56:13 """

    @property
    def resource(self):
        return WwpnAlias

    @property
    def patchable_fields(self):
        return [
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "alias",
            "svm.name",
            "svm.uuid",
            "wwpn",
        ]

class WwpnAlias(Resource):
    r""" A Fibre Channel (FC) world wide port name (WWPN) alias. A WWPN is a unique 64-bit identifier for an FC initiator. It is displayed as a 16-character hexadecimal value. SAN administrators may find it easier to identify FC initiators using an alias, especially in larger SANs. """

    _schema = WwpnAliasSchema
    _path = "/api/network/fc/wwpn-aliases"
    @property
    def _keys(self):
        return ["svm.uuid", "alias"]

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
        r"""Retrieves FC WWPN aliases.
### Related ONTAP commands
* `vserver fcp wwpn-alias show`
### Learn more
* [`DOC /network/fc/wwpn-aliases`](#docs-SAN-network_fc_wwpn-aliases)
"""
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
        r"""Deletes an FC WWPN alias.
### Related ONTAP commands
* `vserver fcp wwpn-alias remove`
### Learn more
* [`DOC /network/fc/wwpn-aliases`](#docs-SAN-network_fc_wwpn-aliases)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves FC WWPN aliases.
### Related ONTAP commands
* `vserver fcp wwpn-alias show`
### Learn more
* [`DOC /network/fc/wwpn-aliases`](#docs-SAN-network_fc_wwpn-aliases)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an FC WWPN alias.
### Related ONTAP commands
* `vserver fcp wwpn-alias show`
### Learn more
* [`DOC /network/fc/wwpn-aliases`](#docs-SAN-network_fc_wwpn-aliases)
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
        r"""Creates an FC WWPN alias.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the FC alias.
* `alias` - Name of the FC alias.
* `wwpn` - FC WWPN for which to create the alias.
### Related ONTAP commands
* `vserver fcp wwpn-alias set`
### Learn more
* [`DOC /network/fc/wwpn-aliases`](#docs-SAN-network_fc_wwpn-aliases)
"""
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
        r"""Deletes an FC WWPN alias.
### Related ONTAP commands
* `vserver fcp wwpn-alias remove`
### Learn more
* [`DOC /network/fc/wwpn-aliases`](#docs-SAN-network_fc_wwpn-aliases)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


