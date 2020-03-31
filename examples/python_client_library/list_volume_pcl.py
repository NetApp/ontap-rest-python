#! /usr/bin/env python3
"""
ONTAP REST API Python Client Library Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list aggregates using ONTAP REST API Python Client Library.

usage: python3 list_volume_pcl.py [-h] -c CLUSTER -vs SVM_NAME [-u API_USER]
                          [-p API_PASS]
list_volume_pcl.py:  the following arguments are required: -c/--cluster, -vn/--vserver_name

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Volume

from utils import Argument, parse_args, setup_logging, setup_connection


def list_volume_pycl(svm_name: str) -> None:
    """List Volumes in a SVM """

    print("\n List of Volumes:- \n")
    try:
        print(*(vol.name for vol in Volume.get_collection(**{"svm.name": svm_name})), sep="\n")
    except NetAppRestError as err:
        print("Error: Volume list  was not created: %s" % err)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details"),
        Argument("-vs", "--svm_name", "SVM Name"),
    ]
    args = parse_args("This script will list ONTAP volumes in an SVM", arguments)
    setup_logging()
    setup_connection(args)

    list_volume_pycl(args.svm_name)


if __name__ == "__main__":
    main()
