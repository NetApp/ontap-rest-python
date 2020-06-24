#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS QUOTA OPERATIONS USING REST API PCL

usage: python3 quota_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
from utils import Argument, parse_args, setup_logging, setup_connection, show_qtree, show_quotarule, show_svm, show_volume, get_key_svms, get_key_volumes
requests.packages.urllib3.disable_warnings()


def list_quotarule(cluster: str, headers_inc: str) -> None:
    """Lists Quota Rule"""
    print()
    print("Getting Quota Rule Details")
    print("==========================")
    # https://10.195.51.149:443/api/storage/quota/rules
    qr_api_url = "https://{}/api/storage/quota/rules".format(
        cluster)
    try:
        response = requests.get(qr_api_url, headers=headers_inc, verify=False)
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

    qrdict = dict(response.json())
    quotas = qrdict['records']
    print(" List of Quota Rules :- ")
    for quota in quotas:
        print("=====")
        print("Quota Volume Name = %s" % quota['volume']['name'])
        print("Quota UUID = %s" % quota['uuid'])


def create_quotarule(cluster: str, headers_inc: str) -> None:
    """Create Quota Rule """
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the Volume on which the Quotas needs to be created:-")
    print()
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    dataobj = {}
    tmp1 = {"name": svm_name}
    dataobj['svm'] = tmp1
    tmp2 = {"name": volume_name}
    dataobj['volume'] = tmp2
    quota_type = input(
        "Enter the Quota Type [qtree/users/group]:-")
    if quota_type == 'qtree':
        show_qtree(svm_name, volume_name, cluster, headers_inc)
        qtree_name = input(
            "Enter the Qtree on which the Quota needs to be applied:-")
        tmp3 = {"name": qtree_name}
        dataobj['qtree'] = tmp3
        dataobj['type'] = "tree"
    if quota_type == 'users':
        dataobj['type'] = user
        dataobj['user_mapping'] = False
        tmp3 = []
        dataobj['users'] = tmp3
    if quota_type == 'group':
        dataobj['type'] = group
        dataobj['group'] = {}
    spahali = input(
        "Enter the Space Hard-Limit:- ")
    spasoli = input(
        "Enter the Space Soft-Limit:- ")
    fihali = input(
        "Enter the File Hard-Limit:- ")
    fisoli = input(
        "Enter the File Soft-Limit:- ")
    tmp4 = {"hard_limit": spahali, "soft_limit": spasoli}
    dataobj['space'] = tmp4
    tmp5 = {"hard_limit": fihali, "soft_limit": fisoli}
    dataobj['files'] = tmp5
    print(dataobj)
    url = "https://{}/api/storage/quota/rules".format(cluster)
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

    print("Quota created successfully...")


def patch_quotarule(cluster: str, headers_inc: str) -> None:
    """Update Quota"""
    print()
    show_quotarule(cluster, headers_inc)
    quota_uuid = input("Enter the UUID of the Quota to be updated :- ")
    spahali = input(
        "Enter the Space Hard-Limit:- ")
    spasoli = input(
        "Enter the Space Soft-Limit:- ")
    fihali = input(
        "Enter the File Hard-Limit:- ")
    fisoli = input(
        "Enter the File Soft-Limit:- ")
    dataobj = {}
    tmp4 = {"hard_limit": spahali, "soft_limit": spasoli}
    dataobj['space'] = tmp4
    tmp5 = {"hard_limit": fihali, "soft_limit": fisoli}
    dataobj['files'] = tmp5
    print(dataobj)
    url = "https://{}/api/storage/quota/rules/{}".format(cluster, quota_uuid)
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

    print("Quota updated successfully...")


def delete_quotarule(cluster: str, headers_inc: str) -> None:
    """Delete Quota"""
    print("=============================================")
    print()
    show_quotarule(cluster, headers_inc)
    quota_uuid = input("Enter the UUID of the Quota to be deleted :- ")
    url = "https://{}/api/storage/quota/rules/{}".format(cluster, quota_uuid)
    try:
        response = requests.delete(
            url,
            headers=headers_inc,
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
    print("Quota deleted successfully...")


def qr_ops(cluster, headers_inc) -> None:
    """Quota-Rule Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS QUOTA OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("====================================================================================")
    print()
    volumebool = input(
        "What Quota Operation would you like to do? [list/create/update/delete] ")
    if volumebool == 'list':
        list_quotarule(cluster, headers_inc)
    if volumebool == 'create':
        create_quotarule(cluster, headers_inc)
    if volumebool == 'update':
        patch_quotarule(cluster, headers_inc)
    if volumebool == 'delete':
        delete_quotarule(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Quota Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    qr_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
