# pylint: disable=line-too-long
"""
Copyright &copy; 2019 NetApp Inc. All rights reserved.

This module defines a unified response object for all resource actions.
"""

import requests

from netapp_ontap.host_connection import HostConnection


class NetAppResponse:
    """Contains the HTTP response received by a client from a server
    for a specific action. The object allows all responses to be examined
    in a consistent way. For example, is this an error or is an ongoing job?
    """

    def __init__(self, http_response: requests.Response) -> None:
        """Create and initialize a NetAppResponse object based on the result of an API call.

        Args:
            http_response: The API response to wrap
        """

        self.http_response = http_response

    @property
    def is_job(self) -> bool:
        """Examine to determine if the response is a job.

        Returns:
            True if the HTTP status code returned was 202, else it will return False.
        """

        try:
            job_link = self.http_response.json()["job"]["_links"]["self"]["href"]
            return job_link
        except:  # pylint: disable=bare-except
            return False

    @property
    def is_err(self) -> bool:
        """Examine to determine if the response is an error.

        Returns:
            True if the HTTP status code was 400 or greater, else it will return False.
        """

        return self.http_response.status_code > 399

    def poll(
            self, connection: HostConnection = None, timeout: int = None, interval: int = None
    ) -> "NetAppResponse":
        """Wait for the job associated with the response to complete.

        Calls 'utils.poll' with the response object and blocks until the job
        completes (that is reaches a terminal state).

        Args:
            connection: The host containing the job to connect to.
            timeout: Seconds to wait before timing out of a poll request. If set,
                the value overrides the timeout set in connection. Otherwise, the
                timeout set in the connection is used.
            interval: Seconds to wait between making REST API calls to check the
                the job status. If set, the value overrides the interval set in the
                connection object. Otherwise, the interval set in connection object
                is used.

        Returns:
            The response received after the job completes. This is normally a success or failure indication for the job.
        """

        from netapp_ontap import utils  # pylint: disable=cyclic-import

        return utils.poll(
            self.http_response,
            connection=connection,
            timeout=timeout,
            interval=interval
        )
