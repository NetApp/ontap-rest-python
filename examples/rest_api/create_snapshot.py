#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to create snapshot using ONTAP REST API.

usage: python3 create_snapshot.py [-h] -c CLUSTER -v VOLUME_NAME -s SNAPSHOT_NAME -vs SVM_NAME
                          [-u API_USER] [-p API_PASS]
create_snapshot.py: the following arguments are required: -c/--cluster, -v/--volume_name, -s/--snapshot_name -vs/--svm_name

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import base64
import argparse
from getpass import getpass
import logging
import requests
requests.packages.urllib3.disable_warnings()

def get_volumes(cluster: str, svm_name: str, headers_inc: str):
    """Get Volumes"""
    url = "https://{}/api/storage/volumes?svm.name={}".format(
        cluster, svm_name)
    response = requests.get(url, headers=headers_inc, verify=False)
    return response.json()


def get_key(cluster: str, svm_name: str, volume_name: str, headers_inc: str):
    """Get Key of the volumes"""
    tmp = dict(get_volumes(cluster, svm_name, headers_inc))
    vols = tmp['records']
    for i in vols:
        if i['name'] == volume_name:
            return i['uuid']


def check_job_status(
        cluster: str,
        job_status_url: str,
        job_status: str,
        headers_inc: str):
    """ Check job status"""
    if job_status['state'] == "failure":
        print(
            "Snapshot creation failed due to :{}".format(
                job_status['message']))
    elif job_status['state'] == "success":
        print("Snapshot created successfully")
    else:
        job_response = requests.get(
            job_status_url, headers=headers_inc, verify=False)
        job_status = job_response.json()
        check_job_status(
            cluster,
            job_status_url,
            job_status,
            headers_inc)

def make_snap(
        cluster: str,
        svm_name: str,
        volume_name: str,
        snapshot_name: str,
        headers_inc: str):
    """ Create Snapshot"""
    vol_uuid = get_key(cluster, svm_name, volume_name, headers_inc)

    data = {
        "name": snapshot_name
    }

    snap_api_url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)

    response = requests.post(snap_api_url, headers=headers_inc, json=data, verify=False)
    url_text = response.json()
    job_status_url = "https://{}/{}".format(cluster,
                                            url_text['job']['_links']['self']['href'])
    job_response = requests.get(job_status_url, headers=headers_inc, verify=False)
    job_status = job_response.json()
    check_job_status(
        cluster,
        job_status_url,
        job_status,
        headers_inc)

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will create a snapshot of a volume.",
    )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument(
        "-v",
        "--volume_name",
        required=True,
        help="Volume from which clone need to be created.")
    parser.add_argument(
        "-s", "--snapshot_name", required=True, help="Snapshot name"
    )
    parser.add_argument(
        "-vs", "--svm_name", required=True, help="Snapshot name"
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
    ARGS = parse_args()
    base64string = base64.encodestring(
        ('%s:%s' %
         (ARGS.api_user, ARGS.api_pass)).encode()).decode().replace('\n', '')

    headers = {
        'authorization': "Basic %s" % base64string,
        'content-type': "application/json",
        'accept': "application/json"
    }

    make_snap(
        ARGS.cluster,
        ARGS.svm_name,
        ARGS.volume_name,
        ARGS.snapshot_name,
        headers)
