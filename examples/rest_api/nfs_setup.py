#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS NFS SETUP OPERATIONS USING REST API.

usage: python3 nfs_setup_restapi_api.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import base64
import argparse
import logging
from getpass import getpass
import requests
requests.packages.urllib3.disable_warnings()

def get_size(vol_size):
    """Convert MBs to Bytes"""
    tmp = int(vol_size) * 1024 * 1024
    return tmp

def get_key_svms(cluster: str, headers_inc: str, svm_name: str):
    """ Get SVM key"""
    tmp = dict(get_svms(cluster, headers_inc))
    svms = tmp['records']
    for i in svms:
        if i['name'] == svm_name:
            # print i
            return i['uuid']

def get_svms(cluster: str, headers_inc: str):
    """ get SVMs"""
    url = "https://{}/api/svm/svms".format(cluster)
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
    return response.json()

def show_svm(cluster: str, headers_inc: str):
    """ Show SVM"""
    url = "https://{}/api/svm/svms".format(cluster)
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

    tmp = dict(response.json())
    svms = tmp['records']
    print()
    print("List of SVMs:- ")
    print("================")
    for i in svms:
        print(i['name'])
    return response.json()

def show_volume(cluster: str, headers_inc: str, svm_name: str):
    """ Show Volume"""
    print()
    print("Getting Volume Details")
    print("======================")
    url = "https://{}/api/storage/volumes/?svm.name={}".format(
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

    tmp = dict(response.json())
    svms = tmp['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for i in svms:
        print(i['name'])
    return response.json()

def nfs_setup(cluster: str, headers_inc: str):
    """Demonstrates NFS Setup using REST APIs."""
    print("Demonstrates NFS Setup using REST APIs.")
    print("=======================================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Choose the SVM on which you would like to create a NFS Share :")
    print("Make sure that NAS  LIFs on each nodes are created on the SVM :")
    print()

    print("Checking and Enabling NFS Protocol on SVM:-")
    print("===========================================")

    payload1 = {
        "enabled": bool("true"),
        "protocol": {
            "v3_enabled": bool("true")
        },
        "svm": {
            "name": svm_name
        }
    }

    url1 = "https://{}/api/protocols/nfs/services".format(cluster)
    try:
        response = requests.post(
            url1,
            headers=headers_inc,
            json=payload1,
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

    print()
    print("Create the Export Policy:-")
    print("==========================")

    export_policy_name = input("Enter the Export Policy Name :- ")
    protocol = input(
        "Enter the protocol name for the Export Policy(nfs/cifs/any):- ")
    clients = input("Enter client details [0.0.0.0/0]:- ")

    url2 = "https://{}/api/protocols/nfs/export-policies".format(cluster)
    svm_uuid = get_key_svms(cluster, base64string, headers, svm_name)
    payload2 = {
        "name": export_policy_name,
        "rules": [
            {
                "clients": [
                    {
                        "match": clients
                    }
                ],
                "protocols": [
                    protocol
                ],
                "ro_rule": [
                    "any"
                ],
                "rw_rule": [
                    "any"
                ]
            }
        ],
        "svm.uuid": svm_uuid
    }

    try:
        response = requests.post(
            url2,
            headers=headers_inc,
            json=payload2,
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

    url_text = response.json()

    print()
    print("Create the Volume:-")
    print("===================")
    vol_name = input("Enter the Volume Name to create NFS Share:-")
    vol_size = input("Enter the Volume Size in MBs :-")
    aggr_name = input("Enter the aggregate name:-")

    v_size = get_size(vol_size)

    pather = "/" + vol_name

    payload3 = {"aggregates": [{"name": aggr_name}],
                "svm": {"name": svm_name},
                "name": vol_name,
                "size": v_size,
                "nas": {"export_policy": {"name": export_policy_name},
                        "security_style": "unix",
                        "path": pather}}

    url3 = "https://{}/api/storage/volumes".format(cluster)
    try:
        response = requests.post(
            url3,
            headers=headers_inc,
            json=payload3,
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

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="Demonstrates NFS Setup using REST API.", )
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
    base64string = base64.encodestring(
        ('%s:%s' %
         (ARGS.api_user, ARGS.api_pass)).encode()).decode().replace('\n', '')

    headers = {
        'authorization': "Basic %s" % base64string,
        'content-type': "application/json",
        'accept': "application/json"
    }

    nfs_setup(ARGS.cluster, headers)
    print("Script Complete")
