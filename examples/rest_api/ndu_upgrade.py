#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies.
This script is not officially supported as a
standard NetApp product.

Purpose: This Module covers ndu upgrade via ONTAP REST API

Usage: ndu_upgrade.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
system_fru_check.py: the following arguments are required: -c/--cluster,
-u admin, -p/--password

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""
import sys
import base64
import argparse
import logging
import json
from getpass import getpass
import requests
import urllib3 as ur
from utils import check_job_status
ur.disable_warnings()


def get_system_update_details(cluster: str, headers_inc: str):
    "Get software update information"
    endpoint = "api/cluster/software"
    url = "https://{}/{}".format(
        cluster, endpoint)
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

    soft_dict = dict(response.json())
    #json_object = json.loads(url_text)
    json_formatted_str = json.dumps(url_text, indent=2)
    print(json_formatted_str)
    print("\n STATE OF UPGRADE  = %s " % soft_dict['state'])
    print("\n Short Summary Details \n \n %s" % soft_dict['update_details'])


def get_cluster_jobs(cluster: str, headers_inc: str):
    "update the ONTAP cluster software version"
    ontap_version = input(
        "Enter the ontap software version to upgrade to :  ")
    dataobj = {
        "version": ontap_version
    }
    print(dataobj)

    url = "https://{}/api/cluster/software?skip_warnings=true".format(cluster)
    try:
        response = requests.patch(
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
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message                                                                             )s",
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
    get_cluster_jobs(ARGS.cluster, headers)
    get_system_update_details(ARGS.cluster, headers)
    print("\n==========END OF MODULE=============")
