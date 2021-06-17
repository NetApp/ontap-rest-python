#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS QTREE OPERATIONS USING REST API.

usage: python3 qtree_operations.py [-h] -c CLUSTER [-u API_USER]
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
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import get_key_volumes, show_svm, show_volume, show_qtree
ur.disable_warnings()


def list_qtree(cluster: str, headers_inc: str):
    """ Show Qtree"""
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()

    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the Volume from which the Qtree need to be listed:-")
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

    qtreedict = dict(response.json())
    qtrees = qtreedict['records']
    print()
    print(" List of Qtrees :- ")
    for qtree in qtrees:
        print("Qtree Name:-%s Qtree ID:-%s" % (qtree['name'], qtree['id']))


def create_qtree(cluster: str, headers_inc: str):
    """ Create Qtree"""
    print()
    print("The List of SVMs")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM Name on which the qtree need to be created:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the Volume Name on which the Qtree need to be created:-")
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    print()
    qtree_name = input("Enter the name of the Qtree to be created:-")

    dataobj = {
        "name": qtree_name,
        "volume.uuid": vol_uuid,
        "svm.name": svm_name
    }

    print(dataobj)

    url = "https://{}/api/storage/qtrees".format(cluster)
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

    url_text = response.json()
    print(url_text)


def patch_qtree(cluster: str, headers_inc: str):
    """ Update Qtree"""

    print()
    print("The List of SVMs")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM Name on which the qtree need to be created:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the Volume Name on which the Qtree need to be created:-")
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    print()
    show_qtree(svm_name, volume_name, cluster, headers_inc)
    print()

    qtree_id = input("Enter the ID of the Qtree to be Updated [ID Number]:-")
    print()
    new_qtree_name = input("Enter the new Name of the Qtree to be Updated:-")

    dataobj = {
        "name": new_qtree_name
    }

    print(dataobj)

    url = "https://{}/api/storage/qtrees/{}/{}".format(
        cluster, vol_uuid, qtree_id)
    try:
        response = requests.patch(
            url, headers=headers_inc, json=dataobj, verify=False)
        print("Qtree has been updated.")
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
    print(url_text)


def delete_qtree(cluster: str, headers_inc: str):
    """ Delete Qtree"""

    print()
    print("The List of SVMs")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM Name on which the qtree need to be created:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the Volume Name on which the Qtree need to be created:-")
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    print()
    show_qtree(svm_name, volume_name, cluster, headers_inc)
    print()
    qtree_id = input("Enter the ID of the Qtree to be Deleted [ID Number]:-")

    dataobj = {}

    url = "https://{}/api/storage/qtrees/{}/{}".format(
        cluster, vol_uuid, qtree_id)
    try:
        response = requests.delete(
            url, headers=headers_inc, json=dataobj, verify=False)
        print("Qtree has been deleted.")
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
    print(url_text)


def qtree_ops(cluster, headers_inc):
    """ Qtree Operation"""
    print("Demonstrates Qtree Operations using REST API .")
    print("==============================================")
    print()
    qtreebool = input(
        "What Qtree Operation would you like to do? [list/create/update/delete] ")
    if qtreebool == 'list':
        list_qtree(cluster, headers_inc)
    if qtreebool == 'create':
        create_qtree(cluster, headers_inc)
    if qtreebool == 'update':
        patch_qtree(cluster, headers_inc)
    if qtreebool == 'delete':
        delete_qtree(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Volume Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    qtree_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
