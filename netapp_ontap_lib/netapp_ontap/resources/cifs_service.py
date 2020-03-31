# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
A CIFS server is necessary to provide SMB clients with access to the Storage Virtual Machine (SVM). Before you begin, the following prerequisites must be in place:</br>

 * At least one SVM LIF must exist on the SVM.
 * The LIFs must be able to connect to the DNS servers configured on the SVM and to an Active Directory domain controller of the domain to which you want to join the CIFS server.
 * The DNS servers must contain the service location records that are needed to locate the Active Directory domain services.
 * The cluster time must be synchronized to within five minutes of the Active Directory domain controller.
## Performance monitoring
Performance of the SVM can be monitored by the `metric.*` and `statistics.*` properties. These show the performance of the SVM in terms of IOPS, latency and throughput. The `metric.*` properties denote an average whereas `statistics.*` properties denote a real-time monotonically increasing value aggregated across all nodes.
### Information on the CIFS server
 You must keep the following in mind when creating the CIFS server:

 * The CIFS server name might or might not be the same as the SVM name.
 * The CIFS server name can be up to 15 characters in length.
 * The following characters are not allowed: @ # * ( ) = + [ ] | ; : " , < > \ / ?
 * You must use the FQDN when specifying the domain.
 * The default is to add the CIFS server machine account to the Active Directory "CN=Computer" object.
 * You can choose to add the CIFS server to a different organizational unit (OU) by specifying the "organizational_unit" parameter. When specifying the OU, do not specify the domain portion of the distinguished name; only specify the OU or CN portion of the distinguished name. ONTAP appends the value provided for the required "-domain" parameter onto the value provided for the "-ou" parameter to create the Active Directory distinguished name, which is used when joining the Active Directory domain.
 * You can optionally choose to add a text comment of up to 48 characters about the CIFS server. If there is a space in the comment text, you must enclose the entire string in quotation marks.
 * You can optionally choose to add a comma-delimited list of one or more NetBIOS aliases for the CIFS server.
 * The initial administrative status of the CIFS server is "up".
 * The <i> large-mtu</i> and <i>multichannel</i> features are enabled for the new CIFS server.
 * If LDAP is configured with the <i>use_start_tls</i> and <i>session_security</i> features, the new CIFS server will also have this property set.
