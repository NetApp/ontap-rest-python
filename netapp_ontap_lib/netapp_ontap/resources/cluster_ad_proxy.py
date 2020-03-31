# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
This API configures data SVM account information at the Active Directory. For Active Directory domain-based authentication for cluster accounts, a data SVM must be configured and registered as a machine account at the Active Directory. All authentication requests are proxied through this SVM.
## Examples
### Creating a data SVM proxy for domain-based authentication for cluster accounts
```
# The API:
POST  "/api/security/authentication/cluster/ad-proxy"
# The call:
curl -X POST "https://<mgmt-ip>/api/security/authentication/cluster/ad-proxy" -d '{"svm.uuid":"13f87d78-70c7-11e9-b722-0050568ec89f"}'
```
### Updating a data SVM proxy for domain-based authentication for cluster accounts
```
# The API:
PATCH "/api/security/authentication/cluster/ad-proxy"
# The call:
curl -X PATCH "https://<mgmt-ip>/api/security/authentication/cluster/ad-proxy" -d '{"svm.uuid":"13f87d78-70c7-11e9-b722-0050568ec89f"}'
```
### Retrieving a data SVM proxy for domain-based authentication for cluster accounts
```
# The API:
GET "/api/security/authentication/cluster/ad-proxy"
# The call:
curl -X GET "https://<mgmt-ip>/api/security/authentication/cluster/ad-proxy"
# The response:
{
  "svm": {
    "uuid": "512eab7a-6bf9-11e9-a896-005056bb9ce1",
    "name": "vs2",
    "_links": {
      "self": {
        "href": "/api/svm/svms/512eab7a-6bf9-11e9-a896-005056bb9ce1"
      }
    }
  },
  "_links": {
    "self": {
      "href": "/api/security/authentication/cluster/ad-proxy"
    }
  }
}
```
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["ClusterAdProxy", "ClusterAdProxySchema"]
__pdoc__ = {
    "ClusterAdProxySchema.resource": False,
    "ClusterAdProxySchema.patchable_fields": False,
    "ClusterAdProxySchema.postable_fields": False,
}


class ClusterAdProxySchema(ResourceSchema):
    """The fields of the ClusterAdProxy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cluster_ad_proxy. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the cluster_ad_proxy. """

    @property
    def resource(self):
        return ClusterAdProxy

    @property
    def patchable_fields(self):
        return [
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "svm.name",
            "svm.uuid",
        ]

class ClusterAdProxy(Resource):
    r""" The SVM configured as proxy for Active Directory authentication of cluster accounts. """

    _schema = ClusterAdProxySchema
    _path = "/api/security/authentication/cluster/ad-proxy"





    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves SVM information configured as an Active Directory domain-tunnel.
### Learn more
* [`DOC /security/authentication/cluster/ad-proxy`](#docs-security-security_authentication_cluster_ad-proxy)"""
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
        r"""Configures a data SVM as a proxy for Active Directory-based authentication for cluster user accounts.
### Learn more
* [`DOC /security/authentication/cluster/ad-proxy`](#docs-security-security_authentication_cluster_ad-proxy)"""
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
        r"""Updates the data SVM configured as a tunnel for Active Directory-based authentication for cluster user accounts.
### Learn more
* [`DOC /security/authentication/cluster/ad-proxy`](#docs-security-security_authentication_cluster_ad-proxy)"""
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
        r"""Deletes the data SVM configured as a tunnel for Active Directory-based authentication for cluster user accounts.
### Learn more
* [`DOC /security/authentication/cluster/ad-proxy`](#docs-security-security_authentication_cluster_ad-proxy)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


