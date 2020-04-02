# ONTAP-REST-Python Examples

NetApp® ONTAP® version 9.6 and later includes support for an expansive RESTful web services API. In comparison to an ONTAPI® application, the REST API offers a vastly simplified and workflow-driven user experience, allowing you to perform multiple operations on the storage objects with a single API. REST is the industry standard for APIs and the ONTAP REST API provides a tremendous opportunity to automate your storage deployments.

This repository contains sample scripts illustrating how to use the ONTAP REST API. You can access the API through the Python client library, which is preferable in most situations. If needed, you can also connect directly to the API using the native capabilities provided with Python.

## Directly accessing the ONTAP REST API

The repository folder **rest_api** contains samples scripts you can use to directly access the ONTAP REST API using the requests library. You must run each of the scripts with the appropriate parameters.

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
