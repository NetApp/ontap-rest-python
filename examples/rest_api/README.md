# ONTAP REST API Python Examples

The repository folder **rest_api** contains samples scripts you can refer to understand how the ONTAP REST API can be accessed using the requests library

## How to Use

To make use of these scripts you must run each of the scripts with the appropriate parameters.Please refer the table for more information:-

| Script                               | Purpose       | Syntax  |
|:------------------------------------:|:-------------:|:-----:|
| cifs_setup_restapi_api.py            | Script demonsrates CIFS Setups. | python3 cifs_setup_restapi_api.py [-h] -c CLUSTER [-u API_USER]  [-p API_PASS] |
| create_clone.py                      | Script demonstrates Volume Clone creation.      |  python3 create_clone.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -s SNAPSHOT_NAME -cn CLONE_NAME  [-u API_USER]  [-p API_PASS] |
| create_snapshot.py                   | Script demonstrates Volume Snapshot creation.      |    python3 create_snapshot.py [-h] -c CLUSTER -v VOLUME_NAME -s SNAPSHOT_NAME -vs SVM_NAME [-u API_USER] [-p API_PASS] |
| create_svm_volume.py      |  Script demonstrates SVM, Volume and associated Export Policy creation.      |  python3   create_svm_volume.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -sz VOLUME_SIZE -a AGGR_NAME -er EXPORT_POLICY_RULE -en EXPORT_POLICY_NAME [-u API_USER] [-p API_PASS] |
| create_volume.py                     | Script to create Volume     |   python3 create_volume.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a AGGR_NAME -sz VOLUME_SIZE [-u API_USER] [-p API_PASS] |
| iscsi_setup_restapi_api.py           | Script demonsrates ISCSI setup.      |    python3 iscsi_setup__restapi_api.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| list_aggregates.py                   | Script to list all the aggregates in a cluster.      |   list_aggregates.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| list_clones.py                       | Script to list all clone volumes in a cluster.       |     python3 list_clones.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| list_snapshots.py                    | Script to list all the snapshots.      |     python3 list_snapshots.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME [-u API_USER] [-p API_PASS] |
| list_volumes.py                      | Script to list volumes.     |   list_volumes.py [-h] -c CLUSTER -vs SVM_NAME [-u API_USER] [-p API_PASS] |
| list_vserver.py                      | Script to list SVMs using ONTAP REST API.      |    list_vserver.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| nfs_setup_restapi_api.py             | Script demonsrates NFS setup.      |     python3 nfs_setup_restapi_api.py [-h] -c CLUSTER [-u API_USER][-p API_PASS] |
| qtree_operations_restapi_api.py      | Script demonsrates Qtree Operations.      |    python3 qtree_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| snapmirror_operations_restapi_api.py | Script demonsrates SnapMirror Operations.       |     python3 snapmirror_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
| snapshot_operations_restapi_api.py   | Script demonsrates Snapshot Operations.     | python3 svm_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER][-p API_PASS]    |
| svm_operations_restapi_api.py        | Script demonsrates SVM Operations.      |   python3 svm_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER][-p API_PASS] |
| volume_operations_restapi_api.py     | Script demonsrates Volume Operations.      |    python3 volume_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS] |
