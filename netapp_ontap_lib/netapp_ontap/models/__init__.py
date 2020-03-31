"""
Copyright &copy; 2019 NetApp Inc. All rights reserved.

All of the modules in this package define the supporting objects used to
organize the fields in the corresponding `netapp_ontap.resource.Resource`
types. These models are a subset of `netapp_ontap.resource.Resource` and
do not have any actions that can be performed on them.
"""

# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from netapp_ontap.models.volume_tiering import VolumeTiering
from netapp_ontap.models.vsi_on_san_new_igroups import VsiOnSanNewIgroups
from netapp_ontap.models.performance_metric_raw import PerformanceMetricRaw
from netapp_ontap.models.volume_space import VolumeSpace
from netapp_ontap.models.volume_qos import VolumeQos
from netapp_ontap.models.nfs_service_protocol import NfsServiceProtocol
from netapp_ontap.models.volume_guarantee import VolumeGuarantee
from netapp_ontap.models.cluster_space_block_storage_medias import ClusterSpaceBlockStorageMedias
from netapp_ontap.models.node_ha_giveback import NodeHaGiveback
from netapp_ontap.models.node_vm import NodeVm
from netapp_ontap.models.snapmirror_policy_rule import SnapmirrorPolicyRule
from netapp_ontap.models.application_statistics_iops import ApplicationStatisticsIops
from netapp_ontap.models.fc_port_speed import FcPortSpeed
from netapp_ontap.models.raid_group_disk import RaidGroupDisk
from netapp_ontap.models.vsi_on_nas import VsiOnNas
from netapp_ontap.models.port_vlan import PortVlan
from netapp_ontap.models.software_reference_metrocluster_progress_summary import SoftwareReferenceMetroclusterProgressSummary
from netapp_ontap.models.security_saml_sp_certificate import SecuritySamlSpCertificate
from netapp_ontap.models.snapmirror_relationship_policy import SnapmirrorRelationshipPolicy
from netapp_ontap.models.nvme_subsystem_hosts import NvmeSubsystemHosts
from netapp_ontap.models.vsi_on_nas_datastore_storage_service import VsiOnNasDatastoreStorageService
from netapp_ontap.models.ad_domain import AdDomain
from netapp_ontap.models.oracle_rac_on_nfs_oracle_crs import OracleRacOnNfsOracleCrs
from netapp_ontap.models.application_statistics_latency import ApplicationStatisticsLatency
from netapp_ontap.models.scope_ipspace import ScopeIpspace
from netapp_ontap.models.volume_efficiency import VolumeEfficiency
from netapp_ontap.models.lun_status import LunStatus
from netapp_ontap.models.version import Version
from netapp_ontap.models.key_server_state import KeyServerState
from netapp_ontap.models.node_cluster_interface import NodeClusterInterface
from netapp_ontap.models.svm_nis import SvmNis
from netapp_ontap.models.nvme_interface_fc_interface import NvmeInterfaceFcInterface
from netapp_ontap.models.nvme_subsystem_host_subsystem import NvmeSubsystemHostSubsystem
from netapp_ontap.models.oracle_rac_on_san_new_igroups import OracleRacOnSanNewIgroups
from netapp_ontap.models.maxdata_on_san import MaxdataOnSan
from netapp_ontap.models.nas_storage_service import NasStorageService
from netapp_ontap.models.nvme_namespace_space_guarantee import NvmeNamespaceSpaceGuarantee
from netapp_ontap.models.node_management_interface import NodeManagementInterface
from netapp_ontap.models.vdi_on_nas_hyper_v_access import VdiOnNasHyperVAccess
from netapp_ontap.models.oracle_on_nfs_ora_home import OracleOnNfsOraHome
from netapp_ontap.models.snapmirror_endpoint import SnapmirrorEndpoint
from netapp_ontap.models.application_links import ApplicationLinks
from netapp_ontap.models.node_ha_takeover_failure import NodeHaTakeoverFailure
from netapp_ontap.models.application_subsystem_map_object_subsystem_links import ApplicationSubsystemMapObjectSubsystemLinks
from netapp_ontap.models.lun_lun_maps import LunLunMaps
from netapp_ontap.models.sql_on_san_log import SqlOnSanLog
from netapp_ontap.models.application_nfs_properties_permissions import ApplicationNfsPropertiesPermissions
from netapp_ontap.models.ip_interface_svm_location import IpInterfaceSvmLocation
from netapp_ontap.models.iscsi_connection_interface import IscsiConnectionInterface
from netapp_ontap.models.autosupport_connectivity_issue import AutosupportConnectivityIssue
from netapp_ontap.models.node_setup_ip import NodeSetupIp
from netapp_ontap.models.maxdata_on_san_metadata import MaxdataOnSanMetadata
from netapp_ontap.models.shelf_frus import ShelfFrus
from netapp_ontap.models.cluster_peer_setup_response_authentication import ClusterPeerSetupResponseAuthentication
from netapp_ontap.models.maxdata_on_san_application_components_storage_service import MaxdataOnSanApplicationComponentsStorageService
from netapp_ontap.models.oracle_on_nfs_redo_log_storage_service import OracleOnNfsRedoLogStorageService
from netapp_ontap.models.s3_user_post_patch import S3UserPostPatch
from netapp_ontap.models.application_rpo_components import ApplicationRpoComponents
from netapp_ontap.models.iscsi_credentials_chap_inbound import IscsiCredentialsChapInbound
from netapp_ontap.models.nfs_service_protocol_v40_features import NfsServiceProtocolV40Features
from netapp_ontap.models.iscsi_connection_interface_ip import IscsiConnectionInterfaceIp
from netapp_ontap.models.oracle_rac_on_nfs_oracle_crs_storage_service import OracleRacOnNfsOracleCrsStorageService
from netapp_ontap.models.volume_metrics_cloud import VolumeMetricsCloud
from netapp_ontap.models.fcp_service_target import FcpServiceTarget
from netapp_ontap.models.job_link import JobLink
from netapp_ontap.models.cluster_peer_encryption import ClusterPeerEncryption
from netapp_ontap.models.fc_interface_svm_location import FcInterfaceSvmLocation
from netapp_ontap.models.quota_report_qtree import QuotaReportQtree
from netapp_ontap.models.nvme_namespace_subsystem_map import NvmeNamespaceSubsystemMap
from netapp_ontap.models.plex_resync import PlexResync
from netapp_ontap.models.lun_space_guarantee import LunSpaceGuarantee
from netapp_ontap.models.svm_nfs import SvmNfs
from netapp_ontap.models.timezone_cluster import TimezoneCluster
from netapp_ontap.models.shelf_drawers import ShelfDrawers
from netapp_ontap.models.application_statistics_space1 import ApplicationStatisticsSpace1
from netapp_ontap.models.license_capacity import LicenseCapacity
from netapp_ontap.models.autosupport_message_error import AutosupportMessageError
from netapp_ontap.models.mongo_db_on_san_protection_type import MongoDbOnSanProtectionType
from netapp_ontap.models.application_statistics import ApplicationStatistics
from netapp_ontap.models.fc_login_initiator import FcLoginInitiator
from netapp_ontap.models.lun_map_igroup import LunMapIgroup
from netapp_ontap.models.volume_consistency_group import VolumeConsistencyGroup
from netapp_ontap.models.cloud_storage_tier import CloudStorageTier
from netapp_ontap.models.cluster_peer_links import ClusterPeerLinks
from netapp_ontap.models.quota_report_space_used import QuotaReportSpaceUsed
from netapp_ontap.models.zapp_nvme_rpo_local import ZappNvmeRpoLocal
from netapp_ontap.models.software_status_details_reference_node import SoftwareStatusDetailsReferenceNode
from netapp_ontap.models.ndmp_scsi import NdmpScsi
from netapp_ontap.models.disk_key_id import DiskKeyId
from netapp_ontap.models.nvme_subsystem_controller_interface import NvmeSubsystemControllerInterface
from netapp_ontap.models.software_status_details import SoftwareStatusDetails
from netapp_ontap.models.volume_encryption import VolumeEncryption
from netapp_ontap.models.application_san_access_iscsi_endpoint import ApplicationSanAccessIscsiEndpoint
from netapp_ontap.models.application_template1 import ApplicationTemplate1
from netapp_ontap.models.software_reference_metrocluster import SoftwareReferenceMetrocluster
from netapp_ontap.models.nas_application_components_tiering_object_stores import NasApplicationComponentsTieringObjectStores
from netapp_ontap.models.application_component_snapshot_component import ApplicationComponentSnapshotComponent
from netapp_ontap.models.schedule_cluster import ScheduleCluster
from netapp_ontap.models.schedule_cron import ScheduleCron
from netapp_ontap.models.svm_iscsi import SvmIscsi
from netapp_ontap.models.cluster_management_interface import ClusterManagementInterface
from netapp_ontap.models.performance_metric_raw_svm import PerformanceMetricRawSvm
from netapp_ontap.models.application_rpo_remote import ApplicationRpoRemote
from netapp_ontap.models.autosupport_connectivity_corrective_action import AutosupportConnectivityCorrectiveAction
from netapp_ontap.models.application_snapshot_components import ApplicationSnapshotComponents
from netapp_ontap.models.oracle_rac_on_san_db_sids import OracleRacOnSanDbSids
from netapp_ontap.models.application_protection_groups import ApplicationProtectionGroups
from netapp_ontap.models.application_cifs_properties_share import ApplicationCifsPropertiesShare
from netapp_ontap.models.application_cifs_properties_permissions import ApplicationCifsPropertiesPermissions
from netapp_ontap.models.snapmirror_destination_creation_storage_service import SnapmirrorDestinationCreationStorageService
from netapp_ontap.models.license_compliance import LicenseCompliance
from netapp_ontap.models.oracle_rac_on_nfs_grid_binary_storage_service import OracleRacOnNfsGridBinaryStorageService
from netapp_ontap.models.backup_node import BackupNode
from netapp_ontap.models.nvme_subsystem_subsystem_maps import NvmeSubsystemSubsystemMaps
from netapp_ontap.models.volume_snapmirror import VolumeSnapmirror
from netapp_ontap.models.key_server_readcreate import KeyServerReadcreate
from netapp_ontap.models.security_certificate_sign import SecurityCertificateSign
from netapp_ontap.models.snapshot_policy_schedule1 import SnapshotPolicySchedule1
from netapp_ontap.models.igroup_initiator_igroup import IgroupInitiatorIgroup
from netapp_ontap.models.quota_rule_space import QuotaRuleSpace
from netapp_ontap.models.vdi_on_nas import VdiOnNas
from netapp_ontap.models.volume_nas import VolumeNas
from netapp_ontap.models.volume_snaplock import VolumeSnaplock
from netapp_ontap.models.svm_snapmirror import SvmSnapmirror
from netapp_ontap.models.svm_fcp import SvmFcp
from netapp_ontap.models.quota_report_group import QuotaReportGroup
from netapp_ontap.models.zapp_nvme import ZappNvme
from netapp_ontap.models.software_update_details_reference_node import SoftwareUpdateDetailsReferenceNode
from netapp_ontap.models.quota_report_files import QuotaReportFiles
from netapp_ontap.models.security_key_manager_onboard import SecurityKeyManagerOnboard
from netapp_ontap.models.security_audit_log_svm import SecurityAuditLogSvm
from netapp_ontap.models.application_lun_mapping_object import ApplicationLunMappingObject
from netapp_ontap.models.broadcast_domain_reference_ipspace import BroadcastDomainReferenceIpspace
from netapp_ontap.models.oracle_on_nfs_db import OracleOnNfsDb
from netapp_ontap.models.nas import Nas
from netapp_ontap.models.application_component_svm import ApplicationComponentSvm
from netapp_ontap.models.vscan_on_access_scope import VscanOnAccessScope
from netapp_ontap.models.application_volume_object import ApplicationVolumeObject
from netapp_ontap.models.fpolicy_event_filters import FpolicyEventFilters
from netapp_ontap.models.snapmirror_transfer_relationship import SnapmirrorTransferRelationship
from netapp_ontap.models.maxdata_on_san_application_components import MaxdataOnSanApplicationComponents
from netapp_ontap.models.volume_space_snapshot import VolumeSpaceSnapshot
from netapp_ontap.models.lun_clone_source import LunCloneSource
from netapp_ontap.models.performance_metric_io_type_rwt import PerformanceMetricIoTypeRwt
from netapp_ontap.models.oracle_on_san_new_igroups import OracleOnSanNewIgroups
from netapp_ontap.models.volume_clone import VolumeClone
from netapp_ontap.models.sql_on_smb import SqlOnSmb
from netapp_ontap.models.aggregate_block_storage_mirror import AggregateBlockStorageMirror
from netapp_ontap.models.audit_schedule import AuditSchedule
from netapp_ontap.models.account_application import AccountApplication
from netapp_ontap.models.peer import Peer
from netapp_ontap.models.mongo_db_on_san_new_igroups import MongoDbOnSanNewIgroups
from netapp_ontap.models.key_server_no_records import KeyServerNoRecords
from netapp_ontap.models.qos_policy_adaptive import QosPolicyAdaptive
from netapp_ontap.models.snaplock_log_file import SnaplockLogFile
from netapp_ontap.models.nvme_namespace_clone import NvmeNamespaceClone
from netapp_ontap.models.nas_flexcache_origin_svm import NasFlexcacheOriginSvm
from netapp_ontap.models.aggregate_data_encryption import AggregateDataEncryption
from netapp_ontap.models.s3_service_delete_response_records import S3ServiceDeleteResponseRecords
from netapp_ontap.models.s3_bucket_encryption import S3BucketEncryption
from netapp_ontap.models.application_protection_groups_rpo_local import ApplicationProtectionGroupsRpoLocal
from netapp_ontap.models.snapmirror_error import SnapmirrorError
from netapp_ontap.models.node_controller_flash_cache import NodeControllerFlashCache
from netapp_ontap.models.application_rpo_local import ApplicationRpoLocal
from netapp_ontap.models.quota_rule_files import QuotaRuleFiles
from netapp_ontap.models.chassis_frus import ChassisFrus
from netapp_ontap.models.quota_rule_group import QuotaRuleGroup
from netapp_ontap.models.usm import Usm
from netapp_ontap.models.lun_map_lun import LunMapLun
from netapp_ontap.models.application_san_access_backing_storage import ApplicationSanAccessBackingStorage
from netapp_ontap.models.s3_service_user_post import S3ServiceUserPost
from netapp_ontap.models.lun_map_lun_node import LunMapLunNode
from netapp_ontap.models.lun_movement import LunMovement
from netapp_ontap.models.sql_on_smb_access import SqlOnSmbAccess
from netapp_ontap.models.qos_policy_fixed import QosPolicyFixed
from netapp_ontap.models.software_package_download_get import SoftwarePackageDownloadGet
from netapp_ontap.models.svm_nvme import SvmNvme
from netapp_ontap.models.application_nvme_access_backing_storage import ApplicationNvmeAccessBackingStorage
from netapp_ontap.models.performance_svm_nfs_metric import PerformanceSvmNfsMetric
from netapp_ontap.models.mongo_db_on_san_dataset_storage_service import MongoDbOnSanDatasetStorageService
from netapp_ontap.models.vsi_on_nas_datastore import VsiOnNasDatastore
from netapp_ontap.models.ip_interface_svm import IpInterfaceSvm
from netapp_ontap.models.aggregate_block_storage import AggregateBlockStorage
from netapp_ontap.models.license import License
from netapp_ontap.models.ems_destination_certificate import EmsDestinationCertificate
from netapp_ontap.models.application_snapshot_application import ApplicationSnapshotApplication
from netapp_ontap.models.shelf_bays import ShelfBays
from netapp_ontap.models.application_protection_groups_rpo_remote import ApplicationProtectionGroupsRpoRemote
from netapp_ontap.models.application_snapshot_restore import ApplicationSnapshotRestore
from netapp_ontap.models.application_statistics_components import ApplicationStatisticsComponents
from netapp_ontap.models.ndmp_data import NdmpData
from netapp_ontap.models.iscsi_credentials_chap_outbound import IscsiCredentialsChapOutbound
from netapp_ontap.models.ad_domain_svm import AdDomainSvm
from netapp_ontap.models.software_status_details_reference_action import SoftwareStatusDetailsReferenceAction
from netapp_ontap.models.broadcast_domain_svm import BroadcastDomainSvm
from netapp_ontap.models.application_component_application import ApplicationComponentApplication
from netapp_ontap.models.collection_links import CollectionLinks
from netapp_ontap.models.oracle_rac_on_nfs import OracleRacOnNfs
from netapp_ontap.models.svm_cifs_service import SvmCifsService
from netapp_ontap.models.lun_clone import LunClone
from netapp_ontap.models.iscsi_session_initiator import IscsiSessionInitiator
from netapp_ontap.models.zapp_nvme_components_tiering import ZappNvmeComponentsTiering
from netapp_ontap.models.nvme_namespace_clone_source import NvmeNamespaceCloneSource
from netapp_ontap.models.application_lun_object import ApplicationLunObject
from netapp_ontap.models.node_ha_giveback_failure import NodeHaGivebackFailure
from netapp_ontap.models.aggregate_space import AggregateSpace
from netapp_ontap.models.snapshot_policy_copies import SnapshotPolicyCopies
from netapp_ontap.models.nvme_namespace_status import NvmeNamespaceStatus
from netapp_ontap.models.san_application_components_tiering import SanApplicationComponentsTiering
from netapp_ontap.models.application_component_snapshot_svm import ApplicationComponentSnapshotSvm
from netapp_ontap.models.oracle_on_nfs import OracleOnNfs
from netapp_ontap.models.volume_space_logical_space import VolumeSpaceLogicalSpace
from netapp_ontap.models.application_rpo_rpo_remote import ApplicationRpoRpoRemote
from netapp_ontap.models.nvme_subsystem_controller_host import NvmeSubsystemControllerHost
from netapp_ontap.models.application_statistics_latency1 import ApplicationStatisticsLatency1
from netapp_ontap.models.application_rpo_rpo_local import ApplicationRpoRpoLocal
from netapp_ontap.models.maxdata_on_san_application_components_protection_type import MaxdataOnSanApplicationComponentsProtectionType
from netapp_ontap.models.disk_drawer import DiskDrawer
from netapp_ontap.models.iscsi_connection import IscsiConnection
from netapp_ontap.models.quota_rule_qtree import QuotaRuleQtree
from netapp_ontap.models.iscsi_credentials_initiator_address import IscsiCredentialsInitiatorAddress
from netapp_ontap.models.lun_space import LunSpace
from netapp_ontap.models.snapmirror_transfer_files import SnapmirrorTransferFiles
from netapp_ontap.models.application_rpo_rpo import ApplicationRpoRpo
from netapp_ontap.models.fc_interface_location import FcInterfaceLocation
from netapp_ontap.models.mongo_db_on_san import MongoDbOnSan
from netapp_ontap.models.nvme_namespace_location import NvmeNamespaceLocation
from netapp_ontap.models.software_node import SoftwareNode
from netapp_ontap.models.error_responses import ErrorResponses
from netapp_ontap.models.sql_on_san_new_igroups import SqlOnSanNewIgroups
from netapp_ontap.models.network_route_for_svm import NetworkRouteForSvm
from netapp_ontap.models.ems_event_parameter import EmsEventParameter
from netapp_ontap.models.quota_report_files_used import QuotaReportFilesUsed
from netapp_ontap.models.application_lun_mapping_object_igroup import ApplicationLunMappingObjectIgroup
from netapp_ontap.models.log_retention import LogRetention
from netapp_ontap.models.raid_group_recomputing_parity import RaidGroupRecomputingParity
from netapp_ontap.models.application_san_access_fcp_endpoint import ApplicationSanAccessFcpEndpoint
from netapp_ontap.models.aggregate_cloud_storage import AggregateCloudStorage
from netapp_ontap.models.ems_event_message import EmsEventMessage
from netapp_ontap.models.nas_protection_type import NasProtectionType
from netapp_ontap.models.flexcache_guarantee import FlexcacheGuarantee
from netapp_ontap.models.ip_interface_and_gateway import IpInterfaceAndGateway
from netapp_ontap.models.space_efficiency import SpaceEfficiency
from netapp_ontap.models.self_link import SelfLink
from netapp_ontap.models.ip_info import IpInfo
from netapp_ontap.models.ip_address_range import IpAddressRange
from netapp_ontap.models.igroup_lun import IgroupLun
from netapp_ontap.models.fpolicy_policy_scope import FpolicyPolicyScope
from netapp_ontap.models.performance_metric_svm import PerformanceMetricSvm
from netapp_ontap.models.application_component_storage_service import ApplicationComponentStorageService
from netapp_ontap.models.iscsi_credentials_chap import IscsiCredentialsChap
from netapp_ontap.models.nvme_subsystem_io_queue import NvmeSubsystemIoQueue
from netapp_ontap.models.node_ha import NodeHa
from netapp_ontap.models.fc_port_transceiver import FcPortTransceiver
from netapp_ontap.models.snapmirror_relationship_transfer import SnapmirrorRelationshipTransfer
from netapp_ontap.models.sql_on_san import SqlOnSan
from netapp_ontap.models.nvme_subsystem_controller_admin_queue import NvmeSubsystemControllerAdminQueue
from netapp_ontap.models.software_validation import SoftwareValidation
from netapp_ontap.models.lun_movement_progress_failure import LunMovementProgressFailure
from netapp_ontap.models.raid_group import RaidGroup
from netapp_ontap.models.onboard_key_manager_configurable_status import OnboardKeyManagerConfigurableStatus
from netapp_ontap.models.software_message_catalog import SoftwareMessageCatalog
from netapp_ontap.models.ems_filter_rule_message_criteria import EmsFilterRuleMessageCriteria
from netapp_ontap.models.fpolicy_event_file_operations import FpolicyEventFileOperations
from netapp_ontap.models.autosupport_issues import AutosupportIssues
from netapp_ontap.models.san_application_components import SanApplicationComponents
from netapp_ontap.models.software_update_details import SoftwareUpdateDetails
from netapp_ontap.models.application_protection_groups_rpo import ApplicationProtectionGroupsRpo
from netapp_ontap.models.cluster_peer_authentication import ClusterPeerAuthentication
from netapp_ontap.models.security_key_manager_external import SecurityKeyManagerExternal
from netapp_ontap.models.fc_interface_svm import FcInterfaceSvm
from netapp_ontap.models.bgp_peer_group_local_ip import BgpPeerGroupLocalIp
from netapp_ontap.models.performance_metric_io_type import PerformanceMetricIoType
from netapp_ontap.models.node_ha_takeover import NodeHaTakeover
from netapp_ontap.models.application_component_snapshot_restore_application import ApplicationComponentSnapshotRestoreApplication
from netapp_ontap.models.igroup_initiator_no_records import IgroupInitiatorNoRecords
from netapp_ontap.models.quota_report_users import QuotaReportUsers
from netapp_ontap.models.raid_group_reconstruct import RaidGroupReconstruct
from netapp_ontap.models.application_cifs_properties_backing_storage import ApplicationCifsPropertiesBackingStorage
from netapp_ontap.models.software_status_details_reference_issue import SoftwareStatusDetailsReferenceIssue
from netapp_ontap.models.application_snapshot_restore_application import ApplicationSnapshotRestoreApplication
from netapp_ontap.models.nvme_subsystem_namespace import NvmeSubsystemNamespace
from netapp_ontap.models.zapp_nvme_rpo import ZappNvmeRpo
from netapp_ontap.models.volume_quota import VolumeQuota
from netapp_ontap.models.application_subsystem_map_object_subsystem import ApplicationSubsystemMapObjectSubsystem
from netapp_ontap.models.vdi_on_san_new_igroups import VdiOnSanNewIgroups
from netapp_ontap.models.application_backing_storage import ApplicationBackingStorage
from netapp_ontap.models.ndmp_connect import NdmpConnect
from netapp_ontap.models.nvme_namespace_space import NvmeNamespaceSpace
from netapp_ontap.models.related_link import RelatedLink
from netapp_ontap.models.lun_movement_paths import LunMovementPaths
from netapp_ontap.models.lun_igroup import LunIgroup
from netapp_ontap.models.snaplock_log_volume import SnaplockLogVolume
from netapp_ontap.models.volume_snaplock_retention import VolumeSnaplockRetention
from netapp_ontap.models.fc_port_fabric import FcPortFabric
from netapp_ontap.models.nfs_service_transport import NfsServiceTransport
from netapp_ontap.models.kerberos_realm_ad_server import KerberosRealmAdServer
from netapp_ontap.models.software_upload import SoftwareUpload
from netapp_ontap.models.volume_statistics_reference_cloud import VolumeStatisticsReferenceCloud
from netapp_ontap.models.aggregate_block_storage_primary import AggregateBlockStoragePrimary
from netapp_ontap.models.flexcache_relationship import FlexcacheRelationship
from netapp_ontap.models.nas_flexcache import NasFlexcache
from netapp_ontap.models.lun_qos_policy import LunQosPolicy
from netapp_ontap.models.nvme_subsystem_map_namespace import NvmeSubsystemMapNamespace
from netapp_ontap.models.key_server_state_array import KeyServerStateArray
from netapp_ontap.models.vsi_on_san import VsiOnSan
from netapp_ontap.models.snapmirror_destination_creation_tiering import SnapmirrorDestinationCreationTiering
from netapp_ontap.models.application_cifs_properties import ApplicationCifsProperties
from netapp_ontap.models.layout_requirement import LayoutRequirement
from netapp_ontap.models.aggregate_block_storage_hybrid_cache import AggregateBlockStorageHybridCache
from netapp_ontap.models.rotation import Rotation
from netapp_ontap.models.sql_on_san_db_storage_service import SqlOnSanDbStorageService
from netapp_ontap.models.volume_autosize import VolumeAutosize
from netapp_ontap.models.application_nfs_properties_export_policy import ApplicationNfsPropertiesExportPolicy
from netapp_ontap.models.ndmp_mover import NdmpMover
from netapp_ontap.models.nas_application_components import NasApplicationComponents
from netapp_ontap.models.dr_node import DrNode
from netapp_ontap.models.cifs_service_delete import CifsServiceDelete
from netapp_ontap.models.application_namespace_object import ApplicationNamespaceObject
from netapp_ontap.models.shelf_remote import ShelfRemote
from netapp_ontap.models.volume_statistics import VolumeStatistics
from netapp_ontap.models.application_statistics_snapshot import ApplicationStatisticsSnapshot
from netapp_ontap.models.cluster_peer_status import ClusterPeerStatus
from netapp_ontap.models.performance_svm_nfs_metric_historical_v3 import PerformanceSvmNfsMetricHistoricalV3
from netapp_ontap.models.software_reference_metrocluster_progress_details import SoftwareReferenceMetroclusterProgressDetails
from netapp_ontap.models.volume_error_state import VolumeErrorState
from netapp_ontap.models.ip_interface_reference_ip import IpInterfaceReferenceIp
from netapp_ontap.models.iscsi_service_target import IscsiServiceTarget
from netapp_ontap.models.cluster_peer_local_network_interfaces import ClusterPeerLocalNetworkInterfaces
from netapp_ontap.models.aggregate_space_block_storage import AggregateSpaceBlockStorage
from netapp_ontap.models.cifs_netbios import CifsNetbios
from netapp_ontap.models.zapp_nvme_components_subsystem_hosts import ZappNvmeComponentsSubsystemHosts
from netapp_ontap.models.iscsi_connection_initiator_address import IscsiConnectionInitiatorAddress
from netapp_ontap.models.lun_location import LunLocation
from netapp_ontap.models.nas_flexcache_origin_component import NasFlexcacheOriginComponent
from netapp_ontap.models.cloud_target_cluster import CloudTargetCluster
from netapp_ontap.models.href import Href
from netapp_ontap.models.quota_report_space import QuotaReportSpace
from netapp_ontap.models.svm_dns import SvmDns
from netapp_ontap.models.software_errors import SoftwareErrors
from netapp_ontap.models.application_nfs_properties import ApplicationNfsProperties
from netapp_ontap.models.license_keys import LicenseKeys
from netapp_ontap.models.cluster_peer_remote import ClusterPeerRemote
from netapp_ontap.models.application_rpo import ApplicationRpo
from netapp_ontap.models.maxdata_on_san_application_components_metadata import MaxdataOnSanApplicationComponentsMetadata
from netapp_ontap.models.lun_movement_progress import LunMovementProgress
from netapp_ontap.models.performance_svm_nfs_statistics import PerformanceSvmNfsStatistics
from netapp_ontap.models.cluster_space_block_storage import ClusterSpaceBlockStorage
from netapp_ontap.models.application_component_snapshot_restore import ApplicationComponentSnapshotRestore
from netapp_ontap.models.ip_interface_svm_ip import IpInterfaceSvmIp
from netapp_ontap.models.aggregate_spare import AggregateSpare
from netapp_ontap.models.application_subsystem_map_object_subsystem_hosts import ApplicationSubsystemMapObjectSubsystemHosts
from netapp_ontap.models.fc_port_reference_node import FcPortReferenceNode
from netapp_ontap.models.node_controller_frus import NodeControllerFrus
from netapp_ontap.models.kerberos_realm_kdc import KerberosRealmKdc
from netapp_ontap.models.log import Log
from netapp_ontap.models.oracle_rac_on_nfs_grid_binary import OracleRacOnNfsGridBinary
from netapp_ontap.models.performance_svm_nfs_metric_historical import PerformanceSvmNfsMetricHistorical
from netapp_ontap.models.application_statistics_iops1 import ApplicationStatisticsIops1
from netapp_ontap.models.port_reference_node import PortReferenceNode
from netapp_ontap.models.mongo_db_on_san_secondary_igroups import MongoDbOnSanSecondaryIgroups
from netapp_ontap.models.application_san_access import ApplicationSanAccess
from netapp_ontap.models.cluster_peer_local_network import ClusterPeerLocalNetwork
from netapp_ontap.models.application_svm import ApplicationSvm
from netapp_ontap.models.vdi_on_nas_desktops import VdiOnNasDesktops
from netapp_ontap.models.performance_svm import PerformanceSvm
from netapp_ontap.models.bgp_peer_group_peer import BgpPeerGroupPeer
from netapp_ontap.models.cluster_peer_setup import ClusterPeerSetup
from netapp_ontap.models.vdi_on_nas_desktops_storage_service import VdiOnNasDesktopsStorageService
from netapp_ontap.models.volume_movement import VolumeMovement
from netapp_ontap.models.svm_nsswitch import SvmNsswitch
from netapp_ontap.models.node_controller import NodeController
from netapp_ontap.models.svm_s3_service import SvmS3Service
from netapp_ontap.models.nvme_subsystem_host_io_queue import NvmeSubsystemHostIoQueue
from netapp_ontap.models.cifs_target import CifsTarget
from netapp_ontap.models.volume_encryption_status import VolumeEncryptionStatus
from netapp_ontap.models.nvme_subsystem_controller_io_queue import NvmeSubsystemControllerIoQueue
from netapp_ontap.models.s3_service_post import S3ServicePost
from netapp_ontap.models.shelf_ports import ShelfPorts
from netapp_ontap.models.snapmirror_destination_creation import SnapmirrorDestinationCreation
from netapp_ontap.models.storage_port_error import StoragePortError
from netapp_ontap.models.application_statistics_storage_service import ApplicationStatisticsStorageService
from netapp_ontap.models.maxdata_on_san_new_igroups import MaxdataOnSanNewIgroups
from netapp_ontap.models.volume_efficiency_policy import VolumeEfficiencyPolicy
from netapp_ontap.models.mongo_db_on_san_dataset import MongoDbOnSanDataset
from netapp_ontap.models.bgp_peer_group_local import BgpPeerGroupLocal
from netapp_ontap.models.s3_service_delete import S3ServiceDelete
from netapp_ontap.models.zapp_nvme_performance import ZappNvmePerformance
from netapp_ontap.models.software_mcc import SoftwareMcc
from netapp_ontap.models.application_statistics_space import ApplicationStatisticsSpace
from netapp_ontap.models.oracle_on_san import OracleOnSan
from netapp_ontap.models.error_arguments import ErrorArguments
from netapp_ontap.models.oracle_on_nfs_archive_log import OracleOnNfsArchiveLog
from netapp_ontap.models.app_cifs_access import AppCifsAccess
from netapp_ontap.models.application_cifs_properties_server import ApplicationCifsPropertiesServer
from netapp_ontap.models.cloud_store_unavailable_reason import CloudStoreUnavailableReason
from netapp_ontap.models.cluster_space_cloud_storage import ClusterSpaceCloudStorage
from netapp_ontap.models.ip_interface_location import IpInterfaceLocation
from netapp_ontap.models.port_lag import PortLag
from netapp_ontap.models.oracle_on_nfs_ora_home_storage_service import OracleOnNfsOraHomeStorageService
from netapp_ontap.models.vdi_on_san import VdiOnSan
from netapp_ontap.models.app_nfs_access import AppNfsAccess
from netapp_ontap.models.application_subsystem_map_object import ApplicationSubsystemMapObject
from netapp_ontap.models.nas_application_components_tiering import NasApplicationComponentsTiering
from netapp_ontap.models.nas_flexcache_origin import NasFlexcacheOrigin
from netapp_ontap.models.oracle_on_nfs_archive_log_storage_service import OracleOnNfsArchiveLogStorageService
from netapp_ontap.models.oracle_on_nfs_redo_log import OracleOnNfsRedoLog
from netapp_ontap.models.application_component_snapshot_restore_component import ApplicationComponentSnapshotRestoreComponent
from netapp_ontap.models.sql_on_san_db import SqlOnSanDb
from netapp_ontap.models.sql_on_san_log_storage_service import SqlOnSanLogStorageService
from netapp_ontap.models.error import Error
from netapp_ontap.models.volume_application import VolumeApplication
from netapp_ontap.models.node_ha_ports import NodeHaPorts
from netapp_ontap.models.key_manager_state import KeyManagerState
from netapp_ontap.models.nvme_subsystem_io_queue_default import NvmeSubsystemIoQueueDefault
from netapp_ontap.models.volume_encryption_support import VolumeEncryptionSupport
from netapp_ontap.models.application_component_snapshot_application import ApplicationComponentSnapshotApplication
from netapp_ontap.models.layout_requirement_raid_group import LayoutRequirementRaidGroup
from netapp_ontap.models.vscan_on_demand_scope import VscanOnDemandScope
from netapp_ontap.models.sql_on_san_temp_db import SqlOnSanTempDb
from netapp_ontap.models.san import San
from netapp_ontap.models.shelf_cable import ShelfCable
from netapp_ontap.models.nvme_subsystem_host_no_records import NvmeSubsystemHostNoRecords
from netapp_ontap.models.san_new_igroups import SanNewIgroups
from netapp_ontap.models.nfs_service_protocol_v41_features import NfsServiceProtocolV41Features
from netapp_ontap.models.s3_service_post_response_records import S3ServicePostResponseRecords
from netapp_ontap.models.application_nvme_access import ApplicationNvmeAccess
from netapp_ontap.models.oracle_rac_on_san import OracleRacOnSan
from netapp_ontap.models.sql_on_san_temp_db_storage_service import SqlOnSanTempDbStorageService
from netapp_ontap.models.svm_ldap import SvmLdap
from netapp_ontap.models.aggregate_space_cloud_storage import AggregateSpaceCloudStorage
from netapp_ontap.models.audit_events import AuditEvents
from netapp_ontap.models.cifs_service_security import CifsServiceSecurity
from netapp_ontap.models.zapp_nvme_components_subsystem import ZappNvmeComponentsSubsystem
from netapp_ontap.models.zapp_nvme_components import ZappNvmeComponents
from netapp_ontap.models.igroup_lun_maps import IgroupLunMaps
from netapp_ontap.models.volume_files import VolumeFiles
from netapp_ontap.models.service_processor import ServiceProcessor

