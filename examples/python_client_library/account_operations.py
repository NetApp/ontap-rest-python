#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts
This script was developed by NetApp to help demonstrate
NetApp technologies. This script is not officially
supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS LUN OPERATIONS USING REST API.

usage: python3 account_operations.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New or Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

from netapp_ontap import NetAppRestError
from netapp_ontap.resources import (
    Account,
    AccountApplication,
    Role,
    RolePrivilege
)
from utils import Argument, step, substep, parse_args, setup_connection, setup_logging


def show_account() -> None:
    """Lists Accounts"""

    substep("List Accounts")
    print("======================")
    try:
        for account in Account.get_collection():
            print("=====")
            print("Account Name = %s" % account.name)
            print("Account Owner Name = %s" % account.owner.name)
            print("Account Owner UUID = %s" % account.owner.uuid)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def create_account():
    """Create an account and a role and assign the account to the role.
    """

    step("Create an account and the role.")

    substep("Create the test account")
    print("======================")
    accname = input(
        "Enter the name of the Account to be created:- ")
    accpwd = getpass()
    accapp = input(
        "Enter the Application type for the Account [http/snmp/ontapi/ssh/rsh/telnet]:- ")
    accauth = input(
        "Enter the Athentication Method for the Account [password/domain/nsswitch]:- ")
    account = Account(
        name=accname,
        password=accpwd,
        applications=[
            AccountApplication(
                application=accapp, authentication_methods=[accauth]
            )
        ],
    )

    try:
        account.post(hydrate=True)
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))
    print("New account created: %s" % account.name)
    print("======================")
    substep("Create the test role")
    rolename = input(
        "Enter the name of the Role to be created:- ")
    privpath = input(
        "Enter the name of the Command Directoey PATH [eg: /api/storage/volume]:- ")
    pathaccess = input(
        "Enter the Access for the Command Directory PATH [none/all/readonly]:- ")
    role = Role(
        name=rolename,
        privileges=[
            RolePrivilege(access=pathaccess, path=privpath),
        ],
    )
    try:
        role.post()
    except NetAppRestError as error:
        print("Exception caught :" + str(error))

    print("New role created: %s" % rolename)

    substep("Assign the test account to the test role")
    account.role = role
    try:
        account.patch()
    except NetAppRestError as error:
        print("Exception caught :" + str(error))
    print("======================")
    print("Account assigned to role: %s" % account)

    return account, role


def update_account():
    """Module to update the account details with new role"""

    step("Update the account with new roles")
    show_account()
    accname = input(
        "Enter the name of the Account that needs to be updated with the new role:- ")
    try:
        account = Account.find(name=accname)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))

    print("======================")
    substep("Create the new role")
    rolename = input(
        "Enter the name of the Role to be created:- ")
    privpath = input(
        "Enter the name of the Command Directoey PATH [eg: /api/storage/volume]:- ")
    pathaccess = input(
        "Enter the Access for the Command Directory PATH [none/all/readonly]:- ")
    role = Role(
        name=rolename,
        privileges=[
            RolePrivilege(access=pathaccess, path=privpath),
        ],
    )
    try:
        role.post()
    except NetAppRestError as error:
        print("Exception caught :" + str(error))
    print("New role created: %s" % rolename)

    substep("Assign the test account to the test role")
    account.role = role
    try:
        account.patch()
    except NetAppRestError as error:
        print("Exception caught :" + str(error))
    print("======================")
    print("Account updated with the new role: %s" % account)


def delete_account():
    """Delete the User"""

    step("Delete the limited account and role")
    show_account()
    accname = input(
        "Enter the name of the Account that needs to be deleted:- ")
    try:
        account = Account.find(name=accname)
    except NetAppRestError as error:
        print("Exception caught :" + str(error))

    substep("Delete our %s account" % accname)
    try:
        account.delete()
    except NetAppRestError as error:
        print("Exception caught :" + str(error))


def account_ops():
    """Volume Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS ACCOUNT OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("=====================================================================================")
    print()
    accountbool = input(
        "Choose the Account Operation would you like to do? [show/create/update/delete] ")
    if accountbool == 'show':
        show_account()
    if accountbool == 'create':
        create_account()
    if accountbool == 'update':
        update_account()
    if accountbool == 'delete':
        delete_account()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Account Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    account_ops()


if __name__ == "__main__":
    main()
