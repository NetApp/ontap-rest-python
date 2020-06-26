# ONTAP REST Python Client Library Examples

The repository folder **python_client_library** contains samples scripts you can refer to understand how the ONTAP REST API can be accessed through the Python client library.

# Preparation

Before running the example scripts, make sure the following packages are installed:

* python 3.5 or later
* requests 2.21.0 or later
* marshmallow 3.2.1 or later

See the [PyPI netapp-ontap](https://pypi.org/project/netapp-ontap/) package web page for more information.

**Note: **
If you are using ONTAP 9.6 "netapp_ontap" Python client library module, make sure to replace `from netapp_ontap import NetAppRestError` header with `from netapp_ontap.error import NetAppRestError` header.  


# Summary of the Python client library scripts  

The following table summaries the scripts used to access the ONTAP REST API using the Python client library. Make sure to run each of the scripts with the appropriate parameters.  

| Script                               | Description       |
|:------------------------------------|:-------------|
| account_operations.py    	           | Demonstrates user account creation, deletion, updation and listing using ONTAP REST API Python Client Library.    |
| aggregate_operations.py  	           | Demonstrates aggregate creation, deletion, updation and listing using ONTAP REST API Python Client Library.     |   
| cert_auth.py                         | Creates or updates user account to enable certificate based authentication for that account.     |   
| cifs_setup.py            			   | Demonstrates how CIFS shares can be setup using ONTAP REST API Python Client Library. It creates a volume and then creates a share on the volume. |  
| create_clone.py                      | Demonstrates clone creation using ONTAP REST API Python Client Library on the specified volume.      |  
| create_snapshot.py                   | Demonstrates snapshot creation using ONTAP REST API Python Client Library on the specified volume.       |    
| events.py                 |  Demonstrates listing of config, events, filters, destinations using ONTAP REST API Python Client Library.     |
| initiator_operations.py              | Demonstrates initiator creation, deletion, updation and listing using ONTAP REST API Python Client Library.      |    
| interface_operations.py              | Demonstrates interface creation, deletion, updation and listing using ONTAP REST API Python Client Library.      |    
| iscsi_setup.py           | Demonstrates how ISCSI luns can be setup using ONTAP REST API Python Client Library. It creates a lun within a volume and creates a new initiator group. The script, then, maps the lun to the initiator group.      |    
| license_operations.py                | Demonstrates license creation, deletion and listing using ONTAP REST API Python Client Library.      |    
| list_aggregates.py                   | Lists all the aggregates in a cluster using ONTAP REST API Python Client Library.      |   
| list_clones.py                       | Lists all the clones in a cluster using ONTAP REST API Python Client Library.       |     
| list_snapshots.py                    | Lists all the snapshots in the specified volume using ONTAP REST API Python Client Library.      |     
| list_volumes.py                      | Lists all the volumes in a SVM using ONTAP REST API Python Client Library.     |   
| list_vserver.py                      | Lists all the SVMs in a cluster using ONTAP REST API Python Client Library.      |    
| lun_operations.py                    | Demonstrates lun creation, deletion, updation and listing using ONTAP REST API Python Client Library.      |    
| nfs_setup.py             | Demonstrates NFS Setup using ONTAP REST API Python Client Library. The script creates an export-policy and a volume and then, sets up a mount.      |     
| qtree_operations.py      | Demonstrates qtree operations like qtree creation, updation, deletion and listing using ONTAP REST API Python Client Library.      |    
| quota_operations.py      | Demonstrates quota operations like quota creation, updation, deletion and listing using ONTAP REST API Python Client Library.      |    
| snapmirror_operations.py | Demonstrates SnapMirror operations like SnapMirror relationship creation, deletion, updation and listing using ONTAP REST API Python Client Library.       |     
| snapshot_operations.py   | Demonstrates snapshot operations like snapshot creation, deletion, updation and listing using ONTAP REST API Python Client Library.     |
| svm_operations.py        | Demonstrates SVM operations like SVM creation, deletion, updation and listing using ONTAP REST API Python Client Library.      |   
| volume_batch_delete.py   | Demonstrates volume batch delete operations using ONTAP REST API Python Client Library.     |   
| volume_batch_patch.py    | Demonstrates volume batch update operations using ONTAP REST API Python Client Library.     |   
| volume_operations.py     | Demonstrates volume operations like volume creation, deletion, updation, cloning and listing using ONTAP REST API Python Client Library.      |    
