# ONTAP REST Python Client Library Examples

The repository folder **python_client_library** contains samples scripts you can refer to understand how the ONTAP REST API can be accessed through the Python client library.

## Preparation

Before running the example scripts , make sure the following packages are installed:

* python 3.5 or later
* requests 2.21.0 or later
* marshmallow 3.2.1 or later

## Summary of the Python client library scripts

The following table summaries the scripts used to access the ONTAP REST API using the Python client library. Make sure to run each of the scripts with the appropriate parameters.

| Script                               | Description       |
|:------------------------------------|:-------------|
| cifs_setup.py  | Demonstrates how CIFS shares can be setup using ONTAP REST API Python Client Library. It creates a volume and then creates a share on the volume.   |
| create_snap.py  | Creates a snapshot using ONTAP REST API Python Client Library on the specified volume.  |
| create_volume.py  | creates a volume using ONTAP REST API Python Client Library on the specified SVM . |
| iscsi_setup_restapi.py  | Demonstrates how ISCSI Luns can be setup using ONTAP REST API Python Client Library. It creates a lun within a volume and creates a new initiator group. The script, then, maps the lun to the initiator group. |
| list_aggregates.py  | Lists all the aggregates using ONTAP REST API Python Client Library in a cluster. |
| list_volume.py   | Script to list volumes. |  
| nfs_setup_restapi.py   | Script demonstrates NFS Setups. |
| qtree_operations.py   | Script demonstrates Qtree operations. |
| snapmirror_operations.py   | Script demonstrates SnapMirror operations. |
| snapshot_operations.py    | Script demonstrates Snapshot operations. |
| svm_operations.py    | Script demonstrates SVM operations. |
| snapshot_operations.py    | Script demonstrates Volume operations. |
| volume_batch_delete.py    | Script demonstrates batch delete operations. |
| volume_batch_patch.py    | Script demonstrates batch update operations. |
| volume_operations.py    | Script demonsrates volume operations. |
