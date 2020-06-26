#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS QTREE OPERATIONS USING REST API PCL

usage: python3 qtree_operations.py [-h] -c CLUSTER [-u API_USER]
                                       [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Qtree
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import show_svm, show_volume, get_key_volume, show_qtree


def list_qtree():
    """List Qtrees in a Volume"""
    print()
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
        "Enter the Volume from which the Qtrees need to be listed:-")
    print()
    vol_uuid = get_key_volume(svm_name, volume_name)
    print()
    print("The List of Qtrees:-")
    print("====================")
    try:
        for qtree in Qtree.get_collection(**{"volume.uuid": vol_uuid}):
            print("Name:- %s  ID:- %s" % (qtree.name, qtree.id))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))
    return vol_uuid


def create_qtree() -> None:
    """Create qtrees"""
    print()
    print("The List of SVMs")
    print("================")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM Name on which the qtree need to be created:-")
    print()
    show_volume(svm_name)
    print()
    vol_name = input(
        "Enter the Volume Name on which the Qtree need to be created:-")

    print()
    qtree_name = input("Enter the name of the Qtree to be created:-")

    qtree = Qtree.from_dict({
        'name': qtree_name,
        'volume.name': vol_name,
        'svm.name': svm_name
    })

    try:
        if qtree.post(poll=True):
            print("Qtree  %s created Successfully" % qtree.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_qtree() -> None:
    """Update Qtree"""
    print("=============================================")
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
    show_qtree(svm_name, volume_name)
    print()
    print("=============================================")
    print("Enter the following details to Update a qtree")

    qtree_name = input("Enter the Name of the Qtree to be updated:-")

    try:
        qtree = Qtree.find(vol_uuid, name=qtree_name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))

    nambool = input("Would you like to update the Qtree name (y/n): ")
    if nambool == 'y':
        qtreename = input("Enter the name of the qtree to be updated:-")
        qtree.name = qtreename

    try:
        if qtree.patch(poll=True):
            print("Qtree  %s Updated Successfully" % qtree.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_qtree() -> None:
    """Delete Qtree"""
    print("=============================================")
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
    show_qtree(svm_name, volume_name)
    print()
    print("=============================================")
    print("Enter the following details to Delete a qtree")

    qtree_name = input("Enter the Name of the Qtree to be Deleted:-")

    try:
        qtree = Qtree.find(vol_uuid, name=qtree_name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))

    try:
        if qtree.delete(poll=True):
            print("Qtree  %s has been deleted Successfully." % qtree.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def qtree_ops() -> None:
    """Qtree Operations"""
    print("Demonstrates Qtree Operations using REST API Python Client Library.")
    print("===================================================================")
    print()
    qtreebool = input(
        "What Qtree Operation would you like to do? [list/create/update/delete] ")
    if qtreebool == 'list':
        list_qtree()
    if qtreebool == 'create':
        create_qtree()
    if qtreebool == 'update':
        patch_qtree()
    if qtreebool == 'delete':
        delete_qtree()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Qtree Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    qtree_ops()


if __name__ == "__main__":
    main()
