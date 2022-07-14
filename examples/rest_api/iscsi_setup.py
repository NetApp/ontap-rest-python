#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS ISCSI SETUP USING REST API.
usage: python3 iscsi_setup.py [-h] -c CLUSTER [-u API_USER]
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
from utils import Argument, parse_args, setup_logging
from utils import setup_connection, get_size, show_svm, show_volume
ur.disable_warnings()


def iscsi_setup(cluster: str, headers_inc: str):
    """Demonstrates ISCSI setup using REST API"""
    print("Demonstrates ISCSI setup using REST API")
    print("====================================================")
    print()
    show_svm(cluster, headers_inc)
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
                url, headers=headers_inc, json=payload, verify=False)
            print("Volume creation completed.")
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
        show_volume(cluster, headers_inc, svm_name)
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
            headers=headers_inc,
            json=payload2,
            verify=False)
        print("LUN Creation completed.")
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
            headers=headers_inc,
            json=payload3,
            verify=False)
        print("Igroup creation completed.")
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
            headers=headers_inc,
            json=payload4,
            verify=False)
        print("LUN Mapping completed.")
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


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates ISCSI Setup using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    iscsi_setup(args.cluster, headers)
    print("Script Complete")


if __name__ == "__main__":
    main()
