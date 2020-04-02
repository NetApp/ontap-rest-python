# ONTAP REST Python Client Library Examples

The repository folder **python_client_library** contains samples scripts you can refer to understand how the ONTAP REST API can be accessed through the Python client library.

Before running the example scripts , make sure the following packages are installed.

* python 3.5 or later
* requests 2.21.0 or later
* marshmallow 3.2.1 or later


## Using the Python client library

To make use of these scripts you must run each of the scripts with the appropriate parameters.Please refer the table for more information:-

| Script                               | Purpose       | Syntax  |
|:------------------------------------:|:-------------:|:-----:|
| cifs_setup_restapi_pcl.py  | Script demonstrates CIFS Setups. | python3 cifs_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| create_snap_pcl.py  | Script demonstrates Volume Snapshot creation. | python3 create_snap_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -s SNAPSHOT_NAME -vs SVM_NAME [-u API_USER] [-p API_PASS] |
| create_volume_pcl.py  | Script to create Volume. | python3 create_volume_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -vs VSERVER_NAME -a AGGR NAME -sz VOLUME_SIZE(MBs) [-u API_USER][-p API_PASS] |
| iscsi_setup_restapi_pcl.py  | Script demonstrates ISCSI setup. | python3 iscsi_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| list_aggregates_pcl.py  | Script to list all the aggregates in a cluster. | python3 list_aggregates_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| list_volume_pcl.py   | Script to list volumes. |  python3 list_volume_pcl.py [-h] -c CLUSTER -vs SVM_NAME [-u API_USER]                        [-p API_PASS] |
| nfs_setup_restapi_pcl.py   | Script demonstrates NFS Setups. | python3 nfs_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER][-p API_PASS] |
| qtree_operations_restapi_pcl.py   | Script demonstrates Qtree operations. | python3 qtree_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| snapmirror_operations_restapi_pcl.py   | Script demonstrates SnapMirror operations. | python3 snapmirror_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| snapshot_operations_restapi_pcl.py    | Script demonstrates Snapshot operations. | python3 snapshot_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER][-p API_PASS] |
| svm_operations_restapi_pcl.py    | Script demonstrates SVM operations. | python3 svm_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER][-p API_PASS] |
| snapshot_operations_restapi_pcl.py    | Script demonstrates Volume operations. | python3 volume_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| volume_batch_delete_restapi_pcl.py    | Script demonstrates batch delete operations. | python3 volume_batch_delete_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| volume_batch_patch_restapi_pcl.py    | Script demonstrates batch update operations. | python3 volume_batch_patch_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]  |
| volume_operations_restapi_pcl.py    | Script demonsrates volume operations. | python3 volume_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
  
