"""
This module is used by the other example modules in this directory. It is not
meant as a stand-alone application.
Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""

import argparse
from getpass import getpass
import logging
import subprocess
from typing import List, Union

from netapp_ontap import config, HostConnection


SUBSTEP_INDEX = 1
STEP_INDEX = 1


class Argument:  # pylint: disable=too-few-public-methods
    """A structure to hold details of an argument"""
    def __init__(self, short_arg: str, long_arg: str, help_string: str, default=None, required=False):
        self.short_arg = short_arg
        self.long_arg = long_arg
        self.help_string = help_string
        self.default = default
        self.required = required


def parse_args(program_description: str, arguments: List[Argument]) -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(description=program_description)
    for argument in arguments:
        parser.add_argument(
            argument.short_arg, argument.long_arg, required=argument.required,
            help=argument.help_string, default=argument.default,
        )
    parser.add_argument("-u", "--api_user", default="admin", help="API Username")
    parser.add_argument("-p", "--api_pass", help="API Password")
    parsed_args = parser.parse_args()

    # collect the password without echo if not already provided
    if not parsed_args.api_pass:
        parsed_args.api_pass = getpass()

    return parsed_args


def setup_logging() -> None:
    """Configure logging for the application"""

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
    )


def setup_connection(cluster: str, api_user: str, api_pass: str) -> None:
    """Configure the default connection for the application"""

    config.CONNECTION = HostConnection(
        cluster, username=api_user, password=api_pass, verify=False,
    )


def get_size(vol_size: int):
    """ Convert MB to Bytes"""
    tmp = int(vol_size) * 1024 * 1024
    return tmp


def step(text: str) -> None:
    """Print a header for this step of the script

    Args:
        text: The message that describes what this step is doing
    """

    global SUBSTEP_INDEX, STEP_INDEX  # pylint: disable=global-statement
    SUBSTEP_INDEX = 1

    logging.info("#" * 80)
    logging.info("# Step %s: %s", STEP_INDEX, text)
    logging.info("#" * 80)
    STEP_INDEX += 1


def substep(text: str) -> None:
    """Print a header for this substep

    Args:
        text: The message that describes what this substep is doing
    """

    global SUBSTEP_INDEX  # pylint: disable=global-statement
    logging.info("%s) %s", SUBSTEP_INDEX, text)
    SUBSTEP_INDEX += 1


def run_cmd(command: Union[List[str], str]) -> None:
    """Run the given command from the system.

    If the command is provided as a string, a shell will be invoked to parse and
    run the command. If it is provided as a list of strings, the command will be
    executed directly. See the subprocess module documentation around the use of
    the shell argument.

    Args:
        command: A string or a list of strings which represent the command to be
            run on the system shell.

    Raises:
        subprocess.CalledProcessError: This will be raised if the return code
            was not 0.
    """

    if isinstance(command, list):
        run_in_shell = False
        logging.info(">>> %s", " ".join(command))
    else:
        run_in_shell = True
        logging.info(">>> %s", command)
    result = subprocess.run(
        command, shell=run_in_shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True,
    )
    if result.returncode != 0:
        logging.info("<<<: %s", result.stderr.decode("utf-8"))
        result.check_returncode()
    else:
        logging.info("<<< %s", result.stdout.decode("utf-8"))
