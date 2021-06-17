#! /usr/bin/env python3

"""
ONTAP REST API Python Client Library Sample Scripts
This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to use CLI commands using ONTAP REST API Python Client Library.

usage: python3 system_node_power_update_cli.py [-h] -c CLUSTER -vs SVM_NAME [-u API_USER]
                          [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import json
import time
from netapp_ontap.resources import CLI
from utils import Argument, parse_args, setup_logging, setup_connection


def system_node_power_on() -> None:
    """ system node power on module"""
    node_name = input("\n Enter the node name: ")
    response = CLI().execute(
        "system node power on",
        body={
            "node": node_name},
        privilege_level="diagnostic")
    time.sleep(15)
    response = CLI().execute(
        "system node power show", status="on")
    print(json.dumps(response.http_response.json(), indent=4))


def system_node_power_off() -> None:
    """ System node power off module """
    node = input("\n Enter the node name: ")
    response = CLI().execute(
        "system node power off", body={
            "node": node}, privilege_level="diagnostic")
    time.sleep(5)
    response = CLI().execute(
        "system node power show", status="off")
    print(json.dumps(response.http_response.json(), indent=4))


def check_system_power() -> None:
    """Module to retrieve user input for system node power"""
    print("\n===============================================================")
    print("This Module covers System node power CLI command usage in PCL")
    print("===============================================================")
    print("\n 1. CLI Command >> system node power on")
    print("\n 2. CLI Command >> system node power off")
    option = input("\n\nEnter the option: ")
    if option == '1':
        system_node_power_on()
    if option == '2':
        system_node_power_off()


def main() -> None:
    """Main function"""
    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "This script will update system power status ON/OFF", arguments)
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)
    check_system_power()


if __name__ == "__main__":
    main()
