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
    def __init__(self, short_arg: str, long_arg: str, help_string: str, default=None, required=False, arg_type=None):
        self.short_arg = short_arg
        self.long_arg = long_arg
        self.help_string = help_string
        self.default = default
        self.required = required
        self.arg_type = arg_type if arg_type else str


def parse_args(program_description: str, arguments: List[Argument]) -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(description=program_description)
    for argument in arguments:
        parser.add_argument(
            argument.short_arg, argument.long_arg, required=argument.required,
            help=argument.help_string, default=argument.default, type=argument.arg_type,
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


class LiveMultilineOutput:
    """This is a class for managing multiline text output on the screen.

    While inside this class' context, the application can change the output's
    buffer by calling change() and the buffer will be redrawn, clearing the
    previous output and printing all of the new output. Once the context is
    exited, the cursor is moved to the line after the last line in the output
    so that normal printing can continue.
    """

    def __init__(self, initial_data=None):
        self.buffer = []
        if initial_data:
            self.buffer = initial_data
        self._lines_drawn = 0
        self.draw()

    def change(self, new_list):
        """Update the text buffer with a new list of strings"""

        self.buffer = new_list
        self.draw()

    def draw(self):
        """Erase our current line and write a new one, then move down"""

        for line in self.buffer:
            print("\033[K%s" % line)
        self._lines_drawn = len(self.buffer)
        # now that we're done, move all the way back to the top left
        if self._lines_drawn > 0:
            print("\033[%sA\r" % self._lines_drawn, end="")

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        # move down to the bottom
        print("\033[%sB" % (self._lines_drawn - 1))
