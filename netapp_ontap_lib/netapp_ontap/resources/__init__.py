# pylint: disable=line-too-long
"""
Copyright &copy; 2019 NetApp Inc. All rights reserved.

All of the modules in this package represent individual object models which can
be imported and used for communicating with the REST APIs. To see their interface,
look at `netapp_ontap.resource.Resource`.

## Constructor
Once you've imported the resources you want to work with into your application and set the host
connection, the next step is to create an instance of the resource you want to perform
operations on. A resource represents a snapshot of an object that exist on the host. Any keyword
arguments passed into the constructor will be set as properties of that instance.

```python
# Create an instance of the cluster resource
from netapp_ontap.resources import Cluster
from netapp_ontap import config, HostConnection
config.CONNECTION(host, username, password)
cluster = Cluster()
cluster.get()
```
## to_dict()
to_dict() is a function that will return a dictionary representation of the object's state.
It serializes the current state of the object which is a `netapp_ontap.resource.Resource` type into
a 'dict' type, allowing you to view the information in a readable format.
If you only want certain fields in the dictionary, 'only' may be passed in as a tuple of strings.

## from_dict()
from_dict() is a function that can be used to construct a resource from a dictionary.
It does the opposite of to_dict(), it will deserialize a dictionary to a
`netapp_ontap.resource.Resource` type. This can be used when constructing an object that
you want to post to a resource. Field validation is done when you call from_dict.
Enums, strings, and integers of the object will be validated
When invalid data is passed in, a ValidationError will be raised.

## Verb methods
The following operations are supported by this library. However, for a specific resource,
you might only be able to call a subset of these functions.

### get()
get() will fetch the details of an object from the host. For the required keys (if any) that need
to be set, refer to the resource's page to see what those are.
```python
svm = Svm.find(name = "test_vserver")
svm.get()
print(svm.to_dict())
```

### get_collection()
get_collection() will fetch all records of the resource type from the host. It returns a list which
you can then iterate through to view information about each object on the host. By default, only
key values are returned for each resource. You can specify 'fields=field1,field2,...' to
retrieve more fields for each resource.
```python
for svm in Svm.get_collection():
    svm.get()
    pprint.pprint(svm.to_dict())
```

### find()
find() will find an instance of an object of the desired resource on the host given a query.
A query will be constructed with the provided key/value pairs and will be sent to the host.
The find() operation is a wrapper on get_collection. It will only return true if exactly one
matching record is found, so you are expected to provide the necessary query parameters to filter
get_collection() down to exactly one record.
```python
svm = Svm.find(name = "test_vserver")
```

### patch()
patch() will modify any fields of an object that have been changed by the client application.
You can modify a field of an object by setting it to the desired value, then calling the patch() on
it. Only the fields of the object that have changed since the last iteraction with the host
will be sent in the PATCH request body. To see which fields are modifiable, you can reference
the ONTAP REST API Documentation.

```python
svm = Svm.find(name = "test_vserver")
svm.state = "stopped"
svm.comment = "this svm is offline"
svm.patch()
```

### patch_collection()
patch_collection() will patch all objects in a collection which match a given query
with the request body.
```python
# modify the state of all volumes whose name begins with 'testVol' on vserver vs1
volumes = Volume.patch_collection(
    {'state': 'offline'},
    name = 'testVol*',
    return_records='true')
```

### delete()
delete() will send a request to delete the object from the host.
```python
aggr = Aggregate.find(name='test_aggr')
aggr.delete()
```

### delete_collection()
delete_collection() will delete all objects on the host which match
the provided query.
```python
svm = Svm.delete_collection(name='test_vserver')
```

### post()
post() will create a new object on the host. During post(), the resource will update it's location
and key fields. This allows you to perform other instance methods such as get(), patch(),
or delete() following the post() operation. In order to POST to a resource, you first
have to create an object, then you may call post() on it. The operation will send the object
to the host as a request to create a new object of the resource type.
```python
volume = Volume.from_dict({
    'name': 'vol1',
    'svm': {'name':'vs1'},
    'aggregates': [{'name'}:'aggr1'
}]
volume.post()
```
## Resources
URL|Resource
:----------------|:-------
/api/storage/luns| <a title="netapp_ontap.resources.lun.Lun" href="../resources/lun.html"><code>Lun</code></a>
/api/support/autosupport| <a title="netapp_ontap.resources.autosupport.Autosupport" href="../resources/autosupport.html"><code>Autosupport</code></a>
/api/cluster/software/download| <a title="netapp_ontap.resources.software_package_download.SoftwarePackageDownload" href="../resources/software_package_download.html"><code>SoftwarePackageDownload</code></a>
/api/storage/volumes/{volume[uuid]}/files| <a title="netapp_ontap.resources.file_info.FileInfo" href="../resources/file_info.html"><code>FileInfo</code></a>
/api/network/ip/service-policies| <a title="netapp_ontap.resources.ip_service_policy.IpServicePolicy" href="../resources/ip_service_policy.html"><code>IpServicePolicy</code></a>
/api/protocols/nfs/export-policies| <a title="netapp_ontap.resources.export_policy.ExportPolicy" href="../resources/export_policy.html"><code>ExportPolicy</code></a>
/api/storage/snaplock/file-fingerprints| <a title="netapp_ontap.resources.snaplock_file_fingerprint.SnaplockFileFingerprint" href="../resources/snaplock_file_fingerprint.html"><code>SnaplockFileFingerprint</code></a>
/api/network/ipspaces| <a title="netapp_ontap.resources.ipspace.Ipspace" href="../resources/ipspace.html"><code>Ipspace</code></a>
/api/network/http-proxy| <a title="netapp_ontap.resources.network_http_proxy.NetworkHttpProxy" href="../resources/network_http_proxy.html"><code>NetworkHttpProxy</code></a>
/api/protocols/fpolicy| <a title="netapp_ontap.resources.fpolicy.Fpolicy" href="../resources/fpolicy.html"><code>Fpolicy</code></a>
/api/security/roles| <a title="netapp_ontap.resources.role.Role" href="../resources/role.html"><code>Role</code></a>
/api/support/ems/filters/{ems_filter[name]}/rules| <a title="netapp_ontap.resources.ems_filter_rule.EmsFilterRule" href="../resources/ems_filter_rule.html"><code>EmsFilterRule</code></a>
/api/storage/flexcache/flexcaches| <a title="netapp_ontap.resources.flexcache.Flexcache" href="../resources/flexcache.html"><code>Flexcache</code></a>
/api/protocols/fpolicy/{svm[uuid]}/events| <a title="netapp_ontap.resources.fpolicy_event.FpolicyEvent" href="../resources/fpolicy_event.html"><code>FpolicyEvent</code></a>
/api/network/fc/logins| <a title="netapp_ontap.resources.fc_login.FcLogin" href="../resources/fc_login.html"><code>FcLogin</code></a>
/api/application/applications/{application[uuid]}/components/{component[uuid]}/snapshots| <a title="netapp_ontap.resources.application_component_snapshot.ApplicationComponentSnapshot" href="../resources/application_component_snapshot.html"><code>ApplicationComponentSnapshot</code></a>
/api/protocols/cifs/shares| <a title="netapp_ontap.resources.cifs_share.CifsShare" href="../resources/cifs_share.html"><code>CifsShare</code></a>
/api/protocols/cifs/services| <a title="netapp_ontap.resources.cifs_service.CifsService" href="../resources/cifs_service.html"><code>CifsService</code></a>
/api/protocols/nvme/subsystems/{subsystem[uuid]}/hosts| <a title="netapp_ontap.resources.nvme_subsystem_host.NvmeSubsystemHost" href="../resources/nvme_subsystem_host.html"><code>NvmeSubsystemHost</code></a>
/api/protocols/nfs/kerberos/realms| <a title="netapp_ontap.resources.kerberos_realm.KerberosRealm" href="../resources/kerberos_realm.html"><code>KerberosRealm</code></a>
/api/protocols/nfs/kerberos/interfaces| <a title="netapp_ontap.resources.kerberos_interface.KerberosInterface" href="../resources/kerberos_interface.html"><code>KerberosInterface</code></a>
/api/security/ssh| <a title="netapp_ontap.resources.cluster_ssh_server.ClusterSshServer" href="../resources/cluster_ssh_server.html"><code>ClusterSshServer</code></a>
/api/network/fc/wwpn-aliases| <a title="netapp_ontap.resources.wwpn_alias.WwpnAlias" href="../resources/wwpn_alias.html"><code>WwpnAlias</code></a>
/api/storage/flexcache/origins| <a title="netapp_ontap.resources.flexcache_origin.FlexcacheOrigin" href="../resources/flexcache_origin.html"><code>FlexcacheOrigin</code></a>
/api/storage/shelves| <a title="netapp_ontap.resources.shelf.Shelf" href="../resources/shelf.html"><code>Shelf</code></a>
/api/storage/volumes| <a title="netapp_ontap.resources.volume.Volume" href="../resources/volume.html"><code>Volume</code></a>
/api/protocols/san/igroups/{igroup[uuid]}/initiators| <a title="netapp_ontap.resources.igroup_initiator.IgroupInitiator" href="../resources/igroup_initiator.html"><code>IgroupInitiator</code></a>
/api/network/ethernet/ports| <a title="netapp_ontap.resources.port.Port" href="../resources/port.html"><code>Port</code></a>
/api/storage/snaplock/compliance-clocks| <a title="netapp_ontap.resources.snaplock_compliance_clock.SnaplockComplianceClock" href="../resources/snaplock_compliance_clock.html"><code>SnaplockComplianceClock</code></a>
/api/support/autosupport/messages| <a title="netapp_ontap.resources.autosupport_message.AutosupportMessage" href="../resources/autosupport_message.html"><code>AutosupportMessage</code></a>
/api/support/ems/filters| <a title="netapp_ontap.resources.ems_filter.EmsFilter" href="../resources/ems_filter.html"><code>EmsFilter</code></a>
/api/network/fc/ports| <a title="netapp_ontap.resources.fc_port.FcPort" href="../resources/fc_port.html"><code>FcPort</code></a>
/api/network/ip/bgp/peer-groups| <a title="netapp_ontap.resources.bgp_peer_group.BgpPeerGroup" href="../resources/bgp_peer_group.html"><code>BgpPeerGroup</code></a>
/api/cloud/targets| <a title="netapp_ontap.resources.cloud_target.CloudTarget" href="../resources/cloud_target.html"><code>CloudTarget</code></a>
/api/cluster/schedules| <a title="netapp_ontap.resources.schedule.Schedule" href="../resources/schedule.html"><code>Schedule</code></a>
/api/network/ip/interfaces| <a title="netapp_ontap.resources.ip_interface.IpInterface" href="../resources/ip_interface.html"><code>IpInterface</code></a>
/api/support/snmp| <a title="netapp_ontap.resources.snmp.Snmp" href="../resources/snmp.html"><code>Snmp</code></a>
/api/protocols/san/lun-maps| <a title="netapp_ontap.resources.lun_map.LunMap" href="../resources/lun_map.html"><code>LunMap</code></a>
/api/support/configuration-backup/backups| <a title="netapp_ontap.resources.configuration_backup_file.ConfigurationBackupFile" href="../resources/configuration_backup_file.html"><code>ConfigurationBackupFile</code></a>
/api/security| <a title="netapp_ontap.resources.security_config.SecurityConfig" href="../resources/security_config.html"><code>SecurityConfig</code></a>
/api/name-services/dns| <a title="netapp_ontap.resources.dns.Dns" href="../resources/dns.html"><code>Dns</code></a>
/api/protocols/nfs/services| <a title="netapp_ontap.resources.nfs_service.NfsService" href="../resources/nfs_service.html"><code>NfsService</code></a>
/api/support/ems/messages| <a title="netapp_ontap.resources.ems_message.EmsMessage" href="../resources/ems_message.html"><code>EmsMessage</code></a>
/api/protocols/fpolicy/{svm[uuid]}/policies| <a title="netapp_ontap.resources.fpolicy_policy.FpolicyPolicy" href="../resources/fpolicy_policy.html"><code>FpolicyPolicy</code></a>
/api/security/authentication/password| <a title="netapp_ontap.resources.account_password.AccountPassword" href="../resources/account_password.html"><code>AccountPassword</code></a>
/api/protocols/vscan/{svm[uuid]}/on-access-policies| <a title="netapp_ontap.resources.vscan_on_access.VscanOnAccess" href="../resources/vscan_on_access.html"><code>VscanOnAccess</code></a>
/api/security/authentication/cluster/ad-proxy| <a title="netapp_ontap.resources.cluster_ad_proxy.ClusterAdProxy" href="../resources/cluster_ad_proxy.html"><code>ClusterAdProxy</code></a>
/api/cluster/ntp/servers| <a title="netapp_ontap.resources.ntp_server.NtpServer" href="../resources/ntp_server.html"><code>NtpServer</code></a>
/api/storage/volumes/{volume[uuid]}/snapshots| <a title="netapp_ontap.resources.snapshot.Snapshot" href="../resources/snapshot.html"><code>Snapshot</code></a>
/api/protocols/vscan| <a title="netapp_ontap.resources.vscan.Vscan" href="../resources/vscan.html"><code>Vscan</code></a>
/api/storage/namespaces| <a title="netapp_ontap.resources.nvme_namespace.NvmeNamespace" href="../resources/nvme_namespace.html"><code>NvmeNamespace</code></a>
/api/storage/snaplock/audit-logs| <a title="netapp_ontap.resources.snaplock_log.SnaplockLog" href="../resources/snaplock_log.html"><code>SnaplockLog</code></a>
/api/protocols/nfs/services/{svm[uuid]}/metrics| <a title="netapp_ontap.resources.performance_svm_nfs.PerformanceSvmNfs" href="../resources/performance_svm_nfs.html"><code>PerformanceSvmNfs</code></a>
/api/security/authentication/publickeys| <a title="netapp_ontap.resources.publickey.Publickey" href="../resources/publickey.html"><code>Publickey</code></a>
/api/protocols/s3/services/{svm[uuid]}/users| <a title="netapp_ontap.resources.s3_user.S3User" href="../resources/s3_user.html"><code>S3User</code></a>
/api/security/login/messages| <a title="netapp_ontap.resources.login_messages.LoginMessages" href="../resources/login_messages.html"><code>LoginMessages</code></a>
/api/svm/peer-permissions| <a title="netapp_ontap.resources.svm_peer_permission.SvmPeerPermission" href="../resources/svm_peer_permission.html"><code>SvmPeerPermission</code></a>
/api/protocols/san/fcp/services| <a title="netapp_ontap.resources.fcp_service.FcpService" href="../resources/fcp_service.html"><code>FcpService</code></a>
/api/storage/luns/{lun[uuid]}/metrics| <a title="netapp_ontap.resources.performance_lun_metric.PerformanceLunMetric" href="../resources/performance_lun_metric.html"><code>PerformanceLunMetric</code></a>
/api/protocols/vscan/{svm[uuid]}/scanner-pools| <a title="netapp_ontap.resources.vscan_scanner_pool.VscanScannerPool" href="../resources/vscan_scanner_pool.html"><code>VscanScannerPool</code></a>
/api/storage/aggregates/{aggregate[uuid]}/metrics| <a title="netapp_ontap.resources.performance_metric.PerformanceMetric" href="../resources/performance_metric.html"><code>PerformanceMetric</code></a>
/api/storage/qos/policies| <a title="netapp_ontap.resources.qos_policy.QosPolicy" href="../resources/qos_policy.html"><code>QosPolicy</code></a>
/api/storage/snapshot-policies/{snapshot-policy[uuid]}/schedules| <a title="netapp_ontap.resources.snapshot_policy_schedule.SnapshotPolicySchedule" href="../resources/snapshot_policy_schedule.html"><code>SnapshotPolicySchedule</code></a>
/api/security/authentication/cluster/ldap| <a title="netapp_ontap.resources.cluster_ldap.ClusterLdap" href="../resources/cluster_ldap.html"><code>ClusterLdap</code></a>
/api/svm/peers| <a title="netapp_ontap.resources.svm_peer.SvmPeer" href="../resources/svm_peer.html"><code>SvmPeer</code></a>
/api/storage/cluster| <a title="netapp_ontap.resources.cluster_space.ClusterSpace" href="../resources/cluster_space.html"><code>ClusterSpace</code></a>
/api/protocols/nfs/connected-clients| <a title="netapp_ontap.resources.nfs_clients.NfsClients" href="../resources/nfs_clients.html"><code>NfsClients</code></a>
/api/storage/disks| <a title="netapp_ontap.resources.disk.Disk" href="../resources/disk.html"><code>Disk</code></a>
/api/protocols/cifs/home-directory/search-paths| <a title="netapp_ontap.resources.cifs_search_path.CifsSearchPath" href="../resources/cifs_search_path.html"><code>CifsSearchPath</code></a>
/api/support/ems| <a title="netapp_ontap.resources.ems_config.EmsConfig" href="../resources/ems_config.html"><code>EmsConfig</code></a>
/api/storage/snaplock/litigations/{litigation[id]}/files| <a title="netapp_ontap.resources.snaplock_litigation_file.SnaplockLitigationFile" href="../resources/snaplock_litigation_file.html"><code>SnaplockLitigationFile</code></a>
/api/storage/qtrees| <a title="netapp_ontap.resources.qtree.Qtree" href="../resources/qtree.html"><code>Qtree</code></a>
/api/protocols/vscan/server-status| <a title="netapp_ontap.resources.vscan_server_status.VscanServerStatus" href="../resources/vscan_server_status.html"><code>VscanServerStatus</code></a>
/api/protocols/nvme/subsystems| <a title="netapp_ontap.resources.nvme_subsystem.NvmeSubsystem" href="../resources/nvme_subsystem.html"><code>NvmeSubsystem</code></a>
/api/protocols/ndmp/sessions| <a title="netapp_ontap.resources.ndmp_session.NdmpSession" href="../resources/ndmp_session.html"><code>NdmpSession</code></a>
/api/application/applications| <a title="netapp_ontap.resources.application.Application" href="../resources/application.html"><code>Application</code></a>
/api/storage/quota/rules| <a title="netapp_ontap.resources.quota_rule.QuotaRule" href="../resources/quota_rule.html"><code>QuotaRule</code></a>
/api/cluster| <a title="netapp_ontap.resources.cluster.Cluster" href="../resources/cluster.html"><code>Cluster</code></a>
/api/protocols/nvme/services| <a title="netapp_ontap.resources.nvme_service.NvmeService" href="../resources/nvme_service.html"><code>NvmeService</code></a>
/api/protocols/ndmp/svms| <a title="netapp_ontap.resources.ndmp_svm.NdmpSvm" href="../resources/ndmp_svm.html"><code>NdmpSvm</code></a>
/api/storage/quota/reports| <a title="netapp_ontap.resources.quota_report.QuotaReport" href="../resources/quota_report.html"><code>QuotaReport</code></a>
/api/protocols/san/iscsi/sessions| <a title="netapp_ontap.resources.iscsi_session.IscsiSession" href="../resources/iscsi_session.html"><code>IscsiSession</code></a>
/api/storage/snaplock/event-retention/policies| <a title="netapp_ontap.resources.snaplock_retention_policy.SnaplockRetentionPolicy" href="../resources/snaplock_retention_policy.html"><code>SnaplockRetentionPolicy</code></a>
/api/storage/snaplock/file| <a title="netapp_ontap.resources.snaplock_file_retention.SnaplockFileRetention" href="../resources/snaplock_file_retention.html"><code>SnaplockFileRetention</code></a>
/api/cluster/chassis| <a title="netapp_ontap.resources.chassis.Chassis" href="../resources/chassis.html"><code>Chassis</code></a>
/api/application/templates| <a title="netapp_ontap.resources.application_template.ApplicationTemplate" href="../resources/application_template.html"><code>ApplicationTemplate</code></a>
/api/storage/file/clone| <a title="netapp_ontap.resources.file_clone.FileClone" href="../resources/file_clone.html"><code>FileClone</code></a>
/api/cluster/nodes| <a title="netapp_ontap.resources.node.Node" href="../resources/node.html"><code>Node</code></a>
/api/support/snmp/users| <a title="netapp_ontap.resources.snmp_user.SnmpUser" href="../resources/snmp_user.html"><code>SnmpUser</code></a>
/api/protocols/audit| <a title="netapp_ontap.resources.audit.Audit" href="../resources/audit.html"><code>Audit</code></a>
/api/network/fc/interfaces| <a title="netapp_ontap.resources.fc_interface.FcInterface" href="../resources/fc_interface.html"><code>FcInterface</code></a>
/api/svm/svms| <a title="netapp_ontap.resources.svm.Svm" href="../resources/svm.html"><code>Svm</code></a>
/api/protocols/cifs/services/{svm[uuid]}/metrics| <a title="netapp_ontap.resources.performance_cifs_metric.PerformanceCifsMetric" href="../resources/performance_cifs_metric.html"><code>PerformanceCifsMetric</code></a>
/api/name-services/nis| <a title="netapp_ontap.resources.nis_service.NisService" href="../resources/nis_service.html"><code>NisService</code></a>
/api/protocols/nvme/services/{svm[uuid]}/metrics| <a title="netapp_ontap.resources.performance_nvme_metric.PerformanceNvmeMetric" href="../resources/performance_nvme_metric.html"><code>PerformanceNvmeMetric</code></a>
/api/application/applications/{application[uuid]}/components| <a title="netapp_ontap.resources.application_component.ApplicationComponent" href="../resources/application_component.html"><code>ApplicationComponent</code></a>
/api/name-services/name-mappings| <a title="netapp_ontap.resources.name_mapping.NameMapping" href="../resources/name_mapping.html"><code>NameMapping</code></a>
/api/protocols/s3/services/{svm[uuid]}/buckets| <a title="netapp_ontap.resources.s3_bucket_svm.S3BucketSvm" href="../resources/s3_bucket_svm.html"><code>S3BucketSvm</code></a>
/api/support/snmp/traphosts| <a title="netapp_ontap.resources.snmp_traphost.SnmpTraphost" href="../resources/snmp_traphost.html"><code>SnmpTraphost</code></a>
/api/storage/ports| <a title="netapp_ontap.resources.storage_port.StoragePort" href="../resources/storage_port.html"><code>StoragePort</code></a>
/api/snapmirror/relationships/{relationship[uuid]}/transfers| <a title="netapp_ontap.resources.snapmirror_transfer.SnapmirrorTransfer" href="../resources/snapmirror_transfer.html"><code>SnapmirrorTransfer</code></a>
/api/protocols/san/igroups| <a title="netapp_ontap.resources.igroup.Igroup" href="../resources/igroup.html"><code>Igroup</code></a>
/api/security/certificates| <a title="netapp_ontap.resources.security_certificate.SecurityCertificate" href="../resources/security_certificate.html"><code>SecurityCertificate</code></a>
/api/name-services/ldap| <a title="netapp_ontap.resources.ldap_service.LdapService" href="../resources/ldap_service.html"><code>LdapService</code></a>
/api/snapmirror/relationships| <a title="netapp_ontap.resources.snapmirror_relationship.SnapmirrorRelationship" href="../resources/snapmirror_relationship.html"><code>SnapmirrorRelationship</code></a>
/api/storage/volumes/{volume[uuid]}/metrics| <a title="netapp_ontap.resources.volume_metrics.VolumeMetrics" href="../resources/volume_metrics.html"><code>VolumeMetrics</code></a>
/api/protocols/nvme/interfaces| <a title="netapp_ontap.resources.nvme_interface.NvmeInterface" href="../resources/nvme_interface.html"><code>NvmeInterface</code></a>
/api/protocols/nvme/subsystem-controllers| <a title="netapp_ontap.resources.nvme_subsystem_controller.NvmeSubsystemController" href="../resources/nvme_subsystem_controller.html"><code>NvmeSubsystemController</code></a>
/api/protocols/s3/services| <a title="netapp_ontap.resources.s3_service.S3Service" href="../resources/s3_service.html"><code>S3Service</code></a>
/api/storage/snaplock/event-retention/operations| <a title="netapp_ontap.resources.ebr_operation.EbrOperation" href="../resources/ebr_operation.html"><code>EbrOperation</code></a>
/api/snapmirror/policies| <a title="netapp_ontap.resources.snapmirror_policy.SnapmirrorPolicy" href="../resources/snapmirror_policy.html"><code>SnapmirrorPolicy</code></a>
/api/cluster/software| <a title="netapp_ontap.resources.software.Software" href="../resources/software.html"><code>Software</code></a>
/api/protocols/nvme/subsystem-maps| <a title="netapp_ontap.resources.nvme_subsystem_map.NvmeSubsystemMap" href="../resources/nvme_subsystem_map.html"><code>NvmeSubsystemMap</code></a>
/api/support/ems/events| <a title="netapp_ontap.resources.ems_event.EmsEvent" href="../resources/ems_event.html"><code>EmsEvent</code></a>
/api/protocols/s3/buckets| <a title="netapp_ontap.resources.s3_bucket.S3Bucket" href="../resources/s3_bucket.html"><code>S3Bucket</code></a>
/api/network/ip/routes| <a title="netapp_ontap.resources.network_route.NetworkRoute" href="../resources/network_route.html"><code>NetworkRoute</code></a>
/api/support/ems/destinations| <a title="netapp_ontap.resources.ems_destination.EmsDestination" href="../resources/ems_destination.html"><code>EmsDestination</code></a>
/api/network/ethernet/broadcast-domains| <a title="netapp_ontap.resources.broadcast_domain.BroadcastDomain" href="../resources/broadcast_domain.html"><code>BroadcastDomain</code></a>
/api/protocols/san/iscsi/services/{svm[uuid]}/metrics| <a title="netapp_ontap.resources.performance_iscsi_metric.PerformanceIscsiMetric" href="../resources/performance_iscsi_metric.html"><code>PerformanceIscsiMetric</code></a>
/api/cluster/ntp/keys| <a title="netapp_ontap.resources.ntp_key.NtpKey" href="../resources/ntp_key.html"><code>NtpKey</code></a>
/api/storage/snaplock/litigations/{litigation[id]}/operations| <a title="netapp_ontap.resources.snaplock_legal_hold_operation.SnaplockLegalHoldOperation" href="../resources/snaplock_legal_hold_operation.html"><code>SnaplockLegalHoldOperation</code></a>
/api/cluster/licensing/licenses| <a title="netapp_ontap.resources.license_package.LicensePackage" href="../resources/license_package.html"><code>LicensePackage</code></a>
/api/storage/snapshot-policies| <a title="netapp_ontap.resources.snapshot_policy.SnapshotPolicy" href="../resources/snapshot_policy.html"><code>SnapshotPolicy</code></a>
/api/protocols/nfs/export-policies/{policy[id]}/rules/{export_rule[index]}/clients| <a title="netapp_ontap.resources.export_client.ExportClient" href="../resources/export_client.html"><code>ExportClient</code></a>
/api/protocols/ndmp/nodes| <a title="netapp_ontap.resources.ndmp_node.NdmpNode" href="../resources/ndmp_node.html"><code>NdmpNode</code></a>
/api/cluster/software/packages| <a title="netapp_ontap.resources.software_package.SoftwarePackage" href="../resources/software_package.html"><code>SoftwarePackage</code></a>
/api/security/audit/destinations| <a title="netapp_ontap.resources.security_audit_log_forward.SecurityAuditLogForward" href="../resources/security_audit_log_forward.html"><code>SecurityAuditLogForward</code></a>
/api/storage/snaplock/litigations| <a title="netapp_ontap.resources.snaplock_litigation.SnaplockLitigation" href="../resources/snaplock_litigation.html"><code>SnaplockLitigation</code></a>
/api/security/authentication/cluster/nis| <a title="netapp_ontap.resources.cluster_nis_service.ClusterNisService" href="../resources/cluster_nis_service.html"><code>ClusterNisService</code></a>
/api/protocols/fpolicy/{svm[uuid]}/engines| <a title="netapp_ontap.resources.fpolicy_engine.FpolicyEngine" href="../resources/fpolicy_engine.html"><code>FpolicyEngine</code></a>
/api/support/configuration-backup| <a title="netapp_ontap.resources.configuration_backup.ConfigurationBackup" href="../resources/configuration_backup.html"><code>ConfigurationBackup</code></a>
/api/protocols/nfs/export-policies/{policy[id]}/rules| <a title="netapp_ontap.resources.export_rule.ExportRule" href="../resources/export_rule.html"><code>ExportRule</code></a>
/api/security/authentication/cluster/saml-sp| <a title="netapp_ontap.resources.security_saml_sp.SecuritySamlSp" href="../resources/security_saml_sp.html"><code>SecuritySamlSp</code></a>
/api/storage/aggregates/{aggregate[uuid]}/plexes| <a title="netapp_ontap.resources.plex.Plex" href="../resources/plex.html"><code>Plex</code></a>
/api/protocols/cifs/shares/{svm[uuid]}/{cifs_share[share]}/acls| <a title="netapp_ontap.resources.cifs_share_acl.CifsShareAcl" href="../resources/cifs_share_acl.html"><code>CifsShareAcl</code></a>
/api/security/key-managers/{security_key_manager[uuid]}/key-servers| <a title="netapp_ontap.resources.key_server.KeyServer" href="../resources/key_server.html"><code>KeyServer</code></a>
/api/application/applications/{application[uuid]}/snapshots| <a title="netapp_ontap.resources.application_snapshot.ApplicationSnapshot" href="../resources/application_snapshot.html"><code>ApplicationSnapshot</code></a>
/api/security/audit/messages| <a title="netapp_ontap.resources.security_audit_log.SecurityAuditLog" href="../resources/security_audit_log.html"><code>SecurityAuditLog</code></a>
/api/cluster/jobs| <a title="netapp_ontap.resources.job.Job" href="../resources/job.html"><code>Job</code></a>
/api/protocols/ndmp| <a title="netapp_ontap.resources.cluster_ndmp_properties.ClusterNdmpProperties" href="../resources/cluster_ndmp_properties.html"><code>ClusterNdmpProperties</code></a>
/api/cluster/metrics| <a title="netapp_ontap.resources.cluster_metrics.ClusterMetrics" href="../resources/cluster_metrics.html"><code>ClusterMetrics</code></a>
/api/security/key-managers| <a title="netapp_ontap.resources.security_key_manager.SecurityKeyManager" href="../resources/security_key_manager.html"><code>SecurityKeyManager</code></a>
/api/security/audit| <a title="netapp_ontap.resources.security_audit.SecurityAudit" href="../resources/security_audit.html"><code>SecurityAudit</code></a>
/api/storage/aggregates| <a title="netapp_ontap.resources.aggregate.Aggregate" href="../resources/aggregate.html"><code>Aggregate</code></a>
/api/storage/aggregates/{aggregate[uuid]}/cloud-stores| <a title="netapp_ontap.resources.cloud_store.CloudStore" href="../resources/cloud_store.html"><code>CloudStore</code></a>
/api/security/roles/{owner[uuid]}/{role[name]}/privileges| <a title="netapp_ontap.resources.role_privilege.RolePrivilege" href="../resources/role_privilege.html"><code>RolePrivilege</code></a>
/api/cluster/peers| <a title="netapp_ontap.resources.cluster_peer.ClusterPeer" href="../resources/cluster_peer.html"><code>ClusterPeer</code></a>
/api/protocols/vscan/{svm[uuid]}/on-demand-policies| <a title="netapp_ontap.resources.vscan_on_demand.VscanOnDemand" href="../resources/vscan_on_demand.html"><code>VscanOnDemand</code></a>
/api/protocols/san/fcp/services/{svm[uuid]}/metrics| <a title="netapp_ontap.resources.performance_fcp_metric.PerformanceFcpMetric" href="../resources/performance_fcp_metric.html"><code>PerformanceFcpMetric</code></a>
/api/cluster/software/history| <a title="netapp_ontap.resources.software_history.SoftwareHistory" href="../resources/software_history.html"><code>SoftwareHistory</code></a>
/api/protocols/san/iscsi/services| <a title="netapp_ontap.resources.iscsi_service.IscsiService" href="../resources/iscsi_service.html"><code>IscsiService</code></a>
/api/protocols/san/iscsi/credentials| <a title="netapp_ontap.resources.iscsi_credentials.IscsiCredentials" href="../resources/iscsi_credentials.html"><code>IscsiCredentials</code></a>
/api/protocols/cifs/unix-symlink-mapping| <a title="netapp_ontap.resources.cifs_symlink_mapping.CifsSymlinkMapping" href="../resources/cifs_symlink_mapping.html"><code>CifsSymlinkMapping</code></a>
/api/security/accounts| <a title="netapp_ontap.resources.account.Account" href="../resources/account.html"><code>Account</code></a>
"""

