#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS CONSISTENCY GROUPS CREATION
WITH EXISTING VOLUMES AND SNAPSHOT CREATION USING REST API.

usage: python3 consistency_groups.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2021 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import sys
import requests
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection, show_svm, get_key_svms
ur.disable_warnings()


def get_key_cg(
        cg_name: str,
        cluster: str,
        headers_inc: str):
    """ Get CG Key"""
    snap_api_url = "https://{}/api/application/consistency-groups".format(
        cluster)

    try:
        job_response = requests.get(
            snap_api_url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    snapshotsdict = dict(job_response.json())
    snapshots = snapshotsdict['records']
    print()
    print("The UUID of the CG is ")
    for snapshot in snapshots:
        if snapshot['name'] == cg_name:
            print(snapshot['uuid'])
        return snapshot['uuid']


def create_cg_snapshot(cg_key: str, cluster: str, headers_inc: str):
    """ create consistency group snapshot"""
    print()
    print("Create Consistency Groups snapshot")
    print("==================================================")
    print("\nPlease enter the following details:-")
    snap_name = input("enter the snapshot name:  ")
    type_s = input("enter the snapshot type(app/crash):  ")
    snap_label = input("enter the snapmirror_label")
    dataobj = {
        "comment": "this is a sample script",
        "name": snap_name,
        "consistency_type": type_s,
        "snapmirror_label": snap_label
    }
    print(dataobj)
    url = "https://{}/api/application/consistency-groups/{}/snapshots".format(
        cluster, cg_key)
    print(url)
    response = requests.post(
        url,
        headers=headers_inc,
        json=dataobj,
        verify=False)
    url_text = response.json()
    print(url_text)
    print("snapshot created successfully")


def check_job_status(cluster: str, job_status: str, headers_inc: str):
    """ Check job status"""
    if job_status['state'] == "failure":
        print(
            "\n\nConsistency Group creation failed due to :{}".format(
                job_status['message']))
    elif job_status['state'] == "success":
        print("\n\nConsistency Group created successfully")
    else:
        job_status_url = "https://{}/api/cluster/jobs/{}".format(
            cluster, job_status['uuid'])
        job_response = requests.get(
            job_status_url, headers=headers_inc, verify=False)
        job_status = job_response.json()
        check_job_status(cluster, job_status, headers_inc)


def create_consistency(cluster: str, headers_inc: str):
    """Create Consistency Groups with existing volumes"""
    print()
    print("Create Consistency Groups with existing volumes")
    print("==================================================")
    print("\nPlease enter the following details:-")
    cg_name = input("\n\nEnter the Consistency Group name :-")
    show_svm(cluster, headers_inc)
    src_svm_name = input("\nEnter the SVM :-")
    key_svm = get_key_svms(src_svm_name, cluster, headers_inc)
    count = int(input("enter the no of volumes to input: "))
    vol = []
    for i in range(0, count):
        src_vol_name = input("\n Enter the existing volumes names to add: ")
        vol.append(src_vol_name)
    print(vol)
    policy = input("\nEnter the snapshot policy names:-")
    dataobj = {
        "svm": {
            "uuid": key_svm
        },
        "name": cg_name,
        "snapshot_policy":
        {
            "name": policy
        }
    }
    dataobj["volumes"] = []
    for i in range(0, count):
        tmp = {
            "name": vol[i],
            "provisioning_options": {
                "action": "add"
            }
        }
        dataobj["volumes"].append(tmp)
    print(dataobj)
    url = "https://{}/api/application/consistency-groups".format(cluster)
    response = requests.post(
        url,
        headers=headers_inc,
        json=dataobj,
        verify=False)
    url_text = response.json()
    job_status = "https://{}/{}".format(cluster,
                                        url_text['job']['_links']['self']['href'])
    job_response = requests.get(job_status, headers=headers_inc, verify=False)
    job_status = job_response.json()
    check_job_status(cluster, job_status, headers_inc)
    key_cg = get_key_cg(cg_name, cluster, headers_inc)
    create_cg_snapshot(key_cg, cluster, headers_inc)


def sm_ops(cluster: str, headers_inc: str):
    """Demonstrates Consistency Groups using REST APIs."""

    print("===================================================")
    create_consistency(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Consistency Groups(CG) and CG snapshot creation using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    sm_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
