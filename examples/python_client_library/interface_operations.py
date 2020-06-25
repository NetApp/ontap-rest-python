#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API PCL

usage: python3 interface_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import IpInterface
from utils import Argument, parse_args, setup_logging
from utils import setup_connection, show_svm, show_node, show_interface


def list_interface():
    """ List Interface"""
    print("\n List of Interface:- \n")
    try:
        for interface in IpInterface.get_collection():
            print(
                "Interface Name:- %s; Inteface UUID:- %s " %
                (interface.name, interface.uuid))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_interface():
    """Create Interface"""
    int_name = input("Enter the name of the Interface:- ")
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the name of the SVM on which the interface should be created :- ")
    svm_uuid = input(
        "Enter the UUID of the SVM on which the interface should be created :- ")
    print()
    show_node()
    print()
    node_name = input(
        "Enter the name of the home node on which the interface should be created :- ")
    node_uuid = input(
        "Enter the uuid of the home node on which the interface should be created :- ")
    ip_add = input("Enter the IP address:- ")
    netmask = input("Enter the NetMask:- ")

    interfaceobj = {
        "enabled": True,
        "ip": {
            "address": ip_add,
            "netmask": netmask
        },
        "name": int_name,
        "scope": "svm",
        "svm": {
            "name": svm_name,
            "uuid": svm_uuid
        },
        "location": {"home_node": {
            "name": node_name,
            "uuid": node_uuid
            }
                    }
    }
    try:
        ipint = IpInterface.from_dict(interfaceobj)
        if ipint.post(poll=True):
            print("Interface created successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_interface() -> None:
    """ Patch Interface"""
    print("----------Patch Interface-----------")
    print()
    show_interface()
    int_name = input("Enter the name of the Interface Name :- ")
    int_new_name = input(
        "Enter the new name of the interface  to be updated :- ")
    try:
        ipint = IpInterface.find(name=int_name)
        ipint.name = int_new_name
        if ipint.patch(poll=True):
            print("Interface updated successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_interface() -> None:
    """ delete Interface"""
    print("----------Patch Interface-----------")
    print()
    show_interface()
    int_name = input("Enter the name of the Interface Name :- ")
    try:
        ipint = IpInterface.find(name=int_name)
        if ipint.delete(poll=True):
            print("Interface deleted successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def interface_ops() -> None:
    """Interface Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS INTERFACE OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("=======================================================================================")
    print()
    interfacebool = input(
        "What Interface Operation would you like to do? [list/create/update/delete] ")
    if interfacebool == 'list':
        list_interface()
    if interfacebool == 'create':
        create_interface()
    if interfacebool == 'update':
        patch_interface()
    if interfacebool == 'delete':
        delete_interface()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Interface Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    interface_ops()


if __name__ == "__main__":
    main()
