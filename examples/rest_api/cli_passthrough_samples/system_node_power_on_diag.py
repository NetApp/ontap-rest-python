#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies.
This script is not officially supported as a
standard NetApp product.

Purpose: This Module covers system_node_power_on_diag CLI usage using ONTAP REST API

Usage: system_node_power_on_diag.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
system_node_power_on_diag.py: the following arguments are required: -c/--cluster,
-u/--admin, -p/--password

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""

import sys
import base64
import argparse
from getpass import getpass
import logging
import requests
import urllib3 as ur
ur.disable_warnings()


def system_node_power_on(cluster: str, headers_inc: str):
    """Module to Turn on power nodes"""
    print(" \nModule 1 - System node power on")
    node_name = input("\nEnter the Node name to turn ON : ")

    dataobj = {
        'node': node_name
    }
    cli_endpoint = "api/private/cli/system/node/power/on"
    url = "https://{}/{}?privilege_level=diagnostic".format(
        cluster, cli_endpoint)
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
    else:
        print("\n Turned on node", node_name)


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""
    parser = argparse.ArgumentParser(
        description="This script creates,updates and deletes service-policy via cli passthrough")
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
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n THIS MODULE COVERS SYSTEM NODE POWER ON USAGE IN CLI PASSTHROUGH VIA ONTAP REST APIS")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    system_node_power_on(ARGS.cluster, headers)
