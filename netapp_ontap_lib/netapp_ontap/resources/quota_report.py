# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
Quota reports provide the current file and space consumption for a user, group, or qtree in a FlexVol or a FlexGroup volume.
## Quota report APIs
The following APIs can be used to retrieve quota reports associated with a volume in ONTAP.

* GET       /api/storage/quota/reports
* GET       /api/storage/quota/reports/{volume_uuid}/{index}
## Examples
### Retrieving all the quota report records
This API is used to retrieve all the quota report records. <br/>
The following example shows how to retrieve quota report records for all FlexVol volumes and FlexGroup volumes.
<br/>
---
```
# The API:
GET /api/storage/quota/reports
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/quota/reports"  -H 'accept: application/hal+json'
# The response:
  {
    "records": [
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "314a328f-502d-11e9-8771-005056a7f717",
          "name": "fg",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/314a328f-502d-11e9-8771-005056a7f717"
            }
          }
        },
        "index": 0,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/314a328f-502d-11e9-8771-005056a7f717/0"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "314a328f-502d-11e9-8771-005056a7f717",
          "name": "fg",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/314a328f-502d-11e9-8771-005056a7f717"
            }
          }
        },
        "index": 1152921504606846976,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/314a328f-502d-11e9-8771-005056a7f717/1152921504606846976"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "314a328f-502d-11e9-8771-005056a7f717",
          "name": "fg",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/314a328f-502d-11e9-8771-005056a7f717"
            }
          }
        },
        "index": 3458764513820540928,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/314a328f-502d-11e9-8771-005056a7f717/3458764513820540928"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "314a328f-502d-11e9-8771-005056a7f717",
          "name": "fg",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/314a328f-502d-11e9-8771-005056a7f717"
            }
          }
        },
        "index": 4611686018427387904,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/314a328f-502d-11e9-8771-005056a7f717/4611686018427387904"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "314a328f-502d-11e9-8771-005056a7f717",
          "name": "fg",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/314a328f-502d-11e9-8771-005056a7f717"
            }
          }
        },
        "index": 5764607523034234880,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/314a328f-502d-11e9-8771-005056a7f717/5764607523034234880"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 0,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/0"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 281474976710656,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/281474976710656"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 1152921504606846976,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/1152921504606846976"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 1153202979583557632,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/1153202979583557632"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 2305843013508661248,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/2305843013508661248"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 3458764513820540928,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/3458764513820540928"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 3459045988797251584,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/3459045988797251584"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 4611686018427387904,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/4611686018427387904"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 4611967493404098560,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/4611967493404098560"
          }
        }
      },
      {
        "svm": {
          "uuid": "b68f961b-4cee-11e9-930a-005056a7f717",
          "name": "svm1",
          "_links": {
            "self": {
              "href": "/api/svm/svms/b68f961b-4cee-11e9-930a-005056a7f717"
            }
          }
        },
        "volume": {
          "uuid": "cb20da45-4f6b-11e9-9a71-005056a7f717",
          "name": "fv",
          "_links": {
            "self": {
              "href": "/api/storage/volumes/cb20da45-4f6b-11e9-9a71-005056a7f717"
            }
          }
        },
        "index": 5764607523034234880,
        "_links": {
          "self": {
            "href": "/api/storage/quota/reports/cb20da45-4f6b-11e9-9a71-005056a7f717/5764607523034234880"
          }
        }
      }
    ],
    "num_records": 15,
    "_links": {
      "self": {
        "href": "/api/storage/quota/reports/"
      }
    }
  }
```
---
### Retrieving a specific quota report record
This API is used to retrieve a specific quota report record. <br/>
The following example shows how to retrieve a single quota report user record.
<br/>
---
```
# The API:
GET /api/storage/quota/reports/{volume.uuid}/{index}
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/281474976710656"  -H 'accept: application/hal+json'
# Response for quota report user record:
{
  "svm": {
    "uuid": "5093e722-248e-11e9-96ee-005056a7657c",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/5093e722-248e-11e9-96ee-005056a7657c"
      }
    }
  },
  "volume": {
    "uuid": "cf480c37-2a6b-11e9-8513-005056a7657c",
    "name": "fv",
    "_links": {
      "self": {
        "href": "/api/storage/volumes/cf480c37-2a6b-11e9-8513-005056a7657c"
      }
    }
  },
  "index": 281474976710656,
  "type": "user",
  "users": [
    {
      "name": "fred",
      "id"  : "300008"
    }
  ],
  "qtree": {
    "name": "qt1",
    "id": 1,
    "_links": {
      "self": {
        "href": "/api/storage/qtrees/cf480c37-2a6b-11e9-8513-005056a7657c/1"
      }
    }
  },
  "space": {
    "hard_limit": 41943040,
    "soft_limit": 31457280,
    "used": {
      "total": 10567680,
      "soft_limit_percent": 34,
      "hard_limit_percent": 25
    }
  }
  "files": {
    "soft_limit": 30,
    "hard_limit": 40,
    "used": {
      "total": 11,
      "soft_limit_percent": 37,
      "hard_limit_percent": 28
    }
  }
  "_links": {
    "self": {
      "href": "/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/281474976710656"
      }
    }
  }
}
```
---
### Retrieving a single quota report multi-user record
<br/>
---
```
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/281474976710656"  -H 'accept: application/hal+json'
# Response for quota report multi-user record:
{
  "svm": {
    "uuid": "5093e722-248e-11e9-96ee-005056a7657c",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/5093e722-248e-11e9-96ee-005056a7657c"
      }
    }
  },
  "volume": {
    "uuid": "cf480c37-2a6b-11e9-8513-005056a7657c",
    "name": "fv",
    "_links": {
      "self": {
        "href": "/api/storage/volumes/cf480c37-2a6b-11e9-8513-005056a7657c"
      }
    }
  },
  "index": 1153484454560268288,
  "type": "user",
  "users": [
    {
      "name": "fred",
      "id"  : "300008"
    },
    {
      "name": "john",
      "id"  : "300009"
    },
    {
      "name": "smith",
      "id"  : "300010"
    }
  ],
  "qtree": {
    "name": "qt1",
    "id": 1,
    "_links": {
      "self": {
        "href": "/api/storage/qtrees/cf480c37-2a6b-11e9-8513-005056a7657c/1"
      }
    }
  },
  "space": {
    "hard_limit": 41943040,
    "soft_limit": 31457280,
    "used": {
      "total": 10567680,
      "soft_limit_percent": 34,
      "hard_limit_percent": 25
    }
  }
  "files": {
    "soft_limit": 30,
    "hard_limit": 40,
    "used": {
      "total": 11,
      "soft_limit_percent": 37,
      "hard_limit_percent": 28
    }
  }
  "_links": {
    "self": {
      "href": "/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/1153484454560268288"
      }
    }
  }
}
```
---
### Retrieving a single quota report group record
<br/>
---
```
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/3459045988797251584"  -H 'accept: application/hal+json'
# Response for quota report group record:
{
  "svm": {
    "uuid": "5093e722-248e-11e9-96ee-005056a7657c",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/5093e722-248e-11e9-96ee-005056a7657c"
      }
    }
  },
  "volume": {
    "uuid": "cf480c37-2a6b-11e9-8513-005056a7657c",
    "name": "fv",
    "_links": {
      "self": {
        "href": "/api/storage/volumes/cf480c37-2a6b-11e9-8513-005056a7657c"
      }
    }
  },
  "index": 3459045988797251584,
  "type": "group",
  "group": {
    "name"  : "test_group",
    "id"    : "500009"
  },
  "qtree": {
    "name": "qt1",
    "id": 1,
    "_links": {
      "self": {
        "href": "/api/storage/qtrees/cf480c37-2a6b-11e9-8513-005056a7657c/1"
      }
    }
  },
  "space": {
    "hard_limit": 41943040,
    "soft_limit": 31457280,
    "used": {
      "total": 10567680,
      "soft_limit_percent": 34,
      "hard_limit_percent": 25
    }
  }
  "files": {
    "soft_limit": 30,
    "hard_limit": 40,
    "used": {
      "total": 11,
      "soft_limit_percent": 37,
      "hard_limit_percent": 28
    }
  }
  "_links": {
    "self": {
      "href": "/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/3459045988797251584"
      }
    }
  }
}
```
---
### Retrieving a single quota report tree record
<br/>
---
```
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/4612248968380809216"  -H 'accept: application/hal+json'
# Response for quota report tree record:
{
  "svm": {
    "uuid": "5093e722-248e-11e9-96ee-005056a7657c",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/5093e722-248e-11e9-96ee-005056a7657c"
      }
    }
  },
  "volume": {
    "uuid": "cf480c37-2a6b-11e9-8513-005056a7657c",
    "name": "fv",
    "_links": {
      "self": {
        "href": "/api/storage/volumes/cf480c37-2a6b-11e9-8513-005056a7657c"
      }
    }
  },
  "index": 4612248968380809216,
  "type": "tree",
  "qtree": {
    "name": "qt1",
    "id": 1,
    "_links": {
      "self": {
        "href": "/api/storage/qtrees/cf480c37-2a6b-11e9-8513-005056a7657c/1"
      }
    }
  },
  "space": {
    "hard_limit": 41943040,
    "soft_limit": 31457280,
    "used": {
      "total": 10567680,
      "soft_limit_percent": 34,
      "hard_limit_percent": 25
    }
  }
  "files": {
    "soft_limit": 30,
    "hard_limit": 40,
    "used": {
      "total": 11,
      "soft_limit_percent": 37,
      "hard_limit_percent": 28
    }
  }
  "_links": {
    "self": {
      "href": "/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/4612248968380809216"
      }
    }
  }
}
```
---
### Retrieving only records enforced by non-default rules
<br/>
---
```
# The call:
curl -X GET "https://<mgmt-ip>/api/storage/quota/reports?show_default_records=false"  -H 'accept: application/hal+json'
# Response from only  non-default records
{
  "svm": {
    "uuid": "5093e722-248e-11e9-96ee-005056a7657c",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/5093e722-248e-11e9-96ee-005056a7657c"
      }
    }
  },
  "volume": {
    "uuid": "cf480c37-2a6b-11e9-8513-005056a7657c",
    "name": "fv",
    "_links": {
      "self": {
        "href": "/api/storage/volumes/cf480c37-2a6b-11e9-8513-005056a7657c"
      }
    }
  },
  "index": 4612248968380809216,
  "type": "tree",
  "qtree": {
    "name": "qt1",
    "id": 1,
    "_links": {
      "self": {
        "href": "/api/storage/qtrees/cf480c37-2a6b-11e9-8513-005056a7657c/1"
      }
    }
  },
  "space": {
    "hard_limit": 41943040,
    "soft_limit": 31457280,
    "used": {
      "total": 10567680,
      "soft_limit_percent": 34,
      "hard_limit_percent": 25
    }
  }
  "files": {
    "soft_limit": 30,
    "hard_limit": 40,
    "used": {
      "total": 11,
      "soft_limit_percent": 37,
      "hard_limit_percent": 28
    }
  }
  "_links": {
    "self": {
      "href": "/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/4612248968380809216"
      }
    }
  }
},
{
  "svm": {
    "uuid": "5093e722-248e-11e9-96ee-005056a7657c",
    "name": "svm1",
    "_links": {
      "self": {
        "href": "/api/svm/svms/5093e722-248e-11e9-96ee-005056a7657c"
      }
    }
  },
  "volume": {
    "uuid": "cf480c37-2a6b-11e9-8513-005056a7657c",
    "name": "fv",
    "_links": {
      "self": {
        "href": "/api/storage/volumes/cf480c37-2a6b-11e9-8513-005056a7657c"
      }
    }
  },
  "index": 1153484454560268288,
  "type": "user",
  "users": [
    {
      "name": "fred",
      "id"  : "300008"
    },
    {
      "name": "john",
      "id"  : "300009"
    },
    {
      "name": "smith",
      "id"  : "300010"
    }
  ],
  "qtree": {
    "name": "qt1",
    "id": 1,
    "_links": {
      "self": {
        "href": "/api/storage/qtrees/cf480c37-2a6b-11e9-8513-005056a7657c/1"
      }
    }
  },
  "space": {
    "hard_limit": 41943040,
    "soft_limit": 31457280,
    "used": {
      "total": 10567680,
      "soft_limit_percent": 34,
      "hard_limit_percent": 25
    }
  }
  "files": {
    "soft_limit": 30,
    "hard_limit": 40,
    "used": {
      "total": 11,
      "soft_limit_percent": 37,
      "hard_limit_percent": 28
    }
  }
  "_links": {
    "self": {
      "href": "/api/storage/quota/reports/cf480c37-2a6b-11e9-8513-005056a7657c/1153484454560268288"
      }
    }
  }
}
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


__all__ = ["QuotaReport", "QuotaReportSchema"]
__pdoc__ = {
    "QuotaReportSchema.resource": False,
    "QuotaReportSchema.patchable_fields": False,
    "QuotaReportSchema.postable_fields": False,
}


class QuotaReportSchema(ResourceSchema):
    """The fields of the QuotaReport object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the quota_report. """

    files = fields.Nested("netapp_ontap.models.quota_report_files.QuotaReportFilesSchema", data_key="files", unknown=EXCLUDE)
    r""" The files field of the quota_report. """

    group = fields.Nested("netapp_ontap.models.quota_report_group.QuotaReportGroupSchema", data_key="group", unknown=EXCLUDE)
    r""" The group field of the quota_report. """

    index = fields.Integer(
        data_key="index",
    )
    r""" Index that identifies a unique quota record. Valid in URL. """

    qtree = fields.Nested("netapp_ontap.models.quota_rule_qtree.QuotaRuleQtreeSchema", data_key="qtree", unknown=EXCLUDE)
    r""" The qtree field of the quota_report. """

    space = fields.Nested("netapp_ontap.models.quota_report_space.QuotaReportSpaceSchema", data_key="space", unknown=EXCLUDE)
    r""" The space field of the quota_report. """

    specifier = fields.Str(
        data_key="specifier",
    )
    r""" Quota specifier """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the quota_report. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['tree', 'user', 'group']),
    )
    r""" Quota type associated with the quota record.

Valid choices:

* tree
* user
* group """

    users = fields.List(fields.Nested("netapp_ontap.models.quota_report_users.QuotaReportUsersSchema", unknown=EXCLUDE), data_key="users")
    r""" This parameter specifies the target user or users associated with the given quota report record. This parameter is available for user quota records and is not available for group or tree quota records. The target user or users are identified by a user name and user identifier. The user name can be a UNIX user name or a Windows user name, and the identifer can be a UNIX user identifier or a Windows security identifier. """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the quota_report. """

    @property
    def resource(self):
        return QuotaReport

    @property
    def patchable_fields(self):
        return [
            "files",
            "group",
            "qtree.id",
            "qtree.name",
            "space",
            "svm.name",
            "svm.uuid",
            "users",
            "volume.name",
            "volume.uuid",
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
            "users",
            "volume.name",
            "volume.uuid",
        ]

class QuotaReport(Resource):
    """Allows interaction with QuotaReport objects on the host"""

    _schema = QuotaReportSchema
    _path = "/api/storage/quota/reports"
    @property
    def _keys(self):
        return ["volume.uuid", "index"]

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
        r"""Retrieves the quota report records for all FlexVol volumes and FlexGroup volumes.
### Related ONTAP commands
* `quota report`

### Learn more
* [`DOC /storage/quota/reports`](#docs-storage-storage_quota_reports)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the quota report records for all FlexVol volumes and FlexGroup volumes.
### Related ONTAP commands
* `quota report`

### Learn more
* [`DOC /storage/quota/reports`](#docs-storage-storage_quota_reports)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific quota report record.
### Related ONTAP commands
* `quota report`

### Learn more
* [`DOC /storage/quota/reports`](#docs-storage-storage_quota_reports)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





