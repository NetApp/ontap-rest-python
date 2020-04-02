#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SNAPMIRROR OPERATIONS USING REST API.

usage: python3 snapmirror_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER]
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

def get_volumes(cluster: str, headers_inc: str):
    """Get Volumes"""
    url = "https://{}/api/storage/volumes/".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    return response.json()

def get_key_volumes(vol_name: str, cluster: str, headers_inc: str):
    """ Get Volume Keys"""
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
    """ Get SVM keys"""
    tmp = dict(get_svms(cluster, headers_inc))
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

def show_volume(cluster: str, headers_inc: str):
    """ List Volumes"""
    print("The List of SVMs")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
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
    url_text = requests.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    tmp = dict(requests.json())
    svms = tmp['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for i in svms:
        print(i['name'])
    return response.json()

def show_snapmirror(cluster: str, headers_inc: str):
    """ Show Snapmirror"""
    print()
    print("Getting Snapmirror Details")
    print("==========================")
    snap_api_url = "https://{}/api/snapmirror/relationships".format(cluster)
    try:
        response = requests.get(snap_api_url, headers=headers_inc, verify=False)
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
    sms = tmp['records']
    print()
    print(" List of Snapmirror :- ")
    print("=======================")
    for i in sms:
        print(i['uuid'])
        snap_api_url1 = "https://{}/api/snapmirror/relationships/{}".format(
            cluster, i['uuid'])
        try:
            response1 = requests.get(snap_api_url1, headers=headers, verify=False)
        except requests.exceptions.HTTPError as err:
            print(str(err))
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print(str(err))
            sys.exit(1)
        url_text = response1.json()
        if 'error' in url_text:
            print(url_text)
            sys.exit(1)

        tmp1 = dict(response1.json())
        print(tmp1['source']['path'])
        print(tmp1['destination']['path'])
        print(tmp1['state'])
        print("------------------------------")

def delete_snapmirror(cluster: str, headers_inc: str):
    """Snapmirror Delete"""
    print("=============================================")
    print()
    show_snapmirror(cluster, headers_inc)
    print()
    snapmirror_uuid = input("Enter the UUID of the snapmirror to be deleted:-")

    dataobj = {}

    dataobj['uuid'] = snapmirror_uuid

    url = "https://{}/api/snapmirror/relationships".format(cluster)
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

def create_snapmirror(cluster: str, headers_inc: str):
    """ Create snapmirror"""
    print()
    print("The List of Snapmirror Relations")
    print("===============================")
    show_snapmirror(cluster, headers_inc)
    print()
    print("Please enter the following details:-")
    src_svm_name = input("Enter the Source SVM :-")
    src_vol_name = input("Enter the Source Volume :-")
    dst_svm_name = input("Enter the Destination SVM :-")
    dst_vol_name = input("Enter the Destination Volume :-")

    dataobj = {}
    src = src_svm_name + ":" + src_vol_name
    dst = dst_svm_name + ":" + dst_vol_name
    dataobj['source'] = {"path": src}
    dataobj['destination'] = {"path": dst}

    print(dataobj)

    url = "https://{}/api/snapmirror/relationships/".format(cluster)
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

def patch_snapmirror(cluster: str, headers_inc: str):
    """ Update SnapMirror"""
    print("=============================================")
    print()
    show_snapmirror(cluster, headers_inc)
    print()
    snapmirror_uuid = input("Enter the UUID of the snapmirror to be patched:-")

    dataobj = {}

    snapchoice = input(
        "What state update would you like? [snapmirrored/paused/broken_off/uninitialized/synchronizing] ")

    dataobj['state'] = snapchoice

    print(dataobj)

    url = "https://{}/api/snapmirror/relationships/{}".format(
        cluster, snapmirror_uuid)
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

def post_snapmirror_transfer(cluster: str, headers_inc: str):
    """Snapmirror Transfer"""
    print("=============================================")
    print()
    show_snapmirror(cluster, headers_inc)
    print()
    snapmirror_uuid = input(
        "Enter the UUID of the snapmirror to be updated/initialized:-")

    print("This would update or initialize the snapmirror relationship.")

    url = "https://{}/api/snapmirror/relationships/{}/transfers".format(
        cluster, snapmirror_uuid)
    try:
        response = requests.post(url, headers=headers_inc, verify=False)
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

def sm_ops(cluster: str, headers_inc: str):
    """Demonstrates SnapMirror Operations using REST APIs."""
    print("Demonstrates SnapMirror Operations using REST APIs.")
    print("==============================================================")
    print()
    snapmirrorbool = input(
        "What state Operation would you like? SnapMirror [show/create/update/delete/initialize] ")
    if snapmirrorbool == 'show':
        show_snapmirror(cluster, headers_inc)
    if snapmirrorbool == 'create':
        create_snapmirror(cluster, headers_inc)
    if snapmirrorbool == 'update':
        patch_snapmirror(cluster, headers_inc)
    if snapmirrorbool == 'delete':
        delete_snapmirror(cluster, headers_inc)
    if snapmirrorbool == 'initialize':
        post_snapmirror_transfer(cluster, headers_inc)

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will execute Snapmirror operations using ONTAP REST APIs.", )
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

    sm_ops(ARGS.cluster, headers)
    print("Script Complete")
