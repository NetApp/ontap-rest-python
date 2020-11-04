#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies.
This script is not officially supported as a
standard NetApp product.

Purpose: This Module covers vserver security file-directory CLI usage using ONTAP REST API

Usage: vserver_file_security_cli_passthrough.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
vserver_file_security_cli_passthrough.py: the following arguments are required: -c/--cluster, -u/--admin, -p/--password

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""
import sys
import base64
import argparse
from getpass import getpass
import logging
import texttable as tt
import requests
import urllib3 as ur
ur.disable_warnings()


def get_policy(cluster: str, headers_inc: str):
    "Get Policy name in all vserver"
    endpoint = "api/private/cli/vserver/security/file-directory/policy"
    url = "https://{}/{}?fields=vserver,policy_name".format(cluster, endpoint)
    print()
    response = requests.get(url, headers=headers_inc, verify=False)
    return response.json()


def get_texttable(cluster: str, headers_inc: str):
    "Display events call output"
    ctr = 0
    tmp = dict(get_policy(cluster, headers_inc))
    print()
    vols = tmp['records']
    tab = tt.Texttable()
    header = ['vserver', 'policy_name']
    tab.header(header)
    tab.set_cols_align(['c', 'c'])
    for eventlist in vols:
        ctr = ctr + 1
        vserver = eventlist['vserver']
        policy_name = eventlist['policy_name']
        row = [vserver, policy_name]
        tab.set_cols_width([20, 20])
        tab.add_row(row)
        tab.set_cols_align(['c', 'c'])
    setdisplay = tab.draw()
    print(setdisplay)
    print("\n Number of records displayed: {}".format(ctr))


def create_ntfs_policy(cluster: str, headers_inc: str):
    """Module to create NTFS policy"""
    vserver = input("Enter the svm name: ")
    policy_name = input("Enter the policy name: ")
    dataobj = {
        'vserver': vserver,
        'policy_name': policy_name
    }
    url = "https://{}/api/private/cli/vserver/security/file-directory/policy/".format(
        cluster)
    print("\n Passing input values:")
    print(dataobj)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
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
    create_ntfs_task(cluster, headers_inc)


def create_ntfs_task(
        cluster: str,
        headers_inc: str):
    """ Module to create NTFS task"""
    print("\n===================================================================")
    print("\n Module to Create NTFS task")
    vserver = input("Enter the svm name: ")
    policy_name = input("Enter the policy name: ")
    dataobj = {
        'vserver': vserver,
        'policy-name': policy_name
    }
    path = input("Enter the path: ")
    dataobj = {
        'vserver': vserver,
        'policy_name': policy_name,
        'ntfs_sd': ['ntfs_sd'],
        'path': path,
        'security_type': 'ntfs',
        'ntfs_mode': 'replace',
        'access_control': 'file-directory'
    }
    url = "https://{}/api/private/cli/vserver/security/file-directory/policy/task/add".format(
        cluster)
    print("\n Passing input values:")
    print(dataobj)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
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
    get_texttable(cluster, headers_inc)
    vserver_apply(cluster, headers_inc)


def vserver_apply(
        cluster: str,
        headers_inc: str):
    """ Module to create policy apply"""
    print("\n===================================================================")
    print("\n Module to apply the policy on Vserver")
    vserver = input("Enter the svm name: ")
    policy_name = input("Enter the policy name: ")
    dataobj = {
        'vserver': vserver,
        'policy_name': policy_name
    }
    url = "https://{}/api/private/cli/vserver/security/file-directory/apply".format(
        cluster)
    print(url)
    print("\n ")
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
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
    print("Applied Policy to vserver tasks")
    cleanup_ntfs(cluster, headers_inc)


def cleanup_ntfs(
        cluster: str,
        headers_inc: str):
    """ Module to cleanup NTFS policy"""
    print("\n===================================================================")
    print("\n Module to Cleanup the polices that were created\n")
    vserver = input("Enter the svm name: ")
    policy_name = input("Enter the policy name: ")
    dataobj = {
        'policy_name': policy_name,
        'vserver': vserver
    }
    url = "https://{}/api/private/cli/vserver/security/file-directory/policy".format(
        cluster)
    print("\n Delete vserver security file-directory Policy")
    try:
        response = requests.delete(
            url,
            headers=headers_inc,
            json=dataobj,
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
    get_texttable(cluster, headers_inc)


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""
    parser = argparse.ArgumentParser(
        description="This script will list vserver file security ")
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details")
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


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
    )
    ARGS = parse_args()
    BASE64STRING = base64.encodebytes(
        ('%s:%s' %
         (ARGS.api_user, ARGS.api_pass)).encode()).decode().replace('\n', '')
    headers = {
        'authorization': "Basic %s " % BASE64STRING,
        'content-type': "application/json",
        'accept': "application/json"
    }
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n THIS MODULE COVERS Vserver Security file-directory USAGE IN CLI PASSTHROUGH")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    create_ntfs_policy(ARGS.cluster, headers)
    print("==========END OF MODULE=============")
