# ONTAP-REST-Python Examples

NetApp® ONTAP® version 9.6 and later includes support for an expansive RESTful web services API. In comparison to an ONTAPI® application, the REST API offers a vastly simplified and workflow-driven user experience, allowing you to perform multiple operations on the storage objects with a single API. REST is the industry standard for APIs and the ONTAP REST API provides a tremendous opportunity to automate your storage deployments.

This repository contains sample scripts illustrating how to use the ONTAP REST API. You can access the API through the Python client library, which is preferable in most situations. If needed, you can also connect directly to the API using the native capabilities provided with Python.

## Directly accessing the ONTAP REST API

The repository folder **rest_api** contains samples scripts you can use to directly access the ONTAP REST API using the requests library. You must run each of the scripts with the appropriate parameters. For example:

```
python3 create_volume_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a AGGR_NAME
-sz VOLUME_SIZE [-u API_USER] [-p API_PASS]
```
| Script                               | Purpose       | Syntax  |
| ------------------------------------ |:-------------:| -----:|
| cifs_setup_restapi_api.py            | right-aligned | $1600 |
| create_clone.py                      | centered      |   $12 |
| create_snapshot.py                   | are neat      |    $1 |
| create_svm_volume.py                 | are neat      |    $1 |
| create_volume.py                     | are neat      |    $1 |
| iscsi_setup_restapi_api.py           | are neat      |    $1 |
| list_aggregates.py                   | are neat      |    $1 |
| list_clones.py                       | are neat      |    $1 |
| list_snapshots.py                    | are neat      |    $1 |
| list_volumes.py                      | are neat      |    $1 |
| list_vserver.py                      | are neat      |    $1 |
| nfs_setup_restapi_api.py             | are neat      |    $1 |
| qtree_operations_restapi_api.py      | are neat      |    $1 |
| snapmirror_operations_restapi_api.py | are neat      |    $1 |
| snapshot_operations_restapi_api.py   | are neat      |    $1 |
| svm_operations_restapi_api.py        | are neat      |    $1 |
| volume_operations_restapi_api.py     | are neat      |    $1 |
