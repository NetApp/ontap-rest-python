#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts
This script was developed by NetApp to help demonstrate
NetApp technologies. This script is not officially
supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS ACCOUNT OPERATIONS USING REST API

usage: python3 account_operations.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New or Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
from utils import Argument, parse_args, setup_logging, setup_connection, get_key_accountowner, show_account
requests.packages.urllib3.disable_warnings()


def list_account(cluster: str, headers_inc: str) -> None:
    """Lists Accounts"""
    print("======================")
    print()
    account_api_url = " https://{}/api/security/accounts".format(
        cluster)
    try:
        response = requests.get(
            account_api_url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    accountdict = dict(response.json())
    accounts = accountdict['records']
    print()
    print(" List of Accounts :- ")
    for account in accounts:
        print("=====")
        print("Account Name = %s" % account['name'])
        print("Account  Owner Name = %s" % account['owner']['name'])
        print("Account Owner UUID = %s" % account['owner']['uuid'])


def create_account(cluster: str, headers_inc: str) -> None:
    """Create an account and a role and assign the account to the role."""

    print("Create the Account")
    print("======================")
    accname = input(
        "Enter the name of the Account to be created:- ")
    accpwd = input(
        "Enter the password of the Account:- ")
    accapp = input(
        "Enter the Application type for the Account [http/snmp/ontapi/ssh/rsh/telnet]:- ")
    accauth = input(
        "Enter the Athentication Method for the Account [password/domain/nsswitch]:- ")
    accountobj = {"applications": [{"authentication_methods": [
        accauth], "application": accapp}], "password": accpwd, "name": accname}
    print(accountobj)

    url = "https://{}/api/security/accounts".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=accountobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    url_text = response.json()
    print(url_text)
    print("New account created: %s" % accname)
    print("======================")
    print("Create the test role")
    rolename = input(
        "Enter the name of the Role to be created:- ")
    privpath = input(
        "Enter the name of the Command Directoey PATH [eg: /api/storage/volume]:- ")
    pathaccess = input(
        "Enter the Access for the Command Directory PATH [none/all/readonly]:- ")
    roleobj = {"name": rolename, "privileges": [
        {"path": privpath, "access": pathaccess}]}
    print(roleobj)

    url = "https://{}/api/security/roles".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=roleobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    url_text = response.json()
    print(url_text)
    print("New role created: %s" % rolename)

    print("Assign the test account to the test role")
    accownerkey = get_key_accountowner(accname, cluster, headers_inc)
    print(accownerkey)
    rolepatchobj = {"role": {"name": rolename}}
    print(rolepatchobj)

    url = "https://{}/api/security/accounts/{}/{}".format(
        cluster, accownerkey, accname)
    try:
        response = requests.patch(
            url,
            headers=headers_inc,
            json=rolepatchobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    print("Account assigned to role: %s" % accname)


def update_account(cluster, headers_inc):
    """Call the /volumes API and list the current volumes. We should be allowed
    to do this. Then modify our role to deny the access and call it again. This
    time we should get an error.
    """

    print("Update the account with new roles")
    show_account(cluster, headers_inc)
    accname = input(
        "Enter the name of the Account that needs to be updated with the new role:- ")
    accownerkey = get_key_accountowner(accname, cluster, headers_inc)

    print("New account created: %s" % accname)
    print("======================")
    print("Create the test role")
    rolename = input(
        "Enter the name of the Role to be created:- ")
    privpath = input(
        "Enter the name of the Command Directoey PATH [eg: /api/storage/volume]:- ")
    pathaccess = input(
        "Enter the Access for the Command Directory PATH [none/all/readonly]:- ")
    roleobj = {"name": rolename, "privileges": [
        {"path": privpath, "access": pathaccess}]}
    print(roleobj)

    url = "https://{}/api/security/roles".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=roleobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    url_text = response.json()
    print(url_text)
    print("New role created: %s" % rolename)

    print("Assign the test account to the test role")
    accownerkey = get_key_accountowner(accname, cluster, headers_inc)
    print(accownerkey)
    rolepatchobj = {"role": {"name": rolename}}
    print(rolepatchobj)

    url = "https://{}/api/security/accounts/{}/{}".format(
        cluster, accownerkey, accname)
    try:
        response = requests.patch(
            url,
            headers=headers_inc,
            json=rolepatchobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    print("Account assigned to role: %s" % accname)


def delete_account(cluster, headers_inc):
    """Delete the Account"""

    print("Delete the Account and role")
    show_account(cluster, headers_inc)
    accname = input(
        "Enter the name of the Account that needs to be deleted:- ")
    accownerkey = get_key_accountowner(accname, cluster, headers_inc)

    url = "https://{}/api/security/accounts/{}/{}".format(
        cluster, accownerkey, accname)
    try:
        response = requests.delete(
            url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    print("Account %s deleted" % (accname))


def account_ops(cluster, headers_inc):
    """Account Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS ACCOUNT OPERATIONS USING REST API:- ")
    print("=====================================================================================")
    print()
    accountbool = input(
        "Choose the Account Operation would you like to do? [list/create/update/delete] ")
    if accountbool == 'list':
        list_account(cluster, headers_inc)
    if accountbool == 'create':
        create_account(cluster, headers_inc)
    if accountbool == 'update':
        update_account(cluster, headers_inc)
    if accountbool == 'delete':
        delete_account(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Account Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    account_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
