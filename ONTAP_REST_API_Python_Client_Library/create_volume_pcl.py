#! /usr/bin/env python3

"""
ONTAP REST API Python Client Library Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to create volume using Python Client Library.

usage: create_volume_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -vn VSERVER_NAME -a
                            AGGR_NAME -s VOLUME_SIZE [-u API_USER]
                            [-p API_PASS]
create_volume_pcl.py:  the following arguments are required: -c/--cluster,                              -v/--volume_name, -vn/--vserver_name, -a/--aggr_name, -s/--volume_size
"""

import argparse
from getpass import getpass
import logging

from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Volume

def make_volume_pycl(volume_name: str, vserver_name: str, aggr_name: str, volume_size: int) -> None:
    """Creates a new volume in a SVM"""

    volume = Volume.from_dict({
    'name': volume_name,
    'svm': {'name':vserver_name},
    'aggregates': [{'name': aggr_name }],
    'size': volume_size
    })

    try:
        volume.post()
        print("Volume %s created successfully" % volume.name)
    except NetAppRestError as err:
        print("Error: Volume was not created: %s" % err)
    return	
	
def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will create a new volume."
    )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument(
        "-v", "--volume_name", required=True, help="Volume to create or clone from"
    )
    parser.add_argument(
        "-vn", "--vserver_name", required=True, help="SVM to create the volume from"
    )
    parser.add_argument(
        "-a", "--aggr_name", required=True, help="Aggregate to create the volume from"
    )
    parser.add_argument(
        "-s", "--volume_size", required=True, help="Size of the volume."
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

    make_volume_pycl(args.volume_name, args.vserver_name, args.aggr_name , args.volume_size)
