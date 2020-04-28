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
import time
import base64
import argparse
import logging
from getpass import getpass
import requests
requests.packages.urllib3.disable_warnings()

def get_snapshots(cluster: str, headers_inc: str, vol_uuid: str):
    """ get snapshot json"""
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
    """ get snapshot key"""
    print()
    tmp = dict(get_snapshots(vol_uuid, cluster, headers_inc))
    snap = tmp['records']
    print()
    print("The UUID of the Snapshot is ")
    for i in snap:
        if i['name'] == snapshot_name:
            print(i['uuid'])
            return i['uuid']

def get_volumes(cluster: str, headers_inc: str):
    """ get volume json"""
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
    """ get volume key"""
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
    """ get svm"""
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

def get_key_svms(cluster: str, svm_name: str, headers_inc: str):
    """ get svm key"""
    tmp = dict(get_svms(cluster, headers_inc))
    svms = tmp['records']
    print("The UUID of the SVM is ")
    for i in svms:
        if (i['name']) == svm_name:
            print(i['uuid'])
            return i['uuid']

def show_svm(cluster: str, headers_inc: str):
    """ list the svm"""
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
    """ list the volumes"""
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
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tmp = dict(response.json())
    svms = tmp['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for i in svms:
        print(i['name'])
    return response.json()

def show_snapshot(cluster: str, headers_inc: str):
    """ list snapshot"""
    show_volume(cluster, headers_inc)
    print()
    vol_name = input(
        "Enter the Volume from which the Snapshot need to be listed:-")
    vol_uuid = get_key_volumes(vol_name, cluster, headers_inc)
    print()
    print("Getting Snapshot Details")
    print("========================")
    snap_api_url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
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
    snaps = tmp['records']
    print()
    for i in snaps:
        print("Snapshot Name:-%s Snapshot UUID:-%s" % (i['name'], i['uuid']))

def check_job_status(job_status: str, cluster: str, headers_inc: str):
    """Check job status"""
    if job_status['state'] == "failure":
        if job_status['code'] == 460770:
            print("SVM Already Exists")
        else:
            print("Operation failed due to :{}".format(job_status['message']))
    elif job_status['state'] == "success":
        print("Operation completed successfully.")
    else:
        job_status_url = "https://{}/api/cluster/jobs/{}".format(
            cluster, job_status['uuid'])
        try:
            job_response = requests.get(
                job_status, headers=headers_inc, verify=False)
        except requests.exceptions.HTTPError as err:
            print(str(err))
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print(str(err))
            sys.exit(1)
        job_status = job_response.json()
        time.sleep(5)
        check_job_status(job_status, cluster, headers_inc)

def delete_snapshot(cluster: str, headers_inc: str):
    """ snapshot delete"""
    print("=============================================")
    print()
    show_snapshot(cluster, headers_inc)
    print()
    vol_uuid = input("Enter the UUID of the Volume  to be updated [UUID]:-")
    snapshot_uuid = input(
        "Enter the UUID of the snapshot to be Deleted [UUID]:-")
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
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(job_status, headers=headers_inc, verify=False)
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
    job_status = job_response.json()
    check_job_status(job_status, cluster, headers_inc)

def create_snapshot(cluster: str, headers_inc: str):
    """ create snapshot"""
    print()
    show_volume(cluster, headers_inc)
    print()
    vol_name = input(
        "Enter the name of the Volume on which the snapshot needs to be created:- ")
    vol_uuid = get_key_volumes(vol_name, cluster, headers_inc)
    snapshot_name = input("Enter the name of the Snapshot to be created:- ")
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
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(job_status, headers=headers_inc, verify=False)
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
    job_status = job_response.json()
    check_job_status(job_status, cluster, headers_inc)

def patch_snapshot(cluster: str, headers_inc: str):
    "update snapshot"
    print("=============================================")
    print()
    show_snapshot(cluster, headers_inc)
    print()
    vol_uuid = input("Enter the UUID of the Volume  to be updated [UUID]:-")
    snapshot_uuid = input(
        "Enter the UUID of the snapshot to be updated [UUID]:-")
    dataobj = {}
    snapbool = input("Would you like to update the name (y/n):- ")
    if snapbool == 'y':
        snapname = input("Enter the new name of the snapshot to be updated:-")
        dataobj['name'] = snapname
    combool = input("Would you like to update the comment (y/n):- ")
    if combool == 'y':
        snapcom = input("Enter the comment of the snapshot to be updated:-")
        dataobj['name'] = snapcom
    expirybool = input("Would you like to update the Expiry Date (y/n):- ")
    if expirybool == 'y':
        snapexpiry = input(
            "Enter the expiry date of the snapshot to be updated (format:- 2019-02-04T19:00:00Z):-")
        dataobj['expiry_time'] = snapname
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
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(job_status, headers=headers_inc, verify=False)
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
    job_status = job_response.json()
    check_job_status(job_status, cluster, headers_inc)

def snapshot_ops(cluster: str, headers_inc: str):
    """Demonstrates SnapShot Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS SNAPSHOT OPERATIONS USING REST API.")
    print("==================================================================")
    print()
    snapshotbool = input(
        "What Snapshot Operation would you like to do? [show/create/update/delete] ")
    if snapshotbool == 'show':
        show_snapshot(cluster, headers_inc)
    if snapshotbool == 'create':
        create_snapshot(cluster, headers_inc)
    if snapshotbool == 'update':
        patch_snapshot(cluster, headers_inc)
    if snapshotbool == 'delete':
        delete_snapshot(cluster, headers_inc)

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="THE FOLLOWING SCRIPT SHOWS SNAPSHOT OPERATIONS USING REST API.", )
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

    snapshot_ops(ARGS.cluster, headers)
    print("Script Complete")