# pylint: disable=trailing-newlines
# pylint: disable=too-many-lines

from netapp_ontap.models import *

from netapp_ontap.resources.cli import CLI

from netapp_ontap.resources.lun import Lun
from netapp_ontap.resources.autosupport import Autosupport
from netapp_ontap.resources.software_package_download import SoftwarePackageDownload
from netapp_ontap.resources.file_info import FileInfo
from netapp_ontap.resources.ip_service_policy import IpServicePolicy
from netapp_ontap.resources.export_policy import ExportPolicy
from netapp_ontap.resources.snaplock_file_fingerprint import SnaplockFileFingerprint
from netapp_ontap.resources.ipspace import Ipspace
from netapp_ontap.resources.network_http_proxy import NetworkHttpProxy
from netapp_ontap.resources.fpolicy import Fpolicy
from netapp_ontap.resources.role import Role
from netapp_ontap.resources.ems_filter_rule import EmsFilterRule
from netapp_ontap.resources.flexcache import Flexcache
from netapp_ontap.resources.fpolicy_event import FpolicyEvent
from netapp_ontap.resources.fc_login import FcLogin
from netapp_ontap.resources.application_component_snapshot import ApplicationComponentSnapshot
from netapp_ontap.resources.cifs_share import CifsShare
from netapp_ontap.resources.cifs_service import CifsService
from netapp_ontap.resources.nvme_subsystem_host import NvmeSubsystemHost
from netapp_ontap.resources.kerberos_realm import KerberosRealm
from netapp_ontap.resources.kerberos_interface import KerberosInterface
from netapp_ontap.resources.cluster_ssh_server import ClusterSshServer
from netapp_ontap.resources.wwpn_alias import WwpnAlias
from netapp_ontap.resources.flexcache_origin import FlexcacheOrigin
from netapp_ontap.resources.shelf import Shelf
from netapp_ontap.resources.volume import Volume
from netapp_ontap.resources.igroup_initiator import IgroupInitiator
from netapp_ontap.resources.port import Port
from netapp_ontap.resources.snaplock_compliance_clock import SnaplockComplianceClock
from netapp_ontap.resources.autosupport_message import AutosupportMessage
from netapp_ontap.resources.ems_filter import EmsFilter
from netapp_ontap.resources.fc_port import FcPort
from netapp_ontap.resources.bgp_peer_group import BgpPeerGroup
from netapp_ontap.resources.cloud_target import CloudTarget
from netapp_ontap.resources.schedule import Schedule
from netapp_ontap.resources.ip_interface import IpInterface
from netapp_ontap.resources.snmp import Snmp
from netapp_ontap.resources.lun_map import LunMap
from netapp_ontap.resources.configuration_backup_file import ConfigurationBackupFile
from netapp_ontap.resources.security_config import SecurityConfig
from netapp_ontap.resources.dns import Dns
from netapp_ontap.resources.nfs_service import NfsService
from netapp_ontap.resources.ems_message import EmsMessage
from netapp_ontap.resources.fpolicy_policy import FpolicyPolicy
from netapp_ontap.resources.account_password import AccountPassword
from netapp_ontap.resources.vscan_on_access import VscanOnAccess
from netapp_ontap.resources.cluster_ad_proxy import ClusterAdProxy
from netapp_ontap.resources.ntp_server import NtpServer
from netapp_ontap.resources.snapshot import Snapshot
from netapp_ontap.resources.vscan import Vscan
from netapp_ontap.resources.nvme_namespace import NvmeNamespace
from netapp_ontap.resources.snaplock_log import SnaplockLog
from netapp_ontap.resources.performance_svm_nfs import PerformanceSvmNfs
from netapp_ontap.resources.publickey import Publickey
from netapp_ontap.resources.s3_user import S3User
from netapp_ontap.resources.login_messages import LoginMessages
from netapp_ontap.resources.svm_peer_permission import SvmPeerPermission
from netapp_ontap.resources.fcp_service import FcpService
from netapp_ontap.resources.performance_lun_metric import PerformanceLunMetric
from netapp_ontap.resources.vscan_scanner_pool import VscanScannerPool
from netapp_ontap.resources.performance_metric import PerformanceMetric
from netapp_ontap.resources.qos_policy import QosPolicy
from netapp_ontap.resources.snapshot_policy_schedule import SnapshotPolicySchedule
from netapp_ontap.resources.cluster_ldap import ClusterLdap
from netapp_ontap.resources.svm_peer import SvmPeer
from netapp_ontap.resources.cluster_space import ClusterSpace
from netapp_ontap.resources.nfs_clients import NfsClients
from netapp_ontap.resources.disk import Disk
from netapp_ontap.resources.cifs_search_path import CifsSearchPath
from netapp_ontap.resources.ems_config import EmsConfig
from netapp_ontap.resources.snaplock_litigation_file import SnaplockLitigationFile
from netapp_ontap.resources.qtree import Qtree
from netapp_ontap.resources.vscan_server_status import VscanServerStatus
from netapp_ontap.resources.nvme_subsystem import NvmeSubsystem
from netapp_ontap.resources.ndmp_session import NdmpSession
from netapp_ontap.resources.application import Application
from netapp_ontap.resources.quota_rule import QuotaRule
from netapp_ontap.resources.cluster import Cluster
from netapp_ontap.resources.nvme_service import NvmeService
from netapp_ontap.resources.ndmp_svm import NdmpSvm
from netapp_ontap.resources.quota_report import QuotaReport
from netapp_ontap.resources.iscsi_session import IscsiSession
from netapp_ontap.resources.snaplock_retention_policy import SnaplockRetentionPolicy
from netapp_ontap.resources.snaplock_file_retention import SnaplockFileRetention
from netapp_ontap.resources.chassis import Chassis
from netapp_ontap.resources.application_template import ApplicationTemplate
from netapp_ontap.resources.file_clone import FileClone
from netapp_ontap.resources.node import Node
from netapp_ontap.resources.snmp_user import SnmpUser
from netapp_ontap.resources.audit import Audit
from netapp_ontap.resources.fc_interface import FcInterface
from netapp_ontap.resources.svm import Svm
from netapp_ontap.resources.performance_cifs_metric import PerformanceCifsMetric
from netapp_ontap.resources.nis_service import NisService
from netapp_ontap.resources.performance_nvme_metric import PerformanceNvmeMetric
from netapp_ontap.resources.application_component import ApplicationComponent
from netapp_ontap.resources.name_mapping import NameMapping
from netapp_ontap.resources.s3_bucket_svm import S3BucketSvm
from netapp_ontap.resources.snmp_traphost import SnmpTraphost
from netapp_ontap.resources.storage_port import StoragePort
from netapp_ontap.resources.snapmirror_transfer import SnapmirrorTransfer
from netapp_ontap.resources.igroup import Igroup
from netapp_ontap.resources.security_certificate import SecurityCertificate
from netapp_ontap.resources.ldap_service import LdapService
from netapp_ontap.resources.snapmirror_relationship import SnapmirrorRelationship
from netapp_ontap.resources.volume_metrics import VolumeMetrics
from netapp_ontap.resources.nvme_interface import NvmeInterface
from netapp_ontap.resources.nvme_subsystem_controller import NvmeSubsystemController
from netapp_ontap.resources.s3_service import S3Service
from netapp_ontap.resources.ebr_operation import EbrOperation
from netapp_ontap.resources.snapmirror_policy import SnapmirrorPolicy
from netapp_ontap.resources.software import Software
from netapp_ontap.resources.nvme_subsystem_map import NvmeSubsystemMap
from netapp_ontap.resources.ems_event import EmsEvent
from netapp_ontap.resources.s3_bucket import S3Bucket
from netapp_ontap.resources.network_route import NetworkRoute
from netapp_ontap.resources.ems_destination import EmsDestination
from netapp_ontap.resources.broadcast_domain import BroadcastDomain
from netapp_ontap.resources.performance_iscsi_metric import PerformanceIscsiMetric
from netapp_ontap.resources.ntp_key import NtpKey
from netapp_ontap.resources.snaplock_legal_hold_operation import SnaplockLegalHoldOperation
from netapp_ontap.resources.license_package import LicensePackage
from netapp_ontap.resources.snapshot_policy import SnapshotPolicy
from netapp_ontap.resources.export_client import ExportClient
from netapp_ontap.resources.ndmp_node import NdmpNode
from netapp_ontap.resources.software_package import SoftwarePackage
from netapp_ontap.resources.security_audit_log_forward import SecurityAuditLogForward
from netapp_ontap.resources.snaplock_litigation import SnaplockLitigation
from netapp_ontap.resources.cluster_nis_service import ClusterNisService
from netapp_ontap.resources.fpolicy_engine import FpolicyEngine
from netapp_ontap.resources.configuration_backup import ConfigurationBackup
from netapp_ontap.resources.export_rule import ExportRule
from netapp_ontap.resources.security_saml_sp import SecuritySamlSp
from netapp_ontap.resources.plex import Plex
from netapp_ontap.resources.cifs_share_acl import CifsShareAcl
from netapp_ontap.resources.key_server import KeyServer
from netapp_ontap.resources.application_snapshot import ApplicationSnapshot
from netapp_ontap.resources.security_audit_log import SecurityAuditLog
from netapp_ontap.resources.job import Job
from netapp_ontap.resources.cluster_ndmp_properties import ClusterNdmpProperties
from netapp_ontap.resources.cluster_metrics import ClusterMetrics
from netapp_ontap.resources.security_key_manager import SecurityKeyManager
from netapp_ontap.resources.security_audit import SecurityAudit
from netapp_ontap.resources.aggregate import Aggregate
from netapp_ontap.resources.cloud_store import CloudStore
from netapp_ontap.resources.role_privilege import RolePrivilege
from netapp_ontap.resources.cluster_peer import ClusterPeer
from netapp_ontap.resources.vscan_on_demand import VscanOnDemand
from netapp_ontap.resources.performance_fcp_metric import PerformanceFcpMetric
from netapp_ontap.resources.software_history import SoftwareHistory
from netapp_ontap.resources.iscsi_service import IscsiService
from netapp_ontap.resources.iscsi_credentials import IscsiCredentials
from netapp_ontap.resources.cifs_symlink_mapping import CifsSymlinkMapping
from netapp_ontap.resources.account import Account

