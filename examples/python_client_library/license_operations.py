#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API PCL

usage: python3 license_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import LicensePackage
from utils import Argument, parse_args, setup_logging, setup_connection


def list_license() -> None:
    """Lists Licenses"""
    print()
    print("Getting License Details")
    print("=======================")
    try:
        for lic in LicensePackage.get_collection(
                fields="licenses.serial_number"):
            print(
                "License Name = %s, License Serial Number = %s" %
                (lic.name, lic.licenses[0].serial_number))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_license() -> None:
    """Create Licenses"""
    print()
    license_name = input(
        "Enter the License that needs to be added:- ")
    try:
        if LicensePackage(keys=[license_name]).post(poll=True):
            print("License submitted successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_license() -> None:
    """Delete Licenses"""
    print()
    license_type = input(
        "which license would you like to delete:- ")

    try:
        licen = LicensePackage.find(name=license_type)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))

    try:
        if licen.delete(poll=True):
            print("License deleted successfully.")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def license_ops() -> None:
    """License Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS LICENSE OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("=====================================================================================")
    print()
    licbool = input(
        "What License Operation would you like to do? [list/create/delete] ")
    if licbool == 'list':
        list_license()
    if licbool == 'create':
        create_license()
    if licbool == 'delete':
        delete_license()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates License Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    license_ops()


if __name__ == "__main__":
    main()
