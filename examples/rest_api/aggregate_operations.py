#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS AGGREGATE OPERATIONS USING REST API PCL

usage: python3 aggregate_operations.py [-h] -c CLUSTER [-u API_USER]
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
from utils import Argument, parse_args, setup_logging
from utils import setup_connection, show_aggregate, show_node, show_disk
ur.disable_warnings()


def list_aggregate(cluster: str, headers_inc: str) -> None:
    """Lists the Aggregate"""
    url = "https://{}/api/storage/aggregates".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    tmp = dict(response.json())
    aggr = tmp['records']
    print()
    print("List of Aggregates:- ")
    print("=====================")
    for i in aggr:
        print("Aggregate Name = %s " % i['name'])
        print("Aggregate UUID = %s " % i['uuid'])


def create_aggregate(cluster: str, headers_inc: str) -> None:
    """ Create aggregate"""
    print("----------Create Aggregate-----------")
    print()
    show_node(cluster, headers_inc)
    node_name = input("Enter the name of the node name :- ")
    node_uuid = input("Enter the name of the node uuid :- ")
    print()
    show_disk(cluster, headers_inc)
    aggr_name = input("Enter the name of the Aggregate :- ")
    disk_count = input("Enter the Disk Count :- ")
    raid_size = input("Enter the RAID size :- ")
    raid_type = input("Enter the RAID type :- ")

    aggrobj = {
        "block_storage": {
            "mirror": {
                "enabled": False
            },
            "primary": {
                "checksum_style": "block",
                "disk_class": "performance",
                "disk_count": disk_count,
                "raid_size": raid_size,
                "raid_type": raid_type
            }
        },
        "name": aggr_name,
        "node": {
            "name": node_name,
            "uuid": node_uuid
        },
        "snaplock_type": "non_snaplock"
    }

    url = "https://{}/api/storage/aggregates".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=aggrobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    print(response)
    print(" Aggregate creation completed. ")


def patch_aggregate(cluster: str, headers_inc: str) -> None:
    """ Upate aggregate"""
    print("----------Upate Aggregate-----------")
    print()
    show_aggregate(cluster, headers_inc)
    aggr_uuid = input("Enter the UUID of Aggregate :- ")
    aggr_new_name = input(
        "Enter the new name of the aggregate to be updated :- ")
    aggrobj = {"name": aggr_new_name}
    url = "https://{}/api/storage/aggregates/{}".format(cluster, aggr_uuid)
    try:
        response = requests.patch(
            url,
            headers=headers_inc,
            json=aggrobj,
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

    print("Aggregate  has been updated with the new name")


def delete_aggregate(cluster: str, headers_inc: str) -> None:
    """ Delete aggregate"""
    print("----------Delete Aggregate-----------")
    print()
    show_aggregate(cluster, headers_inc)
    aggr_uuid = input("Enter the UUID of the Aggregate to be Deleted:- ")
    url = "https://{}/api/storage/aggregates/{}".format(cluster, aggr_uuid)
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

    print("Aggregate  has been deleted .")


def aggr_ops(cluster, headers_inc) -> None:
    """Aggregate Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS AGGREGATE OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("====================================================================================")
    print()
    aggrbool = input(
        "What Aggregate Operation would you like to do? [list/create/update/delete] ")
    if aggrbool == 'list':
        list_aggregate(cluster, headers_inc)
    if aggrbool == 'create':
        create_aggregate(cluster, headers_inc)
    if aggrbool == 'update':
        patch_aggregate(cluster, headers_inc)
    if aggrbool == 'delete':
        delete_aggregate(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Aggregate Operation using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    aggr_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