__all__ = [
    "VolumeTiering",
    "VsiOnSanNewIgroups",
    "PerformanceMetricRaw",
    "VolumeSpace",
    "VolumeQos",
    "NfsServiceProtocol",
    "VolumeGuarantee",
    "ClusterSpaceBlockStorageMedias",
    "NodeHaGiveback",
    "NodeVm",
    "SnapmirrorPolicyRule",
    "ApplicationStatisticsIops",
    "FcPortSpeed",
    "RaidGroupDisk",
    "VsiOnNas",
    "PortVlan",
    "SoftwareReferenceMetroclusterProgressSummary",
    "SecuritySamlSpCertificate",
    "SnapmirrorRelationshipPolicy",
    "NvmeSubsystemHosts",
    "VsiOnNasDatastoreStorageService",
    "AdDomain",
    "OracleRacOnNfsOracleCrs",
    "ApplicationStatisticsLatency",
    "ScopeIpspace",
    "VolumeEfficiency",
    "LunStatus",
    "Version",
    "KeyServerState",
    "NodeClusterInterface",
    "SvmNis",
    "NvmeInterfaceFcInterface",
    "NvmeSubsystemHostSubsystem",
    "OracleRacOnSanNewIgroups",
    "MaxdataOnSan",
    "NasStorageService",
    "NvmeNamespaceSpaceGuarantee",
    "NodeManagementInterface",
    "VdiOnNasHyperVAccess",
    "OracleOnNfsOraHome",
    "SnapmirrorEndpoint",
    "ApplicationLinks",
    "NodeHaTakeoverFailure",
    "ApplicationSubsystemMapObjectSubsystemLinks",
    "LunLunMaps",
    "SqlOnSanLog",
    "ApplicationNfsPropertiesPermissions",
    "IpInterfaceSvmLocation",
    "IscsiConnectionInterface",
    "AutosupportConnectivityIssue",
    "NodeSetupIp",
    "MaxdataOnSanMetadata",
    "ShelfFrus",
    "ClusterPeerSetupResponseAuthentication",
    "MaxdataOnSanApplicationComponentsStorageService",
    "OracleOnNfsRedoLogStorageService",
    "S3UserPostPatch",
    "ApplicationRpoComponents",
    "IscsiCredentialsChapInbound",
    "NfsServiceProtocolV40Features",
    "IscsiConnectionInterfaceIp",
    "OracleRacOnNfsOracleCrsStorageService",
    "VolumeMetricsCloud",
    "FcpServiceTarget",
    "JobLink",
    "ClusterPeerEncryption",
    "FcInterfaceSvmLocation",
    "QuotaReportQtree",
    "NvmeNamespaceSubsystemMap",
    "PlexResync",
    "LunSpaceGuarantee",
    "SvmNfs",
    "TimezoneCluster",
    "ShelfDrawers",
    "ApplicationStatisticsSpace1",
    "LicenseCapacity",
    "AutosupportMessageError",
    "MongoDbOnSanProtectionType",
    "ApplicationStatistics",
    "FcLoginInitiator",
    "LunMapIgroup",
    "VolumeConsistencyGroup",
    "CloudStorageTier",
    "ClusterPeerLinks",
    "QuotaReportSpaceUsed",
    "ZappNvmeRpoLocal",
    "SoftwareStatusDetailsReferenceNode",
    "NdmpScsi",
    "DiskKeyId",
    "NvmeSubsystemControllerInterface",
    "SoftwareStatusDetails",
    "VolumeEncryption",
    "ApplicationSanAccessIscsiEndpoint",
    "ApplicationTemplate1",
    "SoftwareReferenceMetrocluster",
    "NasApplicationComponentsTieringObjectStores",
    "ApplicationComponentSnapshotComponent",
    "ScheduleCluster",
    "ScheduleCron",
    "SvmIscsi",
    "ClusterManagementInterface",
    "PerformanceMetricRawSvm",
    "ApplicationRpoRemote",
    "AutosupportConnectivityCorrectiveAction",
    "ApplicationSnapshotComponents",
    "OracleRacOnSanDbSids",
    "ApplicationProtectionGroups",
    "ApplicationCifsPropertiesShare",
    "ApplicationCifsPropertiesPermissions",
    "SnapmirrorDestinationCreationStorageService",
    "LicenseCompliance",
    "OracleRacOnNfsGridBinaryStorageService",
    "BackupNode",
    "NvmeSubsystemSubsystemMaps",
    "VolumeSnapmirror",
    "KeyServerReadcreate",
    "SecurityCertificateSign",
    "SnapshotPolicySchedule1",
    "IgroupInitiatorIgroup",
    "QuotaRuleSpace",
    "VdiOnNas",
    "VolumeNas",
    "VolumeSnaplock",
    "SvmSnapmirror",
    "SvmFcp",
    "QuotaReportGroup",
    "ZappNvme",
    "SoftwareUpdateDetailsReferenceNode",
    "QuotaReportFiles",
    "SecurityKeyManagerOnboard",
    "SecurityAuditLogSvm",
    "ApplicationLunMappingObject",
    "BroadcastDomainReferenceIpspace",
    "OracleOnNfsDb",
    "Nas",
    "ApplicationComponentSvm",
    "VscanOnAccessScope",
    "ApplicationVolumeObject",
    "FpolicyEventFilters",
    "SnapmirrorTransferRelationship",
    "MaxdataOnSanApplicationComponents",
    "VolumeSpaceSnapshot",
    "LunCloneSource",
    "PerformanceMetricIoTypeRwt",
    "OracleOnSanNewIgroups",
    "VolumeClone",
    "SqlOnSmb",
    "AggregateBlockStorageMirror",
    "AuditSchedule",
    "AccountApplication",
    "Peer",
    "MongoDbOnSanNewIgroups",
    "KeyServerNoRecords",
    "QosPolicyAdaptive",
    "SnaplockLogFile",
    "NvmeNamespaceClone",
    "NasFlexcacheOriginSvm",
    "AggregateDataEncryption",
    "S3ServiceDeleteResponseRecords",
    "S3BucketEncryption",
    "ApplicationProtectionGroupsRpoLocal",
    "SnapmirrorError",
    "NodeControllerFlashCache",
    "ApplicationRpoLocal",
    "QuotaRuleFiles",
    "ChassisFrus",
    "QuotaRuleGroup",
    "Usm",
    "LunMapLun",
    "ApplicationSanAccessBackingStorage",
    "S3ServiceUserPost",
    "LunMapLunNode",
    "LunMovement",
    "SqlOnSmbAccess",
    "QosPolicyFixed",
    "SoftwarePackageDownloadGet",
    "SvmNvme",
    "ApplicationNvmeAccessBackingStorage",
    "PerformanceSvmNfsMetric",
    "MongoDbOnSanDatasetStorageService",
    "VsiOnNasDatastore",
    "IpInterfaceSvm",
    "AggregateBlockStorage",
    "License",
    "EmsDestinationCertificate",
    "ApplicationSnapshotApplication",
    "ShelfBays",
    "ApplicationProtectionGroupsRpoRemote",
    "ApplicationSnapshotRestore",
    "ApplicationStatisticsComponents",
    "NdmpData",
    "IscsiCredentialsChapOutbound",
    "AdDomainSvm",
    "SoftwareStatusDetailsReferenceAction",
    "BroadcastDomainSvm",
    "ApplicationComponentApplication",
    "CollectionLinks",
    "OracleRacOnNfs",
    "SvmCifsService",
    "LunClone",
    "IscsiSessionInitiator",
    "ZappNvmeComponentsTiering",
    "NvmeNamespaceCloneSource",
    "ApplicationLunObject",
    "NodeHaGivebackFailure",
    "AggregateSpace",
    "SnapshotPolicyCopies",
    "NvmeNamespaceStatus",
    "SanApplicationComponentsTiering",
    "ApplicationComponentSnapshotSvm",
    "OracleOnNfs",
    "VolumeSpaceLogicalSpace",
    "ApplicationRpoRpoRemote",
    "NvmeSubsystemControllerHost",
    "ApplicationStatisticsLatency1",
    "ApplicationRpoRpoLocal",
    "MaxdataOnSanApplicationComponentsProtectionType",
    "DiskDrawer",
    "IscsiConnection",
    "QuotaRuleQtree",
    "IscsiCredentialsInitiatorAddress",
    "LunSpace",
    "SnapmirrorTransferFiles",
    "ApplicationRpoRpo",
    "FcInterfaceLocation",
    "MongoDbOnSan",
    "NvmeNamespaceLocation",
    "SoftwareNode",
    "ErrorResponses",
    "SqlOnSanNewIgroups",
    "NetworkRouteForSvm",
    "EmsEventParameter",
    "QuotaReportFilesUsed",
    "ApplicationLunMappingObjectIgroup",
    "LogRetention",
    "RaidGroupRecomputingParity",
    "ApplicationSanAccessFcpEndpoint",
    "AggregateCloudStorage",
    "EmsEventMessage",
    "NasProtectionType",
    "FlexcacheGuarantee",
    "IpInterfaceAndGateway",
    "SpaceEfficiency",
    "SelfLink",
    "IpInfo",
    "IpAddressRange",
    "IgroupLun",
    "FpolicyPolicyScope",
    "PerformanceMetricSvm",
    "ApplicationComponentStorageService",
    "IscsiCredentialsChap",
    "NvmeSubsystemIoQueue",
    "NodeHa",
    "FcPortTransceiver",
    "SnapmirrorRelationshipTransfer",
    "SqlOnSan",
    "NvmeSubsystemControllerAdminQueue",
    "SoftwareValidation",
    "LunMovementProgressFailure",
    "RaidGroup",
    "OnboardKeyManagerConfigurableStatus",
    "SoftwareMessageCatalog",
    "EmsFilterRuleMessageCriteria",
    "FpolicyEventFileOperations",
    "AutosupportIssues",
    "SanApplicationComponents",
    "SoftwareUpdateDetails",
    "ApplicationProtectionGroupsRpo",
    "ClusterPeerAuthentication",
    "SecurityKeyManagerExternal",
    "FcInterfaceSvm",
    "BgpPeerGroupLocalIp",
    "PerformanceMetricIoType",
    "NodeHaTakeover",
    "ApplicationComponentSnapshotRestoreApplication",
    "IgroupInitiatorNoRecords",
    "QuotaReportUsers",
    "RaidGroupReconstruct",
    "ApplicationCifsPropertiesBackingStorage",
    "SoftwareStatusDetailsReferenceIssue",
    "ApplicationSnapshotRestoreApplication",
    "NvmeSubsystemNamespace",
    "ZappNvmeRpo",
    "VolumeQuota",
    "ApplicationSubsystemMapObjectSubsystem",
    "VdiOnSanNewIgroups",
    "ApplicationBackingStorage",
    "NdmpConnect",
    "NvmeNamespaceSpace",
    "RelatedLink",
    "LunMovementPaths",
    "LunIgroup",
    "SnaplockLogVolume",
    "VolumeSnaplockRetention",
    "FcPortFabric",
    "NfsServiceTransport",
    "KerberosRealmAdServer",
    "SoftwareUpload",
    "VolumeStatisticsReferenceCloud",
    "AggregateBlockStoragePrimary",
    "FlexcacheRelationship",
    "NasFlexcache",
    "LunQosPolicy",
    "NvmeSubsystemMapNamespace",
    "KeyServerStateArray",
    "VsiOnSan",
    "SnapmirrorDestinationCreationTiering",
    "ApplicationCifsProperties",
    "LayoutRequirement",
    "AggregateBlockStorageHybridCache",
    "Rotation",
    "SqlOnSanDbStorageService",
    "VolumeAutosize",
    "ApplicationNfsPropertiesExportPolicy",
    "NdmpMover",
    "NasApplicationComponents",
    "DrNode",
    "CifsServiceDelete",
    "ApplicationNamespaceObject",
    "ShelfRemote",
    "VolumeStatistics",
    "ApplicationStatisticsSnapshot",
    "ClusterPeerStatus",
    "PerformanceSvmNfsMetricHistoricalV3",
    "SoftwareReferenceMetroclusterProgressDetails",
    "VolumeErrorState",
    "IpInterfaceReferenceIp",
    "IscsiServiceTarget",
    "ClusterPeerLocalNetworkInterfaces",
    "AggregateSpaceBlockStorage",
    "CifsNetbios",
    "ZappNvmeComponentsSubsystemHosts",
    "IscsiConnectionInitiatorAddress",
    "LunLocation",
    "NasFlexcacheOriginComponent",
    "CloudTargetCluster",
    "Href",
    "QuotaReportSpace",
    "SvmDns",
    "SoftwareErrors",
    "ApplicationNfsProperties",
    "LicenseKeys",
    "ClusterPeerRemote",
    "ApplicationRpo",
    "MaxdataOnSanApplicationComponentsMetadata",
    "LunMovementProgress",
    "PerformanceSvmNfsStatistics",
    "ClusterSpaceBlockStorage",
    "ApplicationComponentSnapshotRestore",
    "IpInterfaceSvmIp",
    "AggregateSpare",
    "ApplicationSubsystemMapObjectSubsystemHosts",
    "FcPortReferenceNode",
    "NodeControllerFrus",
    "KerberosRealmKdc",
    "Log",
    "OracleRacOnNfsGridBinary",
    "PerformanceSvmNfsMetricHistorical",
    "ApplicationStatisticsIops1",
    "PortReferenceNode",
    "MongoDbOnSanSecondaryIgroups",
    "ApplicationSanAccess",
    "ClusterPeerLocalNetwork",
    "ApplicationSvm",
    "VdiOnNasDesktops",
    "PerformanceSvm",
    "BgpPeerGroupPeer",
    "ClusterPeerSetup",
    "VdiOnNasDesktopsStorageService",
    "VolumeMovement",
    "SvmNsswitch",
    "NodeController",
    "SvmS3Service",
    "NvmeSubsystemHostIoQueue",
    "CifsTarget",
    "VolumeEncryptionStatus",
    "NvmeSubsystemControllerIoQueue",
    "S3ServicePost",
    "ShelfPorts",
    "SnapmirrorDestinationCreation",
    "StoragePortError",
    "ApplicationStatisticsStorageService",
    "MaxdataOnSanNewIgroups",
    "VolumeEfficiencyPolicy",
    "MongoDbOnSanDataset",
    "BgpPeerGroupLocal",
    "S3ServiceDelete",
    "ZappNvmePerformance",
    "SoftwareMcc",
    "ApplicationStatisticsSpace",
    "OracleOnSan",
    "ErrorArguments",
    "OracleOnNfsArchiveLog",
    "AppCifsAccess",
    "ApplicationCifsPropertiesServer",
    "CloudStoreUnavailableReason",
    "ClusterSpaceCloudStorage",
    "IpInterfaceLocation",
    "PortLag",
    "OracleOnNfsOraHomeStorageService",
    "VdiOnSan",
    "AppNfsAccess",
    "ApplicationSubsystemMapObject",
    "NasApplicationComponentsTiering",
    "NasFlexcacheOrigin",
    "OracleOnNfsArchiveLogStorageService",
    "OracleOnNfsRedoLog",
    "ApplicationComponentSnapshotRestoreComponent",
    "SqlOnSanDb",
    "SqlOnSanLogStorageService",
    "Error",
    "VolumeApplication",
    "NodeHaPorts",
    "KeyManagerState",
    "NvmeSubsystemIoQueueDefault",
    "VolumeEncryptionSupport",
    "ApplicationComponentSnapshotApplication",
    "LayoutRequirementRaidGroup",
    "VscanOnDemandScope",
    "SqlOnSanTempDb",
    "San",
    "ShelfCable",
    "NvmeSubsystemHostNoRecords",
    "SanNewIgroups",
    "NfsServiceProtocolV41Features",
    "S3ServicePostResponseRecords",
    "ApplicationNvmeAccess",
    "OracleRacOnSan",
    "SqlOnSanTempDbStorageService",
    "SvmLdap",
    "AggregateSpaceCloudStorage",
    "AuditEvents",
    "CifsServiceSecurity",
    "ZappNvmeComponentsSubsystem",
    "ZappNvmeComponents",
    "IgroupLunMaps",
    "VolumeFiles",
    "ServiceProcessor",
]
