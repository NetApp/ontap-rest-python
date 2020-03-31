# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Quotas are defined in quota rules specific to FlexVol volumes or FlexGroup volumes.  Each quota rule has a type. The type can be "user", "group", or "tree".</br>

* User rules must have the user property and qtree property.
* Group rules must have the group property and qtree property.
* Tree rules must have the qtree property and not have the user or group property.
## Quota policy rule APIs
The following APIs can be used to perform create, retrieve, modify, and delete operations related to quota policy rules.

* POST      /api/storage/quota/rules
* GET       /api/storage/quota/rules
* GET       /api/storage/quota/rules/{rule-uuid}
* PATCH     /api/storage/quota/rules/{rule-uuid}
* DELETE    /api/storage/quota/rules/{rule-uuid}
## Examples
### Retrieving all quota policy rules
This API is used to retrieve all quota policy rules.<br/>
The following example shows how to retrieve quota policy rules for FlexVol volumes and FlexGroup volumes.
<br/>
---
```
# The API:
GET /api/storage/quota/rules
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/quota/rules' -H 'accept: application/hal+json'
# The response:
{
    "records": [
      {
        "svm": {
          "uuid": "038545f8-9ff8-11e8-bce6-005056a73bed",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/038545f8-9ff8-11e8-bce6-005056a73bed"
            }
          }
        },
        "volume": {
          "uuid": "ab3df793-0f02-43c6-9514-4f142fc8cc92",
          "name": "vol1",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/ab3df793-0f02-43c6-9514-4f142fc8cc92"
            }
          }
        },
        "uuid": "66319cbe-b837-11e8-9c5a-005056a7e88c",
        "_links": {
          "self": {
            "href": "/api/storage/quota/rules/66319cbe-b837-11e8-9c5a-005056a7e88c"
          }
        }
      },
      {
        "svm": {
          "uuid": "038545f8-9ff8-11e8-bce6-005056a73bed",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/038545f8-9ff8-11e8-bce6-005056a73bed"
            }
          }
        },
        "volume": {
          "uuid": "ab3df793-0f02-43c6-9514-4f142fc8cc92",
          "name": "vol1",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/ab3df793-0f02-43c6-9514-4f142fc8cc92"
            }
          }
        },
        "uuid": "dbd5b443-b7a4-11e8-bc58-005056a7e88c",
        "_links": {
          "self": {
            "href": "/api/storage/quota/rules/dbd5b443-b7a4-11e8-bc58-005056a7e88c"
          }
        }
      }
    ],
    "num_records": 2,
    "_links": {
      "self": {
        "href": "/api/storage/quota/rules"
      }
    }
}
```
---
### Retrieving a specific quota policy rule
This API is used to retrieve a quota policy rule for a specific qtree.<br/>
The following example shows how to retrieve a quota policy user rule for a specific qtree.
<br/>
---
```
# The API:
GET /api/storage/quota/rules/{uuid}
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/quota/rules/264a9e0b-2e03-11e9-a610-005056a7b72d' -H 'accept: application/hal+json'
# Response for a user rule at a qtree level:
{
    "svm": {
      "uuid": "fd5db15a-15b9-11e9-a6ad-005056a760e0",
      "name": "svm1",
      "_links": {
        "self": {
          "href": "/api/svm/svms/fd5db15a-15b9-11e9-a6ad-005056a760e0"
        }
      }
    },
    "volume": {
      "uuid": "c1b64eea-ca8b-45ec-9397-ab489830d268",
      "name": "vol1",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/c1b64eea-ca8b-45ec-9397-ab489830d268"
        }
      }
    },
    "uuid": "264a9e0b-2e03-11e9-a610-005056a7b72d",
    "type": "user",
    "users": [ {"name" : "fred"} ],
    "qtree": {
      "name": "qt1",
      "id": 1,
      "_links": {
        "self": {
          "href": "/api/storage/qtrees/c1b64eea-ca8b-45ec-9397-ab489830d268/1"
        }
      }
    },
    "user_mapping": on,
    "space": {
      "hard_limit": 1222800,
      "soft_limit": 51200
    },
    "files": {
      "hard_limit": 100,
      "soft_limit": 80
    },
    "_links": {
      "self": {
        "href": "/api/storage/quota/rules/264a9e0b-2e03-11e9-a610-005056a7b72d"
      }
    }
}
```
---
### Retrieving a quota policy multi-user rule at the volume level
<br/>
---
```
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/quota/rules/0ab84fba-19aa-11e9-a04d-005056a72f42' -H 'accept: application/hal+json'
# Response for a multi-user rule at volume level:
{
    "svm": {
      "uuid": "fd5db15a-15b9-11e9-a6ad-005056a760e0",
      "name": "svm1",
      "_links": {
        "self": {
          "href": "/api/svm/svms/fd5db15a-15b9-11e9-a6ad-005056a760e0"
        }
      }
    },
    "volume": {
      "uuid": "c1b64eea-ca8b-45ec-9397-ab489830d268",
      "name": "vol1",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/c1b64eea-ca8b-45ec-9397-ab489830d268"
        }
      }
    },
    "uuid": "0ab84fba-19aa-11e9-a04d-005056a72f42",
    "type": "user",
    "users": [
      {
        "name": "sam",
      },
      {
        "name": "smith",
      },
      {
        "id": "300010",
      },
    ],
    "space": {
      "hard_limit": 1222800,
      "soft_limit": 51200
    },
    "files": {
      "hard_limit": 100,
      "soft_limit": 80
    },
    "_links": {
      "self": {
        "href": "/api/storage/quota/rules/0ab84fba-19aa-11e9-a04d-005056a72f42"
      }
    }
}
```
---
### Retrieving a quota policy default tree rule
<br/>
---
```
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/quota/rules/4a276b8c-1753-11e9-8101-005056a760e0' -H 'accept: application/hal+json'
# Response for a default tree rule:
{
    "svm": {
      "uuid": "fd5db15a-15b9-11e9-a6ad-005056a760e0",
      "name": "svm1",
      "_links": {
        "self": {
          "href": "/api/svm/svms/fd5db15a-15b9-11e9-a6ad-005056a760e0"
        }
      }
    },
    "volume": {
      "uuid": "c1b64eea-ca8b-45ec-9397-ab489830d268",
      "name": "vol1",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/c1b64eea-ca8b-45ec-9397-ab489830d268"
        }
      }
    },
    "uuid": "4a276b8c-1753-11e9-8101-005056a760e0",
    "type": "tree",
    "qtree": {
      "name": ""
    },
    "space": {
      "hard_limit": 1034000,
      "soft_limit": 51200
    },
    "files": {
      "hard_limit": 20,
      "soft_limit": 10
    },
    "_links": {
      "self": {
        "href": "/api/storage/quota/rules/4a276b8c-1753-11e9-8101-005056a760e0"
      }
    }
}
```
---
### Retrieving a quota policy tree rule for a specific qtree
<br/>
---
```
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/quota/rules/49b1134f-19ab-11e9-a04d-005056a72f42' -H 'accept: application/hal+json'
# Response for a tree rule for a specific qtree:
{
    "svm": {
      "uuid": "fd5db15a-15b9-11e9-a6ad-005056a760e0",
      "name": "svm1",
      "_links": {
        "self": {
          "href": "/api/svm/svms/fd5db15a-15b9-11e9-a6ad-005056a760e0"
        }
      }
    },
    "volume": {
      "uuid": "c1b64eea-ca8b-45ec-9397-ab489830d268",
      "name": "vol1",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/c1b64eea-ca8b-45ec-9397-ab489830d268"
        }
      }
    },
    "uuid": "49b1134f-19ab-11e9-a04d-005056a72f42",
    "type": "tree",
    "qtree": {
      "name": "qt1",
      "id": 1,
      "_links": {
        "self": {
          "href": "/api/storage/qtrees/c1b64eea-ca8b-45ec-9397-ab489830d268/1"
        }
      }
    },
    "space": {
      "hard_limit": 1048576,
      "soft_limit": 838861
    },
    "files": {
      "hard_limit": 100,
      "soft_limit": 40
    },
    "_links": {
      "self": {
        "href": "/api/storage/quota/rules/49b1134f-19ab-11e9-a04d-005056a72f42"
      }
    }
}
```
---
### Retrieving a quota policy group rule for a specific qtree
<br/>
---
```
# The call:
curl -X GET 'https://<mgmt-ip>/api/storage/quota/rules/b9236852-19ab-11e9-a04d-005056a72f42' -H 'accept: application/hal+json'
# Response for a group rule:
{
    "svm": {
      "uuid": "fd5db15a-15b9-11e9-a6ad-005056a760e0",
      "name": "svm1",
      "_links": {
        "self": {
          "href": "/api/svm/svms/fd5db15a-15b9-11e9-a6ad-005056a760e0"
        }
      }
    },
    "volume": {
      "uuid": "c1b64eea-ca8b-45ec-9397-ab489830d268",
      "name": "vol1",
      "_links": {
        "self": {
          "href": "/api/storage/volumes/c1b64eea-ca8b-45ec-9397-ab489830d268"
        }
      }
    },
    "uuid": "b9236852-19ab-11e9-a04d-005056a72f42",
    "type": "group",
    "group": {"name" : "group1"},
    "qtree": {
      "name": "qt1",
      "id": 1,
      "_links": {
        "self": {
          "href": "/api/storage/qtrees/c1b64eea-ca8b-45ec-9397-ab489830d268/1"
        }
      }
    },
    "space": {
      "hard_limit": 2097152,
      "soft_limit": 1572864
    },
    "files": {
      "hard_limit": 250,
      "soft_limit": 200
    },
    "_links": {
      "self": {
        "href": "/api/storage/quota/rules/b9236852-19ab-11e9-a04d-005056a72f42"
      }
    }
}
```
---
### Creating a quota policy rule
This API is used to create a new quota policy rule. When an explicit rule or a qtree-scoped rule of a type is created on a volume, a default rule of the same type is automatically added if it does not already exist on the volume. <br/>
The following example shows how to create a quota policy user rule using POST.
<br/>
---
```
# The API:
POST /api/storage/quota/rules
# The call:
curl -X POST 'https://<mgmt-ip>/api/storage/quota/rules?return_records=true' -H 'accept: application/hal+json' -d @test_quota_post.txt
test_quota_post.txt(body):
{
  "svm": {
    "name": "svm1"
  },
  "volume": {
    "name": "vol1"
  },
  "type": "user",
  "users": [ {"name" : "jsmith"} ],
  "qtree": {
    "name":"qt1"
  },
  "user_mapping": "on",
  "space": {
    "hard_limit": 8192,
    "soft_limit": 1024
  },
  "files": {
    "hard_limit": 20,
    "soft_limit": 10
  }
}
# The response
{
    "num_records": 1,
    "records": [
      {
        "svm": {
          "name": "svm1"
        },
        "volume": {
          "name": "fv"
        },
        "uuid": "3220eea6-5049-11e9-bfb7-005056a7f717",
        "type": "user",
        "users": [
          {
            "name" : "jsmith"
          }
        ],
        "qtree": {
          "name": "qt1"
        },
        "user_mapping": "on",
        "space": {
          "hard_limit": 8192,
          "soft_limit": 1024
        },
        "files": {
          "hard_limit": 20,
          "soft_limit": 10
        },
        "_links": {
          "self": {
            "href": "/api/storage/quota/rules/3220eea6-5049-11e9-bfb7-005056a7f717"
          }
        }
      }
    ],
    "job": {
      "uuid": "32223924-5049-11e9-bfb7-005056a7f717",
      "_links": {
        "self": {
          "href": "/api/cluster/jobs/32223924-5049-11e9-bfb7-005056a7f717"
        }
      }
    }
}
```
---
### Creating a quota policy group rule using POST.
<br/>
---
```
# The API:
POST /api/storage/quota/rules
# The call:
curl -X POST 'https://<mgmt-ip>/api/storage/quota/rules?return_records=true' -H 'accept: application/hal+json' -d @test_quota_post.txt
test_quota_post.txt(body):
{
  "svm": {
    "name": "svm1"
  },
  "volume": {
    "name": "vol1"
  },
  "type": "group",
  "group": {
    "name" : "test_group1"
  }
  "qtree": {
    "name":"qt1"
  },
  "space": {
    "hard_limit": 8192,
    "soft_limit": 1024
  },
  "files": {
    "hard_limit": 20,
    "soft_limit": 10
  }
}
# The response
{
    "num_records": 1,
    "records": [
      {
        "svm": {
          "name": "svm1"
        },
        "volume": {
          "name": "fv"
        },
        "uuid": "3b130f7d-504a-11e9-bfb7-005056a7f717",
        "type": "group",
        "group": {
            "name" : "test_group1"
        },
        "qtree": {
          "name": "qt1"
        },
        "space": {
          "hard_limit": 8192,
          "soft_limit": 1024
        },
        "files": {
          "hard_limit": 20,
          "soft_limit": 10
        },
        "_links": {
          "self": {
            "href": "/api/storage/quota/rules/3b130f7d-504a-11e9-bfb7-005056a7f717"
          }
        }
      }
    ],
    "job": {
      "uuid": "32223924-5049-11e9-bfb7-005056a7f717",
      "_links": {
        "self": {
          "href": "/api/cluster/jobs/32223924-5049-11e9-bfb7-005056a7f717"
        }
      }
    }
}
```
---
### Creating a quota policy tree rule using POST
<br/>
---
```
# The API:
POST /api/storage/quota/rules
# The call:
curl -X POST 'https://<mgmt-ip>/api/storage/quota/rules?return_records=true' -H 'accept: application/hal+json' -d @test_quota_post.txt
test_quota_post.txt(body):
{
  "svm": {
    "name": "svm1"
  },
  "volume": {
    "name": "vol1"
  },
  "type": "tree",
  "qtree": {
    "name":"qt1"
  },
  "space": {
    "hard_limit": 8192,
    "soft_limit": 1024
  },
  "files": {
    "hard_limit": 20,
    "soft_limit": 10
  }
}
# The response
{
    "num_records": 1,
    "records": [
      {
        "svm": {
          "name": "svm1"
        },
        "volume": {
          "name": "fv"
        },
        "uuid": "e5eb03be-504a-11e9-bfb7-005056a7f717",
        "type": "tree",
        "qtree": {
          "name": "qt1"
        },
        "space": {
          "hard_limit": 8192,
          "soft_limit": 1024
        },
        "files": {
          "hard_limit": 20,
          "soft_limit": 10
        },
        "_links": {
          "self": {
            "href": "/api/storage/quota/rules/e5eb03be-504a-11e9-bfb7-005056a7f717"
          }
        }
      }
    ],
    "job": {
      "uuid": "32223924-5049-11e9-bfb7-005056a7f717",
      "_links": {
        "self": {
          "href": "/api/cluster/jobs/32223924-5049-11e9-bfb7-005056a7f717"
        }
      }
    }
}
```
---
### Updating the quota policy rule
This API is used to update a quota policy rule.<br/>
The following example shows how to update a quota policy rule.
<br/>
---
```
# The API:
PATCH /storage/quota/rules/{uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/storage/quota/rules/364d38eb-8e87-11e8-a806-005056a7e73a" -H 'accept: application/hal+json' -d "@test_quota_patch.txt"
test_quota_patch.txt(body):
{
  "space": {
    "hard_limit": 16554,
    "soft_limit": 8192
  },
  "files": {
    "hard_limit": 40,
    "soft_limit": 20
  }
}
```
---
### Deleting the quota policy rule
This API is used to delete a quota policy rule.<br/>
The following example shows how to delete a quota policy rule.
<br/>
---
```
# The API:
DELETE /storage/quota/rules/{uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/storage/quota/rules/364d38eb-8e87-11e8-a806-005056a7e73a" -H 'accept: application/hal+json'
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


__all__ = ["QuotaRule", "QuotaRuleSchema"]
__pdoc__ = {
    "QuotaRuleSchema.resource": False,
    "QuotaRuleSchema.patchable_fields": False,
    "QuotaRuleSchema.postable_fields": False,
}


class QuotaRuleSchema(ResourceSchema):
    """The fields of the QuotaRule object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the quota_rule. """

    files = fields.Nested("netapp_ontap.models.quota_rule_files.QuotaRuleFilesSchema", data_key="files", unknown=EXCLUDE)
    r""" The files field of the quota_rule. """

    group = fields.Nested("netapp_ontap.models.quota_rule_group.QuotaRuleGroupSchema", data_key="group", unknown=EXCLUDE)
    r""" The group field of the quota_rule. """

    qtree = fields.Nested("netapp_ontap.models.quota_rule_qtree.QuotaRuleQtreeSchema", data_key="qtree", unknown=EXCLUDE)
    r""" The qtree field of the quota_rule. """

    space = fields.Nested("netapp_ontap.models.quota_rule_space.QuotaRuleSpaceSchema", data_key="space", unknown=EXCLUDE)
    r""" The space field of the quota_rule. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the quota_rule. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['tree', 'user', 'group']),
    )
    r""" This parameter specifies the quota policy rule type. This is required in POST only and can take either one of the \"user\", \"group\" or \"tree\" values.

Valid choices:

* tree
* user
* group """

    user_mapping = fields.Boolean(
        data_key="user_mapping",
    )
    r""" This parameter enables user mapping for user quota policy rules. This is valid in POST or PATCH for user quota policy rules only. """

    users = fields.List(fields.Nested("netapp_ontap.models.quota_report_users.QuotaReportUsersSchema", unknown=EXCLUDE), data_key="users")
    r""" This parameter specifies the target user to which the user quota policy rule applies. This parameter takes single or multiple user names or identifiers. This parameter is valid only for the POST operation of a user quota policy rule. If this parameter is used as an input to create a group or a tree quota policy rule, the POST operation will fail with an appropriate error. For POST, this input parameter takes either a user name or a user identifier, not both. For default quota rules, the user name must be chosen and specified as "". For explicit user quota rules, this parameter can indicate either a user name or user identifier. The user name can be a UNIX user name or a Windows user name. If a name contains a space, enclose the entire value in quotes. A UNIX user name cannot include a backslash (\) or an @ sign; user names with these characters are treated as Windows names. The user identifer can be a UNIX user identifier or a Windows security identifier. For multi-user quota, this parameter can contain multiple user targets separated by a comma. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Unique identifier for the quota policy rule. This field is generated when the quota policy rule is created.

Example: 5f1d13a7-f401-11e8-ac1a-005056a7c3b9 """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the quota_rule. """

    @property
    def resource(self):
        return QuotaRule

    @property
    def patchable_fields(self):
        return [
            "files",
            "space",
            "user_mapping",
        ]

    @property
    def postable_fields(self):
        return [
            "files",
            "group",
            "qtree.id",
            "qtree.name",
            "space",
            "svm.name",
            "svm.uuid",
            "type",
            "user_mapping",
            "users",
            "volume.name",
            "volume.uuid",
        ]

class QuotaRule(Resource):
    """Allows interaction with QuotaRule objects on the host"""

    _schema = QuotaRuleSchema
    _path = "/api/storage/quota/rules"
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
        r"""Retrieves quota policy rules configured for all FlexVol volumes and FlexGroup volumes.
### Related ONTAP commands
* `quota policy rule show`

### Learn more
* [`DOC /storage/quota/rules`](#docs-storage-storage_quota_rules)"""
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
        r"""Updates properties of a specific quota policy rule. <br>
Important notes:
* The quota resize functionality is supported with the PATCH operation.
* Quota resize allows you to modify the quota limits, directly in the filesystem.
* The quota must be enabled on a FlexVol or a FlexGroup volume for `quota resize` to take effect.
* If the quota is disabled on the volume, the quota policy rule PATCH API modifies the rule, but this does not affect the limits in the filesystem.
### Related ONTAP commands
* `quota policy rule modify`
* `quota resize`

### Learn more
* [`DOC /storage/quota/rules`](#docs-storage-storage_quota_rules)"""
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
        r"""Deletes a quota policy rule.
### Related ONTAP commands
* `quota policy rule delete`

### Learn more
* [`DOC /storage/quota/rules`](#docs-storage-storage_quota_rules)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves quota policy rules configured for all FlexVol volumes and FlexGroup volumes.
### Related ONTAP commands
* `quota policy rule show`

### Learn more
* [`DOC /storage/quota/rules`](#docs-storage-storage_quota_rules)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves properties for a specific quota policy rule.
### Related ONTAP commands
* `quota policy rule show`

### Learn more
* [`DOC /storage/quota/rules`](#docs-storage-storage_quota_rules)"""
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
        r"""Creates a quota policy rule for a FlexVol or a FlexGroup volume.<br/>
Important notes:
* Unlike CLI/ONTAPI, the `quota policy` input is not needed for POST.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the qtree.
* `volume.uuid` or `volume.name` - Existing volume in which to create the qtree.
* `type` - Quota type for the rule. This type can be `user`, `group`, or `tree`.
* `users.name` or `user.id` -  If the quota type is user, this property takes the user name or user ID. For default user quota rules, the user name must be specified as "".
* `group.name` or `group.id` - If the quota type is group, this property takes the group name or group ID. For default group quota rules, the group name must be specified as "".
* `qtree.name` - Qtree for which to create the rule. For default tree rules, the qtree name must be specified as "".
### Recommended optional properties
* `space.hard_limit` - Specifies the space hard limit, in bytes. If less than 1024 bytes, the value is rounded up to 1024 bytes.
* `space.soft_limit` - Specifies the space soft limit, in bytes. If less than 1024 bytes, the value is rounded up to 1024 bytes.
* `files.hard_limit` - Specifies the hard limit for files.
* `files.hard_limit` - Specifies the soft limit for files.
* `user_mapping` - Specifies the user_mapping. This property is valid only for quota policy rules of type `user`.
### Related ONTAP commands
* `quota policy rule create`

### Learn more
* [`DOC /storage/quota/rules`](#docs-storage-storage_quota_rules)"""
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
        r"""Updates properties of a specific quota policy rule. <br>
Important notes:
* The quota resize functionality is supported with the PATCH operation.
* Quota resize allows you to modify the quota limits, directly in the filesystem.
* The quota must be enabled on a FlexVol or a FlexGroup volume for `quota resize` to take effect.
* If the quota is disabled on the volume, the quota policy rule PATCH API modifies the rule, but this does not affect the limits in the filesystem.
### Related ONTAP commands
* `quota policy rule modify`
* `quota resize`

### Learn more
* [`DOC /storage/quota/rules`](#docs-storage-storage_quota_rules)"""
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
        r"""Deletes a quota policy rule.
### Related ONTAP commands
* `quota policy rule delete`

### Learn more
* [`DOC /storage/quota/rules`](#docs-storage-storage_quota_rules)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


