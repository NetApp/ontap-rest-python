#! /usr/bin/env python3

"""
ONTAP REST API Python Client Library Sample Scripts
This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to use CLI commands using ONTAP REST API Python Client Library.

usage: python3 system_power_status_cli.py [-h] -c CLUSTER -vs SVM_NAME [-u API_USER]
                          [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import json
from netapp_ontap.resources import CLI
from utils import Argument, parse_args, setup_logging, setup_connection


def system_power_status_cli_pycl() -> None:
    """ list system power status """
    response = CLI().execute(
        "system node power show", status="on")
    print(json.dumps(response.http_response.json(), indent=4))


def main() -> None:
    """Main function"""
    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "This script will list ONTAP System Power status", arguments)
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)
    system_power_status_cli_pycl()


if __name__ == "__main__":
    main()
