#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list all the aggregates in a cluster using ONTAP REST API.

usage:python3 list_aggregates.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import base64
import argparse
import logging
from getpass import getpass
import texttable as tt
import requests
requests.packages.urllib3.disable_warnings()


def get_aggr(cluster: str, headers_inc: str):
    """Get  Aggregates"""
    url = "https://{}/api/storage/aggregates".format(cluster)
    response = requests.get(url, headers=headers_inc, verify=False)
    return response.json()


def disp_aggr(cluster: str, headers_inc: str):
    ctr = 0
    tmp = dict(get_aggr(cluster, headers_inc))
    aggr = tmp['records']
    tab = tt.Texttable()
    header = ['Aggregate name']
    tab.header(header)
    tab.set_cols_align(['c'])
    for i in aggr:
        ctr = ctr + 1
        aggre = i['name']
        row = [aggre]
        tab.add_row(row)
        tab.set_cols_align(['c'])
    print("Number of Aggregates for the NetApp cluster:{}".format(ctr))
    setdisplay = tab.draw()
    print(setdisplay)


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will list aggregates.")
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
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

    disp_aggr(ARGS.cluster, headers)
