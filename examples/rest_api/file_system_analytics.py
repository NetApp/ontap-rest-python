#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS File System Analytics using ONTAP REST APIs

usage: python3 file_system_analytics.py [-h] -c CLUSTER [-u API_USER]
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
from utils import get_key_volumes, show_svm, show_volume
ur.disable_warnings()


def get_analytics_meta(cluster: str, headers_inc: str):
    """ To get File System Analytics information for a single directory"""
    print("=============================================")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM name:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volname = input(
        "Enter the name of the volume that needs to be modified:- ")
    path = input("Enter the Path: ")
    print()
    vol_uuid = get_key_volumes(svm_name, volname, cluster, headers_inc)
    print()
    url = "https://{}/api/storage/volumes/{}/files/{}?return_metadata=true".format(
        cluster, vol_uuid, path)
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
    vols = url_text['records']
    tab = tt.Texttable()
    header = [
        'Type',
        'creation_time',
        'inode_number',
        'is_junction']
    tab.header(header)
    tab.set_cols_align(['c', 'c', 'c', 'c'])
    ctr = 0
    for eventlist in vols:
        ctr = ctr + 1
        eve = eventlist['type']
        sev = eventlist['creation_time']
        har = eventlist['inode_number']
        per = eventlist['is_junction']
        row = [eve, sev, har, per]
        tab.set_cols_width([15, 30, 15, 15])
        tab.add_row(row)
        tab.set_cols_align(['c', 'i', 'c', 'c'])
    setdisplay = tab.draw()
    print(setdisplay)
    print("\nThe total no of directory is : ", ctr)


def get_analytics(cluster: str, headers_inc: str):
    """ To get file system details and permissions """
    print("=============================================")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM name:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volname = input(
        "Enter the name of the volume that needs to be modified:- ")
    path = input("Enter the Path: ")
    print()
    vol_uuid = get_key_volumes(svm_name, volname, cluster, headers_inc)
    print()
    url = "https://{}/api/storage/volumes/{}/files/{}?type=directory&fields=*&order_by=name".format(
        cluster, vol_uuid, path)
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
    vols = url_text['records']
    tab = tt.Texttable()
    header = [
        'Name',
        'Type',
        'changed_time',
        'Hard_links Count',
        'Unix Permission']
    tab.header(header)
    tab.set_cols_align(['c', 'c', 'c', 'c', 'c'])
    ctr = 0
    for eventlist in vols:
        ctr = ctr + 1
        vol = eventlist['name']
        eve = eventlist['type']
        sev = eventlist['changed_time']
        har = eventlist['hard_links_count']
        per = eventlist['unix_permissions']
        row = [vol, eve, sev, har, per]
        tab.set_cols_width([10, 15, 30, 15, 15])
        tab.add_row(row)
        tab.set_cols_align(['c', 'c', 'i', 'c', 'i'])
    setdisplay = tab.draw()
    print(setdisplay)
    print("\nThe total no of directory is : ", ctr)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates File System analytics using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)
    get_analytics(args.cluster, headers)
    get_analytics_meta(args.cluster, headers)


if __name__ == "__main__":
    main()
