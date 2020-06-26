#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SNAPSHOT OPERATIONS USING REST API PCL

usage: python3 snapshot_operations.py [-h] -c CLUSTER [-u API_USER]
                                          [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Snapshot
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import show_svm, show_volume, get_key_volume, show_snapshot


def list_snapshot() -> None:
    """List Snapshots in a volume"""
    print()
    print("The List of SVMs:-")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(svm_name)
    print()
    volume_name = input(
        "Enter the Volume from which the Snapshots need to be listed:-")
    print()
    vol_uuid = get_key_volume(svm_name, volume_name)
    print()
    print("The List of Snapshots:-")
    print("=======================")
    try:
        for snapshot in Snapshot.get_collection(vol_uuid):
            print(snapshot.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_snapshot() -> None:
    """Create snapshot """
    print()
    print("The List of SVMs:-")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(svm_name)
    print()
    volume_name = input(
        "Enter the Volume from which the Snapshots need to be listed:-")
    print()
    vol_uuid = get_key_volume(svm_name, volume_name)

    print()
    snapshot_name = input("Enter the name of the snapshot to be created:-")

    snapshot = Snapshot.from_dict(
        {
            'name': snapshot_name,
            'volume.uuid': vol_uuid
        }
    )

    try:
        if snapshot.post(poll=True):
            print("Snapshot  %s created Successfully" % snapshot.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_snapshot() -> None:
    """Update Snapshot"""
    print()
    print("The List of SVMs:-")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(svm_name)
    print()
    volume_name = input(
        "Enter the Volume from which the Snapshots need to be listed:-")
    print()
    vol_uuid = get_key_volume(svm_name, volume_name)
    show_snapshot(svm_name, volume_name)
    print()

    snapshot_name = input("Enter the name of the snapshot to be updated:-")

    snapshot = Snapshot.find(vol_uuid, name=snapshot_name)
    snapbool = input("Would you like to update the name (y/n): ")
    if snapbool == 'y':
        snapname = input("Enter the name of the snapshot to be updated:-")
        snapshot.name = snapname
    combool = input("Would you like to update the comment (y/n): ")
    if combool == 'y':
        snapcom = input("Enter the comment of the snapshot to be updated:-")
        snapshot.comment = snapcom
    expirybool = input("Would you like to update the expiry date (y/n): ")
    if expirybool == 'y':
        snapexpiry = input(
            "Enter the expiry date of the snapshot to be updated (format:- 2019-02-04T19:00:00Z):-")
        snapshot.expiry_time = snapexpiry

    try:
        if snapshot.patch(poll=True):
            print("Snapshot  %s Updated Successfully" % snapshot.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_snapshot() -> None:
    """Delete Snapshot"""

    print()
    print("The List of SVMs:-")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(svm_name)
    print()
    volume_name = input(
        "Enter the Volume from which the Snapshots need to be listed:-")
    print()
    vol_uuid = get_key_volume(svm_name, volume_name)
    show_snapshot(svm_name, volume_name)
    print()

    snapshotname = input(
        "Enter the name of the snapshot that needs to be Deleted:- ")

    try:
        snapshot = Snapshot.find(vol_uuid, name=snapshotname)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))

    try:
        if snapshot.delete(poll=True):
            print(
                "Snapshot  %s has been deleted Successfully." %
                snapshot.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def snapshot_ops() -> None:
    """Snapshot Operation"""
    print("Demonstrates Snapshot Operations using REST API Python Client Library.")
    print("======================================================================")
    print()
    snapshotbool = input(
        "What Snapshot Operation would you like to do? [list/create/update/delete] ")
    if snapshotbool == 'list':
        list_snapshot()
    if snapshotbool == 'create':
        create_snapshot()
    if snapshotbool == 'update':
        patch_snapshot()
    if snapshotbool == 'delete':
        delete_snapshot()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Snapshot Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    snapshot_ops()


if __name__ == "__main__":
    main()
