#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS NFS SETUP OPERATIONS USING REST API.

usage: python3 nfs_setup.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
import urllib3 as ur
from utils import Argument, parse_args, setup_logging
from utils import setup_connection, get_size, get_key_svms, show_svm
ur.disable_warnings()


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

    print()
    print("Create the Export Policy:-")
    print("==========================")

    export_policy_name = input("Enter the Export Policy Name :- ")
    protocol = input(
        "Enter the protocol name for the Export Policy(nfs/cifs/any):- ")
    clients = input("Enter client details [0.0.0.0/0]:- ")

    url2 = "https://{}/api/protocols/nfs/export-policies".format(cluster)
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
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
        print("Volume %s created" % vol_name)
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
    print("NAS creation script completed.")


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Volume Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    nfs_setup(args.cluster, headers)
    print("Script Complete")


if __name__ == "__main__":
    main()
