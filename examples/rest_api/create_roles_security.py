#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list legacy and rest-roles (RBAC) using ONTAP REST API.

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
from getpass import getpass
import logging
import texttable as tt
import requests
import urllib3 as ur
ur.disable_warnings()

def get_volumes(cluster: str, headers_inc: str):
    """Get Roles"""
    url = f"https://{cluster}/api/security/roles?fields=name,owner.name,scope"
    response = requests.get(url, headers=headers_inc, verify=False)
    return response.json()

def disp_vol(cluster: str, headers_inc: str):
    """Display Roles in a cluster"""
    ctr = 0
    tmp = dict(get_volumes(cluster, headers_inc))
    vols = tmp['records']
    tab = tt.Texttable()
    header = ['Owner name', 'Role name', 'Scope']
    tab.header(header)
    tab.set_cols_align(['c', 'c', 'c'])
    for volumelist in vols:
        ctr = ctr + 1
        vol = volumelist['owner']['name']
        vol_2 = volumelist['name']
        vol_3 = volumelist['scope']
        row = [vol, vol_2, vol_3]
        tab.add_row(row)
        tab.set_cols_align(['c', 'c', 'c'])
    print(f"Number of Roles: {ctr}")
    setdisplay = tab.draw()
    print(setdisplay)


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

    disp_vol(ARGS.cluster, headers)
