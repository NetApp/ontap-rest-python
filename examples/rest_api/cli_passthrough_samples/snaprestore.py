#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies.
This script is not officially supported as a
standard NetApp product.

Purpose: This Module covers snap restore CLI command usage via ONTAP REST API

Usage: snaprestore.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
snaprestore.py: the following arguments are required: -c/--cluster,-u/--admin, -p/--password
Note: The direct API for snaprestore is available starting ONTAP 9.10.1 release

Copyright (c) 2022 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""
import base64
import argparse
import logging
from getpass import getpass
import requests
import urllib3 as ur
ur.disable_warnings()


def snaprestore(
        cluster: str,
        headers_inc: str):
    """ Module to restore snapshot"""
    print("\n===================================================================")
    print("\n Module snap restore file")
    vserver = input("Enter the svm name: ")
    vol_name = input("Enter the volume name: ")
    snap_name = input("Enter the snapshot name: ")
    path = input("Enter the path: ")
    dataobj = {
        'vserver': vserver,
        'volume': vol_name,
        'snapshot': snap_name,
        'path': path
    }
    url = "https://{}/api/private/cli/volume/snapshot/restore-file/".format(
        cluster)
    print("\n Passing input values:")
    print(dataobj)
    response = requests.post(
        url,
        headers=headers_inc,
        json=dataobj,
        verify=False)
    print(response)
    print("File Restored")


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""
    parser = argparse.ArgumentParser(
        description="Script to restore file using CLI passthrough via ONTAP REST Call")
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
    snaprestore(ARGS.cluster, headers)
    print("\n==========END OF MODULE=============")
