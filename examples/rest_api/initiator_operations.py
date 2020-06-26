#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts
This script was developed by NetApp to help demonstrate
NetApp technologies. This script is not officially
supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS INITIATOR OPERATIONS USING REST API

usage: python3 initiator_operations.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New or Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
from utils import Argument, parse_args, setup_logging, setup_connection, show_svm, show_igroup, get_key_igroup
requests.packages.urllib3.disable_warnings()


def list_initiator(cluster: str, headers_inc: str) -> None:
    """Lists Initiator Group"""

    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Initiator Groups need to be listed:-")
    print()
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


def create_initiator(cluster: str, headers_inc: str) -> None:
    """Create a Initiator Group"""
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the name of the SVM on which the volume needs to be created:- ")
    igroup_name = input(
        "Enter the name of the Igroup that you would like to create  : ")
    initiator_name = input(
        "Enter the name of the Initiator that you would like to add in the InitiatorGroup :")
    os_type2 = input("Enter the OS-TYPE :")

    payload2 = {
        "initiators": [
            {
                "name": initiator_name
            }
        ],
        "name": igroup_name,
        "os_type": os_type2,
        "svm": {
            "name": svm_name
        }
    }

    url = "https://{}/api/protocols/san/igroups".format(cluster)

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
    print("Inititor group created successfully...")


def update_initiator(cluster, headers_inc):
    """ Update Initiator Group"""
    print("=============================================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_igroup(svm_name, cluster, headers_inc)
    igroup_name = input(
        "Enter the Igroup name:- ")
    igroup_uuid = get_key_igroup(svm_name, igroup_name, cluster, headers_inc)

    initiator_name = input(
        "Enter the Intiator name:- ")

    igroupobj = {"name": initiator_name}
    url = "https://{}/api/protocols/san/igroups/{}/initiators".format(
        cluster, igroup_uuid)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=igroupobj,
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

    print("initiator Group  has been updated with the new name")


def delete_initiator(cluster, headers_inc):
    """Delete Initiator Group"""

    print("=============================================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_igroup(svm_name, cluster, headers_inc)
    igroup_name = input(
        "Enter the Igroup name:- ")
    igroup_uuid = get_key_igroup(svm_name, igroup_name, cluster, headers_inc)

    url = "https://{}/api/protocols/san/igroups/{}".format(
        cluster, igroup_uuid)
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

    print("Initiator Group  has been deleted.")


def init_ops(cluster, headers_inc):
    """Initiator Group Operations"""
    print()
    print("DEMONSTRATES INITIATOR GROUP OPERATIONS USING REST API :- ")
    print("==========================================================")
    print()
    initbool = input(
        "Choose the Initiator Group Operation would you like to do? [list/create/update/delete] ")
    if initbool == 'list':
        list_initiator(cluster, headers_inc)
    if initbool == 'create':
        create_initiator(cluster, headers_inc)
    if initbool == 'update':
        update_initiator(cluster, headers_inc)
    if initbool == 'delete':
        delete_initiator(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Initiator Group Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    init_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
