# pylint: disable=line-too-long
"""
Copyright &copy; 2019 NetApp Inc.
All rights reserved.

This module defines a host connection object which is used to communicate with
the API host.
"""

from typing import Optional, Tuple


_HOST_CONTEXT = None  # type: Optional[HostConnection]


class HostConnection:  # pylint: disable=too-many-instance-attributes
    """The HostConnection allows the client application to store their credentials
    and reuse them for each operation. There are three ways to use a connection
    object:

    * The first is to use the connection object as a context manager. Any operations
      on a resource that are called within the scope of the block will use that
      connection.
    * The second is to call set_connection() on a resource object. This
      will then be the connection used for all actions for that object only.
    * The third way is to call netapp_ontap.config.CONNECTION = connection. This
      connection instance will now be used for all actions on all resource
      objects (that do not otherwise set their own connection). This reduces
      the need to pass the connection around the application.

    Connections will be searched for in this order when executing an action.
    """

    # pylint: disable=bad-continuation,too-many-arguments
    def __init__(
        self,
        host,
        username: str = None,
        password: str = None,
        cert: str = None,
        key: str = None,
        verify: bool = True,
        poll_timeout: int = 30,
        poll_interval: int = 5,
        headers: dict = None,
    ):
        """Store information needed to contact the API host

        Either username and password must be provided or certificate and key must
        be provided.

        If verify is set to False, urllib3's InsecureRequestWarnings will also be
        silenced in the logs.

        Args:
            host: The API host that the library should talk to
            username: The user identifier known to the host
            password: The secret for the user
            cert: The file path to the users public certificate. The common
                name in the certificate must match the account name.
            key: A private key in PEM format
            verify: If an SSL connection is made to the host, this parameter
                controls how the validity of the trust chain of the certificate
                is handled. See the documentation for the requests library for more information:
                https://2.python-requests.org/en/master/user/advanced/#ssl-cert-verification
            poll_timeout: Time in seconds to poll on a job. This setting applies to all polling
                that uses this connection unless overridden as a parameter to poll(). Defaults
                to 30 seconds.
            poll_interval: Time in seconds to wait between polls on a job. This setting applies
                to all polling that uses this connection unless overridden as a parameter to
                poll(). Defaults to 5 seconds.
            headers: Any custom headers to be passed to each request using this connection object.

        """

        argument_error = False
        if not username:
            argument_error = not cert or not key
        elif not cert:
            argument_error = not username or not password
        else:
            argument_error = username is not None and cert is not None

        if argument_error:
            from netapp_ontap.error import NetAppRestError  # pylint: disable=cyclic-import

            raise NetAppRestError(
                "Either username and password must be provided or a cert and a"
                " key must be provided. You may not provide both."
            )

        self.scheme = "https"
        self.host = host
        self.port = 443
        self.username = username
        self.password = password
        self.cert = cert
        self.key = key
        self.verify = verify
        self.poll_timeout = poll_timeout
        self.poll_interval = poll_interval
        self.headers = headers
        self._old_context = None  # type: Optional[HostConnection]

        if not self.verify:
            import urllib3  # type: ignore
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @staticmethod
    def get_host_context() -> "Optional[HostConnection]":
        """Get the current host context, if any.

        Returns:
            A HostConnection object or None if not in a host connection context.
        """

        return _HOST_CONTEXT

    @property
    def basic_auth(self) -> Optional[Tuple[str, str]]:
        """Pulls the credentials out of the connection object.

        Returns:
            A tuple of username and password sufficient for passing to the requests library. Returns None if this connection is not configured for basic auth with a username and password.
        """

        if self.username and self.password:
            return (self.username, self.password)
        return None

    @property
    def cert_auth(self) -> Optional[Tuple[str, str]]:
        """Pulls the certificate details out of the connection object.

        Returns:
            A tuple of cert and key sufficient for passing to the requests library. Returns None if this connection is not configured for cert auth with a cert and key.
        """

        if self.cert and self.key:
            return (self.cert, self.key)
        return None

    @property
    def origin(self) -> str:
        """The beginning of any REST endpoint.

        Returns:
            The origin part of the URL. For example, `http://1.2.3.4:8080`.
        """

        return "%s://%s:%s" % (self.scheme, self.host, self.port)

    @property
    def request_headers(self) -> Optional[dict]:
        """Retrieves the headers set out of the connection object

        Returns:
            A dictionary consisting of header names and values for passing to the requests library. Returns None if no headers are configured.
        """

        if self.headers:
            return self.headers
        return None

    @request_headers.setter
    def request_headers(self, headers):
        """Set the request headers for the connection object"""
        if isinstance(headers, dict):
            self.headers = headers
        else:
            raise TypeError("Request headers must be specified as a 'dict' type")

    def __enter__(self):
        global _HOST_CONTEXT  # pylint: disable=global-statement
        self._old_context = _HOST_CONTEXT
        _HOST_CONTEXT = self
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        global _HOST_CONTEXT  # pylint: disable=global-statement
        _HOST_CONTEXT = self._old_context
