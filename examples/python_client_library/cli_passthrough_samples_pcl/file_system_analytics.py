#! /usr/bin/env python3

"""
ONTAP REST API Python Client Library Sample Scripts
This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list volumes using ONTAP REST API Python Client Library.

usage: python3 file_system_analytics.py [-h] -c CLUSTER -vs SVM_NAME [-u API_USER]
                          [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap.resources import FileInfo
from utils import Argument, parse_args, setup_logging, setup_connection, Volume


def file_system_analytics_pycl(vol_name: str, svm_name: str, path: str) -> None:
    """ List File system analytics of a volume in an SVM """
    volume = Volume.find(**{'svm.name': svm_name, 'name': vol_name})

    resource = FileInfo(volume.uuid, path)
    resource.get(return_metadata=True, fields="*")
    print()
    print("Path:", resource.path)
    print("Bytes Used:", resource.bytes_used)
    print("Accessed Time: ", resource.accessed_time)
    print("Changed Time: ", resource.changed_time)
    print("Inode: ", resource.inode_number)
    print("unix_permissions", resource.unix_permissions)


def main() -> None:
    """Main function"""
    arguments = [
        Argument("-c", "--cluster", "API server IP:port details"),
        Argument("-v", "--volume_name", "Volume Name"),
        Argument("-a", "--path", "path"),
        Argument("-vs", "--svm_name", "SVM Name")]
    args = parse_args(
        "This script will list analytics of a volume in an SVM", arguments)
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)
    file_system_analytics_pycl(args.volume_name, args.svm_name, args.path)


if __name__ == "__main__":
    main()
