#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME BATCH DELETE USING REST API PCL

usage: python3 volume_batch_delete.py [-h] -c CLUSTER [-u API_USER]
                                          [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Volume
from utils import Argument, parse_args, setup_logging, setup_connection, show_svm, show_volume


def delete_collection_volume() -> None:
    """Delete a collection of volumes"""
    print("=============================================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(svm_name)
    print()

    noofnames = int(
        input("Enter number of Volumes to be Deleted [eg: int value:1,2,3] : "))
    volume_names = list(map(str, input(
        "\nEnter the Volume names to be Deleted [eg: aaa bbb ccc] : ").strip().split()))[:noofnames]
    volume_names_final = '|'.join([str(v) for v in volume_names])

    try:
        Volume.delete_collection(name=volume_names_final)
        print(list(Volume.get_collection()))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Batch Deletion Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    delete_collection_volume()


if __name__ == "__main__":
    main()
