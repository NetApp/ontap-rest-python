#! /usr/bin/env python3

"""
ONTAP REST API Python Client Library Sample Scripts
This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list aggregates using Python Client Library.

usage: python3 list_aggregates.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Aggregate

from utils import Argument, parse_args, setup_logging, setup_connection


def list_aggregate_pycl() -> None:
    """List the aggregates."""

    print("\n List of Aggregates:- \n")
    try:
        print(*(aggr.name for aggr in Aggregate.get_collection()), sep="\n")
    except NetAppRestError as err:
        print("Error: Aggregate list could not be retrieved: %s" % err)


def main() -> None:
    """Main function"""

    arguments = [Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args("This script will list the aggregates.", arguments)
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    list_aggregate_pycl()


if __name__ == "__main__":
    main()
