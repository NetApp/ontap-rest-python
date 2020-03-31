# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
The FPolicy policy acts as a container for different constituents of the FPolicy such as FPolicy events and the FPolicy engine. It also provides a platform for policy management functions, such as policy enabling and disabling. As part of FPolicy policy configuration, you can specifiy the name of policy, the SVM to which it belongs, the FPolicy events to monitor, the FPolicy engine to which the generated notifications are sent and the policy priority. FPolicy policy configuration also allows to you to configure the file access behaviour when the primary and secondary servers are down. Under such circumstances, if the "mandatory" field is set to true, file access is denied.</br>
Each FPolicy policy is associated with a scope which allows you to restrain the scope of the policy to specified storage objects such as volume, shares and export or to a set of file extensions such as .txt, .jpeg. An FPolicy policy can be configured to send notifications, to the FPolicy server or for native file blocking which uses the file extension specified in the policy scope. An SVM can have multiple FPolicy policies which can be enabled or disabled independently of each other.
## Examples
### Creating an FPolicy policy
Use the following API to create an FPolicy policy configuration. Note that the <i>return_records=true</i> query parameter used to obtain the newly created entry in the response.
<br/>
---
```
# The API:
POST /protocols/fpolicy/{svm.uuid}/policies
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/polices?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"engine\": { \"name\": \"engine1\" }, \"events\": [ \"cifs\", \"nfs\" ], \"mandatory\": true, \"name\": \"FPolicy_policy_0\", \"scope\": { \"exclude_export_policies\": [ \"export_pol1\" ], \"exclude_extension\": [ \"txt\", \"png\" ], \"exclude_shares\": [ \"sh1\" ], \"exclude_volumes\": [ \"vol0\" ], \"include_export_policies\": [ \"export_pol10\" ], \"include_extension\": [ \"pdf\" ], \"include_shares\": [ \"sh2\", \"sh3\" ], \"include_volumes\": [ \"vol1\", \"vol2\" ] }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "name": "FPolicy_policy_0",
      "events": [
        {
          "name": "cifs"
        },
        {
          "name": "nfs"
        }
        ],
      "engine": {
        "name": "engine1"
      },
      "scope": {
        "include_shares": [
          "sh2",
          "sh3"
        ],
        "exclude_shares": [
          "sh1"
        ],
        "include_volumes": [
          "vol1",
          "vol2"
        ],
        "exclude_volumes": [
          "vol0"
        ],
        "include_export_policies": [
          "export_pol10"
        ],
        "exclude_export_policies": [
          "export_pol1"
        ],
        "include_extension": [
          "pdf"
        ],
        "exclude_extension": [
          "txt",
          "png"
        ]
      },
      "mandatory": true
    }
  ]
}
```
---
### Creating and enable an FPolicy policy
---
```
# The API:
POST /protocols/fpolicy/{svm.uuid}/policies
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/polices?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"priority\": 1, \"engine\": { \"name\": \"engine1\" }, \"events\": [ \"cifs\", \"nfs\" ], \"mandatory\": true, \"name\": \"FPolicy_policy_on\", \"scope\": { \"exclude_export_policies\": [ \"export_pol1\" ], \"exclude_extension\": [ \"txt\", \"png\" ], \"exclude_shares\": [ \"sh1\" ], \"exclude_volumes\": [ \"vol0\" ], \"include_export_policies\": [ \"export_pol10\" ], \"include_extension\": [ \"pdf\" ], \"include_shares\": [ \"sh2\", \"sh3\" ], \"include_volumes\": [ \"vol1\", \"vol2\" ] }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
     "name": "FPolicy_policy_0",
     "priority": 1,
     "events": [
       {
         "name": "cifs"
       },
       {
         "name": "nfs"
       }
     ],
     "engine": {
       "name": "engine1"
     },
     "scope": {
       "include_shares": [
         "sh2",
         "sh3"
       ],
       "exclude_shares": [
         "sh1"
       ],
       "include_volumes": [
         "vol1",
         "vol2"
       ],
       "exclude_volumes": [
         "vol0"
       ],
       "include_export_policies": [
         "export_pol10"
       ],
       "exclude_export_policies": [
         "export_pol1"
       ],
       "include_extension": [
         "pdf"
       ],
       "exclude_extension": [
         "txt",
         "png"
       ]
     },
     "mandatory": true
   }
 ]
}
```
---
### Creating an FPolicy policy with the minimum required fields and a native engine
---
```
# The API:
POST /protocols/fpolicy/{svm.uuid}/policies
# The call:
curl -X POST"https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/polices?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"events\": [ \"cifs\", \"nfs\" ], \"name\": \"pol_minimum_fields\", \"scope\": { \"include_volumes\": [ \"vol1\", \"vol2\" ] }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "name": "pol_minimum_fields",
      "events": [
        {
          "name": "cifs"
        },
        {
          "name": "nfs"
        }
      ],
      "scope": {
        "include_volumes": [
          "vol1",
          "vol2"
        ]
      }
    }
  ]
}
```
---
### Retrieving all the FPolicy policy configurations for an SVM
---
```
# The API:
GET /protocols/fpolicy/{svm.uuid}/policies
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/policis?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "a00fac5d-0164-11e9-b64a-0050568eeb34"
      },
      "name": "pol0",
      "enabled": false,
      "events": [
        {
          "name": "cifs"
        },
        {
          "name": "nfs"
        }
      ],
      "engine": {
        "name": "engine1"
      },
      "scope": {
        "include_shares": [
          "sh2",
          "sh3"
        ],
        "exclude_shares": [
          "sh1"
        ],
        "include_volumes": [
          "vol1",
          "vol2"
        ],
        "exclude_volumes": [
          "vol0"
        ],
        "include_export_policies": [
          "export_pol10"
        ],
        "exclude_export_policies": [
          "export_pol1"
        ],
        "include_extension": [
          "pdf"
        ],
        "exclude_extension": [
          "txt",
          "png"
        ]
      },
      "mandatory": true
    },
    {
      "svm": {
        "uuid": "a00fac5d-0164-11e9-b64a-0050568eeb34"
      },
      "name": "FPolicy_policy_on",
      "enabled": true,
      "priority": 1,
      "events": [
        {
          "name": "cifs"
        },
        {
          "name": "nfs"
        }
      ],
      "engine": {
        "name": "engine1"
      },
       "scope": {
        "include_shares": [
          "sh2",
          "sh3"
        ],
        "exclude_shares": [
          "sh1"
        ],
        "include_volumes": [
          "vol1",
          "vol2"
        ],
        "exclude_volumes": [
          "vol0"
        ],
        "include_export_policies": [
          "export_pol10"
        ],
        "exclude_export_policies": [
          "export_pol1"
        ],
        "include_extension": [
          "pdf"
        ],
        "exclude_extension": [
          "txt",
          "png"
        ]
      },
      "mandatory": true
    },
    {
      "svm": {
        "uuid": "a00fac5d-0164-11e9-b64a-0050568eeb34"
      },
      "name": "cluster_pol",
      "enabled": false,
      "events": [
        {
          "name": "cluster"
        }
      ],
      "engine": {
        "name": "native"
      },
      "mandatory": true
    },
    {
      "svm": {
        "uuid": "a00fac5d-0164-11e9-b64a-0050568eeb34"
      },
      "name": "pol_minimum_fields",
      "enabled": false,
      "events": [
        {
          "name": "cifs"
        },
        {
          "name": "nfs"
        }
      ],
      "engine": {
        "name": "native"
      },
      "scope": {
        "include_volumes": [
          "vol1",
          "vol2"
        ]
      },
      "mandatory": true
    }
  ],
  "num_records": 4
}
```
---
### Retrieving all of the FPolicy policy configurations for the FPolicy engine "engine1" for an SVM
---
```
# The API:
GET /protocols/fpolicy/{svm.uuid}/policies/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/policis?engine.name=engine1&fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "a00fac5d-0164-11e9-b64a-0050568eeb34"
      },
      "name": "pol0",
      "enabled": false,
      "events": [
        {
          "name": "cifs"
        },
        {
          "name": "nfs"
        }
      ],
      "engine": {
        "name": "engine1"
      },
      "scope": {
        "include_export_policies": [
          "export_pol10"
        ],
        "exclude_export_policies": [
          "export_pol1"
        ],
        "include_extension": [
          "pdf"
        ],
        "exclude_extension": [
          "txt",
          "png"
        ]
      },
      "mandatory": true
    },
    {
      "svm": {
        "uuid": "a00fac5d-0164-11e9-b64a-0050568eeb34"
      },
      "name": "FPolicy_policy_on",
      "enabled": true,
      "priority": 1,
      "events": [
        {
          "name": "cifs"
        },
        {
          "name": "nfs"
        }
      ],
      "engine": {
        "name": "engine1"
      },
      "scope": {
        "include_shares": [
          "sh2",
          "sh3"
        ],
        "exclude_shares": [
          "sh1"
        ],
        "include_volumes": [
          "vol1",
          "vol2"
        ],
        "exclude_volumes": [
          "vol0"
        ],
        "include_export_policies": [
          "export_pol10"
        ],
        "exclude_export_policies": [
          "export_pol1"
        ],
        "include_extension": [
          "pdf"
        ],
        "exclude_extension": [
          "txt",
          "png"
        ]
      },
      "mandatory": true
    }
  ],
  "num_records": 2
}
```
---
### Retrieving a particular FPolicy policy configuration for an SVM
---
```
# The API:
GET /protocols/fpolicy/{svm.uuid}/policies/{name}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/policies/pol0" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "a00fac5d-0164-11e9-b64a-0050568eeb34"
  },
  "name": "pol0",
  "enabled": false,
  "events": [
    {
      "name": "cifs"
    },
    {
      "name": "nfs"
    }
  ],
  "engine": {
    "name": "engine1"
  },
  "scope": {
    "include_shares": [
      "sh2",
      "sh3"
    ],
    "exclude_shares": [
      "sh1"
    ],
    "include_volumes": [
      "vol1",
      "vol2"
    ],
    "exclude_volumes": [
      "vol0"
    ],
    "include_export_policies": [
      "export_pol10"
    ],
    "exclude_export_policies": [
      "export_pol1"
    ],
    "include_extension": [
      "pdf"
    ],
    "exclude_extension": [
      "txt",
      "png"
    ]
  },
  "mandatory": true
}
```
---
### Updating a particular FPolicy policy
---
```
# The API:
PATCH /protocols/fpolicy/{svm.uuid}/policies/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/policies/pol0" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"engine\": { \"name\": \"native\" }, \"events\": [ \"cifs\" ], \"mandatory\": false, \"scope\": { \"include_volumes\": [ \"*\" ] }}"
```
---
### Enabling a particular FPolicy policy
---
```
# The API:
PATCH /protocols/fpolicy/{svm.uuid}/policies/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/poliies/pol0" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": true, \"priority\": 3}"
```
---
### Disabling a particular FPolicy policy
---
```
# The API:
PATCH /protocols/fpolicy/{svm.uuid}/policies/{name}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/fpolicy/a00fac5d-0164-11e9-b64a-0050568eeb34/poliies/pol0" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"enabled\": true }"
```
---
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["FpolicyPolicy", "FpolicyPolicySchema"]
__pdoc__ = {
    "FpolicyPolicySchema.resource": False,
    "FpolicyPolicySchema.patchable_fields": False,
    "FpolicyPolicySchema.postable_fields": False,
}


