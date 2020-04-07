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
| create_svm_volume.py      |  The script demonstrates SVM creation, volume creation and the associated Export Policy creation using ONTAP REST API.     |
| create_volume.py                     | The script demonstrates volume creation using ONTAP REST API on the specified SVM.     |  
| iscsi_setup.py           | The script demonstrates how ISCSI luns can be setup using ONTAP REST API. It creates a lun within a volume and creates a new initiator group. The script, then, maps the lun to the initiator group.      |    
| list_aggregates.py                   | The script lists all the aggregates in a cluster using ONTAP REST API.      |   
| list_clones.py                       | The script lists all the clones in a cluster using ONTAP REST API.       |     
| list_snapshots.py                    | The script lists all the snapshots in the specified volume using ONTAP REST API.      |     
| list_volumes.py                      | The script lists all the volumes in a cluster using ONTAP REST API.     |   
| list_vserver.py                      | The script lists all the SVMs in a cluster using ONTAP REST API.      |    
| nfs_setup.py             | The script demonstrates NFS Setup using ONTAP REST API. The script creates an export-policy and a volume and then, sets up a mount.      |     
| qtree_operations.py      | The script demonstrates qtree operations like qtree creation, updation, deletion and listing using ONTAP REST API.      |    
| snapmirror_operations.py | The script demonstrates SnapMirror operations like SnapMirror relationship creation, deletion, updation and listing using ONTAP REST API.       |     
| snapshot_operations.py   | The script demonstrates snapshot operations like snapshot creation, deletion, updation and listing using ONTAP REST API.     |
| svm_operations.py        | The script demonstrates SVM operations like SVM creation, deletion, updation and listing using ONTAP REST API.      |   
| volume_operations.py     | The script demonstrates volume operations like volume creation, deletion, updation, cloning and listing using ONTAP REST API.      |    
