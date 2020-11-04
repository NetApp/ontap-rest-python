#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies.
This script is not officially supported as a
standard NetApp product.

Purpose: This Module covers network/interface/service-policy/ CLI usage using ONTAP REST API

Usage: service_policy.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
service_policy.py: the following arguments are required: -c/--cluster, -u/--admin, -p/--password

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

def create_service_policy(cluster: str, headers_inc: str):
    """Module to create service policy"""
    print(" \nModule 1 - Create Service Policy")
    vserver = input("\n Enter the svm name: ")
    policy_name = input(" Enter the new policy name: ")
    services_name = []
    number = int(input(" Enter the no of services you want to input: "))
    for number in range(0, number):
        services = input(" Enter the services name(e.g: data-cifs): ")
        services_name.append(services)
    print("\nList is - ", services_name)
    allowed_addresses = []
    number = int(input(" Enter the no of addresses you want to input: "))
    for number in range(0, number):
        addresses = input(" Enter the address name : ")
        allowed_addresses.append(addresses)
    print("\nList is - ", allowed_addresses)

    dataobj = {
        'vserver': vserver,
        'policy': policy_name,
        'services': services_name,
        'allowed_addresses': allowed_addresses
    }
    cli_endpoint = "network/interface/service-policy/"
    url = "https://{}/api/private/cli/{}?privilege_level=diagnostic".format(
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
        print("\n Created Service Policy successfully\n")


def modify_service_policy(cluster: str, headers_inc: str):
    """Module to modify the existing service policy"""
    print(" \nModule 2 - Modify Service Policy")
    vserver = input("\n Enter the svm name : ")
    policy_name = input(" Enter the existing service policy name: ")
    service_name = input(" Enter the service name: ")
    allowed_addresses = []
    number = int(input(" Enter the no of addresses you want to input: "))
    for number in range(0, number):
        addresses = input(" Enter the address name : ")
        allowed_addresses.append(addresses)
    print("\n   List is - ", allowed_addresses)
    print("\n Updating..........\n")
    dataobj = {
        'vserver': vserver,
        'policy': policy_name,
        'service': service_name,
        'allowed_addresses': allowed_addresses
    }
    cli_endpoint = "network/interface/service-policy/modify-service"
    url = "https://{}/api/private/cli/{}?privilege_level=diagnostic".format(
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
        print("\n Updated Service Policy successfully\n")


def add_service_policy(cluster: str, headers_inc: str):
    """Module to modify the existing service policy"""
    print("\nModule 2 - Add an additional service entry to an existing service policy")
    vserver = input("\n Enter the svm name : ")
    policy_name = input(" Enter the existing service policy name: ")
    service_name = input(" Enter the service name: ")
    allowed_addresses = []
    number = int(input(" Enter the no of addresses you want to input: "))
    for number in range(0, number):
        addresses = input(" Enter the address name : ")
        allowed_addresses.append(addresses)
    print("\n   List is - ", allowed_addresses)
    print("\n Updating..........\n")
    dataobj = {
        'vserver': vserver,
        'policy': policy_name,
        'service': service_name,
        'allowed_addresses': allowed_addresses
    }
    cli_endpoint = "network/interface/service-policy/add-service"
    url = "https://{}/api/private/cli/{}?privilege_level=diagnostic".format(
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
        print("\n Updated Service Policy successfully\n")

def delete_service_policy(cluster: str, headers_inc: str):
    """Module to delete the existing service policy"""
    print(" \n Module 3 - Delete Service Policy")
    vserver = input("\n Enter the svm name : ")
    policy_name = input(" Enter the existing service policy name to delete: ")
    print("\n Deleting...........\n")
    dataobj = {
        'vserver': vserver,
        'policy': policy_name
    }
    cli_endpoint = "network/interface/service-policy/"
    url = "https://{}/api/private/cli/{}?privilege_level=diagnostic".format(
        cluster, cli_endpoint)
    try:
        response = requests.delete(
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
        print("\n Deleted Service Policy successfully\n")


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
    print("\n THIS MODULE COVERS SERVICE-POLICY USAGE IN CLI PASSTHROUGH VIA ONTAP REST APIS")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    create_service_policy(ARGS.cluster, headers)
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    modify_service_policy(ARGS.cluster, headers)
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    add_service_policy(ARGS.cluster, headers)
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    delete_service_policy(ARGS.cluster, headers)
    print("\n===============================END OF MODULE====================================")
    