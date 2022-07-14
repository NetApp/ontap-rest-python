#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS INITIATOR OPERATIONS USING REST API PCL

usage: python3 intiator_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Igroup, IgroupInitiator
from utils import Argument, parse_args, setup_logging
from utils import setup_connection, show_svm, show_igroup, get_key_igroup

def list_igroup() -> None:
    """Lists Initiator Group."""
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    print("Getting Initiator Group Details")
    print("===============================")
    try:
        for igroup in Igroup.get_collection(
                **{"svm.name": svm_name}, fields="uuid"):
            print(
                "Igroup Name = %s;  Igroup UUID = %s" %
                (igroup.name, igroup.uuid))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))
    igroup_name = input(
        "Enter the Igroup from which the Initiators need to be listed:-")
    igroup_uuid = get_key_igroup(svm_name, igroup_name)
    try:
        for ini in IgroupInitiator.get_collection(
                igroup_uuid):
            print(
                "Initiator Name = %s " %
                (ini.name))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_igroup() -> None:
    """Create Initiator Group."""
    print("Create Initiator Group.")
    print("=======================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the name of the SVM on which the volume needs to be created:- ")
    igroup_name = input(
        "Enter the name of the Igroup that you would like to create  : ")
    initiator_name = input(
        "Enter the name of the Initiator that you would like to add in the InitiatorGroup :")
    os_type2 = input("Enter the OS-TYPE :")

    payload3 = {
        "initiators": [
            {
                "name": initiator_name
            }
        ],
        "name": igroup_name,
        "os_type": os_type2,
        "svm": {
            "name": svm_name
        }
    }

    igroup_object = Igroup.from_dict(payload3)

    try:
        if igroup_object.post(poll=True):
            print(
                "IGROUP created  %s created Successfully" %
                igroup_object.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_igroup() -> None:
    """Delete Initiator Group."""
    print("Delete Initiator Group.")
    print("=======================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_igroup(svm_name)
    igroup_name = input(
        "Enter the Igroup name:- ")
    igroup_uuid = get_key_igroup(svm_name, igroup_name)

    try:
        igrp = Igroup.find(uuid=igroup_uuid)
        if igrp.delete(poll=True):
            print("Igroup  has been deleted Successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_igroup() -> None:
    """Update Initiator Group"""
    print("Update Initiator Group.")
    print("=======================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_igroup(svm_name)
    igroup_name = input(
        "Enter the Igroup name:- ")
    igroup_uuid = get_key_igroup(svm_name, igroup_name)
    print(igroup_uuid)
    initiator_name = input(
        "Enter the Intiator name:- ")
    try:
        dictobj = {"igroup.uuid": igroup_uuid, "name": initiator_name}
        init = IgroupInitiator.from_dict(dictobj)
        init.post()
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def initiator_ops() -> None:
    """Initiator Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("====================================================================================")
    print()
    inibool = input(
        "What Initiator Group Operation would you like to do? [list/create/update/delete] ")
    if inibool == 'list':
        list_igroup()
    if inibool == 'create':
        create_igroup()
    if inibool == 'update':
        patch_igroup()
    if inibool == 'delete':
        delete_igroup()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates BInitiator Group Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    initiator_ops()


if __name__ == "__main__":
    main()
