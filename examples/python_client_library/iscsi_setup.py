#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS ISCSI SETUP USING REST API PCL

usage: iscsi_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Svm, Volume, Igroup, Lun, LunMap
from utils import Argument, parse_args, setup_logging, setup_connection, get_size

def show_svm() -> None:
    """Show SVMs in a cluster"""
    print()
    print("Getting SVM Details")
    print("===================")
    try:
        for svm in Svm.get_collection(fields="uuid"):
            print("SVM name:-%s ; SVM uuid:-%s " % (svm.name, svm.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def show_volume(svm_name) -> None:
    """Show volumes in a SVM"""
    print()
    print("Getting Volume Details")
    print("===================")
    try:
        for volume in Volume.get_collection(
                **{"svm.name": svm_name}, fields="uuid"):
            print(
                "Volume name:-%s ; Volume uuid:-%s " %
                (volume.name, volume.uuid))
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def iscsi_setup() -> None:
    """ Script demostrates the ISCSI Lun Setup"""
    print("THE FOLLOWING SCRIPT DEMOSTRATES ISCSI LUN SETUP USING REST API PCL.")
    print("====================================================================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Choose the SVM on which you would like to create a lun : ")
    print("Make sure that ISCSI protocol and LIFs on each nodes are created on the SVM")
    print()
    volbool = input("Would you like to create a new volume (y/n) :-")
    if volbool == 'y':
        vol_name = input("Enter the Volume Name:-")
        vol_size = input("Enter the Volume Size (MBs):-")
        aggr_name = input("Enter the aggregate name:-")

        v_size = get_size(vol_size)

        payload1 = {
            "name": vol_name,
            "svm": {"name": svm_name},
            "aggregates": [{"name": aggr_name}],
            "size": v_size
        }

        print(payload1)
        volume = Volume.from_dict(payload1)
        try:
            if volume.post(poll=True):
                print("Volume created  created Successfully")
        except NetAppRestError as error:
            print(
                "Error:- " %
                error.http_err_response.http_response.text)
            print("Exception caught :" + str(error))

    else:
        print()
        show_volume(svm_name)
        vol_name = input(
            "Choose the volume on which you would like to create the LUN : ")

    print()
    lun_name = input("Enter the name of the LUN  : ")
    lun_name_ext = "/vol/" + vol_name + "/" + lun_name
    os_type = input("Enter the name of the OS-TYPE  : ")
    lun_size = input("Enter the LUN size in MBs :")
    l_size = get_size(lun_size)

    payload2 = {
        "comment": lun_name,
        "location": {
            "logical_unit": lun_name,
            "volume": {
                "name": vol_name
            }
        },
        "name": lun_name_ext,
        "os_type": os_type,
        "space": {
            "guarantee": {
                "requested": bool("")
            },
            "size": l_size
        },
        "svm": {
            "name": svm_name
        }
    }

    lun_object = Lun.from_dict(payload2)

    try:
        if lun_object.post(poll=True):
            print("LUN created  %s created Successfully" % lun_object.name)
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

    print()

    igroup_name = input(
        "Enter the name of the Igroup that you would like to create  : ")
    initiator_name = input(
        "Enter the name of the Initiator that you would like to add in the InitiatorGroup :")
    os_type2 = input("Enter the OS-TYPE :")

    payload3 = {
        "initiators": [
            {
                "name": initiator_name
            }
        ],
        "name": igroup_name,
        "os_type": os_type2,
        "svm": {
            "name": svm_name
        }
    }

    igroup_object = Igroup.from_dict(payload3)

    try:
        if igroup_object.post(poll=True):
            print(
                "IGROUP created  %s created Successfully" %
                igroup_object.name)
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

    payload4 = {
        "igroup": {
            "name": igroup_name
        },
        "lun": {
            "name": lun_name_ext

        },
        "svm": {
            "name": svm_name

        }
    }

    lunmap_object = LunMap.from_dict(payload4)
    try:
        if lunmap_object.post(poll=True):
            print("Mapping created Successfully")
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))

def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates ISCSI Setup using REST API Python Client Library", arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    iscsi_setup()

if __name__ == "__main__":
    main()
