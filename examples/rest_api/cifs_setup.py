#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS CIFS SETUP OPERATIONS USING REST API.

usage: python3 cifs_setup.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
from utils import Argument, parse_args, setup_logging, setup_connection, get_size, show_svm
requests.packages.urllib3.disable_warnings()


def cifs_setup(cluster: str, headers_inc: str):
    """This modules demonstartes CIFS setup"""
    print("Demonstrates CIFS setup.")
    print("========================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Choose the SVM on which you would like to create a CIFS Share :")
    print("Make sure that NAS  LIFs on each nodes are created on the SVM :")
    print()

    print("Enable CIFS Protocol:-")
    print("======================")

    fqdn = input("Input the Fully Qualified Domain Name :")
    organizational_unit = input("Input the Org Unit :")
    password = input("Input the Password :")
    user = input("Input the User :")

    payload1 = {
        "ad_domain": {
            "fqdn": fqdn,
            "organizational_unit": organizational_unit,
            "password": password,
            "user": user
        },
        "comment": "This CIFS Server",
        "enabled": bool("true"),
        "svm": {
            "name": svm_name
        },
        "name": "cifsserver"
    }

    url1 = "https://{}/api/protocols/cifs/services".format(cluster)
    try:
        response = requests.post(
            url1,
            headers=headers_inc,
            json=payload1,
            verify=False)
    except requests.exceptions.HTTPError as error:
        print(str(error))
        sys.exit(1)
    except requests.exceptions.RequestException as error:
        print(str(error))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
    print()
    print("Create the Volume:-")
    print("===================")
    vol_name = input("Enter the Volume Name to create CIFS Share:-")
    vol_size = input("Enter the Volume Size in MBs :-")
    aggr_name = input("Enter the aggregate name:-")
    v_size = get_size(vol_size)
    pather = "/" + vol_name
    payload2 = {
        "aggregates": [{"name": aggr_name}],
        "svm": {"name": svm_name},
        "name": vol_name,
        "size": v_size,
        "nas": {"security_style": "ntfs", "path": pather}
    }

    url2 = "https://{}/api/storage/volumes".format(cluster)
    try:
        response = requests.post(
            url2,
            headers=headers_inc,
            json=payload2,
            verify=False)
    except requests.exceptions.HTTPError as error:
        print(str(error))
        sys.exit(1)
    except requests.exceptions.RequestException as error:
        print(str(error))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    print()
    print("Create the Share:-")
    print("==================")
    share_name = input("Enter the share  name:-")
    payload3 = {
        "path": pather,
        "svm": {
            "name": svm_name,
        },
        "name": share_name
    }

    url3 = "https://{}/api/protocols/cifs/shares".format(cluster)
    try:
        response = requests.post(
            url3,
            headers=headers_inc,
            json=payload3,
            verify=False)
    except requests.exceptions.HTTPError as error:
        print(str(error))
        sys.exit(1)
    except requests.exceptions.RequestException as error:
        print(str(error))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates CIFS setup using REST API.", arguments,
        )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    cifs_setup(args.cluster, headers)


if __name__ == "__main__":
    main()
