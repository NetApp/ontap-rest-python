#! /usr/bin/env python3
"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: Script to create snapshot using the REST API PYTHON CLIENT LIBRARY.

usage: python3 create_snap.py [-h] -c CLUSTER -v VOLUME_NAME -s SNAPSHOT_NAME -vs SVM_NAME
                          [-u API_USER] [-p API_PASS]
create_snap.py: the following arguments are required: -c/--cluster, -v/--volume_name,
                                                          -s/--snapshot_name, -vs/--svm_name

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Volume, Snapshot

from utils import Argument, parse_args, setup_logging, setup_connection


def make_snap_pycl(vol_name: str, snapshot_name: str, svm_name: str) -> None:
    """Create a new snapshot with default settings for a given volume"""

    volume = Volume.find(**{'svm.name': svm_name, 'name': vol_name})
    snapshot = Snapshot(volume.uuid, name=snapshot_name)

    try:
        snapshot.post()
        print("Snapshot %s created successfully" % snapshot.name)
    except NetAppRestError as err:
        print("Error: Snapshot was not created: %s" % err)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details"),
        Argument("-v", "--volume_name", "Volume Name"),
        Argument("-s", "--snapshot_name", "Snapshot Name"),
        Argument("-vs", "--svm_name", "SVM Name")]
    args = parse_args(
        "This script will create a new snapshot for an existing ONTAP volume",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    make_snap_pycl(args.volume_name, args.snapshot_name, args.svm_name)


if __name__ == "__main__":
    main()
