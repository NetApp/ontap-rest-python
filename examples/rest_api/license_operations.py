#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS LICENSE OPERATIONS USING REST API PCL

usage: python3 license_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""


import sys
import requests
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection
ur.disable_warnings()


def list_license(cluster: str, headers_inc: str) -> None:
    """Lists Volumes"""
    print()
    print("Getting License Details")
    print("======================")
    lic_api_url = "https://{}/api/cluster/licensing/licenses".format(
        cluster)
    try:
        response = requests.get(lic_api_url, headers=headers_inc, verify=False)
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

    licdict = dict(response.json())
    lics = licdict['records']
    print(" List of Licenses :- ")
    for lic in lics:
        print("=====")
        print("License Name = %s" % lic['name'])
        sn_api_url = "https://{}/api/cluster/licensing/licenses/{}".format(
            cluster, lic['name'])
        response1 = requests.get(sn_api_url, headers=headers_inc, verify=False)
        sndict = dict(response1.json())
        sns = sndict['licenses']
        for snitem in sns:
            print("License Serial Number = %s" % snitem['serial_number'])


def create_license(cluster: str, headers_inc: str) -> None:
    """Create license"""
    print()
    license_name = input(
        "Enter the License that needs to be added:- ")
    lic_obj = {
        "keys": [
            license_name
        ]
    }
    url = "https://{}/api/cluster/licensing/licenses".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=lic_obj,
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
    print("License set  successfully...")


def delete_license(cluster: str, headers_inc: str) -> None:
    """Delete License"""
    print()
    list_license(cluster, headers_inc)
    license_type = input(
        "which license would you like to delete:- ")
    lic_api_url = "https://{}/api/cluster/licensing/licenses".format(
        cluster)
    response = requests.get(lic_api_url, headers=headers_inc, verify=False)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    licdict = dict(response.json())
    lics = licdict['records']
    for lic in lics:
        if lic['name'] == license_type:
            sn_api_url = "https://{}/api/cluster/licensing/licenses/{}".format(
                cluster, lic['name'])
            response1 = requests.delete(
                sn_api_url, headers=headers_inc, verify=False)
            url_text = response1.json()
            if 'error' in url_text:
                print(url_text)
                sys.exit(1)
        else:
            print("The requested license could not be found.")
            sys.exit(1)


def license_ops(cluster, headers_inc) -> None:
    """License Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS LICENSE OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("====================================================================================")
    print()
    licbool = input(
        "What License Operation would you like to do? [list/create/delete] ")
    if licbool == 'list':
        list_license(cluster, headers_inc)
    if licbool == 'create':
        create_license(cluster, headers_inc)
    if licbool == 'delete':
        delete_license(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates License Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    license_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