## Examples
### Creating a CIFS server
To create a CIFS server, use the following API. Note the <i>return_records=true</i> query parameter used to obtain the newly created entry in the response.
<br/>
---
```
# The API:
POST /api/protocols/cifs/services
# The call:
curl -X POST "https://<mgmt-ip>/api/protocols/cifs/services?return_records=true" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"ad_domain\": { \"fqdn\": \"CIFS-2008R2-AD.GDL.ENGLAB.NETAPP.COM\", \"organizational_unit\": \"CN=Computers\", \"password\": \"cifs*123\", \"user\": \"administrator\" }, \"comment\": \"This CIFS Server Belongs to CS Department\", \"default_unix_user\": \"string\", \"enabled\": true, \"name\": \"CIFS-DOC\", \"netbios\": { \"aliases\": [ \"ALIAS_1\", \"ALIAS_2\", \"ALIAS_3\" ], \"enabled\": false, \"wins_servers\": [ \"10.224.65.20\", \"10.224.65.21\" ] }, \"security\": { \"kdc_encryption\": false, \"restrict_anonymous\": \"no_enumeration\", \"smb_encryption\": false, \"smb_signing\": false }, \"svm\": { \"name\": \"vs1\", \"uuid\": \"ef087155-f9e2-11e8-ac52-0050568ea248\" }}"
# The response:
{
  "num_records": 1,
  "records": [
    {
      "svm": {
        "uuid": "9f5ab4cb-f703-11e8-91cc-0050568eca13",
        "name": "vs1"
      },
      "name": "CIFS-DOC",
      "ad_domain": {
        "fqdn": "CIFS-2008R2-AD.GDL.ENGLAB.NETAPP.COM",
        "user": "administrator",
        "password": "cifs*123",
        "organizational_unit": "CN=Computers"
      },
      "enabled": true,
      "comment": "This CIFS Server Belongs to CS Department",
      "security": {
        "restrict_anonymous": "no_enumeration",
        "smb_signing": false,
        "smb_encryption": false,
        "kdc_encryption": false
      },
      "netbios": {
        "aliases": [
          "ALIAS_1",
          "ALIAS_2",
          "ALIAS_3"
        ],
        "wins_servers": [
          "10.224.65.20",
          "10.224.65.21"
        ],
        "enabled": false
      },
      "default_unix_user": "string"
    }
  ],
  "job": {
    "uuid": "f232b6da-00a4-11e9-a8c1-0050568eca13",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/f232b6da-00a4-11e9-a8c1-0050568eca13"
      }
    }
  }
}
```
---
### Retrieving the full CIFS server configuration for all SVMs in the cluster
---
```
# The API:
GET /api/protocols/cifs/services
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/services?fields=*&return_records=true&return_timeout=15" -H "accept: application/json"
# The response:
{
  "records": [
    {
      "svm": {
        "uuid": "9f5ab4cb-f703-11e8-91cc-0050568eca13",
        "name": "vs1"
      },
      "name": "CIFS-DOC",
      "ad_domain": {
        "fqdn": "CIFS-2008R2-AD.GDL.ENGLAB.NETAPP.COM",
        "organizational_unit": "CN=Computers"
      },
      "enabled": true,
      "comment": "This CIFS Server Belongs to CS Department",
      "security": {
        "restrict_anonymous": "no_enumeration",
        "smb_signing": false,
        "smb_encryption": false,
        "kdc_encryption": false
      },
      "netbios": {
        "aliases": [
          "ALIAS_1",
          "ALIAS_2",
          "ALIAS_3"
        ],
        "wins_servers": [
          "10.224.65.20",
          "10.224.65.21"
        ],
        "enabled": false
      },
      "default_unix_user": "string"
    }
  ],
  "num_records": 1
}
```
---
### Retrieving CIFS server configuration details for a specific SVM
---
```
# The API:
GET /api/protocols/cifs/services/{svm.uuid}
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/cifs/services/9f5ab4cb-f703-11e8-91cc-0050568eca13" -H "accept: application/json"
# The response:
{
  "svm": {
    "uuid": "9f5ab4cb-f703-11e8-91cc-0050568eca13",
    "name": "vs1"
  },
  "name": "CIFS-DOC",
  "ad_domain": {
    "fqdn": "CIFS-2008R2-AD.GDL.ENGLAB.NETAPP.COM",
    "organizational_unit": "CN=Computers"
  },
  "enabled": true,
  "comment": "This CIFS Server Belongs to CS Department",
  "security": {
    "restrict_anonymous": "no_enumeration",
    "smb_signing": false,
    "smb_encryption": false,
    "kdc_encryption": false
  },
  "netbios": {
    "aliases": [
      "ALIAS_1",
      "ALIAS_2",
      "ALIAS_3"
    ],
    "wins_servers": [
      "10.224.65.20",
      "10.224.65.21"
    ],
    "enabled": false
  },
  "default_unix_user": "string"
}
```
---
### Updating CIFS server properties for the specified SVM
---
```
# The API:
PATCH /api/protocols/cifs/services/{svm.uuid}
# The call:
curl -X PATCH "https://<mgmt-ip>/api/protocols/cifs/services/9f5ab4cb-f703-11e8-91cc-0050568eca13" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"comment\": \"CIFS SERVER MODIFICATION\" }"
```
---
### Removing a CIFS server for a specific SVM
To delete a CIFS server, use the following API. This will delete the CIFS server along with other CIFS configurations such as CIFS share, share ACLs, homedir search-path, and so on.
<br/>
---
```
# The API:
DELETE /api/protocols/cifs/services/{svm.uuid}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/cifs/services/9f5ab4cb-f703-11e8-91cc-0050568eca13" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"ad_domain\": { \"password\": \"cifs*123\", \"user\": \"administrator\" } }"
```
---
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["CifsService", "CifsServiceSchema"]
__pdoc__ = {
    "CifsServiceSchema.resource": False,
    "CifsServiceSchema.patchable_fields": False,
    "CifsServiceSchema.postable_fields": False,
}


class CifsServiceSchema(ResourceSchema):
    """The fields of the CifsService object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cifs_service. """

    ad_domain = fields.Nested("netapp_ontap.models.ad_domain.AdDomainSchema", data_key="ad_domain", unknown=EXCLUDE)
    r""" The ad_domain field of the cifs_service. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=48),
    )
    r""" A descriptive text comment for the CIFS server. SMB clients can see the CIFS server comment when browsing servers on the network. If there is a space in the comment, you must enclose the entire string in quotation marks.

Example: This CIFS Server Belongs to CS Department """

    default_unix_user = fields.Str(
        data_key="default_unix_user",
    )
    r""" Specifies the UNIX user to which any authenticated CIFS user is mapped to, if the normal user mapping rules fails. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies if the CIFS service is administratively enabled. """

    metric = fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the cifs_service. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=15),
    )
    r""" The name of the CIFS server.

Example: CIFS1 """

    netbios = fields.Nested("netapp_ontap.models.cifs_netbios.CifsNetbiosSchema", data_key="netbios", unknown=EXCLUDE)
    r""" The netbios field of the cifs_service. """

    security = fields.Nested("netapp_ontap.models.cifs_service_security.CifsServiceSecuritySchema", data_key="security", unknown=EXCLUDE)
    r""" The security field of the cifs_service. """

    statistics = fields.Nested("netapp_ontap.models.performance_metric_raw_svm.PerformanceMetricRawSvmSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the cifs_service. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the cifs_service. """

    @property
    def resource(self):
        return CifsService

    @property
    def patchable_fields(self):
        return [
            "ad_domain",
            "comment",
            "default_unix_user",
            "enabled",
            "metric.iops",
            "metric.latency",
            "metric.throughput",
            "name",
            "netbios",
            "security",
            "statistics.iops_raw",
            "statistics.latency_raw",
            "statistics.throughput_raw",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "ad_domain",
            "comment",
            "default_unix_user",
            "enabled",
            "metric.iops",
            "metric.latency",
            "metric.throughput",
            "name",
            "netbios",
            "security",
            "statistics.iops_raw",
            "statistics.latency_raw",
            "statistics.throughput_raw",
            "svm.name",
            "svm.uuid",
        ]

