#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies.
This script is not officially supported as a
standard NetApp product.

Purpose: This Module covers Storage Virtual Machine (SVM) disaster recovery via ONTAP REST API

Usage: svm_dr.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
svm_dr.py: the following arguments are required: -c/--cluster,
-u admin, -p/--password

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""
import time
import sys
import base64
import argparse
import logging
from getpass import getpass
import json
import requests
import urllib3 as ur
from utils import check_job_status
ur.disable_warnings()


def xdp_new_dest_svm(cluster: str, headers_inc: str):
    "Provision the destination SVM endpoint and create a SnapMirror relationship of type XDP."
    endpoint = "api/snapmirror/relationships"
    url = "https://{}/{}".format(
        cluster, endpoint)
    source_cluster = input(
        "\nEnter the Source Cluster name: ")
    source_svm = input(
        "\nEnter the Source SVM name: ")
    source_svm = source_svm + ':'
    des_svm = input(
        "\nEnter name for destination svm: ")
    des_svm = des_svm + ':'
    print(des_svm)
    print()
    dataobj = {
        "create_destination": {
            "enabled": "true"
        },
        "source": {
            "path": source_svm,
            "cluster": {
                "name": source_cluster
            }},
        "destination": {
            "path": des_svm
        },

        "policy": {
            "name": "Asynchronous"
        },
        "state": "snapmirrored"
    }
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
            verify=False)
        time.sleep(5)

    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
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
    job_status = job_response.json()
    check_job_status(job_status, headers_inc, cluster)
    json_formatted_str = json.dumps(url_text, indent=2)
    print(json_formatted_str)


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""
    parser = argparse.ArgumentParser(
        description="This script will list system fru-check command in CLI")
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
    BASE64STRING = base64.encodebytes(
        ('%s:%s' %
         (ARGS.api_user, ARGS.api_pass)).encode()).decode().replace('\n', '')
    headers = {
        'authorization': "Basic %s " % BASE64STRING,
        'content-type': "application/json",
        'accept': "application/json"
    }
    print("\n======================================================")
    print("SVM DISASTER RECOVERY with NEW DEST.SVM PROVISIONING")
    print("======================================================\n")
    xdp_new_dest_svm(ARGS.cluster, headers)
    print("\n==========END OF MODULE=============")
