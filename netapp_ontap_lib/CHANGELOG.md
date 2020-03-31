There are several changes to the Python Client Library and the ONTAP REST API, which are organized by release below.

## 9.7.0 GA library updates
(2020-01-23)

**Fixed issues**

* [Bug ID 1279507](https://mysupport.netapp.com/NOW/cgi-bin/bol?Type=Detail&Display=1279507)
  When doing a find() with the fields query parameter, the library was not returning the specified fields, instead, all fields were being returned.

* [Bug ID 1291333](https://mysupport.netapp.com/NOW/cgi-bin/bol?Type=Detail&Display=1291333)
  When 0 records are found in a Resource.find() call and LOG_ALL_API_CALLS is set to True, then an uncaught exception is raised.


## 9.7.0 RC1 library updates
(2019-11-20)

**New**

* The application can now add its own custom headers for each request as part of the `netapp_ontap.host_connection.HostConnection` object.
* When passing verify=False to the HostConnection, the library will now disable urllib3's InsecureRequestWarning from logging messages.

**Incompatibilities**

* In prior versions, Resource.find() would raise an exception if no results were found as well as when more than one was found. In this version, when no results are found, None is returned instead of raising an exception. An exception is still raised when more than one result is found.

**Fixed issues**

* [Bug ID 1271450](https://mysupport.netapp.com/NOW/cgi-bin/bol?Type=Detail&Display=1271450)
  The library doesn't allow sending a body in a DELETE request.

* [Bug ID 1263312](https://mysupport.netapp.com/NOW/cgi-bin/bol?Type=Detail&Display=1263312)
  When POSTing or PATCHing some objects with embeded objects, fields might incorrectly be dropped from the request.

* [Bug ID 1275238](https://mysupport.netapp.com/NOW/cgi-bin/bol?Type=Detail&Display=1275238)
  Retrieving and setting the "from" field of Autosupport object fails.

##ONTAP 9.7 REST API updates

All new ONTAP APIs have corresponding library resource objects which can be used
to perform the operations. See the `netapp_ontap.resources` package for details
about each of the objects and their fields.

For a summary of the changes in the ONTAP REST API between versions of ONTAP 9, see the [ONTAP 9 Release Notes](https://library.netapp.com/ecmdocs/ECMLP2492508/html/frameset.html).

**New endpoints**

* Endpoint: /cluster/nodes/{uuid}  
    HTTP methods: DELETE  
    This API will remove a node from the cluster.

* Endpoint: /cluster/ntp/keys/{id}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs allow for management of NTP server shared keys.

* Endpoint: /cluster/ntp/servers/{server}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs allow for management of keyed NTP servers.

* Endpoint: /cluster/software/download  
    HTTP methods: GET  
    This API allows monitoring the status of the image package download progress.

* Endpoint: /network/http-proxy/{uuid}  
    HTTP methods: GET, POST, PATCH, DELETE  
    This API allow configuration of an HTTP proxy for the cluster of SVM IP spaces.

* Endpoint: /network/ip/bgp/peer-groups/{uuid}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs manage information pertaining to the BGP peer-groups configured in the cluster.

* Endpoint: /protocols/san/fcp/services/{svm.uuid}/metrics  
    HTTP methods: GET  
    This API retrieves historical performance metrics for the FC Protocols service of an SVM.

* Endpoint: /protocos/san/iscsi/services/{svm.uuid}/metrics  
    HTTP methods: GET  
    This API retrieves history performance metrics for the iSCSI protocol of an SVM.

* Endpoint: /storage/luns/{uuid}/metrics  
    HTTP methods: GET  
    This API retrieves history performance metrics for a LUN.

* Endpoint: /protocls/nvme/services/{svm.uuid}/metrics  
    HTTP methods: GET  
    This API retrieve historical performance metrics for NVME protocol of an SVM.

* Endpoint: /support/configuration-backup/{node.uuid}/name  
    HTTP methods: GET, POST, DELETE  
    These APIs create, retrieve, and delete backup configuraiton for the cluster.

* Endpoint: /support/snmp/traphosts/{host}  
    HTTP methods: GET, POST, DELETE  
    These APIs configure SNMP traphosts which will receive SNMP traps from ONTAP.

* Endpoint: /support/snmp/users/{engine_id}/{name}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs configure SNMP users that are able to query for the ONTAP SNMP server.

* Endpoint: /security  
    HTTP methods: GET  
    This API retrieves information about the security configured on the cluster.

* Endpoint: /security/authentication/cluster/ad-proxy  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs configure which data SVM will be use to proxy cluster management AD authentication.

* Endpoint: /security/authentiation/publickeys/{owner.uuid}/{account.name}/{index}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs configure the public keys for user accounts.

* Endpoint: /security/key-managers/{source.uuid}/migrate  
    HTTP methods: POST  
    This API migrates the keys belonging to an SVM between the cluster's key manager and the SVM's key manager.

* Endpoint: /security/ssh  
    HTTP methods: GET, PATCH  
    This API manages the SSH server running in ONTAP.

* Endpoint: /storage/aggregates/{uuid}/metrics  
    HTTP methods: GET  
    This API provide historical performance metrics for the specified aggregate.

* Endpoint: /storage/disks  
    HTTP methods: PATCH  
    This API updates the encryption controls of self-encrypting disks.

* Endpoint: /storage/snapshot-policies/{snapshot-policy.uuid}/schedules/{uuid}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs manage the policies reqarding when snapshots are taken.

* Endpoint: /protocols/ndmp  
    HTTP methods: GET, PATCH  
    This API manages NDMP mode at either SVM-scope or node-scope.

* Endpoint: /protocols/ndmp/{node.uuid}  
    HTTP methods: GET, PATCH  
    This API manages node-scoped NDMP settings.

* Endpoint: /protocols/ndmp/sessions/{owner.uuid}/{session.id}  
    HTTP methods: GET, DELETE  
    These APIs manage diagnostics information on NDMP settings belonging to a specific SVM in the case of SVM-scope or to a specific node in the case of node-scope.

* Endpoint: /protocols/ndmp/svms/{svm.uuid}  
    HTTP methods: GET, PATCH  
    These APIs manage SVM-scoped NDMP settings.

* Endpoint: /storage/snaplock/audit-logs/{svm.uuid}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs manage the loggin policies for a snaplock volume.

* Endpoint: /storage/snaplock/compliance-clocks/{node.uuid}  
    HTTP methods: GET  
    This API manages the Compliance Clock of the system which determines the expiry time of the SnapLock objects in the system.

* Endpoint: /storage/snaplock/event-retention/operations/{id}  
    HTTP methods: GET, POST  
    These APIs display all Event Based Retentions (EBR) operations and allow for applying an EBR policy on a specified volume.

* Endpoint: /storage/snaplock/event-retention/policies/{policy.name}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs manage retention policies for snaplock files and directories.

* Endpoint: /storage/snaplock/files/{volume.uuid}/{path}  
    HTTP methods: GET, PATCH, DELETE  
    These APIs manage the SnapLock retention time of a file.

* Endpoint: /storage/snaplock/file-fingerprints/{id}  
    HTTP methods: GET, POST, DELETE  
    These APIs manage key information about snaplock files and volumes.

* Endpoint: /storage/snaplock/litigations/{id}  
    HTTP methods: GET, POST, DELETE  
    These APIs retain Compliance-mode WORM files for the duration of a litigation.

* Endpoint: /storage/snaplock/litigations/{litigation.id/files  
    HTTP methods: GET  
    This API displays the list of files under the specified litigation ID.

* Endpoint: /storage/snaplock/litigations/{litigation.id}/operations/{id}  
    HTTP methods: GET, POST, DELETE  
    This API manages the legal-hold operations for the specified litigation ID.

* Endpoint: /protocols/cifs/services/{svm.uuid}/metrics  
    HTTP methods: GET  
    This API retrieves history performance metrics for the CIFS protocol of an SVM.

* Endpoint: /protocols/nfs/connected-clients  
    HTTP methods: GET  
    This API provides a list of currently connected NFS clients or clients that can be connected but are currently idle.

* Endpoint: /protocols/nfs/services/{svm.uuid}/metrics  
    HTTP methods: GET  
    This API retrieves historical performance metrics for the NFS protocol of an SVM.

* Endpoint: /protocols/s3/buckets  
    HTTP methods: GET  
    This API retrieves all S3 buckets for all SVMs.

* Endpoint: /protocols/s3/services/{svm.uuid}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs manage S3 servers which will allow you to store objects in ONTAP using Amazon S3 protocol.

* Endpoint: /protocols/s3/services/{svm.uuid}/buckets/{uuid}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs manage S3 buckets which are a container of objects.

* Endpoint: /protocols/s3/services/{svm.uuid}/users/{name}  
    HTTP methods: GET, POST, PATCH, DELETE  
    These APIs manage S3 user accounts on the server. Buckets that are created are associate with a user.

##9.6.0
(2019-07-16)

Initial release of the library
