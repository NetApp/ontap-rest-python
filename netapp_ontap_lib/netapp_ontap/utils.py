# pylint: disable=line-too-long
"""
Copyright &copy; 2019 NetApp Inc. All rights reserved.

This module contains some of the common utility funcions used in the library.
"""

from functools import wraps
from http.client import responses
import inspect
import logging
import os
import time
from typing import Callable, Optional

import requests

from netapp_ontap import config
from netapp_ontap.error import NetAppRestError
from netapp_ontap.host_connection import HostConnection
from netapp_ontap.response import NetAppResponse


__all__ = ["poll"]

# prevent "No handlers" message if consumer application doesn't configure logging at all
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

DEBUG = os.getenv("DEBUG")
LOG_ALL_API_CALLS = os.getenv("LOG_ALL_API_CALLS")


def pretty_print_request_response(response) -> None:
    """Prints the complete request and response in a pretty way."""

    if response is None:
        return

    from netapp_ontap.resource import Resource  # pylint: disable=cyclic-import

    if isinstance(response, NetAppResponse):
        response = response.http_response
    if isinstance(response, Resource) and response._last_response:  # pylint: disable=protected-access
        response = response._last_response.http_response  # pylint: disable=protected-access
    request = response.request

    result = "\n-----------REQUEST-----------"
    result += "\n%s %s\n" % (request.method, request.url)
    result += "\n".join("%s: %s" % (k, v) for k, v in request.headers.items())
    result += "\n" + str(request.body)
    result += "\n-----------------------------"
    result += "\n"
    result += "\n-----------RESPONSE-----------"
    result += "\n%s %s\n" % (response.status_code, responses[response.status_code])
    result += "\n".join("%s: %s" % (k, v) for k, v in response.headers.items())
    result += "\n" + response.text
    result += "\n------------------------------"
    LOGGER.debug(result)


def api(func: Callable) -> Callable:
    """A decorator for wrapping the library API calls.

    Args:
        func: The API function to call

    Returns:
        The result of the call if successful. Otherwise, if the library is configured to not raise errors, returns error responses.

    Raises:
        `netapp_ontap.error.NetAppRestError`: Will raise any API failure
        ErrorResponses if the library is configured to raise errors.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            if not inspect.isgenerator(response) and LOG_ALL_API_CALLS:
                pretty_print_request_response(response)
            return response
        except requests.exceptions.HTTPError as error:
            return on_api_fail(error)

    return wrapper


def on_api_fail(error: requests.exceptions.HTTPError) -> Optional[NetAppResponse]:
    """Handles API failures according to the global library settings.

    Args:
        error: the error object corresponding to the request

    Returns:
        A `netapp_ontap.response.NetAppResponse` object if the library is configured to not raise errors.

    Raises:
        `netapp_ontap.error.NetAppRestError` if there is an API failure response
        and the library is configured to raise errors.
    """

    if DEBUG:
        pretty_print_request_response(error.response)
    if config.RAISE_API_ERRORS:
        raise NetAppRestError(cause=error) from None
    return NetAppResponse(error.response)


# pylint: disable=bad-continuation
# pylint: disable=too-many-branches
def poll(
    response: requests.Response,
    connection: HostConnection = None,
    timeout: int = None,
    interval: int = None
) -> NetAppResponse:
    """Poll for a job to complete on the host.

    This function accepts an HTTP 202 response from the server and follows the
    associated job link. As long as the state of the job is not terminal,
    it continues retrieving the job and logs a status message as it changes.

    Args:
        response: The initial API response which contains 202 and the job link.
        connection: An optional `netapp_ontap.host_connection.HostConnection`
            object. This is required if there is no globally usable connection set
            for the library.
        timeout: Seconds to wait before timing out of a poll request. If set,
            the value overrides the timeout set in the connection. Otherwise, the
            timeout set in the connection is used.
        interval: Seconds to wait between REST API calls when checking the job
            status. If set, the value overrides the interval in the connection
            object. Otherwise, the interval set in connection object is used.

    Returns:
        The API response.

    Raises:
        `netapp_ontap.error.NetAppRestError`: If there was no connection available
            when the request was made (either passed in or set for the library),
            or if the job times out.
    """

    if not connection:
        host_context = HostConnection.get_host_context()
        if config.CONNECTION:
            connection = config.CONNECTION
        elif host_context:
            connection = host_context
    if not connection:
        raise NetAppRestError(
            "No connection was passed or globally set. In either case, provide a "
            "connection object or set a global connection object for the library."
        )
    if not timeout:
        timeout = connection.poll_timeout
    if not interval:
        interval = connection.poll_interval
    if not timeout or timeout < 0:
        raise NetAppRestError(
            "Invalid timeout value. The timeout must be a positive integer."
        )
    if not interval or interval < 0:
        raise NetAppRestError(
            "Invalid interval value. The interval must be a positive integer."
        )

    try:
        job_link = response.json()["job"]["_links"]["self"]["href"]
    except KeyError:
        # It may have a job link if it is not a 202, but if it is a 202 and doesn't
        # have a job link, that seems certainly wrong
        if response.status_code == 202:
            raise NetAppRestError(
                "The API response does not have a valid job link"
            )
        return NetAppResponse(response)

    job_complete = False
    url = "%s%s" % (connection.origin, job_link)
    last_message = None
    timeout_left = timeout
    while not job_complete and timeout_left > 0:
        response = requests.get(url, auth=connection.basic_auth, verify=False)
        response_body = response.json()
        current_message = response_body.get("message")
        if current_message != last_message:
            last_message = current_message
            LOGGER.info(
                "Job (%s): %s. Timeout remaining: %s.",
                response_body["state"],
                current_message,
                timeout_left
            )
        job_complete = response_body["state"] in ["success", "failure"]
        if not job_complete:
            time.sleep(interval)
            timeout_left -= interval

    if not job_complete:
        raise NetAppRestError(
            "Job (%s): %s. Polling timed out after %s seconds." %
            (response_body["state"], response_body.get("message"), timeout)
        )

    if response_body["state"] != "success" and config.RAISE_API_ERRORS:
        raise NetAppRestError("Job failed: %s" % response_body["message"])

    return NetAppResponse(response)
