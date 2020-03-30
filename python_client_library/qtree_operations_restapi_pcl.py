#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS QTREE OPERATIONS USING REST API PCL

usage: python3 qtree_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER]
                                       [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import argparse
from getpass import getpass
import logging

from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Svm, Volume, Qtree


def get_size(vol_size):
    """Convert MBs to Bytes"""
    tmp = int(vol_size) * 1024 * 1024
    return tmp

def show_svm():
    """ Show SVMs in a cluster"""
    print()
    print("Getting SVM Details")
    print("===================")
    try:
        for svm in Svm.get_collection(fields="uuid"):
            print("SVM name:-%s ; SVM uuid:-%s " % (svm.name, svm.uuid))
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_volume(svm_name):
    """Show volumes in a SVM"""
    print()
    print("Getting Volume Details")
    print("======================")
    try:
        for volume in Volume.get_collection(
                **{"svm.name": svm_name}, fields="uuid"):
            print("Name = %s; UUID = %s" % (volume.name, volume.uuid))
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_qtree():
    """List Qtrees in a Volume"""
    print()
    print("The List of SVMs:-")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(svm_name)
    print()
    vol_uuid = input(
        "Enter the Volume UUID from which the Qtrees need to be listed [UUID]:-")
    print("The List of Qtrees:-")
    print("====================")
    try:
        for qtree in Qtree.get_collection(**{"volume.uuid": vol_uuid}):
            print("Name:- %s  ID:- %s" % (qtree.name, qtree.id))
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))
    return vol_uuid

def create_qtree():
    """Create qtrees"""
    print()
    print("The List of SVMs")
    print("================")
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM Name on which the qtree need to be created:-")
    print()
    show_volume(svm_name)
    print()
    vol_name = input(
        "Enter the Volume Name on which the Qtree need to be created:-")

    print()
    qtree_name = input("Enter the name of the Qtree to be created:-")

    qtree = Qtree.from_dict({
        'name': qtree_name,
        'volume.name': vol_name,
        'svm.name': svm_name
    })

    try:
        if qtree.post(poll=True):
            print("Qtree  %s created Successfully" % qtree.name)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def patch_qtree():
    """Update Qtree"""
    print("=============================================")
    print()
    vol_uuid = show_qtree()

    print()
    print("=============================================")
    print("Enter the following details to Update a qtree")

    qtree_name = input("Enter the Name of the Qtree to be updated:-")

    try:
        qtree = Qtree.find(vol_uuid, name=qtree_name)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

    nambool = input("Would you like to update the Qtree name (y/n): ")
    if nambool == 'y':
        qtreename = input("Enter the name of the qtree to be updated:-")
        qtree.name = qtreename

    try:
        if qtree.patch(poll=True):
            print("Qtree  %s Updated Successfully" % qtree.name)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def delete_qtree():
    """Delete Qtree"""
    print("=============================================")
    print()
    vol_uuid = show_qtree()
    print()
    print("=============================================")
    print("Enter the following details to Delete a qtree")

    qtree_name = input("Enter the Name of the Qtree to be Deleted:-")

    try:
        qtree = Qtree.find(vol_uuid, name=qtree_name)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

    try:
        if qtree.delete(poll=True):
            print("Qtree  %s has been deleted Successfully." % qtree.name)
    except NetAppRestError as error:
        print("HTTP Error Code is " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def qtree_ops():
    """Qtree Operations"""
    print("THE FOLLOWING SCRIPT SHOWS QTREE OPERATIONS USING REST API PYTHON CLIENT LIBRARY.")
    print("==================================================================")
    print()
    qtreebool = input(
        "What Qtree Operation would you like to do? [show/create/update/delete] ")
    if qtreebool == 'show':
        show_qtree()
    if qtreebool == 'create':
        create_qtree()
    if qtreebool == 'update':
        patch_qtree()
    if qtreebool == 'delete':
        delete_qtree()

def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="THE FOLLOWING SCRIPT SHOWS QTREE OPERATIONS USING REST API PYTHON CLIENT LIBRARY:-")
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
    qtree_ops()
