#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API PCL

usage: python3 aggregate_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Aggregate
from utils import Argument, parse_args, setup_logging
from utils import setup_connection, show_aggregate, show_node, show_disk


def list_aggregate() -> None:
    """Lists the Aggregate"""
    print("\n List of Aggregates:- \n")
    try:
        for aggregatelist in Aggregate.get_collection():
            print(aggregatelist.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_aggregate() -> None:
    """ Create aggregate"""
    print("----------Create Aggregate-----------")
    print()
    show_node()
    node_name = input("Enter the name of the node name :- ")
    node_uuid = input("Enter the name of the node uuid :- ")
    print()
    show_disk()
    aggr_name = input("Enter the name of the Aggregate :- ")
    disk_count = input("Enter the Disk Count :- ")
    raid_size = input("Enter the RAID size :- ")
    raid_type = input("Enter the RAID type :- ")

    aggrobj = {
        "block_storage": {
            "mirror": {
                "enabled": "false"
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

    try:
        aggr = Aggregate.from_dict(aggrobj)
        if aggr.post(poll=True):
            print("Aggregate created successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_aggregate() -> None:
    """ Create aggregate"""
    print("----------Create Aggregate-----------")
    print()
    show_aggregate()
    aggr_name = input("Enter the name of the Aggregate Name to be Updated :- ")
    aggr_new_name = input(
        "Enter the new name of the aggregate to be updated :- ")
    try:
        aggr = Aggregate.find(name=aggr_name)
        aggr.name = aggr_new_name
        aggr.patch(poll=True)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_aggregate() -> None:
    """ Delete aggregate"""
    print("----------Delete Aggregate-----------")
    print()
    show_aggregate()
    aggr_name = input("Enter the name of the Aggregate Name to be Deleted:- ")
    print()
    try:
        aggr = Aggregate.find(name=aggr_name)
        aggr.delete(poll=True)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def aggr_ops() -> None:
    """Aggregate Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS AGGREGATE OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("=======================================================================================")
    print()
    aggrbool = input(
        "Choose the Aggregate Operation would you like to do? [list/create/update/delete] ")
    if aggrbool == 'list':
        list_aggregate()
    if aggrbool == 'create':
        create_aggregate()
    if aggrbool == 'update':
        patch_aggregate()
    if aggrbool == 'delete':
        delete_aggregate()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Aggregate Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    aggr_ops()


if __name__ == "__main__":
    main()
