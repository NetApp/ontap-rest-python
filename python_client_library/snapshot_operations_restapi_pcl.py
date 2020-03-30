#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SNAPSHOT OPERATIONS USING REST API PCL

usage: python3 snapshot_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER]
                                          [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import argparse
from getpass import getpass
import logging

from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Svm, Volume, Snapshot

def get_size(vol_size):
    """Convert MBs to Bytes"""
    tmp = int(vol_size) * 1024 * 1024
    return tmp

def show_svm():
    """Show SVM in a cluster"""
    print()
    print("Getting SVM Details")
    print("===================")
    try:
        for svm in Svm.get_collection(fields="uuid"):
            print("SVM name:-%s ; SVM uuid:-%s " % (svm.name, svm.uuid))
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_volume(svm_name):
    """List volumes in a SVM"""
    print()
    print("Getting Volume Details")
    print("======================")
    try:
        for volume in Volume.get_collection(
                **{"svm.name": svm_name}, fields="uuid"):
            print("Name = %s; UUID = %s" % (volume.name, volume.uuid))
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_snapshot():
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
    vol_uuid = input(
        "Enter the Volume UUID from which the Snapshots need to be listed [UUID]:-")
    print("The List of Snapshots:-")
    print("=======================")
    try:
        for snapshot in Snapshot.get_collection(vol_uuid):
            print(snapshot.name)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))
    return vol_uuid

def create_snapshot():
    """Create snapshot """
    print()
    print("The List of SVMs")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM on which the Volume Snapshot need to be created:-")
    print()
    show_volume(svm_name)
    print()
    vol_uuid = input(
        "Enter the Volume UUID on which the Snapshots need to be created[UUID]:-")

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
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def patch_snapshot():
    """Update Snapshot"""
    print("=============================================")
    print()
    vol_uuid = show_snapshot()
    print()
    print("=============================================")
    print("Please enter the following to update the required snapshot")

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
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def delete_snapshot():
    """Delete Snapshot"""
    print("=============================================")
    print()
    vol_uuid = show_snapshot()
    print()
    print("=============================================")
    print("please enter the following the details to delete snapshot.")
    snapshotname = input(
        "Enter the name of the snapshot that needs to be Deleted:- ")

    try:
        snapshot = Snapshot.find(vol_uuid, name=snapshotname)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

    try:
        if snapshot.delete(poll=True):
            print(
                "Snapshot  %s has been deleted Successfully." %
                snapshot.name)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def snapshot_ops():
    """Snapshot Operation"""
    print("THE FOLLOWING SCRIPT SHOWS SNAPSHOT OPERATIONS USING REST API PCL.")
    print("==================================================================")
    print()
    snapshotbool = input(
        "What Snapshot Operation would you like to do? [show/create/update/delete] ")
    if snapshotbool == 'show':
        show_snapshot()
    if snapshotbool == 'create':
        create_snapshot()
    if snapshotbool == 'update':
        patch_snapshot()
    if snapshotbool == 'delete':
        delete_snapshot()

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="SNAPSHOT OPERATIONS USING REST API PYTHON CLIENT LIBRARY:-")
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
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
    config.CONNECTION = HostConnection(
        ARGS.cluster,
        username=ARGS.api_user,
        password=ARGS.api_pass,
        verify=False,
    )
    snapshot_ops()
