"""
This module is used by the other example modules in this directory. It is not
meant as a stand-alone application. 
Common API calls such as getting key for SVM, volumes, displaying methods are added for ease of use of other modules
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
from netapp_ontap.resources import Svm, Volume, Aggregate, Snapshot
from netapp_ontap.resources import SnapmirrorRelationship, Qtree, QuotaRule, Igroup
from netapp_ontap.resources import IgroupInitiator, Disk, Node, IpInterface, Lun
from netapp_ontap import config, HostConnection
from netapp_ontap import NetAppRestError

SUBSTEP_INDEX = 1
STEP_INDEX = 1


class Argument:  # pylint: disable=too-few-public-methods
    """A structure to hold details of an argument"""

    def __init__(
            self,
            short_arg: str,
            long_arg: str,
            help_string: str,
            default=None,
            required=False,
            arg_type=None):
        self.short_arg = short_arg
        self.long_arg = long_arg
        self.help_string = help_string
        self.default = default
        self.required = required
        self.arg_type = arg_type if arg_type else str


def parse_args(
        program_description: str,
        arguments: List[Argument]) -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(description=program_description)
    for argument in arguments:
        parser.add_argument(
            argument.short_arg, argument.long_arg, required=argument.required,
            help=argument.help_string, default=argument.default, type=argument.arg_type,
        )
    parser.add_argument(
        "-u",
        "--api_user",
        default="admin",
        help="API Username")
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
        command,
        shell=run_in_shell,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    if result.returncode != 0:
        logging.info("<<<: %s", result.stderr.decode("utf-8"))
        result.check_returncode()
    else:
        logging.info("<<< %s", result.stdout.decode("utf-8"))


def show_aggregate() -> None:
    """Lists the Aggregate"""
    print("\n List of Aggregates:- \n")
    try:
        for aggregatelist in Aggregate.get_collection():
            print(aggregatelist.name)
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_svm() -> None:
    """Lists SVM"""
    print()
    print("Getting SVM Details")
    print("===================")
    try:
        for svm in Svm.get_collection(fields="uuid"):
            print("SVM name:-%s ; SVM uuid:-%s " % (svm.name, svm.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_volume(svm_name) -> None:
    """Lists Volumes"""
    print()
    print("Getting Volume Details")
    print("======================")
    try:
        for volume in Volume.get_collection(
                **{"svm.name": svm_name}, fields="uuid"):
            print(
                "Volume Name = %s;  Volume UUID = %s" %
                (volume.name, volume.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def get_key_svm(svm_name) -> None:
    """Get key of a SVM"""
    print()
    print("Getting SVM Details")
    print("===================")
    try:
        for svm in Svm.get_collection(
                **{'svm.name': svm_name}, fields="uuid"):
            print(svm.uuid)
            return svm.uuid
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def get_key_volume(svm_name, volume_name) -> None:
    """Lists Volumes"""
    print()
    print("Getting Volume Details")
    print("======================")
    try:
        for volume in Volume.get_collection(
                **{"svm.name": svm_name, 'volume.name': volume_name}, fields="uuid"):
            print(volume.uuid)
            return volume.uuid
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_node() -> None:
    """List nodes"""
    print(" Getting Node Details")
    print("=====================")

    try:
        for node in Node.get_collection(fields="uuid"):
            print("Node name:-%s ; Node uuid:-%s " % (node.name, node.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_snapshot(svm_name, volume_name) -> None:
    """List Snapshots in a volume"""
    print()
    vol_uuid = get_key_volume(svm_name, volume_name)
    print("The List of Snapshots:-")
    print("=======================")
    try:
        for snapshot in Snapshot.get_collection(vol_uuid):
            print(snapshot.name)
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_snapmirror() -> None:
    """List Snapmirror"""
    print("List of SnapMirror Relationships:")
    print("=================================")

    try:
        for snapmirrorrelationship in SnapmirrorRelationship.get_collection(
                fields="uuid"):
            print(snapmirrorrelationship.uuid)
            snapmirror1 = SnapmirrorRelationship.find(
                uuid=snapmirrorrelationship.uuid)
            print(snapmirror1.source.path)
            print(snapmirror1.destination.path)
            print(snapmirror1.state)
            print("-----------------------------")
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_qtree(svm_name, volume_name) -> None:
    """List Qtrees in a Volume"""
    vol_uuid = get_key_volume(svm_name, volume_name)
    print("The List of Qtrees:-")
    print("====================")
    try:
        for qtree in Qtree.get_collection(**{"volume.uuid": vol_uuid}):
            print("Name:- %s  ID:- %s" % (qtree.name, qtree.id))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_quotarule() -> None:
    """Lists Quota Rule"""
    print()
    print("Getting Quota Rule Details")
    print("==========================")
    try:
        for quotarule in QuotaRule.get_collection():
            print(
                "Quota-Rule UUID = %s;  Volume Name = %s" %
                (quotarule.uuid, quotarule.volume.name))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def get_key_quotarule_qtree(svm_name, volume_name, qtree_name) -> None:
    """Lists Quota Rule in a qtree"""
    print()
    print("Getting Quota Rule Details")
    print("==========================")
    try:
        for quotarule in QuotaRule.get_collection(
                **{'svm.name': svm_name, 'volume.name': volume_name, 'qtree.name': qtree_name}):
            print(
                "Quota-Rule UUID = %s;  Volume Name = %s" %
                (quotarule.uuid, quotarule.qtree.name))
            return quotarule.uuid
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def get_key_quotarule_volume(svm_name, volume_name) -> None:
    """Gets key of Quota Rule of volume"""
    print()
    print("Getting Quota Rule Details")
    print("==========================")
    try:
        for quotarule in QuotaRule.get_collection(
                **{'svm.name': svm_name, 'volume.name': volume_name}):
            print(
                "Quota-Rule UUID = %s;  Volume Name = %s" %
                (quotarule.uuid, quotarule.volume.name))
            return quotarule.uuid
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_igroup(svm_name) -> None:
    """Lists iGroup"""
    print()
    print("Getting Initiator Group Details")
    print("===============================")
    try:
        for igroup in Igroup.get_collection(
                **{"svm.name": svm_name}, fields="uuid"):
            print(
                "Igroup Name = %s;  Igroup UUID = %s" %
                (igroup.name, igroup.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_initiator(svm_name, igroup_name) -> None:
    """Lists initiator"""
    igroup_uuid = get_key_igroup(svm_name, igroup_name)
    try:
        for ini in IgroupInitiator.get_collection(
                igroup_uuid):
            print(
                "Initiator Name = %s " %
                (ini.name))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def get_key_igroup(svm_name, igroup_name) -> None:
    """Gets the key for iGroup"""
    print()
    print("Getting Initiator Group Details")
    print("===============================")
    try:
        for igroup in Igroup.get_collection(
                **{"svm.name": svm_name}, name=igroup_name):
            print(
                "Igroup Name = %s;  Igroup UUID = %s" %
                (igroup.name, igroup.uuid))
            return igroup.uuid
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_disk() -> None:
    """Lists disks details in cluster"""
    print()
    print("Getting Disk Details")
    print("===============================")
    try:
        for disk in Disk.get_collection():
            print(
                "Disk  Name = %s  " %
                (disk.name))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_interface() -> None:
    """ List Interface"""
    print("\n List of Interface:- \n")
    try:
        for interface in IpInterface.get_collection():
            print(
                "Interface Name:- %s; Inteface UUID:- %s " %
                (interface.name, interface.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_lun() -> None:
    """ List LUN"""
    print("\n List of LUN:- \n")
    try:
        for lun in Lun.get_collection():
            print("Lun Name:- %s; Lun UUID:- %s " % (lun.name, lun.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


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
