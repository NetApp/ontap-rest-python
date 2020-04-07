# ONTAP REST API Python Examples

The repository folder **rest_api** contains samples scripts you can refer to understand how the ONTAP REST API can be accessed using the requests library.

## Preparation

Before running the example scripts , make sure the following packages are installed:

* requests 2.21.0 or later
* texttable 1.6.2

## Summary of the REST API scripts

The following table lists the description of each scripts which directly accesses the ONTAP REST API. Make sure to run each of the scripts with the appropriate parameters.

| Script                               | Description       |
|:------------------------------------|:-------------|
| cifs_setup.py            | The script demonstrates how CIFS shares can be setup using ONTAP REST API. It creates a volume and then creates a share on the volume. |
| create_clone.py                      | The script demonstrates clone creation using ONTAP REST API on the specified volume.      |  
| create_snapshot.py                   | The script demonstrates snapshot creation using ONTAP REST API on the specified volume.       |    
| create_svm_volume.py      |  The script demonstrates SVM creation , volume creation and the associated Export Policy creation using ONTAP REST API.     |
| create_volume.py                     | The script demonstrates volume creation using ONTAP REST API on the specified SVM.     |  
| iscsi_setup.py           | The script demonstrates how ISCSI luns can be setup using ONTAP REST API. It creates a lun within a volume and creates a new initiator group. The script, then, maps the lun to the initiator group.      |    
| list_aggregates.py                   | The script lists all the aggregates using ONTAP REST API in a cluster.      |   
| list_clones.py                       | The script lists all the clones using ONTAP REST API in a cluster.       |     
| list_snapshots.py                    | The script lists all the snapshots using ONTAP REST API in the specified volume.      |     
| list_volumes.py                      | Script to list volumes.     |   
| list_vserver.py                      | Script to list SVMs using ONTAP REST API.      |    
| nfs_setup.py             | Script demonstrates NFS setup.      |     
| qtree_operations.py      | Script demonstrates Qtree Operations.      |    
| snapmirror_operations.py | Script demonstrates SnapMirror Operations.       |     
| snapshot_operations.py   | Script demonstrates Snapshot Operations.     |
| svm_operations.py        | Script demonstrates SVM Operations.      |   
| volume_operations.py     | Script demonstrates Volume Operations.      |    
