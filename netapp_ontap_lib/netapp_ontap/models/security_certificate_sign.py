# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema


__all__ = ["SecurityCertificateSign", "SecurityCertificateSignSchema"]
__pdoc__ = {
    "SecurityCertificateSignSchema.resource": False,
    "SecurityCertificateSign": False,
}


class SecurityCertificateSignSchema(ResourceSchema):
    """The fields of the SecurityCertificateSign object"""

    expiry_time = fields.Str(data_key="expiry_time")
    r""" Certificate expiration time. The allowed expiration time range is between 1 day to 10 years. """

    hash_function = fields.Str(data_key="hash_function")
    r""" Hashing function

Valid choices:

* sha256
* sha224
* sha384
* sha512 """

    signing_request = fields.Str(data_key="signing_request")
    r""" Certificate signing request to be signed by the given certificate authority. Request should be in X509 PEM format.

Example: '-----BEGIN CERTIFICATE REQUEST----- MIICYDCCAUgCAQAwGzEMMAoGA1UEAxMDQUJDMQswCQYDVQQGEwJVUzCCASIwDQYJ KoZIhvcNAQEBBQADggEPADCCAQoCggEBAPF+82SlqT3Vyu3Jx4IAwHcO5EGwLOxy zQ6KNjz71Fca0n1/A1CbCPyOsSupGVObvdWxX7xLVMJ2SXb7h43GCqYyX6FXJO4F HOpmLvB+jxdeiW7SDbiZyLUlsvA+oRO/uNlcug773QZdKLjJD64erZZMRUNbUJB8 bARxAUi0FPvgTraSQ0UW5sRLiGKeAyKA4wekYe1VgjHRTBizFbD4dI3njfva/2Bl jf+kkulgcLJTuJNtkgeimqMKyraYuleYcYk2K+C//0NuNOuPbDfTXCM7O61vik09 Szi8nLN7OXE9KoAA93U/BCpSfpl8XIb4cGnEr8hgVHOOtZSo+KZBFxMCAwEAAaAA MA0GCSqGSIb3DQEBCwUAA4IBAQC2vFYpvgsFrm5GnPx8tOBD1xsTyYjbWJMD8hAF lFrvF9Sw9QGCtDyacxkwgJhQx8l8JiIS5GOY6WWLBl9FMkLQNAhDL9xF3WF7vfYq RKgrz3bd/Vg96fsRZNYIPLGmoEaqLOh3FOCGc2VbdsR9PwOn3fwthxkIRd6ds6/q jc5cpSmVsCOgu+OKcpRXikYDbkWXfTZ1AhSfn6njBYFdZ9+PNAu/0JRQh5bX60nO 5heniTcAJLwUZP/CQ8nxHY0Wqy+1rAtM33d5cVmhUlBXQSIru/0ZkA/b9fK5Zv8E ZMADYUoEvIG59Vxhyci8lzYf+Mxl8qBSF+ZdC4yWhzDqZtM9 -----END CERTIFICATE REQUEST-----' """

    @property
    def resource(self):
        return SecurityCertificateSign

    @property
    def patchable_fields(self):
        return [
            "expiry_time",
            "hash_function",
            "signing_request",
        ]

    @property
    def postable_fields(self):
        return [
            "expiry_time",
            "hash_function",
            "signing_request",
        ]


class SecurityCertificateSign(Resource):  # pylint: disable=missing-docstring

    _schema = SecurityCertificateSignSchema
