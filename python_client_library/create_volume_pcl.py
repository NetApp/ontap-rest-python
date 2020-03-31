#! /usr/bin/env python3
"""
ONTAP REST API Python Client Library Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to create volume using ONTAP REST API Python Client Library.

usage: python3 create_volume_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -vs VSERVER_NAME -a
                            AGGR_NAME -sz VOLUME_SIZE(MBs) [-u API_USER]
                            [-p API_PASS]
create_volume_pcl.py:  the following arguments are required: -c/--cluster, -v/--volume_name,
                                                             -vs/--vserver_name, -a/--aggr_name,
                                                             -sz/--volume_size

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Volume

from utils import Argument, parse_args, setup_logging, setup_connection


def make_volume_pycl(
        volume_name: str,
        svm_name: str,
        aggr_name: str,
        volume_size: int) -> None:
    """Creates a new volume in a SVM"""

    v_size = int(volume_size) * 1024 * 1024  # MB -> Bytes
    volume = Volume.from_dict({
        'name': volume_name,
        'svm': {'name': svm_name},
        'aggregates': [{'name': aggr_name}],
        'size': v_size,
    })

    try:
        volume.post()
        print("Volume %s created successfully" % volume.name)
    except NetAppRestError as err:
        print("Error: Volume was not created: %s" % err)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details"),
        Argument("-v", "--volume_name", "Volume Name"),
        Argument("-vs", "--svm_name", "SVM Name"),
        Argument("-a", "--aggr_name", "Aggregate Name"),
        Argument("-sz", "--volume_size", "Size of the volume(MBs)."),
    ]
    args = parse_args("This script will create a new volume.", arguments)
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    make_volume_pycl(
        args.volume_name,
        args.svm_name,
        args.aggr_name,
        args.volume_size)


if __name__ == "__main__":
    main()
