# ONTAP REST Python Client Library Examples

The repository folder **python_client_library** contains samples scripts you can refer to understand how the ONTAP REST API can be accessed through the Python client library.

## Preparation

Before running the example scripts , make sure the following packages are installed:

* python 3.5 or later
* requests 2.21.0 or later
* marshmallow 3.2.1 or later

## Summary of the Python client library scripts

The following table lists the description of each scripts which accesses the ONTAP REST API using the Python client library. Make sure to run each of the scripts with the appropriate parameters.

| Script                               | Description       |
|:------------------------------------|:-------------|
| cifs_setup.py  | Demonstrates how CIFS shares can be setup using ONTAP REST API Python Client Library. It creates a volume and then creates a share on the volume.   |
| create_snap.py  | Creates a snapshot using ONTAP REST API Python Client Library on the specified volume.  |
| create_volume.py  | Creates a volume using ONTAP REST API Python Client Library on the specified SVM . |
| iscsi_setup_restapi.py  | Demonstrates how ISCSI luns can be setup using ONTAP REST API Python Client Library. It creates a lun within a volume and creates a new initiator group. The script, then, maps the lun to the initiator group. |
| list_aggregates.py  | Lists all the aggregates using ONTAP REST API Python Client Library in a cluster. |
| list_volume.py   | Lists all the volumes using ONTAP REST API Python Client Library in the specified SVM. |  
| nfs_setup_restapi.py   | Demonstrates NFS Setup using ONTAP REST API Python Client Library. The script creates an export-policy and a volume and then, sets up a mount. |
| qtree_operations.py   | Demonstrates qtree operations like qtree creation, updation, deletion and listing using ONTAP REST API Python Client Library. |
| snapmirror_operations.py   | Demonstrates SnapMirror operations like SnapMirror relationship creation, deletion, updation and listing using ONTAP REST API Python Client Library. |
| snapshot_operations.py    | Demonstrates snapshot operations like snapshot creation, deletion, updation and listing using ONTAP REST API Python Client Library. |
| svm_operations.py    | Demonstrates SVM operations like SVM creation, deletion, updation and listing using ONTAP REST API Python Client Library. |
| volume_batch_delete.py    | Demonstrates volume batch delete operations using ONTAP REST API Python Client Library. |
| volume_batch_patch.py    | Demonstrates volume batch update operations using ONTAP REST API Python Client Library. |
| volume_operations.py    | Demonstrates volume operations like volume creation, deletion, updation, cloning and listing using ONTAP REST API Python Client Library. |
