# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Use Vscan to protect data from being compromised by viruses or other malicious code. Vscan combines best-in-class third party antivirus software with ONTAP features that give you the flexibility you need to control which files get scanned and when. Storage systems offload scanning operations to external servers hosting antivirus software from third party vendors. An Antivirus Connector on the external server handles communications between the storage system and the antivirus software.
## Examples
### Retrieving all of the Vscan configurations
```
# The API:
/api/protocols/vscan
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "03ce5c36-f269-11e8-8852-0050568e5298",
        "name": "vs1"
      },
      "enabled": true,
      "scanner_pools": [
        {
          "name": "scanner-1",
          "servers": [
            "1.1.1.1",
            "10.72.204.27"
          ],
          "privileged_users": [
            "cifs\\u1",
            "cifs\\u2"
          ],
          "role": "primary",
          "cluster": {
            "name": "Cluster1",
            "uuid": "0228714d-f268-11e8-8851-0050568e5298"
          }
        },
        {
          "name": "scanner-2",
          "servers": [
            "1.1.1.1",
            "10.72.204.27"
          ],
          "privileged_users": [
            "cifs\\u1",
            "cifs\\u2"
          ],
          "role": "primary",
          "cluster": {
            "name": "Cluster1",
            "uuid": "0228714d-f268-11e8-8851-0050568e5298"
          }
        }
      ],
      "on_access_policies": [
        {
          "name": "default_CIFS",
          "vsName": "vs1",
          "enabled": true,
          "mandatory": true,
          "scope": {
            "max_file_size": 2147483648,
            "include_extensions": [
              "*"
            ],
            "scan_without_extension": true,
            "scan_readonly_volumes": false,
            "only_execute_access": false
          }
        },
        {
          "name": "on-access-test1",
          "vsName": "vs1",
          "enabled": false,
          "mandatory": true,
          "scope": {
            "max_file_size": 10000,
            "exclude_paths": [
              "\dir"
            ],
            "include_extensions": [
              "mp*",
              "txt"
            ],
            "exclude_extensions": [
              "mp*",
              "txt"
            ],
            "scan_without_extension": true,
            "scan_readonly_volumes": false,
            "only_execute_access": false
          }
        },
        {
          "name": "on-access-test2",
          "vsName": "vs1",
          "enabled": false,
          "mandatory": true,
          "scope": {
            "max_file_size": 10000,
            "exclude_paths": [
              "\dir"
            ],
            "include_extensions": [
              "mp*",
              "txt"
            ],
            "exclude_extensions": [
              "mp*",
              "txt"
            ],
            "scan_without_extension": true,
            "scan_readonly_volumes": false,
            "only_execute_access": false
          }
        }
      ],
      "on_demand_policies": [
        {
          "name": "task-1",
          "scan_paths": [
            "/vol1"
          ],
          "log_path": "/vol1",
          "scope": {
            "max_file_size": 10000,
            "exclude_paths": [
              "/vol1"
            ],
            "include_extensions": [
              "vmdk",
              "mp*"
            ],
            "exclude_extensions": [
              "mp3",
              "mp4"
            ],
            "scan_without_extension": true
          }
        },
        {
          "name": "task-2",
          "scan_paths": [
            "/vol1"
          ],
          "log_path": "/vol2",
          "scope": {
            "max_file_size": 10000,
            "exclude_paths": [
              "/vol2"
            ],
            "include_extensions": [
              "vmdk",
              "mp*"
            ],
            "exclude_extensions": [
              "mp3",
              "mp4"
            ],
            "scan_without_extension": true
          }
        }
      ]
    },
    {
      "svm": {
        "uuid": "24c2567a-f269-11e8-8852-0050568e5298",
        "name": "vs2"
      },
      "enabled": false,
      "scanner_pools": [
        {
          "name": "sp2",
          "servers": [
            "1.1.1.1"
          ],
          "privileged_users": [
            "cifs\\u1"
          ],
          "role": "idle"
        }
      ],
      "on_access_policies": [
        {
          "name": "default_CIFS",
          "vsName": "vs2",
          "enabled": true,
          "mandatory": true,
          "scope": {
            "max_file_size": 2147483648,
            "include_extensions": [
              "*"
            ],
            "scan_without_extension": true,
            "scan_readonly_volumes": false,
            "only_execute_access": false
          }
        },
        {
          "name": "ap1",
          "vsName": "vs2",
          "enabled": false,
          "mandatory": true,
          "scope": {
            "max_file_size": 2147483648,
            "include_extensions": [
              "*"
            ],
            "scan_without_extension": true,
            "scan_readonly_volumes": false,
            "only_execute_access": false
          }
        }
      ],
      "on_demand_policies": [
        {
          "name": "t1",
          "scan_paths": [
            "/vol1"
          ],
          "log_path": "/vol1",
          "scope": {
            "max_file_size": 10737418240,
            "include_extensions": [
              "*"
            ],
            "scan_without_extension": true
          }
        }
      ]
    }
  ],
  "num_records": 2
}
```
### Retrieving all Vscan configurations for a particular SVM
```
# The API:
/api/protocols/vscan/{svm.uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/vscan/24c2567a-f269-11e8-8852-0050568e5298?fields=*" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "24c2567a-f269-11e8-8852-0050568e5298",
    "name": "vs2"
  },
  "enabled": false,
  "scanner_pools": [
    {
      "name": "sp2",
      "servers": [
        "1.1.1.1"
      ],
      "privileged_users": [
        "cifs\\u1"
      ],
      "role": "idle"
    }
  ],
  "on_access_policies": [
    {
      "name": "default_CIFS",
      "vsName": "vs2",
      "enabled": true,
      "mandatory": true,
      "scope": {
        "max_file_size": 2147483648,
        "include_extensions": [
          "*"
        ],
        "scan_without_extension": true,
        "scan_readonly_volumes": false,
        "only_execute_access": false
      }
    },
    {
      "name": "ap1",
      "vsName": "vs2",
      "enabled": false,
      "mandatory": true,
      "scope": {
        "max_file_size": 2147483648,
        "include_extensions": [
          "*"
        ],
        "scan_without_extension": true,
        "scan_readonly_volumes": false,
        "only_execute_access": false
      }
    }
  ],
  "on_demand_policies": [
    {
      "name": "t1",
      "scan_paths": [
        "/vol1"
      ],
      "log_path": "/vol1",
      "scope": {
        "max_file_size": 10737418240,
        "include_extensions": [
          "*"
        ],
        "scan_without_extension": true
      }
    }
  ]
}
```
### Creating a Vscan configuration
```
# The API:
/api/protocols/vscan
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan?return_records=true" -H "accept: appication/json" -H "Content-Type: application/json" -d "{ \"enabled\": true, \"on_access_policies\": [ { \"enabled\": true, \"mandatory\": true, \"name\": \"on-access-test\", \"scope\": { \"exclude_extensions\": [ \"mp*\", \"txt\" ], \"exclude_paths\": [ \"\\vol\" ], \"include_extensions\": [ \"mp*\", \"txt\" ], \"max_file_size\": 21474, \"only_execute_access\": false, \"scan_readonly_volumes\": false, \"scan_without_extension\": true } } ], \"on_demand_policies\": [ { \"log_path\": \"/vol\", \"name\": \"task-1\", \"scan_paths\": [ \"/vol\" ], \"schedule\": { \"name\": \"daily\", \"uuid\": \"d4984822-17b7-11e9-b450-0050568ecd85\" }, \"scope\": { \"exclude_extensions\": [ \"mp3\", \"mp4\" ], \"exclude_paths\": [ \"/vol\" ], \"include_extensions\": [ \"vmdk\", \"mp*\" ], \"max_file_size\": 10737, \"scan_without_extension\": true } } ], \"scanner_pools\": [ { \"cluster\": { \"name\": \"Cluster1\", \"uuid\": \"ab746d77-17b7-11e9-b450-0050568ecd85\" }, \"name\": \"scanner-1\", \"privileged_users\": [ \"cifs\\\\u1\", \"cifs\\\\u2\" ], \"role\": \"primary\", \"servers\": [ \"1.1.1.1\", \"10.72.204.27\" ] } ], \"svm\": { \"name\": \"vs1\", \"uuid\": \"b103be27-17b8-11e9-b451-0050568ecd85\" }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
      "uuid": "b103be27-17b8-11e9-b451-0050568ecd85",
      "name": "vs1"
      },
      "enabled": true,
      "scanner_pools": [
        {
          "name": "scanner-1",
          "servers": [
            "1.1.1.1",
            "10.72.204.27"
          ],
          "privileged_users": [
            "cifs\\u1",
            "cifs\\u2"
          ],
          "role": "primary",
          "cluster": {
            "name": "Cluster1",
            "uuid": "ab746d77-17b7-11e9-b450-0050568ecd85"
          }
        }
      ],
      "on_access_policies": [
        {
          "name": "on-access-test",
          "enabled": true,
          "mandatory": true,
          "scope": {
            "max_file_size": 21474,
            "exclude_paths": [
              "\\vol"
            ],
            "include_extensions": [
              "mp*",
              "txt"
            ],
            "exclude_extensions": [
              "mp*",
              "txt"
            ],
            "scan_without_extension": true,
            "scan_readonly_volumes": false,
            "only_execute_access": false
          }
        }
      ],
      "on_demand_policies": [
        {
          "name": "task-1",
          "scan_paths": [
            "/vol"
          ],
          "log_path": "/vol",
          "schedule": {
            "uuid": "d4984822-17b7-11e9-b450-0050568ecd85",
            "name": "daily"
          },
          "scope": {
            "max_file_size": 10737,
            "exclude_paths": [
              "//"
            ],
            "include_extensions": [
              "vmdk",
              "mp*"
            ],
            "exclude_extensions": [
              "mp3",
              "mp4"
            ],
            "scan_without_extension": true
          }
        }
      ]
    }
  ]
}
```
### Creating multiple Vscan scanner-pools for the specified SVM
```
# The API:
/api/protocols/vscan
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan?return_records=true" -H "accept: appication/json" -H "Content-Type: application/json" -d "{ \"scanner_pools\": [ { \"cluster\": { \"name\": \"Cluster1\", \"uuid\": \"ab746d77-17b7-11e9-b450-0050568ecd85\" }, \"name\": \"scanner-1\", \"privileged_users\": [ \"cifs\\\\u1\", \"cifs\\\\u2\" ], \"role\": \"primary\", \"servers\": [ \"1.1.1.1\", \"10.72.204.27\" ] }, { \"cluster\": { \"name\": \"Cluster1\", \"uuid\": \"ab746d77-17b7-11e9-b450-0050568ecd85\" }, \"name\": \"scanner-2\", \"privileged_users\": [ \"cifs\\\\u3\", \"cifs\\\\u4\" ], \"role\": \"primary\", \"servers\": [ \"1.1.1.5\", \"10.72.3.27\" ] } ], \"svm\": { \"name\": \"vs1\", \"uuid\": \"b103be27-17b8-11e9-b451-0050568ecd85\" }}"
# The response:
{
"num_records": 1,
"records": [
    {
      "svm": {
      "uuid": "b103be27-17b8-11e9-b451-0050568ecd85",
      "name": "vs1"
      },
      "scanner_pools": [
        {
          "name": "scanner-1",
          "servers": [
            "1.1.1.1",
            "10.72.204.27"
          ],
          "privileged_users": [
            "cifs\\u1",
            "cifs\\u2"
          ],
          "role": "primary",
          "cluster": {
            "name": "Cluster1",
            "uuid": "ab746d77-17b7-11e9-b450-0050568ecd85"
          }
        },
        {
          "name": "scanner-2",
          "servers": [
            "1.1.1.5",
            "10.72.3.27"
          ],
          "privileged_users": [
            "cifs\\u3",
            "cifs\\u4"
          ],
          "role": "primary",
          "cluster": {
            "name": "Cluster1",
            "uuid": "ab746d77-17b7-11e9-b450-0050568ecd85"
          }
        }
      ]
    }
  ]
}
```
### Creating multiple Vscan On-access policies for a specified SVM
```
# The API:
/api/protocols/vscan
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"on_access_policies\": [ { \"enabled\": false, \"mandatory\": true, \"name\": \"on-access-test11\", \"scope\": { \"exclude_extensions\": [ \"mp*\", \"txt\" ], \"exclude_paths\": [ \"\\\\vol\" ], \"include_extensions\": [ \"mp*\", \"txt\" ], \"max_file_size\": 214748, \"only_execute_access\": false, \"scan_readonly_volumes\": false, \"scan_without_extension\": true } }, { \"enabled\": false, \"mandatory\": true, \"name\": \"on-access-test10\", \"scope\": { \"exclude_extensions\": [ \"mp*\", \"txt\" ], \"exclude_paths\": [ \"\\\\vol\" ], \"include_extensions\": [ \"mp*\", \"txt\" ], \"max_file_size\": 21474, \"only_execute_access\": false, \"scan_readonly_volumes\": false, \"scan_without_extension\": true } } ], \"svm\": { \"name\": \"vs1\", \"uuid\": \"b103be27-17b8-11e9-b451-0050568ecd85\" }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "b103be27-17b8-11e9-b451-0050568ecd85",
        "name": "vs1"
      },
      "on_access_policies": [
        {
          "name": "on-access-test11",
          "enabled": false,
          "mandatory": true,
          "scope": {
            "max_file_size": 214748,
            "exclude_paths": [
              "\\vol"
            ],
            "include_extensions": [
              "mp*",
              "txt"
            ],
            "exclude_extensions": [
              "mp*",
              "txt"
            ],
            "scan_without_extension": true,
            "scan_readonly_volumes": false,
            "only_execute_access": false
          }
        },
        {
          "name": "on-access-test10",
          "enabled": false,
          "mandatory": true,
          "scope": {
            "max_file_size": 21474,
            "exclude_paths": [
              "\\vol"
            ],
            "include_extensions": [
              "mp*",
              "txt"
            ],
            "exclude_extensions": [
              "mp*",
              "txt"
            ],
            "scan_without_extension": true,
            "scan_readonly_volumes": false,
            "only_execute_access": false
          }
        }
      ]
    }
  ]
}
```
### Creating multiple Vscan On-demand policies for a specified SVM
```
# The API:
/api/protocols/vscan
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/vscan?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"on_demand_policies\": [ { \"log_path\": \"/vol\", \"name\": \"task-1\", \"scan_paths\": [ \"/vol\" ], \"schedule\": { \"name\": \"daily\", \"uuid\": \"d4984822-17b7-11e9-b450-0050568ecd85\" }, \"scope\": { \"exclude_extensions\": [ \"mp3\", \"mp4\" ], \"exclude_paths\": [ \"/vol1\" ], \"include_extensions\": [ \"vmdk\", \"mp*\" ], \"max_file_size\": 107374, \"scan_without_extension\": true } }, { \"log_path\": \"/vol\", \"name\": \"task-2\", \"scan_paths\": [ \"/vol\" ], \"scope\": { \"exclude_extensions\": [ \"mp3\", \"mp4\" ], \"exclude_paths\": [ \"/vol1\" ], \"include_extensions\": [ \"vmdk\", \"mp*\" ], \"max_file_size\": 107374, \"scan_without_extension\": true } } ], \"svm\": { \"name\": \"vs1\", \"uuid\": \"b103be27-17b8-11e9-b451-0050568ecd85\" }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "b103be27-17b8-11e9-b451-0050568ecd85",
        "name": "vs1"
      },
      "on_demand_policies": [
        {
          "name": "task-1",
          "scan_paths": [
            "/vol"
          ],
          "log_path": "/vol",
          "schedule": {
            "uuid": "d4984822-17b7-11e9-b450-0050568ecd85",
            "name": "daily"
          },
          "scope": {
            "max_file_size": 107374,
            "exclude_paths": [
              "/vol1"
            ],
            "include_extensions": [
              "vmdk",
              "mp*"
            ],
            "exclude_extensions": [
              "mp3",
              "mp4"
            ],
            "scan_without_extension": true
          }
        },
        {
          "name": "task-2",
          "scan_paths": [
            "/vol"
          ],
          "log_path": "/vol",
          "scope": {
            "max_file_size": 107374,
            "exclude_paths": [
              "/vol1"
            ],
            "include_extensions": [
              "vmdk",
              "mp*"
            ],
            "exclude_extensions": [
              "mp3",
              "mp4"
            ],
            "scan_without_extension": true
          }
        }
      ]
    }
  ]
}
```
### Enabling Vscan for a specified SVM
```
# The API:
/api/protocols/vscan/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/vscan/03ce5c36-f269-11e8-8852-0050568e5298" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": true}"
```
### Clearing the Vscan cache for the specified SVM
```
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/vscan/03ce5c36-f269-11e8-8852-0050568e5298" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"cache_clear\": true}"
```
### Deleting the Vscan configuration for a specified SVM
```
# The API:
/api/protocols/vscan/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/vscan/03ce5c36-f269-11e8-8852-0050568e5298" -H "accept: application/json"
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Vscan", "VscanSchema"]
__pdoc__ = {
    "VscanSchema.resource": False,
    "VscanSchema.patchable_fields": False,
    "VscanSchema.postable_fields": False,
}


class VscanSchema(ResourceSchema):
    """The fields of the Vscan object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the vscan. """

    cache_clear = fields.Boolean(
        data_key="cache_clear",
    )
    r""" Discards the cached information of the files that have been successfully scanned. Once the cache is cleared, files are scanned again when they are accessed. PATCH only """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies whether or not Vscan is enabled on the SVM. """

    on_access_policies = fields.List(fields.Nested("netapp_ontap.resources.vscan_on_access.VscanOnAccessSchema", unknown=EXCLUDE), data_key="on_access_policies")
    r""" The on_access_policies field of the vscan. """

    on_demand_policies = fields.List(fields.Nested("netapp_ontap.resources.vscan_on_demand.VscanOnDemandSchema", unknown=EXCLUDE), data_key="on_demand_policies")
    r""" The on_demand_policies field of the vscan. """

    scanner_pools = fields.List(fields.Nested("netapp_ontap.resources.vscan_scanner_pool.VscanScannerPoolSchema", unknown=EXCLUDE), data_key="scanner_pools")
    r""" The scanner_pools field of the vscan. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the vscan. """

    @property
    def resource(self):
        return Vscan

    @property
    def patchable_fields(self):
        return [
            "cache_clear",
            "enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "enabled",
            "on_access_policies",
            "on_demand_policies",
            "scanner_pools",
            "svm.name",
            "svm.uuid",
        ]

class Vscan(Resource):
    r""" Vscan can be used to protect data from being compromised by viruses or other malicious code. This combines best-in-class third-party antivirus software with ONTAP features that give you the flexibility you need to control which files get scanned and when. Storage systems offload scanning operations to external servers hosting antivirus software from thirdparty vendors. An Antivirus Connector on the external server handles communications between the storage system and the antivirus software. """

    _schema = VscanSchema
    _path = "/api/protocols/vscan"
    @property
    def _keys(self):
        return ["svm.uuid"]

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
        r"""Retrieves the Vscan configuration.
This includes scanner-pools, On-Access policies, On-Demand policies, and information about whether a Vscan is enabled or disabled on an SVM.<br/>
Important notes:
* You can enable only one Vscan configuration at a time for an SVM.
* You can only query using `svm.uuid` or `svm.name`.
### Related ONTAP commands
* `vserver vscan show`
* `vserver vscan scanner-pool show`
* `vserver vscan scanner-pool servers show`
* `vserver vscan scanner-pool privileged-users show`
* `vserver vscan scanner-pool show-active`
* `vserver vscan on-access-policy show`
* `vserver vscan on-access-policy file-ext-to-exclude show`
* `vserver vscan on-access-policy file-ext-to-include show`
* `vserver vscan on-access-policy paths-to-exclude show`
* `vserver vscan on-demand-task show`
### Learn more
* [`DOC /protocols/vscan`](#docs-NAS-protocols_vscan)
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Updates the Vscan configuration of an SVM. Allows you to either enable or disable a Vscan, and allows you to clear the Vscan cache that stores the past scanning data for an SVM.<br/>
Important note:
* The Vscan PATCH endpoint does not allow you to modify scanner-pools, On-Demand policies or On-Access policies. Those modifications can only be done through their respective endpoints.
### Related ONTAP commands
* `vserver vscan enable`
* `vserver vscan disable`
* `vserver vscan reset`
### Learn more
* [`DOC /protocols/vscan`](#docs-NAS-protocols_vscan)
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Deletes a Vscan configuration.<br/>
Important notes:
* The Vscan DELETE endpoint deletes all of the Vscan configuration of an SVM. It first disables the Vscan and then deletes all of the SVM scanner-pools, On-Access policies, and On-Demand policies.
* Disable the active Vscan On-Access policy on an SVM before performing the Vscan delete operation on that SVM.
### Related ONTAP commands
* `vserver vscan scanner-pool delete`
* `vserver vscan on-access-policy delete`
* `vserver vscan on-demand-policy delete`
### Learn more
* [`DOC /protocols/vscan`](#docs-NAS-protocols_vscan)
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the Vscan configuration.
This includes scanner-pools, On-Access policies, On-Demand policies, and information about whether a Vscan is enabled or disabled on an SVM.<br/>
Important notes:
* You can enable only one Vscan configuration at a time for an SVM.
* You can only query using `svm.uuid` or `svm.name`.
### Related ONTAP commands
* `vserver vscan show`
* `vserver vscan scanner-pool show`
* `vserver vscan scanner-pool servers show`
* `vserver vscan scanner-pool privileged-users show`
* `vserver vscan scanner-pool show-active`
* `vserver vscan on-access-policy show`
* `vserver vscan on-access-policy file-ext-to-exclude show`
* `vserver vscan on-access-policy file-ext-to-include show`
* `vserver vscan on-access-policy paths-to-exclude show`
* `vserver vscan on-demand-task show`
### Learn more
* [`DOC /protocols/vscan`](#docs-NAS-protocols_vscan)
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the Vscan configuration for a specified SVM.
This includes scanner-pools, On-Access policies, On-Demand policies, and information about whether a Vscan is enabled or disabled on an SVM.<br/>
Important note:
* You can enable only one Vscan configuration at a time for an SVM.
### Related ONTAP commands
* `vserver vscan show`
* `vserver vscan scanner-pool show`
* `vserver vscan scanner-pool servers show`
* `vserver vscan scanner-pool privileged-users show`
* `vserver vscan scanner-pool show-active`
* `vserver vscan on-access-policy show`
* `vserver vscan on-access-policy file-ext-to-exclude show`
* `vserver vscan on-access-policy file-ext-to-include show`
* `vserver vscan on-access-policy paths-to-exclude show`
* `vserver vscan on-demand-task show`
### Learn more
* [`DOC /protocols/vscan`](#docs-NAS-protocols_vscan)
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Creates a Vscan configuration, which includes a list of scanner-pools, Vscan On-Access policies and Vscan On-Demand policies. Defines whether the Vscan configuration you create is enabled or disabled for a specified SVM.<br/>
Important notes:
* You can enable only one Vscan configuration at a time for an SVM.
* There needs to be at least one active scanner-pool and one enabled On-Access policy to enable Vscan successfully.
* By default, a Vscan is enabled when it’s created.
* By default, the Vscan On-Access policies created from this endpoint are in the disabled state. You can use the On-Access policy PATCH endpoint to enable a particular On-Access policy. In ONTAP 9.6, only one Vscan On-Access policy can be enabled and only one Vscan On-Demand policy can be scheduled on an SVM.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the Vscan configuration.
### Recommended optional properties
* `scanner_pools` - There must be at least one active scanner-pool for Vscan configuration. Created either through Vscan POST operation or scanner-pools POST operation.
### Default property values
If not specified in POST, the following default property value is assigned:
* `enabled` - _true_
### Related ONTAP commands
* `vserver vscan enable`
* `vserver vscan scanner-pool create`
* `vserver vscan scanner-pool apply-policy`
* `vserver vscan scanner-pool servers add`
* `vserver vscan scanner-pool privileged-users add`
* `vserver vscan on-access-policy create`
* `vserver vscan on-access-policy file-ext-to-exclude add`
* `vserver vscan on-access-policy file-ext-to-include add`
* `vserver vscan on-access-policy paths-to-exclude add`
* `vserver vscan on-demand-task create`
### Learn more
* [`DOC /protocols/vscan`](#docs-NAS-protocols_vscan)
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Updates the Vscan configuration of an SVM. Allows you to either enable or disable a Vscan, and allows you to clear the Vscan cache that stores the past scanning data for an SVM.<br/>
Important note:
* The Vscan PATCH endpoint does not allow you to modify scanner-pools, On-Demand policies or On-Access policies. Those modifications can only be done through their respective endpoints.
### Related ONTAP commands
* `vserver vscan enable`
* `vserver vscan disable`
* `vserver vscan reset`
### Learn more
* [`DOC /protocols/vscan`](#docs-NAS-protocols_vscan)
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
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
        r"""Deletes a Vscan configuration.<br/>
Important notes:
* The Vscan DELETE endpoint deletes all of the Vscan configuration of an SVM. It first disables the Vscan and then deletes all of the SVM scanner-pools, On-Access policies, and On-Demand policies.
* Disable the active Vscan On-Access policy on an SVM before performing the Vscan delete operation on that SVM.
### Related ONTAP commands
* `vserver vscan scanner-pool delete`
* `vserver vscan on-access-policy delete`
* `vserver vscan on-demand-policy delete`
### Learn more
* [`DOC /protocols/vscan`](#docs-NAS-protocols_vscan)
* [`DOC /protocols/vscan/{svm.uuid}/scanner-pools`](#docs-NAS-protocols_vscan_{svm.uuid}_scanner-pools)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


