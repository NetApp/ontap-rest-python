#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API PCL

usage: python3 quota_operations.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import QuotaRule
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import show_svm, show_volume, show_qtree


def list_quotarule() -> None:
    """Lists Quota Rule"""
    print()
    print("Getting Quota Rule Details")
    print("==========================")
    try:
        for quotarule in QuotaRule.get_collection():
            print(
                "Quota-Rule UUID = %s;  Volume Name = %s" %
                (quotarule.uuid, quotarule.volume.name))
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_quotarule() -> None:
    """Create Quota Rule """
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(svm_name)
    print()
    volume_name = input(
        "Enter the Volume on which the Quotas needs to be created:-")
    print()
    dataobj = {}
    tmp1 = {"name": svm_name}
    dataobj['svm'] = tmp1
    tmp2 = {"name": volume_name}
    dataobj['volume'] = tmp2
    quota_type = input(
        "Enter the Quota Type [qtree/users/group]:-")
    if quota_type == 'qtree':
        show_qtree(svm_name, volume_name)
        qtree_name = input(
            "Enter the Qtree on which the Quota needs to be applied:-")
        tmp3 = {"name": qtree_name}
        dataobj['qtree'] = tmp3
        dataobj['type'] = "tree"
    if quota_type == 'users':
        dataobj['type'] = "user"
        dataobj['user_mapping'] = False
        tmp3 = []
        dataobj['users'] = tmp3
    if quota_type == 'group':
        dataobj['type'] = "group"
        dataobj['group'] = {}
    spahali = input(
        "Enter the Space Hard-Limit:- ")
    spasoli = input(
        "Enter the Space Soft-Limit:- ")
    fihali = input(
        "Enter the File Hard-Limit:- ")
    fisoli = input(
        "Enter the File Soft-Limit:- ")
    tmp4 = {"hard_limit": spahali, "soft_limit": spasoli}
    dataobj['space'] = tmp4
    tmp5 = {"hard_limit": fihali, "soft_limit": fisoli}
    dataobj['files'] = tmp5
    print(dataobj)

    qrule_info = {
        'qtree': {'name': qtree_name},
        'svm': {'name': svm_name},
        'volume': {'name': volume_name},
        'type': 'tree'
    }
    print(qrule_info)
    try:
        quotarule = QuotaRule.from_dict(qrule_info)
        if quotarule.post(poll=True):
            print("Quota-Rule %s created Successfully" % quotarule.uuid)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def patch_quotarule() -> None:
    """Update Quota"""
    print("=============================================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    print()
    show_volume(svm_name)
    print()
    volume_name = input(
        "Enter the name of the volume for which the quota needs to be modified:- ")
    print()
    option = input(
        "Would you like to update Quotas of Volume or Qtree [group/users/qtree]:- ")
    if option == "users":
        users_name = input(
            "Enter the name of the user,s for which the quota needs to be modified:- ")
        try:
            quotarule = QuotaRule.find(
                svm=svm_name, volume=volume_name, users=users_name)
        except NetAppRestError as error:
            print("Exception caught :" + str(error))
    if option == "qtree":
        show_qtree(svm_name, volume_name)
        qtree_name = input(
            "Enter the name of the qtree for which the quota needs to be modified:- ")
        try:
            quotarule = QuotaRule.find(
                svm=svm_name, volume=volume_name, qtree=qtree_name)
        except NetAppRestError as error:
            print("Exception caught :" + str(error))
    if option == "group":
        group_name = input(
            "Enter the name of the group for which the quota needs to be modified:- ")
        try:
            quotarule = QuotaRule.find(
                svm=svm_name, volume=volume_name, group=group_name)
        except NetAppRestError as error:
            print("Exception caught :" + str(error))

    print()
    spacechange = input("Would you like to change the space limits (y/n):- ")
    if spacechange == 'y':
        spahali = input(
            "Enter the Space Hard-Limit:- ")
        spasoli = input(
            "Enter the Space Soft-Limit:- ")
        quotarule.space = {"hard_limit": spahali, "soft_limit": spasoli}

    filechange = input("Would you like to change the file limits (y/n):- ")
    if filechange == 'y':
        fihali = input(
            "Enter the File Hard-Limit:- ")
        fisoli = input(
            "Enter the File Soft-Limit:- ")
        quotarule.files = {"hard_limit": fihali, "soft_limit": fisoli}

    try:
        if quotarule.patch(poll=True):
            print("Quota-Rule updated successfully")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def delete_quotarule() -> None:
    """Delete Quota"""
    print("=============================================")
    print()
    show_svm()
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    print()
    show_volume(svm_name)
    print()
    volume_name = input(
        "Enter the name of the volume for which the quota needs to be modified:- ")
    print()
    option = input(
        "Would you like to update Quotas of Volume or Qtree [group/users/qtree]:- ")
    if option == "users":
        users_name = input(
            "Enter the name of the user,s for which the quota needs to be modified:- ")
        try:
            quotarule = QuotaRule.find(
                svm=svm_name, volume=volume_name, users=users_name)
        except NetAppRestError as error:
            print("Exception caught :" + str(error))
    if option == "qtree":
        show_qtree(svm_name, volume_name)
        qtree_name = input(
            "Enter the name of the qtree for which the quota needs to be modified:- ")
        try:
            quotarule = QuotaRule.find(
                svm=svm_name, volume=volume_name, qtree=qtree_name)
        except NetAppRestError as error:
            print("Exception caught :" + str(error))
    if option == "group":
        group_name = input(
            "Enter the name of the group for which the quota needs to be modified:- ")
        try:
            quotarule = QuotaRule.find(
                svm=svm_name, volume=volume_name, group=group_name)
        except NetAppRestError as error:
            print("Exception caught :" + str(error))
    print()
    try:
        if quotarule.delete(poll=True):
            print("Quota-Rule deleted Successfully")
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def qr_ops() -> None:
    """Quota-Rule Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS QUOTA OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("===================================================================================")
    print()
    volumebool = input(
        "What Quota Operation would you like to do? [list/create/update/delete] ")
    if volumebool == 'list':
        list_quotarule()
    if volumebool == 'create':
        create_quotarule()
    if volumebool == 'update':
        patch_quotarule()
    if volumebool == 'delete':
        delete_quotarule()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Quota Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    qr_ops()
    # tester1()


if __name__ == "__main__":
    main()
