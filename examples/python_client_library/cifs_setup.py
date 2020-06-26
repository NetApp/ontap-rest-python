#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate
 NetApp technologies. This script is not officially
supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS CIFS SETUP USING REST API PCL

usage: cifs_setup [-h] -c CLUSTER [-u API_USER] [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import sys

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Volume
from netapp_ontap.resources import CifsShare
from utils import Argument, parse_args, setup_logging, setup_connection, get_size, show_svm


def cifs_setup() -> None:
    """Script demostrates the CIFS setup using REST API PCL"""
    print("THE FOLLOWING SCRIPT DEMOSTRATES CIFS SETUP USING REST API PCL.")
    print("===============================================================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Choose the SVM on which you would like to create a CIFS Share :")
    print("Make sure that NAS  LIFs on each nodes are created on the SVM :")
    print()
    print("Create the Volume:-")
    print("===================")
    vol_name = input("Enter the Volume Name to be created for CIFS Share:-")
    vol_size = input("Enter the Volume Size in MBs :-")
    aggr_name = input("Enter the aggregate name:-")

    v_size = get_size(vol_size)

    pather = "/" + vol_name

    payload2 = {
        "aggregates": [{"name": aggr_name}],
        "svm": {"name": svm_name},
        "name": vol_name,
        "size": v_size,
        "nas": {"security_style": "ntfs", "path": pather}
    }

    volume = Volume.from_dict(payload2)
    try:
        if volume.post(poll=True):
            print("Volume created  %s created Successfully" % volume.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))
        sys.exit()

    print()
    print("Create the Share:-")
    print("==================")

    share_name = input("Enter the share  name:-")

    payload3 = {
        "path": pather,
        "svm": {
            "name": svm_name,
        },
        "name": share_name
    }

    cifsshare = CifsShare.from_dict(payload3)
    try:
        if cifsshare.post(poll=True):
            print("cifsshare created Successfully")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))
        sys.exit()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details"),
    ]
    args = parse_args(
        "Demonstrates CIFS Setup using REST API Python Client Library",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    cifs_setup()


if __name__ == "__main__":
    main()
