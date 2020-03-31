"""
Copyright &copy; 2019 NetApp Inc. All rights reserved.

This module contains the global configuration options and related functions for the library.
"""

from typing import Optional

from netapp_ontap.host_connection import HostConnection

CONNECTION = None  # type: Optional[HostConnection]
"""This `netapp_ontap.host_connection.HostConnection` object, if set, is used
as the default connection for all library operations if no other connection is set
at a more specific level. The hierarchy of lookups is:

- Any connection being used as a context manager (i.e. inside a with block)
- The connection set on a resource using `netapp_ontap.resource.Resource.set_connection`
- The global connection set here.

If none of these are set, an exception will be raised when a request is attempted.
"""

RAISE_API_ERRORS = True
"""If set to True, the library will raise an exception if a request fails. If set
to false, the library will not raise an exception and the application is responsible
to check if the response was an error or not.
"""


def set_error_model(raise_api_errors: bool = True) -> None:
    """Set the error model for the library.

    By default, operations (GET, POST, PATCH, DELETE) will raise an exception if
    the response code from the host is >= 400. The exception object will contain
    the response so that it can be handled in the client code.

    Optionally, settings raise_api_errors to False will return the response and
    the client will be responsible for checking and handling any errors.

    Args:
        raise_api_errors: If set to true, the library will raise errors back to the
            application. If set to faise, errors will not be raised and the
            application must verify the responses itself.
    """

    global RAISE_API_ERRORS  # pylint: disable=global-statement
    RAISE_API_ERRORS = raise_api_errors
