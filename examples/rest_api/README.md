# ONTAP REST API Python Examples

The repository folder **rest_api** contains samples scripts you can refer to understand how the ONTAP REST API can be accessed using the requests library.

## Preparation

Before running the example scripts , make sure the following packages are installed:

* requests 2.21.0 or later
* texttable 1.6.2 or later
* python-dateutil

## Summary of the REST API scripts

The following table summaries the scripts used to access the ONTAP REST API . Make sure to run each of the scripts with the appropriate parameters.

**Note:** [**utils.py**](https://github.com/NetApp/ontap-rest-python/blob/master/examples/rest_api/utils.py) module in this directory is used by the other example modules in this directory. It is not meant as a stand-alone application. Hence, the utils.py code module needs to be in the same directory structure as of the code executed by the user.

Master Page for ONTAP REST - https://devnet.netapp.com/restapi.php

For e.g: If user executes list_volumes.py code in a directory structure a/b/c, ensure utils.py code exists in the same directory a/b/c.

## Day 0 Scripts:

| Script                               | Description       |
|:------------------------------------|:-------------|
| aggregate_operations.py  	           | Demonstrates aggregate creation, deletion, updation and listing using ONTAP REST API      |
| interface_operations.py              | Demonstrates interface creation, deletion, updation and listing using ONTAP REST API.      |    
| license_operations.py                | Demonstrates license creation, deletion and listing using ONTAP REST API      |    
| ndu_upgrade.py                | Demonstrates cluster software upgrade using ONTAP REST API      |    


## Day 1 Scripts:

| Script                               | Description       |
|:------------------------------------|:-------------|
| account_operations.py    	           | Demonstrates user account creation, deletion, updation and listing using ONTAP REST API      |
| cifs_setup.py            			   | Demonstrates how CIFS shares can be setup using ONTAP REST API. It creates a volume and then creates a share on the volume. |
| file_analytics_enable_disable.py              | Demonstrates enabling and disabling of File System analytics using ONTAP REST API      |    
| initiator_operations.py              | Demonstrates initiator creation, deletion, updation and listing using ONTAP REST API      |    
| iscsi_setup.py           | Demonstrates how ISCSI luns can be setup using ONTAP REST API. It creates a lun within a volume and creates a new initiator group. The script, then, maps the lun to the initiator group.      |    
| nfs_setup.py             | Demonstrates NFS Setup using ONTAP REST API. The script creates an export-policy and a volume and then, sets up a mount.      |     
| portset_operations.py   | Demonstrates portset operations like portset creation, deletion, updation and listing using ONTAP REST API.     |
| snapshot_operations.py   | Demonstrates snapshot operations like snapshot creation, deletion, updation and listing using ONTAP REST API.     |
| svm_operations.py        | Demonstrates SVM operations like SVM creation, deletion, updation and listing using ONTAP REST API.      |   

## Day 2 Scripts:

| Script                               | Description       |
|:------------------------------------|:-------------|
| create_clone.py                      | Demonstrates clone creation using ONTAP REST API on the specified volume.      |  
| create_snapshot.py                   | Demonstrates snapshot creation using ONTAP REST API on the specified volume.       |    
| create_svm_volume.py      |  Demonstrates SVM creation, volume creation and the associated Export Policy creation using ONTAP REST API.     |
| create_volume.py                     | Demonstrates volume creation using ONTAP REST API on the specified SVM.     |  
| events.py                 |   Demonstrates events management usecases in ONTAP such as listing of events, look for specific message and severity,workflow to notify specific event with event,filter and destination creation using ONTAP REST API.    |
| file_system_analytics.py                  | Demonstrates File System Analytics usecases using using ONTAP REST API.      |   
| file_security_permissions.py                  | Demonstrates File Security permissions settings applied on a file or directory using using ONTAP REST API.      |   
| list_aggregates.py                   | Lists all the aggregates in a cluster using ONTAP REST API.      |   
| list_clones.py                       | Lists all the clones in a cluster using ONTAP REST API.       |     
| list_snapshots.py                    | Lists all the snapshots in the specified volume using ONTAP REST API.      |     
| list_volumes.py                      | Lists all the volumes in a SVM using ONTAP REST API.     |   
| list_vserver.py                      | Lists all the SVMs in a cluster using ONTAP REST API.      |    
| lun_operations.py                    | Demonstrates lun creation, deletion, updation and listing using ONTAP REST API      |    
| qtree_operations.py      | Demonstrates qtree operations like qtree creation, updation, deletion and listing using ONTAP REST API.      |    
| qtree_quota_metrics.py      | Demonstrates NAS usecase of qtree creation in a volume, Enabling Quota and displaying raw metrics of Qtree using ONTAP REST API.      |    
| quota_operations.py      | Demonstrates quota operations like quota creation, updation, deletion and listing using ONTAP REST API.      |    
| schedules_policies_sm_relationship.py | Demonstrates workflow of creating new schedules using cron or interval and retriving list of policies using ONTAP REST API.       |  
| snapmirror_operations.py | Demonstrates SnapMirror operations like SnapMirror relationship creation, deletion, updation and listing using ONTAP REST API.       |     
| svm_dr.py        | Demonstrates SVM disaster recovery from destination cluster using ONTAP REST API.      |   
| svm_operations.py        | Demonstrates SVM operations like SVM creation, deletion, updation and listing using ONTAP REST API.      |   
| volume_operations.py     | Demonstrates volume operations like volume creation, deletion, updation, cloning and listing using ONTAP REST API.      |    

## CLI Passthrough Scripts:
To assist CLI and ONTAPI API users in their transition to the ONTAP REST API, ONTAP provides a REST endpoint to access the CLI. You can use this passthrough feature to execute any CLI command. For more information, Read [NetApp Documentation](https://docs.netapp.com/ontap-9/index.jsp?topic=%2Fcom.netapp.doc.dot-rest-api%2FGUID-BC72E449-FD75-4687-96C0-6A9A68708FBF.html).

| Script                               | Description       |
|:------------------------------------|:-------------|
| service_policy.py  	           | Demonstrates network interface service-policy Diag mode CLI command usage in ONTAP REST API      |
| system_fru_check.py              | Demonstrates fru-check show CLI command usage in ONTAP REST API.      |    
| system_node_power.py.py  	           | Demonstrates system node power show  CLI command usage in ONTAP REST API      |
| system_node_power_off_diag.py              | Demonstrates system node power off -node Diag mode CLI command usage in ONTAP REST API.      |    
| system_node_power_on_diag.py              | Demonstrates system node power on -node Diag mode CLI command usage in ONTAP REST API.      |    
| vserver_file_security_cli_passthrough.py               | Demonstrates vserver security file-directory CLI usage in ONTAP REST API      |


