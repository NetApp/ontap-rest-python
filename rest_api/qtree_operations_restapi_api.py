#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS QTREE OPERATIONS USING REST API.

usage: python3 qtree_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER]
                                       [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import time
import base64
import argparse
import requests
import json
import requests
import logging
from getpass import getpass
requests.packages.urllib3.disable_warnings()


def get_snapshots(cluster, base64string, headers, vol_uuid):

    snap_api_url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    return r.json()


def get_key_snapshot(snapshot_name, vol_uuid, cluster, base64string, headers):
    print()
    tmp = dict(get_snapshots(cluster, base64string, headers, vol_uuid))
    snap = tmp['records']
    print()
    print("The UUID of the Snapshot is ")
    for i in snap:
        if i['name'] == snapshot_name:
            print(i['uuid'])
            return i['uuid']


def get_volumes(cluster, base64string, headers):

    url = "https://{}/api/storage/volumes/".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    return r.json()


def get_key_volumes(vol_name, cluster, base64string, headers):
    print()
    tmp = dict(get_volumes(cluster, base64string, headers))
    vols = tmp['records']
    print()
    print("The UUID of the Volume is ")
    for i in vols:
        if i['name'] == vol_name:
            print(i['uuid'])
            return i['uuid']


def get_svms(cluster, base64string, headers):

    url = "https://{}/api/svm/svms".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    return r.json()


def get_key_svms(svm_name, cluster, base64string, headers):
    tmp = dict(get_svms(cluster, base64string, headers))
    svms = tmp['records']
    print("The UUID of the SVM is ")
    for i in svms:
        if (i['name']) == svm_name:
            print(i['uuid'])
    return i['uuid']


def show_svm(cluster, base64string, headers):

    url = "https://{}/api/svm/svms".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    tmp = dict(r.json())
    svms = tmp['records']
    print()
    print(" List of SVMs:- ")
    for i in svms:
        print(i['name'])

    return r.json()


def show_volume(cluster, base64string, headers, svm_name):

    print()
    print("Getting Volume Details")
    print("======================")
    url = "https://{}/api/storage/volumes/?svm.name={}".format(
        cluster, svm_name)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    tmp = dict(r.json())
    svms = tmp['records']
    print()
    print(" List of Volumes :- ")
    for i in svms:
        print(i['name'])

    return r.json()


def show_qtree(cluster, base64string, headers):

    show_svm(cluster, base64string, headers)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()

    show_volume(cluster, base64string, headers, svm_name)
    print()
    vol_name = input(
        "Enter the Volume from which the Qtree need to be listed:-")
    vol_uuid = get_key_volumes(vol_name, cluster, base64string, headers)
    print()
    print("Getting Qtree Details")
    print("======================")
    qtree_api_url = "https://{}/api/storage/qtrees?volume.uuid={}".format(
        cluster, vol_uuid)
    try:
        r = requests.get(qtree_api_url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    tmp = dict(r.json())
    qtrees = tmp['records']
    print()
    print(" List of Qtrees :- ")
    for i in qtrees:
        print("Qtree Name:-%s Qtree ID:-%s" % (i['name'], i['id']))

    return


def create_qtree(cluster, base64string, headers):
    print()
    print("The List of SVMs")
    show_svm(cluster, base64string, headers)
    print()
    svm_name = input(
        "Enter the SVM Name on which the qtree need to be created:-")
    print()
    show_volume(cluster, base64string, headers, svm_name)
    print()
    vol_name = input(
        "Enter the Volume Name on which the Qtree need to be created:-")
    vol_uuid = get_key_volumes(vol_name, cluster, base64string, headers)
    print()
    qtree_name = input("Enter the name of the Qtree to be created:-")

    dataObj = {
        "name": qtree_name,
        "volume.uuid": vol_uuid,
        "svm.name": svm_name
    }

    print(dataObj)

    url = "https://{}/api/storage/qtrees".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers,
            json=dataObj,
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
    return


def patch_qtree(cluster, base64string, headers):
    print()
    show_qtree(cluster, base64string, headers)
    print()
    vol_name = input(
        "Enter the Volume Name on which the Qtree need to be Updated:-")
    vol_uuid = get_key_volumes(vol_name, cluster, base64string, headers)
    print()
    qtree_id = input("Enter the ID of the Qtree to be Updated [ID Number]:-")
    print()
    new_qtree_name = input("Enter the new Name of the Qtree to be Updated:-")

    dataObj = {
        "name": new_qtree_name
    }

    print(dataObj)

    url = "https://{}/api/storage/qtrees/{}/{}".format(
        cluster, vol_uuid, qtree_id)
    try:
        response = requests.patch(
            url, headers=headers, json=dataObj, verify=False)
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
    return


def delete_qtree(cluster, base64string, headers):
    print()
    show_qtree(cluster, base64string, headers)
    print()
    vol_name = input(
        "Enter the Volume Name on which the Qtree need to be Deleted:-")
    vol_uuid = get_key_volumes(vol_name, cluster, base64string, headers)
    print()
    qtree_id = input("Enter the ID of the Qtree to be Deleted [ID Number]:-")

    dataObj = {}

    url = "https://{}/api/storage/qtrees/{}/{}".format(
        cluster, vol_uuid, qtree_id)
    try:
        response = requests.delete(
            url, headers=headers, json=dataObj, verify=False)
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
    return


def qtree_ops(cluster, base64string, headers):
    print("THE FOLLOWING SCRIPT SHOWS QTREE OPERATIONS USING REST API.")
    print("==================================================================")
    print()
    qtreebool = input(
        "What Qtree Operation would you like to do? [show/create/update/delete] ")
    if qtreebool == 'show':
        show_qtree(cluster, base64string, headers)
    if qtreebool == 'create':
        create_qtree(cluster, base64string, headers)
    if qtreebool == 'update':
        patch_qtree(cluster, base64string, headers)
    if qtreebool == 'delete':
        delete_qtree(cluster, base64string, headers)

    return


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will execute Qtree operations using ONTAP REST APIs.", )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
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


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
    )
    args = parse_args()
    base64string = base64.encodestring(
        ('%s:%s' %
         (args.api_user, args.api_pass)).encode()).decode().replace(
        '\n', '')

    headers = {
        'authorization': "Basic %s" % base64string,
        'content-type': "application/json",
        'accept': "application/json"
    }

    qtree_ops(args.cluster, base64string, headers)
    print("Script Complete")
