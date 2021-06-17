#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS FILE SECURITY PERMISSIONS USING REST API.

usage: python3 file_security_permissions.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import json
import sys
import urllib.parse
import requests
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import show_svm, get_key_svms, check_job_status
ur.disable_warnings()


def get_file_security_permissions(cluster: str, headers_inc: str):
    """ Retrieving summary of all portsets in the cluster"""
    print()
    print("=======================================")
    print("  Getting File Security Permissions  ")
    print("=======================================")
    show_svm(cluster, headers_inc)
    svm_name = input("\n Enter the svm name:")
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    path = input("\nEnter the path (target path): ")
    api_url = "https://{}/api/protocols/file-security/permissions/{}/{}".format(
        cluster, svm_uuid, path)
    print(api_url)
    try:
        response = requests.get(
            api_url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    print(url_text)
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    print("\nRetrieving File security permissions for target path\n ")
    print(json.dumps(response.json(), indent=7))


def delete_file_permissions(cluster: str, headers_inc: str):
    """ file permissions delete"""
    print("=================Modify file permissions interface=================")
    print("===================================================================")
    print()
    dataobj = {}
    show_svm(cluster, headers_inc)
    svm_name = input("\n\n Enter the svm name: ")
    path = input("\n Enter the path (target): ")
    path = urllib.parse.quote(path)
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    user = input("\nEnter the user name:  ")
    print()
    url = "https://{}/api/protocols/file-security/permissions/{}/{}/acl/{}".format(
        cluster, svm_uuid, path, user)
    print(url)
    try:
        response = requests.delete(
            url,
            headers=headers_inc,
            json=dataobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    print(url_text)
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    print("New job is created for this creation ... \n {}", job_status)
    try:
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = job_response.json()
    check_job_status(job_status, headers_inc, cluster)


def create_file_security_permissions(cluster: str, headers_inc: str):
    """ create file_security_permissions """
    print("=============================================")
    print()
    print("\n Enter the following Details of acls \n")
    dataobj = {}
    show_svm(cluster, headers_inc)
    svm_name = input("\n\n Enter the svm name: ")
    path = input("\n Enter the path (target): ")
    path = urllib.parse.quote(path)
   # path = base64.b64encode(path)
    print("Path is ", path)
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    url = "https://{}/api/protocols/file-security/permissions/{}/{}".format(
        cluster, svm_uuid, path)
    print(url)
    access = input("dacl/sacl access? [e.g: access_allow]: ")
    files = input("apply to files? [True]: ")
    sub_folders = input("apply to sub_folders? [True]: ")
    this_folder = input("apply to this_folder? [True]: ")
    rights = input("Enter the access right control [e.g: full_control] : ")
    user = input("Enter the user account name or SID to ACE applies: ")
    temp1 = {
        "files": files,
        "sub_folders": sub_folders,
        "this_folder": this_folder}
    acls = [{
            "access": access,
            "apply_to": temp1,
            "rights": rights,
            "user": user}]
    dataobj['acls'] = acls
    # below line to be removed in 9.9.1
    #dataobj["access_control"] = "file_directory"
    control_flags = input(
        "\nEnter the control flags (Hexadecimal value e.g: 8014): ")
    group = input("Enter the owner's primary group: ")
    owner = input(" Enter the owner of the SD: ")
    propagation_mode = input(" Enter the propogation mode: ")
    print()
    dataobj['control_flags'] = control_flags
    dataobj['group'] = group
    dataobj['owner'] = owner
    dataobj['propagation_mode'] = propagation_mode
    print(dataobj)
    #url_path = "https://{}/api/protocols/file-security/permissions/" + svm_uuid + path

    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    print(url_text)
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    print("New job is created for this creation ... \n {}", job_status)
    try:
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = job_response.json()
    check_job_status(job_status, headers_inc, cluster)


def patch_file_permissions(cluster: str, headers_inc: str):
    """ patch file permissions"""
    print("=================Modify file permissions interface=================")
    print("===================================================================")
    print()
    dataobj = {}
    show_svm(cluster, headers_inc)
    svm_name = input("\n\n Enter the svm name: ")
    path = input("\n Enter the path (target): ")
    path = urllib.parse.quote(path)
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    control_flags = input(
        "\nEnter the control flags (Hexadecimal value e.g: 8014): ")
    group = input("Enter the owner's primary group: ")
    owner = input(" Enter the owner of the SD: ")
    print()
    dataobj['control_flags'] = control_flags
    dataobj['group'] = group
    dataobj['owner'] = owner
    print()
    url = "https://{}/api/protocols/file-security/permissions/{}/{}".format(
        cluster, svm_uuid, path)
    print(url)
    try:
        response = requests.patch(
            url,
            headers=headers_inc,
            json=dataobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    print(url_text)
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    print("New job is created for this creation ... \n {}", job_status)
    try:
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = job_response.json()
    check_job_status(job_status, headers_inc, cluster)


def file_permissions(cluster: str, headers_inc: str):
    """Demonstrates File security permission operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS PORTSET OPERATIONS USING REST API.")
    print("==================================================================")
    print("Choose the Portset operation?")
    snapshotbool = input(
        "\n1.list \n2.create \n3.update \n4.delete \n\n[enter option]: ")
    if snapshotbool == '1':
        get_file_security_permissions(cluster, headers_inc)
    if snapshotbool == '2':
        create_file_security_permissions(cluster, headers_inc)
    if snapshotbool == '3':
        patch_file_permissions(cluster, headers_inc)
    if snapshotbool == '4':
        delete_file_permissions(cluster, headers_inc)

def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Snapshot Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    file_permissions(args.cluster, headers)


if __name__ == "__main__":
    main()