class FpolicyPolicySchema(ResourceSchema):
    """The fields of the FpolicyPolicy object"""

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies if the policy is enabled on the SVM or not. If no value is
mentioned for this field but priority is set, then this policy will be enabled. """

    engine = fields.Nested("netapp_ontap.resources.fpolicy_engine.FpolicyEngineSchema", data_key="engine", unknown=EXCLUDE)
    r""" The engine field of the fpolicy_policy. """

    events = fields.List(fields.Nested("netapp_ontap.resources.fpolicy_event.FpolicyEventSchema", unknown=EXCLUDE), data_key="events")
    r""" The events field of the fpolicy_policy.

Example: ["event_nfs_close","event_open"] """

    mandatory = fields.Boolean(
        data_key="mandatory",
    )
    r""" Specifies what action to take on a file access event in a case when all primary and secondary servers are down or no response is received from the FPolicy servers within a given timeout period. When this parameter is set to true, file access events will be denied under these circumstances. """

    name = fields.Str(
        data_key="name",
    )
    r""" Specifies the name of the policy.

Example: fp_policy_1 """

    priority = fields.Integer(
        data_key="priority",
        validate=integer_validation(minimum=1, maximum=10),
    )
    r""" Specifies the priority that is assigned to this policy. """

    scope = fields.Nested("netapp_ontap.models.fpolicy_policy_scope.FpolicyPolicyScopeSchema", data_key="scope", unknown=EXCLUDE)
    r""" The scope field of the fpolicy_policy. """

    @property
    def resource(self):
        return FpolicyPolicy

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "engine.name",
            "events",
            "mandatory",
            "priority",
            "scope",
        ]

    @property
    def postable_fields(self):
        return [
            "engine.name",
            "events",
            "mandatory",
            "name",
            "priority",
            "scope",
        ]

class FpolicyPolicy(Resource):
    """Allows interaction with FpolicyPolicy objects on the host"""

    _schema = FpolicyPolicySchema
    _path = "/api/protocols/fpolicy/{svm[uuid]}/policies"
    @property
    def _keys(self):
        return ["svm.uuid", "name"]

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
        r"""Retrieves the FPolicy policy configuration of an SVM. ONTAP allows the creation of a cluster level FPolicy policy that acts as a template for all the data SVMs belonging to the cluster. This cluster level FPolicy policy is also retrieved for the specified SVM.
