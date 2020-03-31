# pylint: disable=line-too-long
"""
Copyright &copy; 2019 NetApp Inc. All rights reserved.

This module defines the custom exception type. All exceptions raised by
the library descend from this type.
"""

from typing import Optional  # pylint: disable=unused-import

import requests

if False:  # pylint: disable=using-constant-test
    # This is for mypy's benefit. Otherwise, it can't find the name when
    # examining the return type of http_err_response. But If we import it in
    # the module scope, we have a cyclic import problem.
    from netapp_ontap.response import NetAppResponse  # pylint: disable=unused-import


class NetAppRestError(Exception):
    """Common base class for all exceptions raised by the library functions. All
    custom exceptions are derived from this type.
    """

    def __init__(self, message: str = None, cause: Exception = None) -> None:
        """Initalize the error object.

        Optionally accepts a custom message and cause. If provided, the cause is
        the exception object that was handled when this exception is created.

        Args:
            message: A human readable message that explains the error.
            cause: An exception object that caused this exception to be raised.
        """

        from netapp_ontap.response import NetAppResponse  # pylint: disable=redefined-outer-name

        msg = message if message else ""
        if cause:
            self.cause = cause
            msg += " Caused by %r" % cause
            if isinstance(cause, requests.exceptions.HTTPError):
                self._response = NetAppResponse(cause.response)
                try:
                    err_msg = cause.response.json().get("error", {}).get("message")
                    if err_msg:
                        msg += ": %s" % err_msg
                except Exception:  # pylint: disable=broad-except
                    # the error response wasn't json so there's nothing additional
                    # we will add
                    pass

        super().__init__(msg)

    @property
    def http_err_response(self) -> "Optional[NetAppResponse]":
        """Describes a response to an API request that contains an error.

        Returns:
            Response object if the exception was raised because of an API failure (HTTP status code of 400 or higher). None if the exception was not related to an API error.
        """

        return getattr(self, "_response", None)
