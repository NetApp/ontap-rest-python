#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SNAPMIRROR OPERATIONS USING REST API PCL

Usage: snapmirror_operations.py -a <Cluster Address> -u <User Name> -p <Password Name>

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import SnapmirrorRelationship
from utils import Argument, parse_args, setup_logging, setup_connection, show_snapmirror


def list_snapmirror() -> None:
    """List Snapmirror"""
    print("List of SnapMirror Relationships:")
    print("=================================")

    try:
        for snapmirrorrelationship in SnapmirrorRelationship.get_collection(
                fields="uuid"):
            print(snapmirrorrelationship.uuid)
            snapmirror1 = SnapmirrorRelationship.find(
                uuid=snapmirrorrelationship.uuid)
            print(snapmirror1.source.path)
            print(snapmirror1.destination.path)
            print(snapmirror1.state)
            print("-----------------------------")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_snapmirror() -> None:
    """Create snapmirror relationship"""
    print("===================")
    print("Please enter the following details:-")
    src_svm_name = input("Enter the Source SVM :-")
    src_vol_name = input("Enter the Source Volume :-")
    dst_svm_name = input("Enter the Destination SVM :-")
    dst_vol_name = input("Enter the Destination Volume :-")

    dataobj = {}
    src = src_svm_name + ":" + src_vol_name
    dst = dst_svm_name + ":" + dst_vol_name
    dataobj['source'] = {"path": src}
    dataobj['destination'] = {"path": dst}

    snapmirrorrelationship = SnapmirrorRelationship.from_dict(dataobj)

    try:
        if snapmirrorrelationship.post(poll=True):
            print("SnapmirrorRelationship  %s created Successfully")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_snapmirror() -> None:
    """Update Snapmirror Relation"""
    print("=============================================")
    print()
    show_snapmirror()

    snapmirror_uuid = input("Enter the UUID of the snapmirror to be updated:-")
    snapmirrortransfer = SnapmirrorRelationship.find(uuid=snapmirror_uuid)
    snapchoice = input(
        "What state update would you like? [snapmirrored/paused/broken_off/uninitialized/synchronizing] ")
    snapmirrortransfer.state = snapchoice
    try:
        if snapmirrortransfer.patch(poll=True):
            print("Snapmirror Relationship   Updated Successfully")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_snapmirror() -> None:
    """Delete Snapmirror"""
    print("=============================================")
    print()
    show_snapmirror()

    snapmirror_uuid = input("Enter the UUID of the snapmirror to be deleted:-")
    snapmirrorrelationship = SnapmirrorRelationship.find(uuid=snapmirror_uuid)

    try:
        if snapmirrorrelationship.delete(poll=True):
            print("Snapmirror Relationship has been deleted Successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def sm_ops() -> None:
    """SnapMirror Operations"""
    print("Demonstrates SnapMirror Operations using REST API Python Client Library.")
    print("========================================================================")
    print()
    snapmirrorbool = input(
        "What state SnapMirror Operation would you like? SnapMirror [list/create/update/delete] ")
    if snapmirrorbool == 'list':
        list_snapmirror()
    if snapmirrorbool == 'create':
        create_snapmirror()
    if snapmirrorbool == 'update':
        patch_snapmirror()
    if snapmirrorbool == 'delete':
        delete_snapmirror()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates SnapMirror Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    sm_ops()


if __name__ == "__main__":
    main()
