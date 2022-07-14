#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SVM OPERATIONS USING REST API

usage: python3 svm_operations.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, show_node
from utils import setup_connection, get_key_svms, show_svm, check_job_status
ur.disable_warnings()


def list_svm(cluster: str, headers_inc: str):
    """ returns SVM list"""
    url = "https://{}/api/svm/svms".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    svmsdict = dict(response.json())
    svms = svmsdict['records']
    print()
    print("List of SVMs:- ")
    print("===============")
    for svm in svms:
        print(svm['name'])
    url = "https://{}/api/svm/svms".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)


def start_svm(cluster: str, headers_inc: str):
    """ starts svm"""
    show_svm(cluster, headers_inc)
    print()
    print("=============================================")
    print("This option starts a SVM: ")
    print()
    svm_name = input(
        "Enter the SVM which needs to be started:-")
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    print()
    print("The UUID of the requested SVM is:-")
    print(svm_uuid)
    dataobj = {"state": "running", "comment": "This SVM is running."}
    urlpath = "https://{}/api/svm/svms/" + svm_uuid
    url = urlpath.format(cluster)
    try:
        response = requests.patch(
            url, headers=headers_inc, json=dataobj, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
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


def stop_svm(cluster: str, headers_inc: str):
    """stops the svm"""
    show_svm(cluster, headers_inc)
    print("=============================================")
    print("This option stops a SVM: ")
    print()
    svm_name = input(
        "Enter the SVM which needs to be stopped:-")
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    print()
    print("The UUID of the requested SVM is:-")
    print(svm_uuid)
    dataobj = {"state": "stopped", "comment": "This SVM is stopped."}
    urlpath = "https://{}/api/svm/svms/" + svm_uuid
    url = urlpath.format(cluster)
    try:
        response = requests.patch(
            url, headers=headers_inc, json=dataobj, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
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


def delete_svm(cluster: str, headers_inc: str):
    """ delete svm"""
    show_svm(cluster, headers_inc)
    print("=============================================")
    print("This option stops a SVM: ")
    print()
    svm_name = input(
        "Enter the SVM which needs to be deleted:-")
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    print()
    print("The UUID of the requested SVM is:-")
    print(svm_uuid)
    dataobj = {}
    urlpath = "https://{}/api/svm/svms/" + svm_uuid
    url = urlpath.format(cluster)
    try:
        response = requests.delete(
            url, headers=headers_inc, json=dataobj, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
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


def create_svm(cluster: str, headers_inc: str):
    """ create svm"""
    svmname = input("Enter the name of the SVM: ")
    dataobj = {}
    dataobj['name'] = svmname
    dataobj['language'] = "c.utf_8"
    ipspaceobj = {"name": "Default"}
    dataobj['ipspace'] = ipspaceobj
    print()
    intbool = input("Would you like to configure an Interface (y/n): ")
    if intbool == 'y':
        mgmtlif = input("Enter the name of Management LIF: ")
        ipadd = input("Enter the IP address: ")
        nmask = input("Enter the NetMask: ")
        show_node(cluster, headers_inc)
        hnode = input("Enter the Home Node: ")
        uuid = input("Enter the UUID: ")
        intjson = [
            {
                "ip": {
                    "address": ipadd,
                    "netmask": nmask},
                "location": {
                    "broadcast_domain": {
                        "name": "Default"},
                    "home_node": {
                        "name": hnode,
                        "uuid": uuid}},
                "name": mgmtlif,
                "service_policy": "default-data-files"}]
        dataobj['ip_interfaces'] = intjson
    print()
    nfsbool = input("Would you like to configure an NFS (y/n): ")
    if nfsbool == 'y':
        nfsjson = {"enabled": bool("true")}
        dataobj['nfs'] = nfsjson
    print()
    cifsbool = input("Would you like to configure an CIFS (y/n): ")
    if cifsbool == 'y':
        fqdn = input("Enter the name of FQDN: ")
        aduser = input("Enter the User: ")
        adpassword = input("Enter the password: ")
        adname = input("Enter the AD Name: ")
        cifsjson = {
            "ad_domain": {
                "fqdn": fqdn,
                "password": adpassword,
                "user": aduser},
            "enabled": bool("true"),
            "name": adname}
        dataobj['cifs'] = cifsjson
    print()
    dnsbool = input("Would you like to configure an DNS (y/n): ")
    if dnsbool == 'y':
        domain = input("Enter the name of Domain: ")
        server = input("Enter the Server: ")
        dnsjson = {"domains": [domain], "servers": [server]}
        dataobj['dns'] = dnsjson

    print(dataobj)
    url = "https://{}/api/svm/svms".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        print(response)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print(response)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        print(job_response)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print(job_response)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = job_response.json()
    check_job_status(job_status, headers_inc, cluster)


def update_svm(cluster: str, headers_inc: str):
    """ updates the svm"""
    show_svm(cluster, headers_inc)
    print("This option Updates a SVM: ")
    print()
    svm_name = input(
        "Enter the SVM which needs to be updated:-")
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    print()
    print("The UUID of the requested SVM is:-")
    print(svm_uuid)
    urlpath = "https://{}/api/svm/svms/" + svm_uuid
    dataobj = {}
    dataobj['state'] = "running"
    print(dataobj)
    print()
    lanbool = input("Would you like to update language (y/n): ")
    if lanbool == 'y':
        lan = input("Enter the name of language: ")
        dataobj['language'] = lan
    print()
    namebool = input("Would you like to update the name (y/n): ")
    if namebool == 'y':
        nam = input("Enter the new  name of SVM: ")
        dataobj['name'] = nam
    print()
    snapbool = input("Would you like to update an SnapShot Policy (y/n): ")
    if snapbool == 'y':
        snap = input(
            "Enter the name of default snapshot policy that needs to ne updated : ")
        dataobj['snapshot_policy'] = snap
    print()
    aggrbool = input("Would you like to update Aggregate (y/n): ")
    if aggrbool == 'y':
        aggr = input(
            "Enter the name of aggregates(with commas) that needs to ne updated : ")
        dataobj['aggregates'] = {"aggregates": {"name": ["aggr"]}}
    print()
    print("\n JSON file to be submitted:-")
    print(dataobj)
    url = urlpath.format(cluster)
    try:
        response = requests.patch(
            url, headers=headers_inc, json=dataobj, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
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


def svm_ops(cluster: str, headers_inc: str):
    """Demostrates SVM Operations"""
    print()
    print("Demonstrates SVM Operations using REST API:- ")
    print("============================================================")
    print()
    svmget = input(
        "What SVM Operation would you like to do? [list/create/update/start/stop/delete] ")
    if svmget == 'list':
        list_svm(cluster, headers_inc)
    if svmget == 'create':
        create_svm(cluster, headers_inc)
    if svmget == 'update':
        update_svm(cluster, headers_inc)
    if svmget == 'start':
        start_svm(cluster, headers_inc)
    if svmget == 'stop':
        stop_svm(cluster, headers_inc)
    if svmget == 'delete':
        delete_svm(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Volume Operations using REST API Python Client Library.",
        arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    svm_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
