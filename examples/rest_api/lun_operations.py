#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts
This script was developed by NetApp to help demonstrate
NetApp technologies. This script is not officially
supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS LUN OPERATIONS USING REST API.

usage: python3 lun_operations.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New or Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import get_size, show_svm, show_volume, show_lun, get_key_lun
ur.disable_warnings()


def list_lun(cluster: str, headers_inc: str) -> None:
    """Lists LUN"""
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


def create_lun(cluster: str, headers_inc: str) -> None:
    """Create a LUN"""
    print("======================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input("Enter the name of the SVM :- ")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    vol_name = input(
        "Choose the volume on which you would like to create the LUN : ")

    print()
    lun_name = input("Enter the name of the LUN  : ")
    lun_name_ext = "/vol/" + vol_name + "/" + lun_name
    os_type = input("Enter the name of the OS-TYPE  : ")
    lun_size = input("Enter the LUN size in MBs :")
    l_size = get_size(lun_size)

    payload2 = {
        "comment": lun_name,
        "location": {
            "logical_unit": lun_name,
            "volume": {
                "name": vol_name
            }
        },
        "name": lun_name_ext,
        "os_type": os_type,
        "space": {
            "guarantee": {
                "requested": bool("")
            },
            "size": l_size
        },
        "svm": {
            "name": svm_name
        }
    }

    url = "https://{}/api/storage/luns".format(cluster)
    try:
        response = requests.post(
            url,
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
    print("LUN created successfully...")


def update_lun(cluster, headers_inc):
    """ Update LUN"""
    print("======================")
    print()
    show_lun(cluster, headers_inc)
    lun_name = input("Enter the name of the LUN :- ")
    lun_new_name = input(
        "Enter the new name of the LUN  to be updated [Full-Path]:- ")

    lun_uuid = get_key_lun(lun_name, cluster, headers_inc)
    print(lun_uuid)
    lunpatchobj = {"name": lun_new_name}
    print(lunpatchobj)

    url = "https://{}/api/storage/luns/{}".format(cluster, lun_uuid)
    try:
        response = requests.patch(
            url,
            headers=headers_inc,
            json=lunpatchobj,
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

    print("LUN has been updated with the new name")


def delete_lun(cluster, headers_inc):
    """ Delete LUN"""
    print("======================")
    print()
    show_lun(cluster, headers_inc)
    lun_name = input("Enter the name of the LUN to be deleted:- ")

    lun_uuid = get_key_lun(lun_name, cluster, headers_inc)
    print(lun_uuid)

    url = "https://{}/api/storage/luns/{}".format(cluster, lun_uuid)
    try:
        response = requests.delete(
            url,
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

    print("LUN has been deleted.")


def lun_ops(cluster, headers_inc):
    """LUN Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS LUN OPERATIONS USING REST API :- ")
    print("============================================================")
    print()
    lunbool = input(
        "Choose the LUN Operation would you like to do? [list/create/update/delete] ")
    if lunbool == 'list':
        list_lun(cluster, headers_inc)
    if lunbool == 'create':
        create_lun(cluster, headers_inc)
    if lunbool == 'update':
        update_lun(cluster, headers_inc)
    if lunbool == 'delete':
        delete_lun(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates LUN Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    lun_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
