#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS NFS SETUP USING REST API PCL

usage: nfs_setup.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Svm, Volume, ExportPolicy, NfsService
from utils import Argument, parse_args, setup_logging, setup_connection, get_size

def get_key_svms(svm_name) -> None:
    """Get SVM Keys"""
    print()
    try:
        for svm in Svm.get_collection(fields="uuid"):
            if svm.name == svm_name:
                print(svm.uuid)
                return svm.uuid
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_svm() -> None:
    """Show the SVMs in the cluster"""
    print()
    print("Getting SVM Details")
    print("===================")
    try:
        for svm in Svm.get_collection(fields="uuid"):
            print("SVM name:-%s ; SVM uuid:-%s " % (svm.name, svm.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_volume() -> None:
    """Show volumes in the SVMs"""
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
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def nfs_setup() -> None:
    """Script demostrates NFS setup"""
    print("THE FOLLOWING SCRIPT DEMOSTRATES NFS SETUP USING REST API .")
    print("====================================================================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Choose the SVM on which you would like to create a NFS Share :")
    print("Make sure that NAS  LIFs on each nodes are created on the SVM.")
    print()

    nfsbool = input(
        "Would you like to enable NFS protocol on the vserver (y/n):-")
    if nfsbool == 'y':
        print("============================")

        payload1 = {
            "enabled": bool("true"),
            "protocol": {
                "v3_enabled": bool("true")
            },
            "svm": {
                "name": svm_name
            }
        }

        print(payload1)

        try:
            nfsservice = NfsService.from_dict(payload1)
            if nfsservice.post(poll=True):
                print("NFS Service created  created Successfully")
        except NetAppRestError as error:
            print(
                "Error:- " %
                error.http_err_response.http_response.text)
            print("Exception caught :" + str(error))

    print()
    print("Create the Export Policy:-")
    print("==========================")

    export_policy_name = input("Enter New Export Policy Name :- ")
    protocol = input(
        "Enter the protocol name for the Export Policy(nfs/cifs/any):- ")
    clients = input("Enter client details [0.0.0.0/0]:- ")

    svm_uuid = get_key_svms(svm_name)
    payload2 = {
        "name": export_policy_name,
        "rules": [
            {
                "clients": [
                    {
                        "match": clients
                    }
                ],
                "protocols": [
                    protocol
                ],
                "ro_rule": [
                    "any"
                ],
                "rw_rule": [
                    "any"
                ]
            }
        ],
        "svm.uuid": svm_uuid
    }

    print(payload2)
    exportpolicy = ExportPolicy.from_dict(payload2)
    try:
        if exportpolicy.post(poll=True):
            print("Export Policy created  created Successfully")
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

    print()
    print("Create the Volume:-")
    print("===================")
    vol_name = input("Enter new  Volume Name to create NFS Share:-")
    vol_size = input("Enter the Volume Size in MBs :-")
    aggr_name = input("Enter the aggregate name:-")

    v_size = get_size(vol_size)

    pather = "/" + vol_name

    payload3 = {"aggregates": [{"name": aggr_name}],
                "svm": {"name": svm_name},
                "name": vol_name,
                "size": v_size,
                "nas": {"export_policy": {"name": export_policy_name},
                        "security_style": "unix",
                        "path": pather}}

    print(payload3)
    volume = Volume.from_dict(payload3)
    try:
        if volume.post(poll=True):
            print("Volume created  %s created Successfully" % volume.name)
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

    return

def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates NFS Setup using REST API Python Client Library", arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    nfs_setup()

if __name__ == "__main__":
    main()
