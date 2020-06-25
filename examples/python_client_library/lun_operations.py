#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API PCL

usage: python3 lun_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Lun
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import get_size, show_svm, show_volume, show_lun

def list_lun():
    """ List LUN"""
    print("\n List of LUN:- \n")
    try:
        for lun in Lun.get_collection():
            print("Lun Name:- %s; Lun UUID:- %s " % (lun.name, lun.uuid))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_lun():
    """Create Interface"""
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the name of the SVM on which the interface should be created :- ")
    print()
    show_volume(svm_name)
    print()
    vol_name = input(
        "Choose the volume on which you would like to create the LUN : ")

    print()
    lun_name = input("Enter the name of the LUN  : ")
    lun_name_ext = "/vol/" + vol_name + "/" + lun_name
    os_type = input("Enter the name of the OS-TYPE  : ")
    lun_size = input("Enter the LUN size in MBs :")
    l_size = get_size(lun_size)

    payload2 = {
        "comment": lun_name,
        "location": {
            "logical_unit": lun_name,
            "volume": {
                "name": vol_name
            }
        },
        "name": lun_name_ext,
        "os_type": os_type,
        "space": {
            "guarantee": {
                "requested": bool("")
            },
            "size": l_size
        },
        "svm": {
            "name": svm_name
        }
    }

    lun_object = Lun.from_dict(payload2)

    try:
        if lun_object.post(poll=True):
            print("LUN created  %s created Successfully" % lun_object.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_lun() -> None:
    """ Patch lun"""
    print("----------Patch Interface-----------")
    print()
    show_lun()
    lun_name = input("Enter the name of the LUN :- ")
    lun_new_name = input("Enter the new name of the LUN  to be updated :- ")
    try:
        lun = Lun.find(name=lun_name)
        lun.name = lun_new_name
        if lun.patch(poll=True):
            print("LUN updated successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_lun() -> None:
    """ Delete Lun"""
    print("----------Delete Lun-----------")
    print()
    show_lun()
    lun_name = input("Enter the name of the LUN :- ")
    try:
        lun = Lun.find(name=lun_name)
        if lun.delete(poll=True):
            print("LUN deleted successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def lun_ops() -> None:
    """Interface Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS LUN OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("=================================================================================")
    print()
    lunbool = input(
        "Choose the LUN Operation would you like to do? [list/create/update/delete] ")
    if lunbool == 'list':
        list_lun()
    if lunbool == 'create':
        create_lun()
    if lunbool == 'update':
        patch_lun()
    if lunbool == 'delete':
        delete_lun()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates LUN Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    lun_ops()


if __name__ == "__main__":
    main()
