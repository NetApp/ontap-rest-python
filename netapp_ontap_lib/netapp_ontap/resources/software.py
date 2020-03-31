# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
You can use the ONTAP cluster software API to retrieve and display relevant information about a software profile, software packages collection, and software history collection. This API retrieves the information about all software packages present in the cluster, or a specific software package.
<br/>You can use the POST request to download a software package from an HTTP or FTP server. The PATCH request provides the option to upgrade the cluster software version. Select the `validate_only` field to validate the package before triggering the update. Set the `version` field to trigger the installation of the package in the cluster. You can pause, resume, or cancel any ongoing software upgrade by selecting `action`. You can use the DELETE request to remove a specific software package present in the cluster.
---
## Examples
### Retrieving software profile information
The following example shows how to retrieve software profile information. You can check the validation results after selecting the `validate_only` field. Upgrade progress information is available after an upgrade has started.
<br/>
```
# The API:
/api/cluster/software
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/software?return_timeout=15" -H "accept: application/hal+json"
# The response:
{
  "validation_results": [
   {
     "update_check": "NFS mounts",
     "status": "warning",
     "issue": {
         "code": 166,
         "message": "Use NFS hard mounts, if possible.",
       }
     ,
     "action": {
         "code": 166,
         "message": "Use NFS hard mounts, if possible.",
     }
   }
  ],
  "version": "9.5.0",
  "pending_version": "9.6.0",
  "nodes": [
    {
      "node": "sti70-vsim-ucs165n",
      "version": "9.5.0"
    }
  ],
  "metrocluster": {
    "progress_summary": {
            "message": "Update paused by user"
     },
    "progress_details": {
            "message": "Installing software image on cluster \"sti70-vsim-ucs165n_siteA\"."
     },
    "clusters": [
      {
        "name": "sti70-vsim-ucs165n_siteA",
        "uuid": "720f046c-4b13-11e9-9c34-005056ac5626",
        "estimated_duration": 3480,
        "elapsed_duration": 0,
        "state": "waiting"
      },
    ]
  },
  "state": "in_progress",
  "start_time": "2018-05-21T09:53:04+05:30",
  "end_time": "2018-05-21T11:53:04+05:30",
  "estimated_time": 5220,
  "elapsed_time": 2140,
  "update_details": [
    {
      "phase": "Data ONTAP updates",
      "state": "in_progress",
      "estimated_duration": 4620,
      "elapsed_duration": 29,
      "node": {
        "name": "sti70-vsim-ucs165n"
      }
    }
  ],
  "status_details": [
    {
      "name": "do-download-job",
      "state": "completed",
      "issue": {
              "message": "Image update complete"
       },
      "start_time": "2018-05-21T09:53:04+05:30",
      "end_time": "2018-05-21T11:53:04+05:30",
      "node": {
        "name": "sti70-vsim-ucs165n"
      }
    }
  ],
  "_links": {
    "self": {
      "href": "/api/cluster/software/"
    }
  }
}
```
---
### Upgrading the software version
The following example shows how to upgrade cluster software. Set the `version` field to trigger the installation of the package. You can select the `validate_only` field to validate the package before the installation starts. Setting `skip_warning` as `true` ignores the validation warning before the installation starts. Setting the `action` field performs a `pause`, `resume`, or `cancel' operation on an ongoing upgrade. An upgrade can only be resumed if it is in the paused state.
<br/>You can start the upgrade process at the cluster level. There are no options available to start the upgrade for a specific node or HA pair.
#### 1. Validating the package and verifying the validation results
The following example shows how to validate a cluster software package. You must validate the package before the software upgrade. Set the `validate_only` field to `true` to start the validation. You can check for validation results in the GET /cluster/software endpoint.
<br/>
```
# The API:
/api/cluster/software
# The call:
curl -X PATCH "https://<mgmt_ip>/api/cluster/software?validate_only=true" -H "accept: application/json" -H "Content-Type: application/hal+json" -d '{ "version": "9.5.0"}'
# The response:
{
  "job": {
    "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
      }
    }
  }
}
```
---
The call to validate the software cluster version returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the `state` field of the job is set to `success`.
<br/>
```
# The API:
/api/cluster/jobs/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc" -H "accept: application/hal+json"
# The response:
{
  "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
  "description": "PATCH /api/cluster/software",
  "state": "success",
  "message": "success",
  "code": 0,
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
    }
  }
}
```
---
You can check for validation results in the GET /cluster/software endpoint. The following example shows how to check the validation warnings and errors after setting the `validate_only` field to `true`.
<br/>
```
# The API:
/api/cluster/software
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/software" -H "accept: application/hal+json"
# The response:
{
  "version": "9.7.0",
  "validation_results": [
    {
      "update_check": "High Availability status",
      "status": "error",
      "issue": {
        "message": "Cluster HA is not configured in the cluster. Storage failover is not enabled on node \"node1\", \"node2\".",
      },
      "action": {
        "message": "Check cluster HA configuration. Check storage failover status."
      }
    },
    {
      "update_check": "Manual checks",
      "status": "warning",
      "issue" : {
        "message": "Manual validation checks need to be performed. Refer to the Upgrade Advisor Plan or \"Performing manual checks before an automated cluster upgrade\" section in the \"Clustered Data ONTAP Upgrade Express Guide\" for the remaining validation checks that need to be performed before update. Failing to do so can result in an update failure or an I/O disruption."
      },
      "action": {
        "message": "Refer to the Upgrade Advisor Plan or \"Performing manual checks before an automated cluster upgrade\" section in the \"Clustered Data ONTAP Upgrade Express Guide\" for the remaining validation checks that need to be performed before update."
      }
    }
  ],
  "nodes": [
    {
      "node": "node1",
      "version": "9.7.0"
    },
    {
      "node": "node2",
      "version": "9.7.0"
    }
  ],
  "state": "failed",
  "elapsed_duration": 56,
  "estimated_duration": 600,
  "_links": {
    "self": {
      "href": "/api/cluster/software"
    }
  }
}
```
---
#### 2. Updating the cluster
The following example shows how to initiate a cluster software upgrade. You must validate the package before the software upgrade starts. Set the `skip_warnings` field to `true` to skip validation warnings and start the software package upgrade.
<br/>
```
# The API:
/api/cluster/software
# The call:
curl -X PATCH "https://<mgmt_ip>/api/cluster/software?skip_warnings=true" -H "accept: application/json" -H "Content-Type: application/hal+json" -d '{ "version": "9.5.0"}'
# The response:
{
  "job": {
    "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
      }
    }
  }
}
```
---
The call to update the software cluster version returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the `state` field of the job is set to `success`.
<br/>
```
# The API:
/api/cluster/jobs/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc" -H "accept: application/hal+json"
# The response:
{
  "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
  "description": "PATCH /api/cluster/software",
  "state": "success",
  "message": "success",
  "code": 0,
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
    }
  }
}
```
---
You can check the update progress information in the GET /cluster/software endpoint. The following example shows how to check the progress of an update after setting the `skip_warnings` field to `true`.      <br/>
```
# The API:
/api/cluster/software
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/software" -H "accept: application/hal+json"
# The response:
{
  "version": "9.7.0",
  "validation_results": [
    {
      "update_check": "Manual checks",
      "status": "warning",
      "issue" : {
        "message": "Manual validation checks need to be performed. Refer to the Upgrade Advisor Plan or \"Performing manual checks before an automated cluster upgrade\" section in the \"Clustered Data ONTAP Upgrade Express Guide\" for the remaining validation checks that need to be performed before update. Failing to do so can result in an update failure or an I/O disruption."
      },
      "action": {
        "message": "Refer to the Upgrade Advisor Plan or \"Performing manual checks before an automated cluster upgrade\" section in the \"Clustered Data ONTAP Upgrade Express Guide\" for the remaining validation checks that need to be performed before update."
      }
    }
  ],
  "nodes": [
    {
      "node": "node1",
      "version": "9.7.0"
    },
    {
      "node": "node2",
      "version": "9.7.0"
    }
  ],
  "pending_version": "9.7.0",
  "state": "in_progress",
  "elapsed_duration": 63,
  "estimated_duration": 5220,
  "status_details": [
    {
      "name": "do-download-job",
      "status": "running",
      "issue": {
              "message": "Installing software image."
       },
      "start_time": "2019-01-14T23:12:14+05:30",
      "end_time": "2019-01-14T23:12:14+05:30",
      "node": {
        "name": "node1"
      }
    },
    {
      "name": "do-download-job",
      "status": "running",
      "issue": {
              "message": "Installing software image."
      },
      "start_time": "2019-01-14T23:12:14+05:30",
      "end_time": "2019-01-14T23:12:14+05:30",
      "node": {
        "name": "node2"
      }
    }
  ],
  "update_details": [
    {
      "phase": "Data ONTAP updates",
      "status": "in-progress",
      "estimated_duration": 4620,
      "elapsed_duration": 10,
      "node": {
        "name": "node1"
      }
    },
    {
      "phase": "Data ONTAP updates",
      "status": "in-progress",
      "estimated_duration": 4620,
      "elapsed_duration": 10,
      "node": {
        "name": "node2"
      }
    }
  ],
  "_links": {
    "self": {
      "href": "/api/cluster/software"
    }
  }
}
```
---
#### 3. Pausing/resuming/canceling the upgrade
The following example shows how to `pause` an ongoing cluster software package upgrade. Set the `action` field to `pause`, `resume`, or `cancel` to pause, resume or cancel the upgrade respectively. Not all update operations support these actions. An update can only be resumed if it is in the paused state.
<br/>
```
# The API:
/api/cluster/software
# The call:
curl -X PATCH "https://<mgmt_ip>/api/cluster/software?action=pause" -H "accept: application/json" -H "Content-Type: application/hal+json" -d '{ "version": "9.5.0"}'
# The response:
{
  "job": {
    "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
      }
    }
  }
}
```
---
The call to update the software cluster version returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the `state` field of the job is set to `success`.
<br/>
```
# The API:
/api/cluster/jobs/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc" -H "accept: application/hal+json"
# The response:
{
  "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
  "description": "PATCH /api/cluster/software",
  "state": "success",
  "message": "success",
  "code": 0,
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
    }
  }
}
```
---
You can check the progress of the upgrade in the GET /cluster/software endpoint. The following example shows how to check the progress of the pause upgrade state after setting the `action` field to `pause`.
<br/>
```
# The API:
/api/cluster/software
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/software" -H "accept: application/hal+json"
# The response:
{
  "version": "9.7.0",
  "validation_results": [
    {
      "update_check": "Manual checks",
      "status": "warning",
      "issue" : {
        "message": "Manual validation checks need to be performed. Refer to the Upgrade Advisor Plan or \"Performing manual checks before an automated cluster upgrade\" section in the \"Clustered Data ONTAP Upgrade Express Guide\" for the remaining validation checks that need to be performed before update. Failing to do so can result in an update failure or an I/O disruption."
      },
      "action": {
        "message": "Refer to the Upgrade Advisor Plan or \"Performing manual checks before an automated cluster upgrade\" section in the \"Clustered Data ONTAP Upgrade Express Guide\" for the remaining validation checks that need to be performed before update."
      }
    }
  ],
  "nodes": [
    {
      "node": "node1",
      "version": "9.7.0"
    },
    {
      "node": "node2",
      "version": "9.7.0"
    }
  ],
  "pending_version": "9.7.0",
  "state": "pause_pending",
  "elapsed_duration": 103,
  "estimated_duration": 5220,
  "status_details": [
    {
      "status": "in-progress",
      "issue": {
              "message": "Installing software image."
       },
      "start_time": "2019-01-08T02:54:36+05:30",
      "node": {
        "name": "node1"
      }
    },
    {
      "status": "in-progress",
      "issue": {
              "message": "Installing software image."
       },
      "start_time": "2019-01-08T02:54:36+05:30",
      "node": {
        "name": "node2"
      }
    }
  ],
  "update_details": [
    {
      "phase": "Pre-update checks",
      "status": "completed",
      "estimated_duration": 600,
      "elapsed_duration": 54,
      "node": {
        "name": "node1"
      }
    },
    {
      "phase": "Data ONTAP updates",
      "status": "pause-pending",
      "estimated_duration": 4620,
      "elapsed_duration": 49,
      "node": {
        "name": "node2"
      }
    },
    {
      "phase": "Data ONTAP updates",
      "status": "pause-pending",
      "estimated_duration": 4620,
      "elapsed_duration": 49
    }
  ],
  "_links": {
    "self": {
      "href": "/api/cluster/software"
    }
  }
}
```
---
### Downloading the software package
The following example shows how to download the software package from an HTTP or FTP server. Provide the `url`, `username`, and `password`, if required, to start the download of the software package to the cluster.
<br/>
```
# The API:
/api/cluster/software/download
# The call:
curl -X POST "https://<mgmt-ip>/api/cluster/software/download?return_timeout=0" -H "accept: application/json" -H "Content-Type: application/hal+json" -d '{ "url": "http://nbsweb.eng.btc.netapp.in/~suvadipd/99/image1.tgz", "username": "admin", "password": "*********"}'
# The response:
{
  "job": {
    "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
      }
    }
  }
}
```
---
The call to download the software package returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the job `state` field is set to `success`.
<br/>
```
# The API:
/api/cluster/jobs/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc" -H "accept: application/hal+json"
# The response:
{
  "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
  "description": "POST /api/cluster/software/download",
  "state": "success",
  "message": "success",
  "code": 0,
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
    }
  }
}
```
---
### Checking the progress of the software package being downloaded from an HTTP or FTP server
The following example shows how to retrieve the progress status of the software package being
downloaded from a HTTP or FTP server.
<br/>
```
# The API:
/api/cluster/software/download
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/software/download" -H "accept: application/hal+json"
# The response:
{
  "state": "running",
  "message": "Package download in progress",
  "code": 10551760,
  "_links": {
    "self": {
      "href": "/api/cluster/software/download"
    }
  }
}
```
---
### Retrieving cluster software packages information
The following example shows how to retrieve the ONTAP software packages in a cluster.
<br/>
```
# The API:
/api/cluster/software/packages
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/software/packages?return_records=true&return_timeout=15" -H "accept: application/hal+json"
# The response:
{
  "records": [
    {
      "version": "9.7.0",
      "_links": {
        "self": {
          "href": "/api/cluster/software/packages/9.7.0"
        }
      }
    },
    {
      "version": "9.5.0",
      "_links": {
        "self": {
          "href": "/api/cluster/software/packages/9.5.0"
        }
      }
    }
  ],
  "num_records": 2,
  "_links": {
    "self": {
      "href": "/api/cluster/software/packages"
    }
  }
}
```
---
The following example shows how to retrieve the details of a given cluster software package.
<br/>
```
# The API:
/api/cluster/software/packages/{version}
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/software/packages/9.7.0" -H "accept: application/hal+json"
# The response:
{
  "version": "9.7.0",
  "create_time": "2018-05-21T10:06:59+05:30",
  "_links": {
    "self": {
      "href": "/api/cluster/software/packages/9.7.0"
    }
  }
}
```
---
### Deleting a cluster software package
The following example shows how to delete a package from the cluster. You need to provide the package version that you want to delete. The software package delete creates a job to perform the delete operation.
<br/>
```
# The API:
/api/cluster/software/packages/{version}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/cluster/software/packages/9.6.0" -H "accept: application/hal+json"
# The response:
{
  "job": {
    "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
      }
    }
  }
}
```
---
The call to delete the package returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the job `state` field is set to `success`.
<br/>
```
# The API:
/api/cluster/jobs/{uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc" -H "accept: application/hal+json"
# The response:
{
  "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
  "description": "DELETE /api/cluster/software/packages/9.6.0",
  "state": "success",
  "message": "success",
  "code": 0,
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"
    }
  }
}
```
---
#### HTTPS error codes
The following is a list of possible error codes that can be returned during a package delete operation.
<br/>
```
# ONTAP Error Response codes
| ----------- | -------------------------------------------------------- |
| Error codes |                     Description                          |
| ----------- | -------------------------------------------------------- |
| 10551315    | Package store is empty                                   |
| 10551322    | Error in retrieving package cleanup status               |
| 10551323    | Error in cleaning up package information on a node       |
| 10551324    | Error in cleaning up package information on both nodes   |
| 10551325    | Package does not exist on the system                     |
| 10551326    | Error in deleting older package cleanup tasks            |
| 10551346    | Package delete failed since a validation is in progress  |
| 10551347    | Package delete failed since an update is in progress     |
| 10551367    | A package synchronization is in progress                 |
| 10551388    | Package delete operation timed out                       |
| ----------- | -------------------------------------------------------- |
```
---
### Retrieving software installation history information
The following example shows how to:
   - retrieve the software package installation history information.
   - display specific node level software installation history information.
   - provide all the attributes by default in response when the self referential link is not present.
<br/>
```
# The API:
/api/cluster/software/history
# The call:
curl -X GET "https://<mgmt-ip>/api/cluster/software/history" -H "accept: application/hal+json"
# The response:
{
  "node": {
    "uuid": "58cd3a2b-af63-11e8-8b0d-0050568e7279",
    "name": "sti70-vsim-ucs165n",
    "_links": {
      "self": {
        "href": "/api/cluster/nodes/58cd3a2b-af63-11e8-8b0d-0050568e7279"
      }
    }
  },
  "start_time": "2018-09-03T16:18:46+05:30",
  "state": "successful"
  "from_version": "9.4.0",
  "to_version": "9.5.0",
  "end_time": "2018-05-21T10:14:51+05:30"
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


__all__ = ["Software", "SoftwareSchema"]
__pdoc__ = {
    "SoftwareSchema.resource": False,
    "SoftwareSchema.patchable_fields": False,
    "SoftwareSchema.postable_fields": False,
}


class SoftwareSchema(ResourceSchema):
    """The fields of the Software object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the software. """

    action = fields.Str(
        data_key="action",
        validate=enum_validation(['pause', 'cancel', 'resume']),
    )
    r""" User triggered action to apply to the install operation

Valid choices:

* pause
* cancel
* resume """

    elapsed_duration = fields.Integer(
        data_key="elapsed_duration",
    )
    r""" Elapsed time during the upgrade or validation operation

Example: 2140 """

    estimated_duration = fields.Integer(
        data_key="estimated_duration",
    )
    r""" Estimated time remaining until completion of the upgrade or validation operation.

Example: 5220 """

    metrocluster = fields.Nested("netapp_ontap.models.software_reference_metrocluster.SoftwareReferenceMetroclusterSchema", data_key="metrocluster", unknown=EXCLUDE)
    r""" The metrocluster field of the software. """

    nodes = fields.List(fields.Nested("netapp_ontap.models.software_node.SoftwareNodeSchema", unknown=EXCLUDE), data_key="nodes")
    r""" List of nodes and active versions. """

    pending_version = fields.Str(
        data_key="pending_version",
    )
    r""" Version being installed on the system.

Example: ONTAP_X_1 """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['in_progress', 'waiting', 'paused_by_user', 'paused_on_error', 'completed', 'canceled', 'failed', 'pause_pending', 'cancel_pending']),
    )
    r""" Operational state of the upgrade

Valid choices:

* in_progress
* waiting
* paused_by_user
* paused_on_error
* completed
* canceled
* failed
* pause_pending
* cancel_pending """

    status_details = fields.List(fields.Nested("netapp_ontap.models.software_status_details.SoftwareStatusDetailsSchema", unknown=EXCLUDE), data_key="status_details")
    r""" Display status details. """

    update_details = fields.List(fields.Nested("netapp_ontap.models.software_update_details.SoftwareUpdateDetailsSchema", unknown=EXCLUDE), data_key="update_details")
    r""" Display update progress details. """

    validation_results = fields.List(fields.Nested("netapp_ontap.models.software_validation.SoftwareValidationSchema", unknown=EXCLUDE), data_key="validation_results")
    r""" List of validation warnings, errors, and advice. """

    version = fields.Str(
        data_key="version",
    )
    r""" Version of ONTAP installed and currently active on the system. During PATCH, using the 'validate_only' parameter on the request executes pre-checks, but does not perform the full installation.

Example: ONTAP_X """

    @property
    def resource(self):
        return Software

    @property
    def patchable_fields(self):
        return [
            "action",
            "metrocluster",
            "version",
        ]

    @property
    def postable_fields(self):
        return [
            "action",
            "metrocluster",
            "version",
        ]

class Software(Resource):
    """Allows interaction with Software objects on the host"""

    _schema = SoftwareSchema
    _path = "/api/cluster/software"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the software profile of a cluster.
### Related ONTAP commands
* `cluster image show`
* `cluster image show-update-progress`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member


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
        r"""Updates the cluster software version.
Important note:
  * Setting 'version' triggers the package installation.
  * To validate the package for installation but not perform the installation, use the `validate_only` field on the request.
### Required properties
* `version` - Software version to be installed on the cluster.
### Recommended optional parameters
* `validate_only` - Required to validate a software package before an upgrade.
* `skip_warnings` - Used to skip validation warnings when starting a software upgrade.
* `action` - Used to pause, resume, or cancel an ongoing software upgrade.
### Related ONTAP commands
* `cluster image validate`
* `cluster image update`
* `cluster image pause-update`
* `cluster image resume-update`
* `cluster image cancel-update`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



