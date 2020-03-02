#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: Script to create snapshot using the netapp_ontap library.

usage: create_snap_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -s SNAPSHOT_NAME
                          [-u API_USER] [-p API_PASS]
create_snap_pcl.py: the following arguments are required: -c/--cluster,
 -v/--volume_name, -s/--snapshot_name
"""

import argparse
from getpass import getpass
import logging

from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Volume, Snapshot


def make_snap_pycl(vol_name: str, snapshot_name: str) -> None:
    """Create a new snapshot with default settings for a given volume"""

    volume = Volume.find(name=vol_name)
    snapshot = Snapshot(volume.uuid, name=snapshot_name)

    try:
        snapshot.post()
        print("Snapshot %s created successfully" % snapshot.name)
    except NetAppRestError as err:
        print("Error: Snapshot was not created: %s" % err)
    return

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will create a new snapshot for an existing ONTAP volume"
    )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument(
        "-v", "--volume_name", required=True, help="Volume to create or clone from"
    )
    parser.add_argument(
        "-s", "--snapshot_name", required=True, help="Snapshot to create or clone from"
    )
    parser.add_argument("-u", "--api_user", default="admin", help="API Username")
    parser.add_argument("-p", "--api_pass", help="API Password")
    parsed_args = parser.parse_args()

    # collect the password without echo if not already provided
    if not parsed_args.api_pass:
        parsed_args.api_pass = getpass()

    return parsed_args


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
    )
    args = parse_args()
    config.CONNECTION = HostConnection(
        args.cluster, username=args.api_user, password=args.api_pass, verify=False,
    )

    make_snap_pycl(args.volume_name, args.snapshot_name)
