#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME BATCH PATCHING OPERATIONS USING REST API PYTHON CLIENT LIBRARY

usage: python3 volume_batch_patch_restapi_pcl.py [-h] -c CLUSTER [-u API_USER]
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
from netapp_ontap.resources import Svm, Volume
from utils import Argument, parse_args, setup_logging, setup_connection, get_size

def show_svm() -> None:
    """List the SVMs"""
    print()
    print("Getting SVM Details")
    print("===================")
    try:
        for svm in Svm.get_collection(fields="uuid"):
            print("SVM name:-%s ; SVM uuid:-%s " % (svm.name, svm.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_volume() -> None:
    """List volumes"""
    print("The List of SVMs")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    print("Getting Volume Details")
    print("======================")
    try:
        for volume in Volume.get_collection(**{"svm.name": svm_name}):
            print(
                "Volume Name = %s;  Volume UUID = %s" %
                (volume.name, volume.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def patch_collection_volume() -> None:
    """Update the volume collection"""
    """Turn the given volumes off then on again"""
    print("=============================================")
    print()
    show_volume()
    print()
    noofnames = int(
        input("Enter number of Volumes to be Updated [eg: int value:1,2,3] : "))
    volume_names = list(map(str, input(
        "\nEnter the Volume names to be updated [eg: aaa bbb ccc] : ").strip().split()))[:noofnames]
    volume_names_final = '|'.join([str(v) for v in volume_names])
    vol_state = input("Enter the new state of the Volume [offline/online]: ")
    print("Please ensure that the volumes are unmounted. ")
    page_size = min(len(volume_names_final) - 1, 1)

    try:
        Volume.patch_collection({"state": vol_state},
                                name=volume_names_final,
                                max_records=page_size)
        print(
            list(
                Volume.get_collection(
                    fields='state',
                    name=volume_names_final)))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details"),
            ]
    args = parse_args(
        "Demonstrates Batch Update Operations using REST API Python Client Library.", arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    patch_collection_volume()

if __name__ == "__main__":
    main()
