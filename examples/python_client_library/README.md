# ONTAP REST Python Client Library Examples

The repository folder **python_client_library** contains samples scripts you can refer to understand how the ONTAP REST API can be accessed through the Python client library.


## Using the Python client library

To make use of these scripts you must run each of the scripts with the appropriate parameters.Please refer the table for more information:-

| Script                               | Purpose       | Syntax  |
|:------------------------------------:|:-------------:|:-----:|
| cifs_setup_restapi_pcl.py  | Script demonsrates CIFS Setups. | python3 cifs_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| create_snap_pcl.py  | Script demonstrates Volume Snapshot creation. | python3 create_snap_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -s SNAPSHOT_NAME -vs SVM_NAME [-u API_USER] [-p API_PASS] |
| create_volume_pcl.py  | Script to create Volume. | python3 create_volume_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -vs VSERVER_NAME -a AGGR NAME -sz VOLUME_SIZE(MBs) [-u API_USER][-p API_PASS] |
| iscsi_setup_restapi_pcl.py  | Script demonsrates ISCSI setup. | iscsi_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| list_aggregates_pcl.py  | Script to list all the aggregates in a cluster. | python3 list_aggregates_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| list_volume_pcl.py   | Script to list volumes. |  python3 list_volume_pcl.py [-h] -c CLUSTER -vs SVM_NAME [-u API_USER]                        [-p API_PASS] |
| nfs_setup_restapi_pcl.py   | Script demonsrates NFS Setups. | python3 nfs_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER][-p API_PASS] |
| qtree_operations_restapi_pcl.py   | Script demonstrates Qtree Operations. | python3 qtree_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| snapmirror_operations_restapi_pcl.py   | Script demonstrates SnapMirror Operations. | python3 snapmirror_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| snapshot_operations_restapi_pcl.py    | Script demonstrates Snapshot Operations. | python3 snapshot_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER][-p API_PASS] |
| svm_operations_restapi_pcl.py    | Script demonsrates CIFS Setups. | python3 cifs_u API_USER]  [-p API_PASS] |
| snapshot_operations_restapi_pcl.py    | Script demonsrates CIFS Setups. | python3 cifs_u API_USER]  [-p API_PASS] |
| volume_batch_delete_restapi_pcl.py    | Script demonsrates CIFS Setups. | python3 cifs_u API_USER]  [-p API_PASS] |
| volume_batch_patch_restapi_pcl.py    | Script demonsrates CIFS Setups. | python3 cifs_u API_USER]  [-p API_PASS] |
| volume_operations_restapi_pcl.py    | Script demonsrates CIFS Setups. | python3 cifs_u API_USER]  [-p API_PASS] |
  
