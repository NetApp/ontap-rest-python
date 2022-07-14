#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS FILE SYSTEM ANALYTICS ENABLING DISABLING USING REST API

usage: python3 file_analytics_enable_disable.py [-h] -c CLUSTER [-u API_USER]
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
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import get_key_volumes, show_svm, show_volume, check_job_status
ur.disable_warnings()


def enable_analytics(cluster: str, headers_inc: str):
    """ Enable Analytics on a volume"""
    print("=============================================")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM :")
    print()
    show_volume(cluster, headers_inc, svm_name)
    volname = input(
        "Enter the name of the volume to enable analytics:- ")
    tmp4 = {"state": "on"}
    dataobj = {}
    dataobj['analytics'] = tmp4
    vol_uuid = get_key_volumes(svm_name, volname, cluster, headers_inc)
    urlpath = "https://{}/api/storage/volumes/" + vol_uuid
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


def disable_analytics(cluster: str, headers_inc: str):
    """ Disable Analytics on a volume"""
    print("=============================================")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM :")
    print()
    show_volume(cluster, headers_inc, svm_name)
    volname = input(
        "Enter the name of the volume to enable analytics:- ")
    tmp4 = {"state": "off"}
    dataobj = {}
    dataobj['analytics'] = tmp4
    vol_uuid = get_key_volumes(svm_name, volname, cluster, headers_inc)
    urlpath = "https://{}/api/storage/volumes/" + vol_uuid
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


def vol_analytics_ops(cluster: str, headers_inc: str):
    """Volume enabling disabling module"""
    print()
    print("Demostrates the Volume Operations:- ")
    print("====================================")
    print("\nWhich operation would you like to do? ")
    volumebool = input(
        "\n1.Enable Analytics \n2.Disable analytics \n\nEnter option : ")
    if volumebool == "1":
        enable_analytics(cluster, headers_inc)
    if volumebool == "2":
        disable_analytics(cluster, headers_inc)


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates enabling/disabling File system analytics using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)
    vol_analytics_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