class CifsService(Resource):
    """Allows interaction with CifsService objects on the host"""

    _schema = CifsServiceSchema
    _path = "/api/protocols/cifs/services"
    @property
    def _keys(self):
        return ["svm.uuid"]

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves CIFS servers.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `statistics.*`
* `metric.*`
### Related ONTAP commands
* `vserver cifs server show`
* `vserver cifs server options show`
* `vserver cifs server security show`
### Learn more
* [`DOC /protocols/cifs/services`](#docs-NAS-protocols_cifs_services)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates both the mandatory and optional parameters of the CIFS configuration. Ensure the CIFS server is administratively disabled when renaming the CIFS server or modifying the <i>ad_domain</i> properties.
### Related ONTAP commands
* `vserver cifs server modify`
* `vserver cifs server options modify`
* `vserver cifs security modify`
* `vserver cifs server add-netbios-aliases`
* `vserver cifs server remove-netbios-aliases`
### Learn more
* [`DOC /protocols/cifs/services`](#docs-NAS-protocols_cifs_services)
"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def delete_collection(
        cls,
        *args,
        body: Union[Resource, dict] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a CIFS server and related CIFS configurations.
### Related ONTAP commands
* `vserver cifs server delete`
* `vserver cifs remove-netbios-aliases`
### Learn more
* [`DOC /protocols/cifs/services`](#docs-NAS-protocols_cifs_services)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves CIFS servers.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`DOC Requesting specific fields`](#docs-docs-Requesting-specific-fields) to learn more.
* `statistics.*`
* `metric.*`
### Related ONTAP commands
* `vserver cifs server show`
* `vserver cifs server options show`
* `vserver cifs server security show`
### Learn more
* [`DOC /protocols/cifs/services`](#docs-NAS-protocols_cifs_services)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a CIFS server.
### Related ONTAP commands
* `vserver cifs server show`
* `vserver cifs server options show`
* `vserver cifs server security show`
### Learn more
* [`DOC /protocols/cifs/services`](#docs-NAS-protocols_cifs_services)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a CIFS server. Each SVM can have one CIFS server.</br>
### Important notes
- The CIFS server name might or might not be the same as the SVM name.
- The CIFS server name can contain up to 15 characters.
- The CIFS server name does not support the following characters: @ # * ( ) = + [ ] | ; : " , < >  / ?
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the CIFS server.
* `name` -  Name of the CIFS server.
* `ad_domain.fqdn` - Fully qualified domain name of the Windows Active Directory to which this CIFS server belongs.
* `ad_domain.user` - User account with the access to add the CIFS server to the Active Directory.
* `ad_domain.password` - Account password used to add this CIFS server to the Active Directory.
### Recommended optional properties
* `comment` - Add a text comment of up to 48 characters about the CIFS server.
* `netbios.aliases` - Add a comma-delimited list of one or more NetBIOS aliases for the CIFS server.
* `netbios.wins_servers` - Add a list of Windows Internet Name Server (WINS) addresses that manage and map the NetBIOS name of the CIFS server to their network IP addresses. The IP addresses must be IPv4 addresses.
### Default property values
If not specified in POST, the following default property values are assigned:
* `ad_domain.organizational_unit` - _CN=Computers_
* `enabled` - _true_
* `restrict_anonymous` - _no_enumeration_
* `smb_signing` - _false_
* `smb_encryption` - _false_
* `kdc_encryption` - _false_
* `default_unix_user` - _pcuser_
* `netbios_enabled` - _false_ However, if either "netbios.wins-server" or "netbios.aliases" is set during POST and if `netbios_enabled` is not specified then `netbios_enabled` is set to true.
### Related ONTAP commands
* `vserver cifs server create`
* `vserver cifs server options modify`
* `vserver cifs security modify`
* `vserver cifs server add-netbios-aliases`
### Learn more
* [`DOC /protocols/cifs/services`](#docs-NAS-protocols_cifs_services)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates both the mandatory and optional parameters of the CIFS configuration. Ensure the CIFS server is administratively disabled when renaming the CIFS server or modifying the <i>ad_domain</i> properties.
### Related ONTAP commands
* `vserver cifs server modify`
* `vserver cifs server options modify`
* `vserver cifs security modify`
* `vserver cifs server add-netbios-aliases`
* `vserver cifs server remove-netbios-aliases`
### Learn more
* [`DOC /protocols/cifs/services`](#docs-NAS-protocols_cifs_services)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a CIFS server and related CIFS configurations.
### Related ONTAP commands
* `vserver cifs server delete`
* `vserver cifs remove-netbios-aliases`
### Learn more
* [`DOC /protocols/cifs/services`](#docs-NAS-protocols_cifs_services)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


