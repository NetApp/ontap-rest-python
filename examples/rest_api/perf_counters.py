#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list Perf counters for counter name volume using ONTAP REST API.

Usage: security_rbac.py [-h] -c CLUSTER [-u API_USER]
                       [-p API_PASS]

Copyright (c) 2022 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import base64
import argparse
import json
from getpass import getpass
import logging
import requests
import urllib3 as ur
ur.disable_warnings()


def get_volumes(cluster: str, headers_inc: str):
    """Get volume table details specifically"""
    url = f"https://{cluster}/api/cluster/counter/tables?name=volume&fields=*"
    response = requests.get(url, headers=headers_inc, verify=False)
    json_object = dict(response.json())
    s_data = json.dumps(json_object, indent=2)
    print(s_data)


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will list RBAC Roles in a cluster")
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
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",)
    ARGS = parse_args()
    BASE_64_STRING = base64.encodebytes(
        (f'{ARGS.api_user}:{ARGS.api_pass}').encode()).decode().replace(
        '\n', '')
    headers = {
        'authorization': f"Basic {BASE_64_STRING}",
        'content-type': "application/json",
        'accept': "application/json"
    }
    get_volumes(ARGS.cluster, headers)
