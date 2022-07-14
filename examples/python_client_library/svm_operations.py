#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SVM OPERATIONS USING REST API PCL

usage: python3 svm_operations.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Svm
from utils import Argument, parse_args, setup_logging, setup_connection, show_svm, show_node


def list_svm() -> None:
    """List SVM in a cluster"""
    print("Getting SVM Details")
    print("===================")

    try:
        for svm in Svm.get_collection(fields="uuid"):
            svm.get()
            print("SVM name:-%s ; SVM uuid:-%s " % (svm.name, svm.uuid))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_svm() -> None:
    """Create SVM"""
    print()
    svmname = input("Enter the name of the SVM: ")
    dataobj = {}
    dataobj['name'] = svmname
    dataobj['language'] = "c.utf_8"
    ipspaceobj = {"name": "Default"}
    dataobj['ipspace'] = ipspaceobj
    intbool = input("Would you like to configure an Interface (y/n): ")
    if intbool == 'y':
        mgmtlif = input("Enter the name of Management LIF: ")
        ipadd = input("Enter the IP address: ")
        nmask = input("Enter the NetMask: ")
        bdomain = input("Enter the broadcast-domain: ")
        show_node()
        hnode = input("Enter the Home Node: ")
        uuids = input("Enter the UUID: ")
        intjson = [
            {
                "ip":
                {
                    "address": ipadd,
                    "netmask": nmask
                },
                "location":
                {
                    "broadcast_domain":
                    {
                        "name": bdomain
                    },
                    "home_node": {
                        "name": hnode,
                        "uuid": uuids
                    }
                },
                "name": mgmtlif,
                "service_policy": "default-data-files"
            }
        ]
        dataobj['ip_interfaces'] = intjson
    nfsbool = input("Would you like to configure an NFS (y/n): ")
    if nfsbool == 'y':
        nfsjson = {"enabled": bool("true")}
        dataobj['nfs'] = nfsjson
        print(dataobj)
    cifsbool = input("Would you like to configure an CIFS (y/n): ")
    if cifsbool == 'y':
        fqdn = input("Enter the name of FQDN: ")
        aduser = input("Enter the User: ")
        adpassword = input("Enter the password: ")
        adname = input("Enter the AD Name: ")
        cifsjson = {
            "ad_domain":
            {
                "fqdn": fqdn,
                "password": adpassword,
                "user": aduser
            },
            "enabled": bool("true"),
            "name": adname
        }
        dataobj['cifs'] = cifsjson
        print(dataobj)
    dnsbool = input("Would you like to configure an DNS (y/n): ")
    if dnsbool == 'y':
        domain = input("Enter the name of Domain: ")
        server = input("Enter the Server: ")
        dnsjson = {"domains": [domain], "servers": [server]}
        dataobj['dns'] = dnsjson
        print(dataobj)

    try:
        svm = Svm.from_dict(dataobj)
        if svm.post(poll=True):
            print("SVM  %s created Successfully" % svm.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_svm() -> None:
    """Update SVM"""
    print()
    show_svm()
    print("=============================================")
    svmname = input("Enter the name of the SVM that needs to be updated: ")
    svm = Svm.find(name=svmname)
    lanbool = input("Would you like to update language (y/n): ")
    if lanbool == 'y':
        lan = input("Enter the name of language the you would like to update: ")
        svm.language = lan
    namebool = input("Would you like to update the name (y/n): ")
    if namebool == 'y':
        nam = input("Enter the name of SVM: ")
        svm.name = nam
    snapbool = input("Would you like to update an SnapShot Policy (y/n): ")
    if snapbool == 'y':
        snap = input(
            "Enter the name of default snapshot policy that needs to ne updated : ")
        svm.snapshot_policy = snap
    aggrbool = input(
        "Would you like to update the SVM with new Aggregate (y/n): ")
    if aggrbool == 'y':
        aggr = input(
            "Enter the name of aggregates(with commas) that needs to be updated : ")
        svm.aggregates.name = aggr

    try:
        if svm.patch(poll=True):
            print("SVM  %s has been updated/patched Successfully" % svm.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def start_svm() -> None:
    """Start SVM"""
    print()
    show_svm()
    print()
    print("=============================================")
    svmname = input(
        "Enter the name of the SVM name that needs to be started: ")
    svm = Svm.find(name=svmname)
    svm.state = "running"

    try:
        if svm.patch(poll=True):
            print("SVM  %s has been started Successfully" % svm.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def stop_svm() -> None:
    """Stop SVM"""
    print()
    show_svm()
    print("=============================================")
    print()
    svmname = input(
        "Enter the name of the SVM name that needs to be stopped: ")
    svm = Svm.find(name=svmname)
    svm.state = "stopped"

    try:
        if svm.patch(poll=True):
            print("SVM  %s has been stopped Successfully." % svm.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_svm() -> None:
    """Delete SVM"""
    print()
    show_svm()
    print("=============================================")
    print()
    svmname = input("Enter the name of the SVM that needs to be deleted: ")
    try:
        svm = Svm.find(name=svmname)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))

    try:
        if svm.delete(poll=True):
            print("SVM  %s has been deleted Successfully." % svm.name)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def svm_ops() -> None:
    """SVM Operation"""
    print()
    print("Demonstrates SVM Operations using REST API Python Client Library:- ")
    print("===================================================================")
    print()
    svmget = input(
        "What SVM Operation would you like to do? [list/create/update/start/stop/delete:- ] ")
    if svmget == 'list':
        list_svm()
    if svmget == 'create':
        create_svm()
    if svmget == 'update':
        patch_svm()
    if svmget == 'start':
        start_svm()
    if svmget == 'stop':
        stop_svm()
    if svmget == 'delete':
        delete_svm()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates SVM Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    svm_ops()


if __name__ == "__main__":
    main()
