"""
This module is used by the other example modules in this directory. It is not
meant as a stand-alone application.
Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""

import sys
import time
import base64
import argparse
from getpass import getpass
import logging
import subprocess
from typing import List, Union
import requests
requests.packages.urllib3.disable_warnings()


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
            required=False):
        self.short_arg = short_arg
        self.long_arg = long_arg
        self.help_string = help_string
        self.default = default
        self.required = required


def parse_args(
        program_description: str,
        arguments: List[Argument]) -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(description=program_description)
    for argument in arguments:
        parser.add_argument(
            argument.short_arg, argument.long_arg, required=argument.required,
            help=argument.help_string, default=argument.default,
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


def setup_connection(api_user: str, api_pass: str):
    """Configure the default connection for the application"""

    base64string = base64.encodebytes(
        ('%s:%s' %
         (api_user, api_pass)).encode()).decode().replace('\n', '')

    headers = {
        'authorization': "Basic %s" % base64string,
        'content-type': "application/json",
        'accept': "application/json"
    }
    return headers


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


def show_quotarule(cluster: str, headers_inc: str) -> None:
    """Lists Quota Rule"""
    print()
    print("Getting Quota Rule Details")
    print("==========================")
    # https://10.195.51.149:443/api/storage/quota/rules
    qr_api_url = "https://{}/api/storage/quota/rules".format(
        cluster)
    try:
        response = requests.get(qr_api_url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    qrdict = dict(response.json())
    quotas = qrdict['records']
    print(" List of LUNs :- ")
    for quota in quotas:
        print("=====")
        print("Quota Volume Name = %s" % quota['volume']['name'])
        print("Quota UUID = %s" % quota['uuid'])


def show_interface(cluster: str, headers_inc: str):
    """ List Interface"""
    print("\n List of Interface:- \n")
    int_api_url = "https://{}/api/network/ip/interfaces".format(
        cluster)
    try:
        response = requests.get(int_api_url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    intdict = dict(response.json())
    inters = intdict['records']
    print()
    print(" List of Interfaces :- ")
    for inter in inters:
        print("=====")
        print("Interface Name = %s" % inter['name'])
        print("Interface UUID = %s" % inter['uuid'])


def show_disk(cluster: str, headers_inc: str):
    """List the Disk"""
    url = "https://{}/api//storage/disks".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tmp = dict(response.json())
    disks = tmp['records']
    print()
    print(" List of Disks:- ")
    print("================")
    for disk in disks:
        print("Disk Name :- %s" % disk['name'])


def show_node(cluster: str, headers_inc: str):
    """List the nodes"""
    url = "https://{}/api/cluster/nodes".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tmp = dict(response.json())
    nodes = tmp['records']
    print()
    print(" List of Nodes:- ")
    print("================")
    for node in nodes:
        print("Node Name :- %s" % node['name'])
        print("Node UUID :- %s" % node['uuid'])


def get_key_igroup(
        svm_name: str,
        initiator_name: str,
        cluster: str,
        headers_inc: str):
    """Get UUID of the Initiator"""
    # https://10.195.51.149:443 "GET
    # /api/protocols/san/igroups?svm.name=smog1&name=gt1
    url = "https://{}/api/protocols/san/igroups?svm.name={}&name={}".format(
        cluster, svm_name, initiator_name)

    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    initdict = dict(response.json())
    inits = initdict['records']
    print()
    print(" UUID of Initiator Group :- ")
    for init in inits:
        print("Initiator  Name = %s" % init['name'])
        print("Initiator  UUID = %s" % init['uuid'])
        return (init['uuid'])


def show_igroup(svm_name: str, cluster: str, headers_inc: str) -> None:
    """Lists Igroup"""

    print("Getting Initiator Group Details")
    print("===============================")

    url = "https://{}/api/protocols/san/igroups?svm.name={}&fields=uuid".format(
        cluster, svm_name)

    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    initdict = dict(response.json())
    inits = initdict['records']
    print()
    print(" List of Initiator Group :- ")
    print()
    for init in inits:
        print("=====")
        print("Initiator  Name = %s" % init['name'])
        print("Initiator  UUID = %s" % init['uuid'])


def show_lun(cluster: str, headers_inc: str) -> None:
    """Lists Accounts"""
    print("======================")
    print()
    lun_api_url = "https://{}/api/storage/luns".format(
        cluster)
    try:
        response = requests.get(lun_api_url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    lundict = dict(response.json())
    luns = lundict['records']
    print()
    print(" List of LUNs :- ")
    for lun in luns:
        print("=====")
        print("LUN Name = %s" % lun['name'])
        print("LUN UUID = %s" % lun['uuid'])


def get_key_lun(lun_name: str, cluster: str, headers_inc: str) -> None:
    """Lists LUN"""
    print("======================")
    print()
    lun_api_url = "https://{}/api/storage/luns?name={}".format(
        cluster, lun_name)
    try:
        response = requests.get(lun_api_url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    lundict = dict(response.json())
    luns = lundict['records']
    print()
    print(" List of LUNs :- ")
    for lun in luns:
        print(lun['uuid'])
        return lun['uuid']


def get_key_snapshot(
        svm_name: str,
        volume_name: str,
        snapshot_name: str,
        cluster: str,
        headers_inc: str):
    """ Get Snapshot Key"""
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    snap_api_url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
    try:
        job_response = requests.get(
            snap_api_url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    snapshotsdict = dict(job_response.json())
    snapshots = snapshotsdict['records']
    print()
    print("The UUID of the Snapshot is ")
    for snapshot in snapshots:
        if snapshot['name'] == snapshot_name:
            print(snapshot['uuid'])
            return snapshot['uuid']


def get_key_volumes(
        svm_name: str,
        volume_name: str,
        cluster: str,
        headers_inc: str):
    """ get volume keys"""
    print()
    url = "https://{}/api/storage/volumes?name={}&svm.name={}".format(
        cluster, volume_name, svm_name)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    respdict = dict(response.json())
    volumes = respdict['records']
    print("The UUID of the Volume is ")
    for volume in volumes:
        print(volume['uuid'])
        return volume['uuid']


def get_key_accountowner(account_name: str, cluster: str, headers_inc: str):
    print("======================")
    print()
    account_api_url = "https://{}/api/security/accounts?name={}".format(
        cluster, account_name)
    try:
        response = requests.get(
            account_api_url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    accountdict = dict(response.json())
    accounts = accountdict['records']
    print()
    print("Account UUID :- ")
    for account in accounts:
        print(account['owner']['uuid'])
        return account['owner']['uuid']


def show_account(cluster: str, headers_inc: str):
    """Lists Accounts"""
    print("======================")
    print()
    account_api_url = " https://{}/api/security/accounts".format(
        cluster)
    try:
        response = requests.get(
            account_api_url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    accountdict = dict(response.json())
    accounts = accountdict['records']
    print()
    print(" List of Accounts :- ")
    for account in accounts:
        print("=====")
        print("Account Name = %s" % account['name'])
        print("Account  Owner Name = %s" % account['owner']['name'])
        print("Account Owner UUID = %s" % account['owner']['uuid'])


def get_key_svms(svm_name: str, cluster: str, headers_inc: str):
    """ get svm key"""
    url = "https://{}/api/svm/svms".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    svmsdict = dict(response.json())
    svms = svmsdict['records']
    print("The UUID of the SVM is ")
    for svm in svms:
        if (svm['name']) == svm_name:
            print(svm['uuid'])
            return svm['uuid']


def show_svm(cluster: str, headers_inc: str):
    """ List the svm"""
    url = "https://{}/api/svm/svms".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tmp = dict(response.json())
    svms = tmp['records']
    print()
    print(" List of SVMs:- ")
    print("================")
    for i in svms:
        print(i['name'])
    return response.json()


def show_volume(cluster: str, headers_inc: str, svm_name: str):
    """ list the volumes"""
    print()
    print("Getting Volume Details")
    print("======================")
    url = "https://{}/api/storage/volumes/?svm.name={}".format(
        cluster, svm_name)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    volumesdict = dict(response.json())
    volumes = volumesdict['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for volume in volumes:
        print(
            "Volume Name :- %s; Volume UUID :- %s" %
            (volume['name'], volume['uuid']))


def show_snapshot(
        svm_name: str,
        volume_name: str,
        cluster: str,
        headers_inc: str):
    """ list snapshots"""
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    print()
    print("Getting Snapshot Details")
    print("========================")
    snap_api_url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
    try:
        response = requests.get(
            snap_api_url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    svmsdict = dict(response.json())
    svms = svmsdict['records']
    print()
    for svm in svms:
        print(svm['name'])
    return response.json()


def show_aggregate(cluster: str, headers_inc: str):
    """ list aggregates"""
    url = "https://{}/api/storage/aggregates".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    tmp = dict(response.json())
    aggr = tmp['records']
    print()
    print("List of Aggregates:- ")
    print("=====================")
    for i in aggr:
        print("Aggregate Name = %s " % i['name'])
        print("Aggregate UUID = %s " % i['uuid'])


def check_job_status(job_status: str, headers_inc: str, cluster: str):
    """ check job status"""
    if job_status['state'] == "failure":
        if job_status['code'] == 460770:
            print("SVM Already Exists")
        else:
            print("Operation failed due to :{}".format(job_status['message']))
    elif job_status['state'] == "success":
        print("Operation completed successfully.")
    else:
        job_status_url = "https://{}/api/cluster/jobs/{}".format(
            cluster, job_status['uuid'])
        try:
            job_response = requests.get(
                job_status_url, headers=headers_inc, verify=False)
        except requests.exceptions.HTTPError as err:
            print(err)
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print(err)
            sys.exit(1)
        job_status = job_response.json()
        time.sleep(5)
        check_job_status(job_status, headers_inc, cluster)


def show_qtree(
        svm_name: str,
        volume_name: str,
        cluster: str,
        headers_inc: str):
    """ Show Qtree"""
    print()
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    print()
    print("Getting Qtree Details")
    print("======================")
    qtree_api_url = "https://{}/api/storage/qtrees?volume.uuid={}".format(
        cluster, vol_uuid)
    try:
        response = requests.get(
            qtree_api_url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    qtreesdict = dict(response.json())
    qtrees = qtreesdict['records']
    print()
    print(" List of Qtrees :- ")
    for qtree in qtrees:
        print("Qtree Name:-%s Qtree ID:-%s" % (qtree['name'], qtree['id']))
