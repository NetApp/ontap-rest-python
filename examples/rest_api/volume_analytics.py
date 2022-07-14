#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME ANALYTICS using ONTAP REST APIs

usage: python3 volume_analytics.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import sys
import json
import requests
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import get_key_volumes, show_svm, show_volume
ur.disable_warnings()


def get_analytics_users(cluster: str, headers_inc: str, vol_uuid: str):
    """Module to list top users in a volume"""
    url = "https://{}/api/storage/volumes/{}/top-metrics/users?top_metric=throughput.write".format(
        cluster, vol_uuid)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
        print(response)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = dict(response.json())
    if 'error' in url_text:
        print(url_text)
    json_formatted_str = json.dumps(url_text, indent=2)
    print("To get Top users in volume with high write Throughput ")
    print(json_formatted_str)


def get_analytics_files(cluster: str, headers_inc: str, vol_uuid: str):
    """Module to list top files in a volume"""
    url = "https://{}/api/storage/volumes/{}/top-metrics/files?top_metric=throughput.write".format(
        cluster, vol_uuid)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
        print(response)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = dict(response.json())
    if 'error' in url_text:
        print(url_text)
    json_formatted_str = json.dumps(url_text, indent=2)
    print("To get Top files in volume with high write Throughput ")
    print(json_formatted_str)
    get_analytics_users(cluster, headers_inc, vol_uuid)


def get_analytics_directories(cluster: str, headers_inc: str):
    """ To get Analytices of Top Directories in a volume """
    print("=============================================")
    print("To get file system details and permissions ")
    print("=============================================")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM name:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volname = input(
        "Enter the name of the volume name to fetch Analytics:- ")
    print()
    vol_uuid = get_key_volumes(svm_name, volname, cluster, headers_inc)
    print()
    url = "https://{}/api/storage/volumes/{}/top-metrics/directories?top_metric=throughput.write".format(
        cluster, vol_uuid)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
        print(response)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = dict(response.json())
    if 'error' in url_text:
        print(url_text)
    json_formatted_str = json.dumps(url_text, indent=2)
    print("To get Top directories in volume with high write Throughput ")
    print(json_formatted_str)
    get_analytics_files(cluster, headers_inc, vol_uuid)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Volume analytics using ONTAP REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)
    get_analytics_directories(args.cluster, headers)


if __name__ == "__main__":
    main()
