#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SNAPSHOT OPERATIONS USING REST API.

usage: python3 svm_operations.py [-h] -c CLUSTER [-u API_USER]
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
from utils import get_key_snapshot, get_key_volumes, show_svm, show_volume, show_snapshot
ur.disable_warnings()


def list_snapshot(cluster: str, headers_inc: str):
    """ list snapshot"""
    print("=============================================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input("Enter the required SVM :-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input("Enter the Volume to list the snapshots :-")
    print()
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)

    print()
    print("Getting Snapshot Details")
    print("========================")
    snap_api_url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
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
    snapshotsdict = dict(response.json())
    snapshots = snapshotsdict['records']
    print()
    for snapshot in snapshots:
        print("Snapshot Name:-%s Snapshot UUID:-%s" %
              (snapshot['name'], snapshot['uuid']))


def delete_snapshot(cluster: str, headers_inc: str):
    """ snapshot delete"""
    print("=============================================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input("Enter the required SVM :-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input("Enter the Volume to list the snapshots :-")
    print()
    show_snapshot(svm_name, volume_name, cluster, headers_inc)
    print()
    snapshot_name = input("Enter the Snapshot to be deleted :-")
    print()
    snapshot_uuid = get_key_snapshot(
        svm_name,
        volume_name,
        snapshot_name,
        cluster,
        headers_inc)
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    urlpath = "https://{}/api/storage/volumes/" + \
        vol_uuid + "/snapshots/" + snapshot_uuid
    url = urlpath.format(cluster)
    try:
        response = requests.delete(url, headers=headers_inc, verify=False)
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


def create_snapshot(cluster: str, headers_inc: str):
    """ create snapshot"""
    print("=============================================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input("Enter the required SVM :-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the Volume on which the snapshot need to be created:-")
    print()
    show_snapshot(svm_name, volume_name, cluster, headers_inc)
    print()
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    snapshot_name = input("Enter the name of the Snapshot to be created:- ")
    print()
    dataobj = {}
    dataobj['name'] = snapshot_name
    # dataobj['volume.uuid']=vol_uuid
    print(dataobj)
    url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
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


def patch_snapshot(cluster: str, headers_inc: str):
    "update snapshot"
    print("=============================================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input("Enter the required SVM :-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input("Enter the Volume to list the snapshots :-")
    print()
    show_snapshot(svm_name, volume_name, cluster, headers_inc)
    print()
    snapshot_name = input("Enter the Snapshot to be Updated :-")
    print()
    snapshot_uuid = get_key_snapshot(
        svm_name,
        volume_name,
        snapshot_name,
        cluster,
        headers_inc)
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)

    dataobj = {}
    snapbool = input("Would you like to update the name (y/n):- ")
    if snapbool == 'y':
        snapname = input("Enter the new name of the snapshot to be updated:-")
        dataobj['name'] = snapname
    combool = input("Would you like to update the comment (y/n):- ")
    if combool == 'y':
        snapcom = input("Enter the comment of the snapshot to be updated:-")
        dataobj['comment'] = snapcom
    expirybool = input("Would you like to update the Expiry Date (y/n):- ")
    if expirybool == 'y':
        snapexpiry = input(
            "Enter the expiry date of the snapshot to be updated (format:- 2019-02-04T19:00:00Z):-")
        dataobj['expiry_time'] = snapexpiry
    print(dataobj)
    print()
    urlpath = "https://{}/api/storage/volumes/" + \
        vol_uuid + "/snapshots/" + snapshot_uuid
    url = urlpath.format(cluster)
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


def snapshot_ops(cluster: str, headers_inc: str):
    """Demonstrates SnapShot Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS SNAPSHOT OPERATIONS USING REST API.")
    print("==================================================================")
    print()
    snapshotbool = input(
        "What Snapshot Operation would you like to do? [list/create/update/delete] ")
    if snapshotbool == 'list':
        list_snapshot(cluster, headers_inc)
    if snapshotbool == 'create':
        create_snapshot(cluster, headers_inc)
    if snapshotbool == 'update':
        patch_snapshot(cluster, headers_inc)
    if snapshotbool == 'delete':
        delete_snapshot(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Snapshot Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    snapshot_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
