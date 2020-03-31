# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

##  Examples
### Retrieving the Kerberos realm details
```
# The API:
GET /api/protocols/nfs/kerberos/realms
# The call:
curl -X GET "https://<mgmt-ip>/api/protocols/nfs/kerberos/realms"
```
### Creating the Kerberos realm for an SVM
```
# The API:
POST /api/protocols/nfs/kerberos/realms
# The call:
curl -d "@test_post_kerb_realm.txt" -X POST "https://<mgmt-ip>/api/protocols/nfs/kerberos/realms"
test_post_kerb_realm.txt(body):
{
  "svm.uuid": "05c90dc2-7343-11e8-9eb4-0050568be2b7",
  "name": "NFS-NSR-W02.RTP.NETAPP.COM",
    "kdc": {
      "vendor": "microsoft",
      "ip": "10.225.185.112",
      "port": 88
    },
    "comment": "realm",
    "ad_server": {
      "name": "nfs-nsr-w02.rtp.netapp.com",
      "address": "10.225.185.112"
    }
}
```
### Updating the Kerberos realm for an SVM
```
# The API:
PATCH /api/protocols/nfs/kerberos/realms/{svm.uuid}/{name}
# The call:
curl -d "@test_patch_kerb_realm.txt" -X PATCH "https://<mgmt-ip>/api/protocols/nfs/kerberos/realms/05c90dc2-7343-11e8-9eb4-0050568be2b7/NFS-NSR-W02.RTP.NETAPP.COM"
test_patch_kerb_realm.txt(body):
{
  "kdc": {
    "vendor": "Microsoft",
    "ip": "100.225.185.112",
    "port": 88
  },
  "comment": "realm modify",
  "ad_server": {
    "name": "nfs.netapp.com",
    "address": "192.2.18.112"
  }
}
```
### Deleting the Kerberos realm for an SVM
```
# The API:
DELETE /api/protocols/nfs/kerberos/realms/{svm.uuid}/{name}
# The call:
curl -X DELETE "https://<mgmt-ip>/api/protocols/nfs/kerberos/realms/05c90dc2-7343-11e8-9eb4-0050568be2b7/NFS-NSR-W02.RTP.NETAPP.COM"
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


__all__ = ["KerberosRealm", "KerberosRealmSchema"]
__pdoc__ = {
    "KerberosRealmSchema.resource": False,
    "KerberosRealmSchema.patchable_fields": False,
    "KerberosRealmSchema.postable_fields": False,
}


class KerberosRealmSchema(ResourceSchema):
    """The fields of the KerberosRealm object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the kerberos_realm. """

    ad_server = fields.Nested("netapp_ontap.models.kerberos_realm_ad_server.KerberosRealmAdServerSchema", data_key="ad_server", unknown=EXCLUDE)
    r""" The ad_server field of the kerberos_realm. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" Comment """

    encryption_types = fields.List(fields.Str, data_key="encryption_types")
    r""" The encryption_types field of the kerberos_realm. """

    kdc = fields.Nested("netapp_ontap.models.kerberos_realm_kdc.KerberosRealmKdcSchema", data_key="kdc", unknown=EXCLUDE)
    r""" The kdc field of the kerberos_realm. """

    name = fields.Str(
        data_key="name",
    )
    r""" Kerberos realm """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the kerberos_realm. """

    @property
    def resource(self):
        return KerberosRealm

    @property
    def patchable_fields(self):
        return [
            "ad_server",
            "comment",
            "kdc",
            "name",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "ad_server",
            "comment",
            "kdc",
            "name",
            "svm.name",
            "svm.uuid",
        ]

class KerberosRealm(Resource):
    """Allows interaction with KerberosRealm objects on the host"""

    _schema = KerberosRealmSchema
    _path = "/api/protocols/nfs/kerberos/realms"
    @property
    def _keys(self):
        return ["svm.uuid", "name"]

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
        r"""Retrieves Kerberos realms.
### Related ONTAP commands
* `vserver nfs kerberos realm show`
### Learn more
* [`DOC /protocols/nfs/kerberos/realms`](#docs-NAS-protocols_nfs_kerberos_realms)
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
        r"""Updates the properties of a Kerberos realm.
* `vserver nfs kerberos realm modify`
### Learn more
* [`DOC /protocols/nfs/kerberos/realms`](#docs-NAS-protocols_nfs_kerberos_realms)
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
        r"""Deletes a Kerberos realm.
* `vserver nfs kerberos realm delete`
### Learn more
* [`DOC /protocols/nfs/kerberos/realms`](#docs-NAS-protocols_nfs_kerberos_realms)
"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves Kerberos realms.
### Related ONTAP commands
* `vserver nfs kerberos realm show`
### Learn more
* [`DOC /protocols/nfs/kerberos/realms`](#docs-NAS-protocols_nfs_kerberos_realms)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a Kerberos realm.
* `vserver nfs kerberos realm show`
### Learn more
* [`DOC /protocols/nfs/kerberos/realms`](#docs-NAS-protocols_nfs_kerberos_realms)
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
        r"""Creates a Kerberos realm.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM on which to create the Kerberos realm.
* `name` - Base name for the Kerberos realm.
* `kdc.vendor` - Vendor of the Key Distribution Center (KDC) server for this Kerberos realm. If the configuration uses a Microsoft Active Directory domain for authentication, this field nust be `microsoft`.
* `kdc.ip` - IP address of the KDC server for this Kerberos realm.
### Recommended optional properties
* `ad_server.name` - Host name of the Active Directory Domain Controller (DC). This is a mandatory parameter if the kdc-vendor is `microsoft`.
* `ad_server.address` - IP address of the Active Directory Domain Controller (DC). This is a mandatory parameter if the kdc-vendor is `microsoft`.
### Default property values
If not specified in POST, the following default property value is assigned:
* `kdc.port` - _88_
### Related ONTAP commands
* `vserver nfs kerberos realm create`
### Learn more
* [`DOC /protocols/nfs/kerberos/realms`](#docs-NAS-protocols_nfs_kerberos_realms)
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
        r"""Updates the properties of a Kerberos realm.
* `vserver nfs kerberos realm modify`
### Learn more
* [`DOC /protocols/nfs/kerberos/realms`](#docs-NAS-protocols_nfs_kerberos_realms)
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
        r"""Deletes a Kerberos realm.
* `vserver nfs kerberos realm delete`
### Learn more
* [`DOC /protocols/nfs/kerberos/realms`](#docs-NAS-protocols_nfs_kerberos_realms)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


