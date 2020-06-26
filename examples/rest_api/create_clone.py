#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to create a clone using ONTAP REST API.

usage: python3 create_clone.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -s
                       SNAPSHOT_NAME -cn CLONE_NAME  [-u API_USER]
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
from getpass import getpass
import logging
import requests

requests.packages.urllib3.disable_warnings()


def get_key_vol(cluster: str, volume_name: str, headers_inc: str):
    """Get volume key"""
    tmp = dict(get_vols(cluster, headers_inc))
    vols = tmp['records']
    for i in vols:
        if i['name'] == volume_name:
            return i['uuid']


def get_vols(cluster: str, headers_inc: str):
    """Get Volumes"""
    url = "https://{}/api/storage/volumes/".format(cluster)
    response = requests.get(url, headers=headers_inc, verify=False)
    return response.json()


def check_job_status(cluster: str, job_status, headers_inc: str):
    """Check Job Status"""
    if job_status['state'] == "failure":
        print("Clone creation failed due to :{}".format(job_status['message']))
    elif job_status['state'] == "success":
        print("Clone created successfully")
    else:
        print("Clone creation in process...")
        time.sleep(2)
        url_text = '/api/cluster/jobs/' + job_status['uuid']
        job_status = "https://{}/{}".format(cluster, url_text)
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
        job_status = job_response.json()
        check_job_status(cluster, job_status, headers_inc)


def make_clone(
        cluster: str,
        volume_name: str,
        svm_name: str,
        snapshot_name: str,
        clone_name: str,
        headers_inc: str):
    """Create clone"""
    url = "https://{}/api/storage/volumes".format(cluster)
    payload = {
        "svm.name": svm_name,
        "clone.is_flexclone": "true",
        "clone.parent_snapshot.name": snapshot_name,
        "clone.parent_volume.name": volume_name,
        "name": clone_name
    }

    response = requests.post(
        url,
        headers=headers_inc,
        json=payload,
        verify=False)
    url_text = response.json()
    job_status = "https://{}/{}".format(cluster,
                                        url_text['job']['_links']['self']['href'])
    job_response = requests.get(job_status, headers=headers_inc, verify=False)
    job_status = job_response.json()
    check_job_status(cluster, job_status, headers_inc)


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will create a clone of the volume in an SVM.")
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument(
        "-v",
        "--volume_name",
        required=True,
        help="Volume from which clone need to be created.")
    parser.add_argument(
        "-vs", "--svm_name", required=True, help="SVM to create the Clone from"
    )
    parser.add_argument(
        "-s", "--snapshot_name", required=True, help="Snapshot name"
    )
    parser.add_argument(
        "-cn", "--clone_name", required=True, help="Clone name"
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

    make_clone(
        ARGS.cluster,
        ARGS.volume_name,
        ARGS.svm_name,
        ARGS.snapshot_name,
        ARGS.clone_name,
        headers)
