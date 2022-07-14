#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS WORKFLOW OF QTREE, QUOTA CREATION, Show METRICS of QTREE

usage: python3 qtree_quota_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
import texttable as tt
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import show_qtree, show_svm, show_volume, get_key_volumes
ur.disable_warnings()


def list_quotarule(cluster: str, headers_inc: str) -> None:
    """Lists Quota Rule"""
    print("\nGetting Quota Rule Details")
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


def create_qtree(cluster: str, headers_inc: str):
    """ Create Qtree"""
    print("\nThe List of SVMs")
    show_svm(cluster, headers_inc)
    svm_name = input(
        "\nEnter the SVM Name on which the qtree need to be created: ")
    show_volume(cluster, headers_inc, svm_name)
    volume_name = input(
        "\nEnter the Volume Name on which the Qtree need to be created: ")
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    print()
    qtree_name = input("Enter the name of the Qtree to be created:-")

    dataobj = {
        "name": qtree_name,
        "volume.uuid": vol_uuid,
        "svm.name": svm_name
    }

    print(dataobj)

    url = "https://{}/api/storage/qtrees".format(cluster)
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

    url_text = response.json()
    print(
        "\n Qtree {} created successfully under Volume {}".format(
            qtree_name,
            volume_name))


def create_quotarule(cluster: str, headers_inc: str) -> None:
    """Create Quota Rule """
    show_svm(cluster, headers_inc)
    svm_name = input(
        "\nEnter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    volume_name = input(
        "\nEnter the Volume on which the Quotas needs to be created:-")
    print()
    get_key_volumes(svm_name, volume_name, cluster, headers_inc)
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
        dataobj['type'] = "user"
        dataobj['user_mapping'] = False
        tmp3 = []
        dataobj['users'] = tmp3
    if quota_type == 'group':
        dataobj['type'] = "group"
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
    print("\n............Quota created successfully............\n")


def get_qtree_metrics(cluster: str, headers_inc: str):
    "Get Policy name in all vserver"
    show_svm(cluster, headers_inc)
    svm_name = input(
        "\nEnter the SVM Name:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the Volume Name on which the Qtree resides:-")
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    print()
    show_qtree(svm_name, volume_name, cluster, headers_inc)
    qtree_id = input("\nEnter the Qtree ID: ")
    url = "https://{}/api/storage/qtrees/{}/{}".format(
        cluster, vol_uuid, qtree_id)
    print()
    print(url)
    print()
    response = requests.get(url, headers=headers_inc, verify=False)
    return response.json()


def get_texttable(cluster: str, headers_inc: str):
    "Display events call output"
    vols = get_qtree_metrics(cluster, headers_inc)
    tab = tt.Texttable()
    header = [
        'Timestamp',
        'IOPS.Read',
        'IOPS.Write',
        'IOPS.Other',
        'IOPS.Total']
    tab.header(header)
    tab.set_cols_align(['c', 'c', 'c', 'c', 'c'])
    print()
    vol_name = vols['volume']['name']
    path = vols['path']
    status = vols['statistics']['status']
    print("\nVolume name: ", vol_name)
    print("\nPath name  : ", path)
    print("\nStatus     : ", status)
    print("\nPerformance data in IOPS\n")
    timestamp = vols['statistics']['timestamp']
    iops_read = vols['statistics']['iops_raw']['read']
    iops_write = vols['statistics']['iops_raw']['write']
    iops_other = vols['statistics']['iops_raw']['other']
    iops_total = vols['statistics']['iops_raw']['total']
    row = [timestamp, iops_read, iops_write, iops_other, iops_total]
    tab.set_cols_width([10, 10, 10, 10, 10])
    tab.add_row(row)
    tab.set_cols_align(['c', 'c', 'c', 'c', 'c'])
    setdisplay = tab.draw()
    print(setdisplay)
    tab2 = tt.Texttable()

    print("\nPerformance data in Throughput\n")
    header2 = [
        'Timestamp',
        'Throughput.Read',
        'Throughput.Write',
        'Throughput.Other',
        'Throughput.Total']
    tab2.header(header2)
    tab2.set_cols_align(['c', 'c', 'c', 'c', 'c'])
    thr_read = vols['statistics']['throughput_raw']['read']
    thr_write = vols['statistics']['throughput_raw']['write']
    thr_others = vols['statistics']['throughput_raw']['other']
    thr_total = vols['statistics']['throughput_raw']['total']
    row1 = [timestamp, thr_read, thr_write, thr_others, thr_total]
    tab2.set_cols_width([10, 10, 10, 10, 10])
    tab2.add_row(row1)
    tab2.set_cols_align(['c', 'c', 'c', 'c', 'c'])
    setdisplay = tab2.draw()
    print(setdisplay)


def qr_ops(cluster, headers_inc) -> None:
    """Quota-Rule Operations"""
    loop = 'y'
    while loop == 'y':
        print("==================================================================================")
        print("\n1) Creation of Qtree \n2) Enable Quota and \n3) Show Metrics for Qtree")
        print("==================================================================================")
        volumebool = input(
            "\n Which operation would you like to do [e.g. 1,2,3]?: ")
        if volumebool == '1':
            create_qtree(cluster, headers_inc)
        if volumebool == '2':
            create_quotarule(cluster, headers_inc)
        if volumebool == '3':
            get_texttable(cluster, headers_inc)
        loop = input("\n To continue press 'y' to exit press 'n':")
    print("\n")


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Qtree, Quota, Metrics workflow using REST API.",
        arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    qr_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
