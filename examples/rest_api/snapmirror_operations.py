#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SNAPMIRROR OPERATIONS USING REST API.

usage: python3 snapmirror_operations.py [-h] -c CLUSTER [-u API_USER]
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
ur.disable_warnings()


def show_snapmirror(cluster: str, headers_inc: str):
    """ Show Snapmirror"""
    print()
    print("==========================")
    snap_api_url = "https://{}/api/snapmirror/relationships".format(cluster)
    try:
        response = requests.get(
            snap_api_url,
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

    snapmirrordict = dict(response.json())
    sms = snapmirrordict['records']
    print()
    print(" List of Snapmirror :- ")
    print("=======================")
    for smitem in sms:
        print(smitem['uuid'])
        snap_api_url1 = "https://{}/api/snapmirror/relationships/{}".format(
            cluster, smitem['uuid'])
        try:
            response1 = requests.get(
                snap_api_url1, headers=headers_inc, verify=False)
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

        smdict = dict(response1.json())
        print(smdict['source']['path'])
        print(smdict['destination']['path'])
        print(smdict['state'])
        print("------------------------------")


def specific_relationship(cluster: str, headers_inc: str):
    """ Show Snapmirror"""
    print()
    show_snapmirror(cluster, headers_inc)
    print()
    uuid = input("\n\n Enter a UUID from above list to get more details: ")
    specific_fields = "fields=healthy,transfer.total_duration,transfer.end_time,transfer.bytes_transferred,transfer.state"
    snap_api_url = "https://{}/api/snapmirror/relationships/{}?{}".format(
        cluster, uuid, specific_fields)
    try:
        response = requests.get(
            snap_api_url,
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

    smdict = dict(response.json())
    print("\n-------------------------------------------")
    print("Healthy status: ", smdict['healthy'])
    print("Transfer Total Duration: ", smdict['transfer']['total_duration'])
    print("Transfer End time: ", smdict['transfer']['end_time'])
    print("Bytes Transferred: ", smdict['transfer']['bytes_transferred'])
    print("Transfer State: ", smdict['transfer']['state'])
    print("---------------------------------------------")


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
    print("================================")
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
    print("================================")
    print()
    show_snapmirror(cluster, headers_inc)
    print()
    snapmirror_uuid = input("Enter the UUID of the snapmirror to be patched:-")

    dataobj = {}
    print("\nWhat state update would you like to perform?")
    snapchoice = input(
        "[snapmirrored/paused/broken_off/uninitialized/synchronizing] : ")

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
    """Snapmirror Intialize Transfer"""
    print("================================")
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
    print("Demonstrates SnapMirror Operations using REST APIs")
    print("===================================================")
    print("\nWhat Operation would you like in SnapMirror ")
    snapmirrorbool = input(
        "\n[list/create/update/delete/initialize/specifics]: ")
    if snapmirrorbool == 'list':
        show_snapmirror(cluster, headers_inc)
    if snapmirrorbool == 'create':
        create_snapmirror(cluster, headers_inc)
    if snapmirrorbool == 'update':
        patch_snapmirror(cluster, headers_inc)
    if snapmirrorbool == 'delete':
        delete_snapmirror(cluster, headers_inc)
    if snapmirrorbool == 'initialize':
        post_snapmirror_transfer(cluster, headers_inc)
    if snapmirrorbool == 'specifics':
        specific_relationship(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates SnapMirror Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    sm_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
