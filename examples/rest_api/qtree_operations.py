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
import base64
import argparse
import logging
from getpass import getpass
import requests
requests.packages.urllib3.disable_warnings()

def get_snapshots(cluster: str, headers_inc: str, vol_uuid: str):
    """ Get Snapshot"""
    url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
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

def get_key_snapshot(snapshot_name: str, vol_uuid: str, cluster: str, headers_inc: str):
    """ Get Snapshot Key"""
    print()
    tmp = dict(get_snapshots(cluster, headers_inc, vol_uuid))
    snap = tmp['records']
    print()
    print("The UUID of the Snapshot is ")
    for i in snap:
        if i['name'] == snapshot_name:
            print(i['uuid'])
            return i['uuid']

def get_volumes(cluster: str, headers_inc: str):
    """ Get Volumes"""
    url = "https://{}/api/storage/volumes/".format(cluster)
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

def get_key_volumes(vol_name: str, cluster: str, headers_inc: str):
    """ Get Volume Key"""
    print()
    tmp = dict(get_volumes(cluster, headers_inc))
    vols = tmp['records']
    print()
    print("The UUID of the Volume is ")
    for i in vols:
        if i['name'] == vol_name:
            print(i['uuid'])
            return i['uuid']

def get_svms(cluster: str, headers_inc: str):
    """ Get SVMs"""
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

def get_key_svms(svm_name: str, cluster: str, headers_inc: str):
    """ Get SVM Key"""
    tmp = dict(get_svms(cluster, base64string, headers_inc))
    svms = tmp['records']
    print("The UUID of the SVM is ")
    for i in svms:
        if (i['name']) == svm_name:
            print(i['uuid'])
        return i['uuid']

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
    print(" List of SVMs:- ")
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
    print(" List of Volumes :- ")
    for i in svms:
        print(i['name'])
    return response.json()

def show_qtree(cluster: str, headers_inc: str):
    """ Show Qtree"""
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()

    show_volume(cluster, headers_inc, svm_name)
    print()
    vol_name = input(
        "Enter the Volume from which the Qtree need to be listed:-")
    vol_uuid = get_key_volumes(vol_name, cluster, headers_inc)
    print()
    print("Getting Qtree Details")
    print("======================")
    qtree_api_url = "https://{}/api/storage/qtrees?volume.uuid={}".format(
        cluster, vol_uuid)
    try:
        response = requests.get(qtree_api_url, headers=headers_inc, verify=False)
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
    qtrees = tmp['records']
    print()
    print(" List of Qtrees :- ")
    for i in qtrees:
        print("Qtree Name:-%s Qtree ID:-%s" % (i['name'], i['id']))

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
    vol_name = input(
        "Enter the Volume Name on which the Qtree need to be created:-")
    vol_uuid = get_key_volumes(vol_name, cluster, headers_inc)
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
    show_qtree(cluster, headers_inc)
    print()
    vol_name = input(
        "Enter the Volume Name on which the Qtree need to be Updated:-")
    vol_uuid = get_key_volumes(vol_name, cluster, base64string, headers)
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
    show_qtree(cluster, headers_inc)
    print()
    vol_name = input(
        "Enter the Volume Name on which the Qtree need to be Deleted:-")
    vol_uuid = get_key_volumes(vol_name, cluster, base64string, headers)
    print()
    qtree_id = input("Enter the ID of the Qtree to be Deleted [ID Number]:-")

    dataobj = {}

    url = "https://{}/api/storage/qtrees/{}/{}".format(
        cluster, vol_uuid, qtree_id)
    try:
        response = requests.delete(
            url, headers=headers_inc, json=dataobj, verify=False)
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
        "What Qtree Operation would you like to do? [show/create/update/delete] ")
    if qtreebool == 'show':
        show_qtree(cluster, headers_inc)
    if qtreebool == 'create':
        create_qtree(cluster, headers_inc)
    if qtreebool == 'update':
        patch_qtree(cluster, headers_inc)
    if qtreebool == 'delete':
        delete_qtree(cluster, headers_inc)

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will execute Qtree operations using ONTAP REST APIs.", )
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

    qtree_ops(ARGS.cluster, headers)
    print("Script Complete")
