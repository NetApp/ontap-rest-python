"""

Copyright &copy; 2019 NetApp Inc.
All rights reserved.

This module is the implementation of the CLI resource. This resource is used as
an advanced way to send commands to the host system. These commands may or may
not have equivalent method of operation in the other resource sets.

"""

import logging
from typing import Tuple

from netapp_ontap import utils
from netapp_ontap.error import NetAppRestError
from netapp_ontap.resource import Resource
from netapp_ontap.response import NetAppResponse


LOGGER = logging.getLogger(__name__)


class CLI(Resource):
    """To help CLI and ONTAP users transition to the ONTAP REST API, ONTAP 9.6
    provides a private REST API endpoint that can be used to access any CLI command.
    Usage of this API call is recorded and returned in the AutoSupport data
    collection so that NetApp can identify usablity and functionality improvements
    in the REST API for future releases. There is no per-API documentation for the
    REST API access for each CLI command. Unlike the documented REST APIs, the API
    paths and properties for the CLI passthrough correspond very closely to the
    CLI. There are several rules that govern all the differences between a CLI
    command and the REST API mirroring the CLI command.
    """

    _path = "/api/private/cli"

    # pylint: disable=bad-continuation
    @utils.api
    def execute(
        self, command, body: dict = None, poll: bool = True, **kwargs
    ) -> NetAppResponse:
        """Execute a command on the CLI and return the result

        Args:
            command: A string representing the command to execute. This should
                not include any input or query parameters. Only the base command.
                E.g.: "volume show", "system node coredump delete", etc.
            body: Any input parameters required to execute the command. These
                would be passed to the API in the body and used as the required
                or optional command input.
            kwargs: Any parameters needed to filter the objects on which the
                command will operate.

        Returns:
            Returns a `netapp_ontap.response.NetAppResponse` object containing the
            details of the HTTP response.

        Raises:
            `netapp_ontap.error.NetAppRestError`: If the API call returned a status
                code >= 400
        """

        verb, url = _parse_command(command)
        if verb == "post" and kwargs:
            verb = "patch"

        url = "%s%s/%s" % (self.get_connection().origin, self._path, url)
        response = getattr(self._session, verb)(url, params=kwargs, json=body)
        response.raise_for_status()
        self._set_last_state()
        self._last_response = NetAppResponse(response)
        if not self._last_response.is_job:
            # log CLI output if it exists
            response_body = self._last_response.http_response.json()
            if response_body.get("cli_output"):
                LOGGER.info(response_body.get("cli_output"))
        elif poll:
            return self._poll()
        return self._last_response


def _parse_command(command) -> Tuple[str, str]:
    """Return the path for a particular CLI command

    Here are several examples of mappings from the ONTAP CLI to the ONTAP
    REST API for the /api/private/cli path:
        * volume show → GET /api/private/cli/volume
        * volume create → POST /api/private/cli/volume
        * volume modify → PATCH /api/private/cli/volume
        * volume delete → DELETE /api/private/cli/volume
        * volume restrict → POST /api/private/cli/volume/restrict
        * volume show-space → GET /api/private/cli/volume/space
        * volume show-footprint → GET /api/private/cli/volume/footprint
        * cluster add-node → POST /api/private/cli/cluster/add-node
        * cluster add-node-status → GET /api/private/cli/system/node/add-node-status
        * system node coredump show → GET /api/private/cli/system/node/coredump
        * system node coredump delete → DELETE /api/private/cli/system/node/coredump
        * system node coredump delete-all → DELETE /api/private/cli/system/node/coredump/all

    Args:
        command: A string representing the command to execute. This should
            not include any input or query parameters. Only the base command.
            E.g.: "volume show", "system node coredump delete", etc.

    Returns:
        A tuple of URL and verb to use to make a request with.

    Raises:
        `netapp_ontap.error.NetAppRestError`: If the command could not be parsed.
    """

    if not command:
        raise NetAppRestError(
            message="The command must be provided to call any actions."
        )

    try:
        pieces = command.split(" ")
    except Exception:
        raise NetAppRestError(message="Unable to parse the command.")

    action_word = pieces[-1]
    everything_else = pieces[:-1]

    if "show" in action_word or "status" in action_word:
        verb = "get"
        if action_word.startswith("show-"):
            everything_else.append("-".join(action_word.split("-")[1:]))
        elif action_word != "show":
            everything_else.append(action_word)
    elif "modify" in action_word:
        verb = "patch"
    elif "delete" in action_word:
        verb = "delete"
        if action_word.startswith("delete-"):
            everything_else.append("-".join(action_word.split("-")[1:]))
    else:
        verb = "post"
        if action_word != "create":
            everything_else.append(action_word)

    return verb, "/".join(everything_else)
