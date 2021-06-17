#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts
This script was developed by NetApp to help demonstrate
NetApp technologies. This script is not officially
supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS INTERFACE OPERATIONS USING REST API

usage: python3 interface_operations.py [-h] -c CLUSTER [-u API_USER]
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
from utils import show_svm, get_key_svms, show_node, show_interface
ur.disable_warnings()


def list_interface(cluster: str, headers_inc: str):
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


def create_interface(cluster: str, headers_inc: str):
    """Create Interface"""
    int_name = input("Enter the name of the Interface:- ")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the name of the SVM on which the interface should be created :- ")
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    print()
    show_node(cluster, headers_inc)
    print()
    node_name = input(
        "Enter the name of the home node on which the interface should be created :- ")
    node_uuid = input(
        "Enter the uuid of the home node on which the interface should be created :- ")
    ip_add = input("Enter the IP address:- ")
    netmask = input("Enter the NetMask:- ")

    interfaceobj = {
        "enabled": True,
        "ip": {
            "address": ip_add,
            "netmask": netmask
        },
        "name": int_name,
        "scope": "svm",
        "svm": {
            "name": svm_name,
            "uuid": svm_uuid
        },
        "location": {"home_node": {
            "name": node_name,
            "uuid": node_uuid
        }
        }
    }
    url = "https://{}/api/network/ip/interfaces".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=interfaceobj,
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
    print("Interface created successfully...")


def patch_interface(cluster: str, headers_inc: str) -> None:
    """ Patch Interface"""
    print("=======================")
    print()
    show_interface(cluster, headers_inc)
    int_uuid = input("Enter the UUID of the Interface:- ")
    int_new_name = input(
        "Enter the new name of the interface  to be updated :- ")
    intpatchobj = {"name": int_new_name}
    print(intpatchobj)

    url = "https://{}/api/network/ip/interfaces/{}".format(cluster, int_uuid)
    try:
        response = requests.patch(
            url,
            headers=headers_inc,
            json=intpatchobj,
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

    print("Interface has been updated with the new name")


def delete_interface(cluster: str, headers_inc: str) -> None:
    """ delete Interface"""
    print("=======================")
    print()
    show_interface(cluster, headers_inc)

    int_uuid = input("Enter the UUID of the Interface:- ")

    url = "https://{}/api/network/ip/interfaces/{}".format(cluster, int_uuid)
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

    print("Interface has been deleted.")


def interface_ops(cluster: str, headers_inc: str) -> None:
    """Interface Operations"""
    print()
    print("DEMONSTRATES INTERFACE OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("=========================================================================")
    print()
    interfacebool = input(
        "What Interface Operation would you like to do? [list/create/update/delete] ")
    if interfacebool == 'list':
        list_interface(cluster, headers_inc)
    if interfacebool == 'create':
        create_interface(cluster, headers_inc)
    if interfacebool == 'update':
        patch_interface(cluster, headers_inc)
    if interfacebool == 'delete':
        delete_interface(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Interface Operation using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    interface_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
