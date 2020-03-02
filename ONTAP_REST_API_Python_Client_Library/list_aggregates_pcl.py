#! /usr/bin/env python3

"""
ONTAP REST API Python Client Library Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list aggregates using Python Client Library.

usage: list_aggregates_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
list_aggregates_pcl.py:  the following arguments are required: -c/--cluster
"""

import argparse
from getpass import getpass
import logging

from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Aggregate


def list_aggregate_pycl() -> None:
    """List the aggregates."""

    print ("\n List of Aggregates:- \n")
    try:
        for aggregatelist in Aggregate.get_collection():
            aggregatelist.get()
            print (aggregatelist.name)
    except NetAppRestError as err:
            print("Error: Aggregate list was not created: %s" % err)
    return

    

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will list the aggregates."
    )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
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
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s"
    )
    args = parse_args()
    config.CONNECTION = HostConnection(
        args.cluster, username=args.api_user, password=args.api_pass, verify=False
    )

    list_aggregate_pycl()