### Related ONTAP commands
* `fpolicy policy show`
* `fpolicy policy scope show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/policies`](#docs-NAS-protocols_fpolicy_{svm.uuid}_policies)
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
        r"""Updates a particular FPolicy policy configuration for a specified SVM. PATCH can be used to enable or disable the policy. When enabling a policy, you must specify the policy priority. The policy priority of the policy is not required when disabling the policy. If the policy is enabled, the FPolicy policy engine cannot be modified.
### Related ONTAP commands
* `fpolicy policy modify`
* `fpolicy policy scope modify`
* `fpolicy enable`
* `fpolicy disable`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/policies`](#docs-NAS-protocols_fpolicy_{svm.uuid}_policies)
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
        r"""Deletes a particular FPolicy policy configuration for a specified SVM. To delete a policy, you must first disable the policy.
### Related ONTAP commands
* `fpolicy policy scope delete`
* `fpolicy policy delete`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/policies`](#docs-NAS-protocols_fpolicy_{svm.uuid}_policies)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the FPolicy policy configuration of an SVM. ONTAP allows the creation of a cluster level FPolicy policy that acts as a template for all the data SVMs belonging to the cluster. This cluster level FPolicy policy is also retrieved for the specified SVM.
### Related ONTAP commands
* `fpolicy policy show`
* `fpolicy policy scope show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/policies`](#docs-NAS-protocols_fpolicy_{svm.uuid}_policies)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a particular FPolicy policy configuration for a specified SVM. Cluster-level FPolicy policy configuration details cannot be retrieved for a data SVM.
### Related ONTAP commands
* `fpolicy policy show`
* `fpolicy policy scope show`
* `fpolicy show`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/policies`](#docs-NAS-protocols_fpolicy_{svm.uuid}_policies)
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
        r"""Creates an FPolicy policy configuration for the specified SVM. To create an FPolicy policy, you must specify the policy scope and the FPolicy events to be monitored.
</br>Important notes:
* A single policy can monitor multiple events.
* An FPolicy engine is an optional field whose default value is set to native. A native engine can be used to simply block the file access based on the file extensions specified in the policy scope.
* To enable a policy, the policy priority  must be specified. If the priority is not specified, the policy is created but it is not enabled.
* The "mandatory" field, if set to true, blocks the file access when the primary or secondary FPolicy servers are down.
### Required properties
* `svm.uuid` - Existing SVM in which to create the FPolicy policy.
* `events` - Name of the events to monitior.
* `name` - Name of the FPolicy policy.
* `scope` - Scope of the policy. Can be limited to exports, volumes, shares or file extensions.
* `priority`- Priority of the policy (ranging from 1 to 10).
### Default property values
* `mandatory` - _true_
* `engine` - _native_
### Related ONTAP commands
* `fpolicy policy scope create`
* `fpolicy policy create`
* `fpolicy enable`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/policies`](#docs-NAS-protocols_fpolicy_{svm.uuid}_policies)
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
        r"""Updates a particular FPolicy policy configuration for a specified SVM. PATCH can be used to enable or disable the policy. When enabling a policy, you must specify the policy priority. The policy priority of the policy is not required when disabling the policy. If the policy is enabled, the FPolicy policy engine cannot be modified.
### Related ONTAP commands
* `fpolicy policy modify`
* `fpolicy policy scope modify`
* `fpolicy enable`
* `fpolicy disable`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/policies`](#docs-NAS-protocols_fpolicy_{svm.uuid}_policies)
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
        r"""Deletes a particular FPolicy policy configuration for a specified SVM. To delete a policy, you must first disable the policy.
### Related ONTAP commands
* `fpolicy policy scope delete`
* `fpolicy policy delete`
### Learn more
* [`DOC /protocols/fpolicy/{svm.uuid}/policies`](#docs-NAS-protocols_fpolicy_{svm.uuid}_policies)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


