#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS ISCSI SETUP USING REST API.
usage: python3 iscsi_setup__restapi_api.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import time
import base64
import argparse
import requests
import json
import requests
import logging
from getpass import getpass
requests.packages.urllib3.disable_warnings()


def get_size(vol_size):
    tmp = int(vol_size) * 1024 * 1024
    return tmp


def get_key_svms(svm_name):
    tmp = dict(get_svms())
    svms = tmp['records']
    for i in svms:
        if i['name'] == svm_name:
            # print i
            return i['uuid']


def get_svms():

    url = "https://{}/api/svm/svms".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    return r.json()


def show_svm(cluster, base64string, headers):

    url = "https://{}/api/svm/svms".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    tmp = dict(r.json())
    svms = tmp['records']
    print()
    print("List of SVMs:- ")
    print("================")
    for i in svms:
        print(i['name'])

    return r.json()


def show_volume(cluster, base64string, headers, svm_name):

    print()
    print("Getting Volume Details")
    print("======================")
    url = "https://{}/api/storage/volumes/?svm.name={}".format(
        cluster, svm_name)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)

    tmp = dict(r.json())
    svms = tmp['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for i in svms:
        print(i['name'])
    return r.json()


def iscsi_setup(cluster, base64string, headers):

    print("THE FOLLOWING SCRIPT DEMOSTRATES ISCSI LUN SETUP USING REST APIs.")
    print("=================================================================")
    print()
    show_svm(cluster, base64string, headers)
    print()
    svm_name = input(
        "Choose the SVM on which you would like to create a lun : ")
    print("Make sure that ISCSI protocol and LIFs on each nodes are created on the SVM")
    print()
    volbool = input("Would you like to create a new volume on the SVM (y/n) :")
    if volbool == 'y':
        vol_name = input("Enter the Volume Name:-")
        vol_size = input("Enter the Volume Size(MBs):-")
        aggr_name = input("Enter the aggregate name:-")

        v_size = get_size(vol_size)
        payload = {
            "aggregates.name": [aggr_name],
            "svm.name": svm_name,
            "name": vol_name,
            "size": v_size,
        }

        url = "https://{}/api/storage/volumes".format(cluster)
        try:
            response = requests.post(
                url, headers=headers, json=payload, verify=False)
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

    else:
        print()
        show_volume(cluster, base64string, headers, svm_name)
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

    url2 = "https://{}/api/storage/luns".format(cluster)
    try:
        response = requests.post(
            url2,
            headers=headers,
            json=payload2,
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

    print(response.json)

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

    url3 = "https://{}/api/protocols/san/igroups".format(cluster)
    try:
        response = requests.post(
            url3,
            headers=headers,
            json=payload3,
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

    print(response.json())

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

    url4 = "https://{}/api/protocols/san/lun-maps".format(cluster)
    try:
        response = requests.post(
            url4,
            headers=headers,
            json=payload4,
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

    print(response.json())

    return


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="THE FOLLOWING SCRIPT SHOWS ISCSI SETUP USING REST API.",
    )
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
    args = parse_args()
    base64string = base64.encodestring(
        ('%s:%s' %
         (args.api_user, args.api_pass)).encode()).decode().replace(
        '\n', '')

    headers = {
        'authorization': "Basic %s" % base64string,
        'content-type': "application/json",
        'accept': "application/json"
    }

    iscsi_setup(args.cluster, base64string, headers)
    print("Script Complete")
