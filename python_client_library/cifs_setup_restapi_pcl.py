#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate
 NetApp technologies. This script is not officially
supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS CIFS SETUP USING REST API PCL

usage: cifs_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import argparse
from getpass import getpass
import logging
import sys

from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Svm, Volume
from netapp_ontap.resources import CifsShare

def get_size(vol_size):
    tmp = int(vol_size) * 1024 * 1024
    return tmp

def show_svm():
    print()
    print("Getting SVM Details")
    print("===================")
    try:
        for svm in Svm.get_collection(fields="uuid"):
            print("SVM name:-%s ; SVM uuid:-%s " % (svm.name, svm.uuid))
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_volume():
    print("The List of SVMs")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    print("Getting Volume Details")
    print("======================")
    try:
        for volume in Volume.get_collection(
                **{"svm.name": svm_name}, fields="uuid"):
            print(
                "Volume name:-%s ; Volume uuid:-%s " %
                (volume.name, volume.uuid))
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def cifs_setup():

    print("THE FOLLOWING SCRIPT DEMOSTRATES CIFS SETUP USING REST API PCL.")
    print("===========================================================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Choose the SVM on which you would like to create a CIFS Share :")
    print("Make sure that NAS  LIFs on each nodes are created on the SVM :")
    print()
    print("Create the Volume:-")
    print("===================")
    vol_name = input("Enter the Volume Name to create CIFS Share:-")
    vol_size = input("Enter the Volume Size in MBs :-")
    aggr_name = input("Enter the aggregate name:-")

    v_size = get_size(vol_size)

    pather = "/" + vol_name

    payload2 = {
        "aggregates": [{"name": aggr_name}],
        "svm": {"name": svm_name},
        "name": vol_name,
        "size": v_size,
        "nas": {"security_style": "ntfs", "path": pather}
    }

    volume = Volume.from_dict(payload2)
    try:
        if volume.post(poll=True):
            print("Volume created  %s created Successfully" % volume.name)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))
        sys.exit()

    print()
    print("Create the Share:-")
    print("==================")

    share_name = input("Enter the share  name:-")

    payload3 = {
        "path": pather,
        "svm": {
            "name": svm_name,
        },
        "name": share_name
    }

    cifsshare = CifsShare.from_dict(payload3)
    try:
        if cifsshare.post(poll=True):
            print("cifsshare created Successfully")
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))
        sys.exit()

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="THE FOLLOWING SCRIPT SHOWS CIFS SETUP USING REST API PYTHON CLIENT LIBRARY:-")
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument(
        "-u",
        "--api_user",
        default="admin",
        help="API Username")
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
    ARGS = parse_args()
    config.CONNECTION = HostConnection(
        ARGS.cluster,
        username=ARGS.api_user,
        password=ARGS.api_pass,
        verify=False,
    )
    cifs_setup()
    print("Script Complete")