__all__ = [
    "Lun",
    "Autosupport",
    "SoftwarePackageDownload",
    "FileInfo",
    "IpServicePolicy",
    "ExportPolicy",
    "SnaplockFileFingerprint",
    "Ipspace",
    "NetworkHttpProxy",
    "Fpolicy",
    "Role",
    "EmsFilterRule",
    "Flexcache",
    "FpolicyEvent",
    "FcLogin",
    "ApplicationComponentSnapshot",
    "CifsShare",
    "CifsService",
    "NvmeSubsystemHost",
    "KerberosRealm",
    "KerberosInterface",
    "ClusterSshServer",
    "WwpnAlias",
    "FlexcacheOrigin",
    "Shelf",
    "Volume",
    "IgroupInitiator",
    "Port",
    "SnaplockComplianceClock",
    "AutosupportMessage",
    "EmsFilter",
    "FcPort",
    "BgpPeerGroup",
    "CloudTarget",
    "Schedule",
    "IpInterface",
    "Snmp",
    "LunMap",
    "ConfigurationBackupFile",
    "SecurityConfig",
    "Dns",
    "NfsService",
    "EmsMessage",
    "FpolicyPolicy",
    "AccountPassword",
    "VscanOnAccess",
    "ClusterAdProxy",
    "NtpServer",
    "Snapshot",
    "Vscan",
    "NvmeNamespace",
    "SnaplockLog",
    "PerformanceSvmNfs",
    "Publickey",
    "S3User",
    "LoginMessages",
    "SvmPeerPermission",
    "FcpService",
    "PerformanceLunMetric",
    "VscanScannerPool",
    "PerformanceMetric",
    "QosPolicy",
    "SnapshotPolicySchedule",
    "ClusterLdap",
    "SvmPeer",
    "ClusterSpace",
    "NfsClients",
    "Disk",
    "CifsSearchPath",
    "EmsConfig",
    "SnaplockLitigationFile",
    "Qtree",
    "VscanServerStatus",
    "NvmeSubsystem",
    "NdmpSession",
    "Application",
    "QuotaRule",
    "Cluster",
    "NvmeService",
    "NdmpSvm",
    "QuotaReport",
    "IscsiSession",
    "SnaplockRetentionPolicy",
    "SnaplockFileRetention",
    "Chassis",
    "ApplicationTemplate",
    "FileClone",
    "Node",
    "SnmpUser",
    "Audit",
    "FcInterface",
    "Svm",
    "PerformanceCifsMetric",
    "NisService",
    "PerformanceNvmeMetric",
    "ApplicationComponent",
    "NameMapping",
    "S3BucketSvm",
    "SnmpTraphost",
    "StoragePort",
    "SnapmirrorTransfer",
    "Igroup",
    "SecurityCertificate",
    "LdapService",
    "SnapmirrorRelationship",
    "VolumeMetrics",
    "NvmeInterface",
    "NvmeSubsystemController",
    "S3Service",
    "EbrOperation",
    "SnapmirrorPolicy",
    "Software",
    "NvmeSubsystemMap",
    "EmsEvent",
    "S3Bucket",
    "NetworkRoute",
    "EmsDestination",
    "BroadcastDomain",
    "PerformanceIscsiMetric",
    "NtpKey",
    "SnaplockLegalHoldOperation",
    "LicensePackage",
    "SnapshotPolicy",
    "ExportClient",
    "NdmpNode",
    "SoftwarePackage",
    "SecurityAuditLogForward",
    "SnaplockLitigation",
    "ClusterNisService",
    "FpolicyEngine",
    "ConfigurationBackup",
    "ExportRule",
    "SecuritySamlSp",
    "Plex",
    "CifsShareAcl",
    "KeyServer",
    "ApplicationSnapshot",
    "SecurityAuditLog",
    "Job",
    "ClusterNdmpProperties",
    "ClusterMetrics",
    "SecurityKeyManager",
    "SecurityAudit",
    "Aggregate",
    "CloudStore",
    "RolePrivilege",
    "ClusterPeer",
    "VscanOnDemand",
    "PerformanceFcpMetric",
    "SoftwareHistory",
    "IscsiService",
    "IscsiCredentials",
    "CifsSymlinkMapping",
    "Account",
]
__all__.append('CLI')
